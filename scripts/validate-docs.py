#!/usr/bin/env python3
"""Validate setup catalog metadata, plan references, and local Markdown links."""
from __future__ import annotations

import re
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_RESOURCE_FIELDS = {"id", "title", "entry_points", "execution_mode", "status", "supported", "verified_on", "source_docs"}
REQUIRED_PLAN_FIELDS = {"id", "title", "entry_point", "status", "supported", "verified_on"}
VALID_EXECUTION_MODES = {"manual", "automated", "hybrid"}
VALID_STATUSES = {"current", "reference"}
ISO_DATE_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}")
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
FENCED_CODE_BLOCK_PATTERN = re.compile(r"```.*?```", re.DOTALL)
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


def read_text(path: Path, errors: list[str]) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: unable to read file: {exc}")
        return None


def resolve_within_root(relative: str) -> Path | None:
    target = (ROOT / relative).resolve()
    if not target.is_relative_to(ROOT):
        return None
    return target


def parse_front_matter(text: str) -> dict[str, str]:
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


def iter_local_link_targets(path: Path, text: str) -> list[tuple[str, Path]]:
    targets: list[tuple[str, Path]] = []
    for destination in LINK_PATTERN.findall(strip_fenced_code_blocks(text)):
        destination = destination.split("#", 1)[0].strip()
        if not destination or "://" in destination or destination.startswith(("mailto:", "#")):
            continue
        targets.append((destination, (path.parent / destination).resolve()))
    return targets


def extract_local_links(path: Path, text: str) -> set[str]:
    links: set[str] = set()
    for _, target in iter_local_link_targets(path, text):
        if target.is_relative_to(ROOT):
            links.add(target.relative_to(ROOT).as_posix())
    return links


def is_windows_navigation_target(relative_path: str) -> bool:
    path = PurePosixPath(relative_path)
    lowered_parts = [part.lower() for part in path.parts]
    lowered_name = path.name.lower()
    return "windows" in lowered_parts or "windows" in lowered_name


def validate_resource_metadata(path: Path, metadata: dict[str, str], errors: list[str]) -> bool:
    missing = REQUIRED_RESOURCE_FIELDS - metadata.keys()
    if missing:
        errors.append(f"{path.relative_to(ROOT)}: missing metadata: {', '.join(sorted(missing))}")
        return False
    if metadata["execution_mode"] not in VALID_EXECUTION_MODES:
        errors.append(f"{path.relative_to(ROOT)}: invalid execution_mode")
    if metadata["status"] not in VALID_STATUSES:
        errors.append(f"{path.relative_to(ROOT)}: invalid status")
    if metadata["status"] == "current" and not ISO_DATE_PATTERN.fullmatch(metadata["verified_on"]):
        errors.append(f"{path.relative_to(ROOT)}: current resource needs an ISO verified_on date")
    if metadata["status"] == "reference" and metadata["verified_on"] != "pending":
        errors.append(f"{path.relative_to(ROOT)}: reference resource needs verified_on: pending")
    source = resolve_within_root(metadata["source_docs"])
    if source is None:
        errors.append(f"{path.relative_to(ROOT)}: source_docs escapes repository root: {metadata['source_docs']}")
    elif not source.exists():
        errors.append(f"{path.relative_to(ROOT)}: missing source document: {metadata['source_docs']}")
    return True


def validate_resource_adapter(path: Path, metadata: dict[str, str], errors: list[str]) -> None:
    if metadata["execution_mode"] != "automated":
        return
    adapter = metadata.get("provisioning_adapter")
    if not adapter:
        errors.append(f"{path.relative_to(ROOT)}: automated resource needs provisioning_adapter")
        return
    resolved = resolve_within_root(adapter)
    if resolved is None:
        errors.append(f"{path.relative_to(ROOT)}: provisioning_adapter escapes repository root: {adapter}")
    elif not resolved.exists():
        errors.append(f"{path.relative_to(ROOT)}: missing provisioning adapter: {adapter}")


def validate_resources(errors: list[str]) -> set[str]:
    ids: set[str] = set()
    for path in sorted((ROOT / "catalog").glob("*.md")):
        if path.name == "README.md":
            continue
        text = read_text(path, errors)
        if text is None:
            continue
        metadata = parse_front_matter(text)
        if not validate_resource_metadata(path, metadata, errors):
            continue
        resource_id = metadata["id"]
        if resource_id in ids:
            errors.append(f"{path.relative_to(ROOT)}: duplicate resource id: {resource_id}")
        ids.add(resource_id)
        validate_resource_adapter(path, metadata, errors)
    return ids


def validate_plan_metadata(path: Path, metadata: dict[str, str], errors: list[str]) -> None:
    missing = REQUIRED_PLAN_FIELDS - metadata.keys()
    if missing:
        errors.append(f"{path.relative_to(ROOT)}: missing plan metadata: {', '.join(sorted(missing))}")
        return
    if metadata["status"] not in VALID_STATUSES:
        errors.append(f"{path.relative_to(ROOT)}: invalid status")
    if metadata["status"] == "current" and not ISO_DATE_PATTERN.fullmatch(metadata["verified_on"]):
        errors.append(f"{path.relative_to(ROOT)}: current plan needs an ISO verified_on date")
    if metadata["status"] == "reference" and metadata["verified_on"] != "pending":
        errors.append(f"{path.relative_to(ROOT)}: reference plan needs verified_on: pending")


def validate_plans(resource_ids: set[str], errors: list[str]) -> None:
    for path in sorted((ROOT / "plans").glob("*.md")):
        if path.name == "README.md":
            continue
        text = read_text(path, errors)
        if text is None:
            continue
        metadata = parse_front_matter(text)
        validate_plan_metadata(path, metadata, errors)
        for resource_id in re.findall(r"`([a-z0-9-]+)`", text):
            if resource_id.startswith(("linux-", "android-", "osx-", "synology-", "windows-", "printers-", "self-hosting-")) and resource_id not in resource_ids:
                errors.append(f"{path.relative_to(ROOT)}: unknown resource id: {resource_id}")


def validate_navigation_contract(errors: list[str]) -> None:
    for relative_path, required_links in ROLE_NAVIGATION_REQUIREMENTS.items():
        path = ROOT / relative_path
        if not path.exists():
            errors.append(f"{relative_path}: missing required navigation surface")
            continue
        text = read_text(path, errors)
        if text is None:
            continue
        links = extract_local_links(path, text)
        for required_link in sorted(required_links - links):
            errors.append(f"{relative_path}: missing required navigation link: {required_link}")
        for forbidden_link in sorted(link for link in links if is_windows_navigation_target(link)):
            errors.append(f"{relative_path}: forbidden Windows link in active navigation: {forbidden_link}")


def validate_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = read_text(path, errors)
        if text is None:
            continue
        for destination, target in iter_local_link_targets(path, text):
            if not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link: {destination}")


def collect_errors() -> list[str]:
    errors: list[str] = []
    resource_ids = validate_resources(errors)
    validate_plans(resource_ids, errors)
    validate_navigation_contract(errors)
    validate_links(errors)
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        print("Documentation validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("Documentation validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
