#!/usr/bin/env python3
"""Validate setup catalog metadata, plan references, and local Markdown links."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_RESOURCE_FIELDS = {"id", "title", "entry_points", "execution_mode", "status", "supported", "verified_on", "source_docs"}
REQUIRED_PLAN_FIELDS = {"id", "title", "entry_point", "status", "supported", "verified_on"}
VALID_EXECUTION_MODES = {"manual", "automated", "hybrid"}
VALID_STATUSES = {"current", "reference"}
ISO_DATE_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}")
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def front_matter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
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
    if not (ROOT / metadata["source_docs"]).exists():
        errors.append(f"{path.relative_to(ROOT)}: missing source document: {metadata['source_docs']}")
    return True


def validate_resource_adapter(path: Path, metadata: dict[str, str], errors: list[str]) -> None:
    if metadata["execution_mode"] != "automated":
        return
    adapter = metadata.get("provisioning_adapter")
    if not adapter:
        errors.append(f"{path.relative_to(ROOT)}: automated resource needs provisioning_adapter")
    elif not (ROOT / adapter).exists():
        errors.append(f"{path.relative_to(ROOT)}: missing provisioning adapter: {adapter}")


def validate_resources(errors: list[str]) -> set[str]:
    ids: set[str] = set()
    for path in sorted((ROOT / "catalog").glob("*.md")):
        if path.name == "README.md":
            continue
        metadata = front_matter(path)
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
        validate_plan_metadata(path, front_matter(path), errors)
        for resource_id in re.findall(r"`([a-z0-9-]+)`", path.read_text(encoding="utf-8")):
            if resource_id.startswith(("linux-", "android-", "osx-", "synology-", "windows-", "printers-", "self-hosting-")) and resource_id not in resource_ids:
                errors.append(f"{path.relative_to(ROOT)}: unknown resource id: {resource_id}")


def validate_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", "reference"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        for destination in LINK_PATTERN.findall(text):
            destination = destination.split("#", 1)[0].strip()
            if not destination or "://" in destination or destination.startswith(("mailto:", "#")):
                continue
            target = (path.parent / destination).resolve()
            if not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link: {destination}")


def main() -> int:
    errors: list[str] = []
    resource_ids = validate_resources(errors)
    validate_plans(resource_ids, errors)
    validate_links(errors)
    if errors:
        print("Documentation validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("Documentation validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
