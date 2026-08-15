#!/usr/bin/env python3
"""Validate setup catalog metadata, plan references, and local Markdown links."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path, PurePosixPath

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
REQUIRED_RESOURCE_FIELDS = {
    "id",
    "title",
    "entry_points",
    "execution_mode",
    "status",
    "supported",
    "verified_on",
    "source_docs",
}
REQUIRED_PLAN_FIELDS = {"id", "title", "entry_point", "status", "supported", "verified_on"}
VALID_EXECUTION_MODES = {"manual", "automated", "hybrid"}
VALID_STATUSES = {"current", "reference"}
RESOURCE_ID_PREFIXES = (
    "linux-",
    "android-",
    "osx-",
    "synology-",
    "windows-",
    "printers-",
    "self-hosting-",
)
IGNORED_DIRECTORIES = {".git", "node_modules", "__pycache__"}
ISO_DATE_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}")
LINK_PATTERN = re.compile(r"""(?<!!)\[[^\]]*\]\(\s*(<[^>]*>|[^\s)]+)(?:\s+["'(][^)]*)?\)""")
FENCED_CODE_BLOCK_PATTERN = re.compile(r"^[ \t]*(`{3,}|~{3,}).*?^[ \t]*\1[ \t]*$", re.DOTALL | re.MULTILINE)
ROLE_NAVIGATION_REQUIREMENTS = {
    "README.md": {
        "plans/README.md",
        "plans/linux.md",
        "plans/macos.md",
        "plans/android.md",
        "catalog/README.md",
        "exports/README.md",
        "reference/README.md",
    },
    "plans/README.md": {
        "plans/linux.md",
        "plans/macos.md",
        "plans/android.md",
        "catalog/README.md",
        "exports/README.md",
        "reference/README.md",
    },
    "catalog/README.md": {
        "plans/README.md",
        "exports/README.md",
        "reference/README.md",
    },
    "exports/README.md": {
        "README.md",
        "plans/README.md",
        "catalog/README.md",
        "reference/README.md",
    },
    "reference/README.md": {
        "README.md",
        "plans/README.md",
        "catalog/README.md",
        "exports/README.md",
    },
    "plans/linux.md": {
        "catalog/README.md",
        "exports/linux/README.md",
        "reference/README.md",
    },
    "plans/macos.md": {
        "catalog/README.md",
        "exports/macos/README.md",
        "reference/README.md",
    },
    "plans/android.md": {
        "catalog/README.md",
        "exports/android/README.md",
        "reference/README.md",
    },
    "exports/linux/README.md": {
        "plans/linux.md",
        "catalog/README.md",
    },
    "exports/macos/README.md": {
        "plans/macos.md",
        "catalog/README.md",
    },
    "exports/android/README.md": {
        "plans/android.md",
        "catalog/README.md",
    },
}


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


def is_windows_navigation_target(relative_path: str) -> bool:
    path = PurePosixPath(relative_path)
    lowered_parts = [part.lower() for part in path.parts]
    return "windows" in lowered_parts or "windows" in path.name.lower()


def validate_resource_metadata(root: Path, path: Path, metadata: dict[str, str], errors: list[str]) -> bool:
    """Validate one catalog resource, returning False when required fields are missing."""
    label = describe(root, path)
    missing = REQUIRED_RESOURCE_FIELDS - metadata.keys()
    if missing:
        errors.append(f"{label}: missing metadata: {', '.join(sorted(missing))}")
        return False
    if metadata["execution_mode"] not in VALID_EXECUTION_MODES:
        errors.append(f"{label}: invalid execution_mode")
    if metadata["status"] not in VALID_STATUSES:
        errors.append(f"{label}: invalid status")
    if metadata["status"] == "current" and not ISO_DATE_PATTERN.fullmatch(metadata["verified_on"]):
        errors.append(f"{label}: current resource needs an ISO verified_on date")
    if metadata["status"] == "reference" and metadata["verified_on"] != "pending":
        errors.append(f"{label}: reference resource needs verified_on: pending")
    source_docs = metadata["source_docs"]
    source = resolve_within_root(root, source_docs)
    if source is None:
        errors.append(f"{label}: source_docs escapes repository root: {source_docs}")
    elif not source.exists():
        errors.append(f"{label}: missing source document: {source_docs}")
    return True


def validate_resource_adapter(root: Path, path: Path, metadata: dict[str, str], errors: list[str]) -> None:
    if metadata["execution_mode"] != "automated":
        return
    label = describe(root, path)
    adapter = metadata.get("provisioning_adapter")
    if not adapter:
        errors.append(f"{label}: automated resource needs provisioning_adapter")
        return
    resolved = resolve_within_root(root, adapter)
    if resolved is None:
        errors.append(f"{label}: provisioning_adapter escapes repository root: {adapter}")
    elif not resolved.exists():
        errors.append(f"{label}: missing provisioning adapter: {adapter}")


def validate_resources(root: Path, errors: list[str]) -> set[str]:
    ids: set[str] = set()
    for path in sorted((root / "catalog").glob("*.md")):
        if path.name == "README.md":
            continue
        text = read_text(root, path, errors)
        if text is None:
            continue
        metadata = parse_front_matter(text)
        if not validate_resource_metadata(root, path, metadata, errors):
            continue
        resource_id = metadata["id"]
        if resource_id in ids:
            errors.append(f"{describe(root, path)}: duplicate resource id: {resource_id}")
        ids.add(resource_id)
        validate_resource_adapter(root, path, metadata, errors)
    return ids


def validate_plan_metadata(root: Path, path: Path, metadata: dict[str, str], errors: list[str]) -> None:
    label = describe(root, path)
    missing = REQUIRED_PLAN_FIELDS - metadata.keys()
    if missing:
        errors.append(f"{label}: missing plan metadata: {', '.join(sorted(missing))}")
        return
    if metadata["status"] not in VALID_STATUSES:
        errors.append(f"{label}: invalid status")
    if metadata["status"] == "current" and not ISO_DATE_PATTERN.fullmatch(metadata["verified_on"]):
        errors.append(f"{label}: current plan needs an ISO verified_on date")
    if metadata["status"] == "reference" and metadata["verified_on"] != "pending":
        errors.append(f"{label}: reference plan needs verified_on: pending")


def validate_plans(root: Path, resource_ids: set[str], errors: list[str]) -> None:
    for path in sorted((root / "plans").glob("*.md")):
        if path.name == "README.md":
            continue
        text = read_text(root, path, errors)
        if text is None:
            continue
        metadata = parse_front_matter(text)
        validate_plan_metadata(root, path, metadata, errors)
        errors.extend(
            f"{describe(root, path)}: unknown resource id: {resource_id}"
            for resource_id in re.findall(r"`([a-z0-9-]+)`", text)
            if resource_id.startswith(RESOURCE_ID_PREFIXES) and resource_id not in resource_ids
        )


def validate_navigation_contract(root: Path, errors: list[str]) -> None:
    for relative_path, required_links in ROLE_NAVIGATION_REQUIREMENTS.items():
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
        errors.extend(
            f"{relative_path}: forbidden Windows link in active navigation: {forbidden_link}"
            for forbidden_link in sorted(link for link in links if is_windows_navigation_target(link))
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
    resource_ids = validate_resources(root, errors)
    validate_plans(root, resource_ids, errors)
    validate_navigation_contract(root, errors)
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
