#!/usr/bin/env python3
"""Validate setup catalog metadata, plan references, and local Markdown links."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
VALID_EXECUTION_MODES = {"manual", "automated", "hybrid"}
VALID_STATUSES = {"current", "reference"}
ROOT_RELATIVE_PATH_FIELDS = ("source_docs", "provisioning_adapter")
SHARED_RESOURCE_ID_PREFIX = "shared-"
IGNORED_DIRECTORIES = {".git", "node_modules", "__pycache__"}
ISO_DATE_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}")
LINK_PATTERN = re.compile(r"""(?<!!)\[[^\]]*\]\(\s*(<[^>]*>|[^\s)]+)(?:\s+["'(][^)]*)?\)""")
FENCED_CODE_BLOCK_PATTERN = re.compile(r"^[ \t]*(`{3,}|~{3,}).*?^[ \t]*\1[ \t]*$", re.DOTALL | re.MULTILINE)
FLATPAK_APP_ID_PATTERN = re.compile(r"[A-Za-z][\w-]*(?:\.[\w-]+){2,}")
# Links every role hub needs regardless of which Entry Points are active.
HUB_NAVIGATION_REQUIREMENTS = {
    "README.md": {"plans/README.md", "catalog/README.md", "exports/README.md", "reference/README.md"},
    "plans/README.md": {"catalog/README.md", "exports/README.md", "reference/README.md"},
    "catalog/README.md": {"plans/README.md", "exports/README.md", "reference/README.md"},
    "exports/README.md": {"README.md", "plans/README.md", "catalog/README.md", "reference/README.md"},
    "reference/README.md": {"README.md", "plans/README.md", "catalog/README.md", "exports/README.md"},
}


@dataclass(frozen=True)
class RecordKind:
    """The front-matter schema for one kind of record: Inventory Record or Setup Plan."""

    noun: str
    directory: str
    required_fields: frozenset[str]


INVENTORY_RECORD = RecordKind(
    noun="resource",
    directory="catalog",
    required_fields=frozenset(
        {"id", "title", "entry_points", "execution_mode", "status", "supported", "verified_on", "source_docs"}
    ),
)
SETUP_PLAN = RecordKind(
    noun="plan",
    directory="plans",
    required_fields=frozenset({"id", "title", "entry_point", "status", "supported", "verified_on"}),
)


@dataclass(frozen=True)
class Record:
    path: str
    metadata: dict[str, str]
    text: str

    @property
    def current(self) -> bool:
        return self.metadata["status"] == "current"


@dataclass(frozen=True)
class EntryPoint:
    """One Entry Point, derived from its Setup Plan; active when the plan is a Current Guide."""

    name: str
    active: bool

    @property
    def plan(self) -> str:
        return f"plans/{self.name}.md"

    @property
    def export_directory(self) -> str:
        return f"exports/{self.name}"

    @property
    def export_index(self) -> str:
        return f"{self.export_directory}/README.md"


@dataclass(frozen=True)
class FlatpakInventory:
    """Where one Entry Point's Flatpak set is installed, curated, and snapshotted."""

    provisioning_adapter: str
    inventory_record: str
    inventory_export: str


LINUX_FLATPAKS = FlatpakInventory(
    provisioning_adapter="environment/SetupLinux.sh",
    inventory_record="catalog/linux-application-catalog.md",
    inventory_export="exports/linux/primary-machine.md",
)


def describe(root: Path, path: Path) -> str:
    """Render a path for error messages, relative to the root when possible."""
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def read_text(root: Path, path: Path, errors: list[str]) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as exc:
        errors.append(f"{describe(root, path)}: unable to read file: {exc}")
        return None


def resolve_within_root(root: Path, relative: str) -> Path | None:
    """Resolve a root-relative reference, returning None if it escapes the root."""
    target = (root / relative).resolve()
    if not target.is_relative_to(root):
        return None
    return target


def parse_front_matter(text: str) -> dict[str, str]:
    """Parse the flat `key: value` pairs from a leading `---` fenced block."""
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}
    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip()
    return metadata


def strip_fenced_code_blocks(text: str) -> str:
    return FENCED_CODE_BLOCK_PATTERN.sub("", text)


def local_link_targets(path: Path, text: str) -> list[tuple[str, Path]]:
    """Return `(destination, resolved path)` pairs for local links outside code fences."""
    targets: list[tuple[str, Path]] = []
    for match in LINK_PATTERN.findall(strip_fenced_code_blocks(text)):
        destination = match.strip("<>").split("#", 1)[0].strip()
        if not destination or "://" in destination or destination.startswith(("mailto:", "#")):
            continue
        targets.append((destination, (path.parent / destination).resolve()))
    return targets


def extract_local_links(root: Path, path: Path, text: str) -> set[str]:
    links: set[str] = set()
    for _, target in local_link_targets(path, text):
        if target.is_relative_to(root):
            links.add(target.relative_to(root).as_posix())
    return links


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(
        path for path in root.rglob("*.md") if not IGNORED_DIRECTORIES.intersection(path.parts)
    )


def split_list(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


# --- Records -----------------------------------------------------------------


def load_record(root: Path, path: Path, kind: RecordKind, errors: list[str]) -> Record | None:
    """Parse and validate one record, returning None when it cannot be used further."""
    label = describe(root, path)
    text = read_text(root, path, errors)
    if text is None:
        return None
    metadata = parse_front_matter(text)
    missing = kind.required_fields - metadata.keys()
    if missing:
        qualifier = "" if kind is INVENTORY_RECORD else f"{kind.noun} "
        errors.append(f"{label}: missing {qualifier}metadata: {', '.join(sorted(missing))}")
        return None

    status = metadata["status"]
    if status not in VALID_STATUSES:
        errors.append(f"{label}: invalid status")
    if status == "current" and not ISO_DATE_PATTERN.fullmatch(metadata["verified_on"]):
        errors.append(f"{label}: current {kind.noun} needs an ISO verified_on date")
    if status == "reference" and metadata["verified_on"] != "pending":
        errors.append(f"{label}: reference {kind.noun} needs verified_on: pending")

    execution_mode = metadata.get("execution_mode")
    if execution_mode is not None and execution_mode not in VALID_EXECUTION_MODES:
        errors.append(f"{label}: invalid execution_mode")
    if execution_mode == "automated" and not metadata.get("provisioning_adapter"):
        errors.append(f"{label}: automated {kind.noun} needs provisioning_adapter")

    for field in ROOT_RELATIVE_PATH_FIELDS:
        value = metadata.get(field)
        if not value:
            continue
        resolved = resolve_within_root(root, value)
        if resolved is None:
            errors.append(f"{label}: {field} escapes repository root: {value}")
        elif not resolved.exists():
            errors.append(f"{label}: {field} does not exist relative to repository root: {value}")

    return Record(path=label, metadata=metadata, text=text)


def load_records(root: Path, kind: RecordKind, errors: list[str]) -> list[Record]:
    records = []
    for path in sorted((root / kind.directory).glob("*.md")):
        if path.name == "README.md":
            continue
        record = load_record(root, path, kind, errors)
        if record is not None:
            records.append(record)
    return records


# --- Entry Points ------------------------------------------------------------


def entry_points_from_plans(plans: list[Record], errors: list[str]) -> list[EntryPoint]:
    entry_points: dict[str, EntryPoint] = {}
    for plan in plans:
        name = plan.metadata["entry_point"]
        if name in entry_points:
            errors.append(f"{plan.path}: duplicate Setup Plan for entry point: {name}")
            continue
        if plan.path != EntryPoint(name, plan.current).plan:
            errors.append(f"{plan.path}: Setup Plan for entry point {name} must be plans/{name}.md")
        entry_points[name] = EntryPoint(name, plan.current)
    return sorted(entry_points.values(), key=lambda entry_point: entry_point.name)


def navigation_requirements(entry_points: list[EntryPoint]) -> dict[str, set[str]]:
    """Map each active navigation surface to the links it must contain."""
    requirements = {surface: set(links) for surface, links in HUB_NAVIGATION_REQUIREMENTS.items()}
    for entry_point in entry_points:
        if not entry_point.active:
            continue
        requirements["README.md"].add(entry_point.plan)
        requirements["plans/README.md"].add(entry_point.plan)
        requirements[entry_point.plan] = {"catalog/README.md", entry_point.export_index, "reference/README.md"}
        requirements[entry_point.export_index] = {entry_point.plan, "catalog/README.md"}
    return requirements


def retired_entry_point_for(link: str, entry_points: list[EntryPoint]) -> str | None:
    """Return the retired Entry Point a link belongs to, if any."""
    path = PurePosixPath(link)
    parts = {part.lower() for part in path.parts}
    stem = path.stem.lower()
    for entry_point in entry_points:
        name = entry_point.name
        if not entry_point.active and (name in parts or stem == name or stem.startswith(f"{name}-")):
            return name
    return None


def export_snapshots(links: set[str], entry_point: EntryPoint) -> set[str]:
    prefix = f"{entry_point.export_directory}/"
    return {link for link in links if link.startswith(prefix) and link != entry_point.export_index}


# --- Checks ------------------------------------------------------------------


def validate_resources(
    resources: list[Record], entry_points: list[EntryPoint], errors: list[str]
) -> None:
    known = {entry_point.name for entry_point in entry_points}
    ids: set[str] = set()
    for resource in resources:
        resource_id = resource.metadata["id"]
        if resource_id in ids:
            errors.append(f"{resource.path}: duplicate resource id: {resource_id}")
        ids.add(resource_id)
        errors.extend(
            f"{resource.path}: unknown entry point: {name}"
            for name in split_list(resource.metadata["entry_points"])
            if name not in known
        )


def validate_plan_references(
    plans: list[Record], resources: list[Record], entry_points: list[EntryPoint], errors: list[str]
) -> None:
    resource_ids = {resource.metadata["id"] for resource in resources}
    prefixes = (SHARED_RESOURCE_ID_PREFIX, *(f"{entry_point.name}-" for entry_point in entry_points))
    for plan in plans:
        errors.extend(
            f"{plan.path}: unknown resource id: {resource_id}"
            for resource_id in re.findall(r"`([a-z0-9-]+)`", plan.text)
            if resource_id.startswith(prefixes) and resource_id not in resource_ids
        )


def validate_navigation_contract(root: Path, entry_points: list[EntryPoint], errors: list[str]) -> None:
    for relative_path, required_links in navigation_requirements(entry_points).items():
        path = root / relative_path
        if not path.exists():
            errors.append(f"{relative_path}: missing required navigation surface")
            continue
        text = read_text(root, path, errors)
        if text is None:
            continue
        links = extract_local_links(root, path, text)
        errors.extend(
            f"{relative_path}: missing required navigation link: {required_link}"
            for required_link in sorted(required_links - links)
        )
        for link in sorted(links):
            retired = retired_entry_point_for(link, entry_points)
            if retired is not None:
                errors.append(f"{relative_path}: forbidden link to retired entry point {retired}: {link}")


def validate_active_routes(
    root: Path,
    plans: list[Record],
    resources: list[Record],
    entry_points: list[EntryPoint],
    errors: list[str],
) -> None:
    """Each active Setup Plan routes to a current Inventory Record and an Inventory Export snapshot."""
    plans_by_path = {plan.path: plan for plan in plans}
    resources_by_path = {resource.path: resource for resource in resources}
    for entry_point in entry_points:
        if not entry_point.active:
            continue
        plan = plans_by_path.get(entry_point.plan)
        if plan is None:
            continue
        plan_links = extract_local_links(root, root / plan.path, plan.text)
        linked_records = [resources_by_path[link] for link in sorted(plan_links) if link in resources_by_path]
        errors.extend(
            f"{plan.path}: active Setup Plan links reference Inventory Record: {record.path}"
            for record in linked_records
            if not record.current
        )
        if not any(entry_point.name in split_list(record.metadata["entry_points"]) for record in linked_records):
            errors.append(f"{plan.path}: active Setup Plan needs a link to a current {entry_point.name} Inventory Record")
        if not export_snapshots(plan_links, entry_point):
            errors.append(f"{plan.path}: active Setup Plan needs a link to an Inventory Export snapshot")

        index = root / entry_point.export_index
        index_text = read_text(root, index, errors) if index.exists() else None
        if index_text is not None and not export_snapshots(extract_local_links(root, index, index_text), entry_point):
            errors.append(f"{entry_point.export_index}: export index needs a link to an Inventory Export snapshot")


def validate_legacy_directories(root: Path, entry_points: list[EntryPoint], errors: list[str]) -> None:
    errors.extend(
        f"{entry_point.name}/: legacy entry point directory at repository root; move it under reference/"
        for entry_point in entry_points
        if (root / entry_point.name).is_dir() and any((root / entry_point.name).iterdir())
    )


def flatpaks_in_adapter(text: str) -> set[str]:
    """Collect app ids from `flatpak install` commands, following line continuations."""
    app_ids: set[str] = set()
    in_install = False
    for line in text.splitlines():
        if "flatpak install" in line:
            in_install = True
        if in_install:
            app_ids.update(FLATPAK_APP_ID_PATTERN.findall(line.split("#", 1)[0]))
            in_install = line.rstrip().endswith("\\")
    return app_ids


def flatpaks_in_record(text: str) -> set[str]:
    """Collect app ids from table rows whose Install Channel cell is `Flatpak`."""
    app_ids: set[str] = set()
    for line in text.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if line.lstrip().startswith("|") and "Flatpak" in cells:
            app_ids.update(
                code for code in re.findall(r"`([^`]+)`", line) if FLATPAK_APP_ID_PATTERN.fullmatch(code)
            )
    return app_ids


def flatpaks_in_export(text: str) -> set[str]:
    """Collect app ids from the bullets under the export's `## Flatpak applications` heading."""
    app_ids: set[str] = set()
    in_section = False
    for line in text.splitlines():
        if line.startswith("## "):
            in_section = line.strip() == "## Flatpak applications"
        elif in_section and line.startswith("- "):
            app_ids.add(line[2:].strip().strip("`"))
    return app_ids


def validate_flatpak_inventory(root: Path, inventory: FlatpakInventory, errors: list[str]) -> None:
    """The adapter installs exactly the exported Flatpaks, and every one is catalogued."""
    texts = {}
    for relative_path in (inventory.provisioning_adapter, inventory.inventory_record, inventory.inventory_export):
        path = root / relative_path
        if not path.exists():
            errors.append(f"{relative_path}: missing Flatpak inventory source")
            return
        text = read_text(root, path, errors)
        if text is None:
            return
        texts[relative_path] = text

    adapter = flatpaks_in_adapter(texts[inventory.provisioning_adapter])
    record = flatpaks_in_record(texts[inventory.inventory_record])
    export = flatpaks_in_export(texts[inventory.inventory_export])
    errors.extend(
        f"{inventory.inventory_export}: Flatpak installed by {inventory.provisioning_adapter} is missing from export: {app_id}"
        for app_id in sorted(adapter - export)
    )
    errors.extend(
        f"{inventory.inventory_export}: exported Flatpak is not installed by {inventory.provisioning_adapter}: {app_id}"
        for app_id in sorted(export - adapter)
    )
    errors.extend(
        f"{inventory.inventory_record}: Flatpak installed by {inventory.provisioning_adapter} has no Inventory Record row: {app_id}"
        for app_id in sorted(adapter - record)
    )


def validate_links(root: Path, errors: list[str]) -> None:
    for path in iter_markdown_files(root):
        text = read_text(root, path, errors)
        if text is None:
            continue
        for destination, target in local_link_targets(path, text):
            if not target.exists():
                errors.append(f"{describe(root, path)}: broken local link: {destination}")


def collect_errors(root: Path = DEFAULT_ROOT) -> list[str]:
    """Run every documentation check against `root` and return the error messages."""
    root = root.resolve()
    errors: list[str] = []
    plans = load_records(root, SETUP_PLAN, errors)
    resources = load_records(root, INVENTORY_RECORD, errors)
    entry_points = entry_points_from_plans(plans, errors)
    validate_resources(resources, entry_points, errors)
    validate_plan_references(plans, resources, entry_points, errors)
    validate_navigation_contract(root, entry_points, errors)
    validate_active_routes(root, plans, resources, entry_points, errors)
    validate_legacy_directories(root, entry_points, errors)
    validate_flatpak_inventory(root, LINUX_FLATPAKS, errors)
    validate_links(root, errors)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help="repository root to validate (default: %(default)s)",
    )
    args = parser.parse_args(argv)
    errors = collect_errors(args.root)
    if errors:
        print("Documentation validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("Documentation validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
