"""Tests for the documentation validator in `validate_docs.py`."""

from __future__ import annotations

import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import validate_docs


def plan(entry_point: str, status: str = "current", extra_metadata: str = "", body: str = "") -> str:
    verified_on = "2026-08-15" if status == "current" else "pending"
    return (
        "---\n"
        f"id: {entry_point}-setup-plan\n"
        f"title: {entry_point} setup plan\n"
        f"entry_point: {entry_point}\n"
        f"status: {status}\n"
        f"supported: {entry_point}\n"
        f"verified_on: {verified_on}\n"
        f"{extra_metadata}"
        "---\n\n"
        f"{body}"
    )


def record(record_id: str, entry_points: str, status: str = "current", extra_metadata: str = "", body: str = "") -> str:
    verified_on = "2026-08-15" if status == "current" else "pending"
    return (
        "---\n"
        f"id: {record_id}\n"
        f"title: {record_id}\n"
        f"entry_points: {entry_points}\n"
        "execution_mode: manual\n"
        f"status: {status}\n"
        "supported: Linux\n"
        f"verified_on: {verified_on}\n"
        "source_docs: reference/linux/source.md\n"
        f"{extra_metadata}"
        "---\n\n"
        f"{body}"
    )


LINUX_PLAN_BODY = (
    "Apply `linux-application-catalog`.\n\n"
    "- [Catalog](../catalog/README.md)\n"
    "- [Linux apps](../catalog/linux-application-catalog.md)\n"
    "- [Exports](../exports/linux/README.md)\n"
    "- [Primary machine export](../exports/linux/primary-machine.md)\n"
    "- [Reference](../reference/README.md)\n"
)


class ValidatorFixture(unittest.TestCase):
    """A minimal valid repository: Linux is an active Entry Point, Windows is retired."""

    def setUp(self) -> None:
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        self.root = Path(temp_dir.name).resolve()
        self._write_repo()

    def _write(self, relative_path: str, content: str) -> None:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def _append(self, relative_path: str, content: str) -> None:
        path = self.root / relative_path
        self._write(relative_path, path.read_text(encoding="utf-8") + content)

    def _replace(self, relative_path: str, old: str, new: str) -> None:
        path = self.root / relative_path
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        self._write(relative_path, text.replace(old, new))

    def _run_validation(self, root: Path | None = None) -> list[str]:
        return validate_docs.collect_errors(root or self.root)

    def _write_repo(self) -> None:
        self._write(
            "README.md",
            "# Root\n\n"
            "- [Setup Plans](plans/README.md)\n"
            "- [Linux](plans/linux.md)\n"
            "- [Resource Catalog](catalog/README.md)\n"
            "- [Inventory Exports](exports/README.md)\n"
            "- [Reference](reference/README.md)\n",
        )
        self._write(
            "plans/README.md",
            "# Plans\n\n"
            "- [Linux](./linux.md)\n"
            "- [Catalog](../catalog/README.md)\n"
            "- [Exports](../exports/README.md)\n"
            "- [Reference](../reference/README.md)\n",
        )
        self._write(
            "catalog/README.md",
            "# Catalog\n\n"
            "- [Plans](../plans/README.md)\n"
            "- [Exports](../exports/README.md)\n"
            "- [Reference](../reference/README.md)\n",
        )
        self._write(
            "exports/README.md",
            "# Exports\n\n"
            "- [Root](../README.md)\n"
            "- [Plans](../plans/README.md)\n"
            "- [Catalog](../catalog/README.md)\n"
            "- [Reference](../reference/README.md)\n",
        )
        self._write(
            "reference/README.md",
            "# Reference\n\n"
            "- [Root](../README.md)\n"
            "- [Plans](../plans/README.md)\n"
            "- [Catalog](../catalog/README.md)\n"
            "- [Exports](../exports/README.md)\n",
        )
        self._write("plans/linux.md", plan("linux", body=LINUX_PLAN_BODY))
        self._write("plans/windows.md", plan("windows", status="reference"))
        self._write(
            "exports/linux/README.md",
            "# Linux exports\n\n"
            "- [Linux Plan](../../plans/linux.md)\n"
            "- [Catalog](../../catalog/README.md)\n"
            "- [Primary machine](./primary-machine.md)\n",
        )
        self._write(
            "exports/linux/primary-machine.md",
            "# Primary machine\n\n## Flatpak applications\n\n- org.example.Editor\n\n## Other\n\n- not.a.flatpak.Id\n",
        )
        self._write(
            "catalog/linux-application-catalog.md",
            record(
                "linux-application-catalog",
                "linux",
                body="| Application | Install Channel | Notes |\n"
                "| --- | --- | --- |\n"
                "| Editor | Flatpak | `org.example.Editor` from Flathub. |\n"
                "| Optional | Flatpak | `org.example.Optional`; install manually. |\n",
            ),
        )
        self._write(
            "environment/SetupLinux.sh",
            "#!/bin/bash\n"
            "sudo flatpak install --system --noninteractive flathub \\\n"
            "  org.example.Editor\n"
            "echo done.with.three.parts\n",
        )
        self._write("reference/linux/source.md", "# Source\n")
        self._write("reference/windows/Applications.md", "# Windows apps\n")


class NavigationContractTests(ValidatorFixture):
    def test_validation_passes_for_valid_role_navigation(self) -> None:
        self.assertEqual(self._run_validation(), [])

    def test_validation_passes_through_a_symlinked_root(self) -> None:
        link_parent = tempfile.TemporaryDirectory()
        self.addCleanup(link_parent.cleanup)
        link = Path(link_parent.name) / "repo"
        link.symlink_to(self.root, target_is_directory=True)

        self.assertEqual(self._run_validation(link), [])

    def test_validation_rejects_missing_required_navigation_link(self) -> None:
        self._replace("README.md", "- [Linux](plans/linux.md)\n", "")

        errors = self._run_validation()

        self.assertIn("README.md: missing required navigation link: plans/linux.md", errors)

    def test_activating_an_entry_point_derives_its_navigation_requirements(self) -> None:
        self._write("plans/windows.md", plan("windows"))

        errors = self._run_validation()

        self.assertIn("README.md: missing required navigation link: plans/windows.md", errors)
        self.assertIn("plans/README.md: missing required navigation link: plans/windows.md", errors)
        self.assertIn("plans/windows.md: missing required navigation link: exports/windows/README.md", errors)
        self.assertIn("exports/windows/README.md: missing required navigation surface", errors)

    def test_validation_rejects_retired_entry_point_link_in_active_navigation(self) -> None:
        self._append("README.md", "- [Windows](plans/windows.md)\n")
        self._append("reference/README.md", "- [Windows apps](./windows/Applications.md)\n")

        errors = self._run_validation()

        self.assertIn("README.md: forbidden link to retired entry point windows: plans/windows.md", errors)
        self.assertIn(
            "reference/README.md: forbidden link to retired entry point windows: reference/windows/Applications.md",
            errors,
        )

    def test_every_retired_entry_point_is_guarded(self) -> None:
        self._write("plans/synology.md", plan("synology", status="reference"))
        self._write("reference/synology/Apps.md", "# Synology apps\n")
        self._append("plans/README.md", "- [Synology](../reference/synology/Apps.md)\n")

        errors = self._run_validation()

        self.assertIn(
            "plans/README.md: forbidden link to retired entry point synology: reference/synology/Apps.md", errors
        )

    def test_navigation_examples_in_code_fences_do_not_satisfy_contract(self) -> None:
        self._replace("README.md", "- [Linux](plans/linux.md)\n", "```md\n- [Linux](plans/linux.md)\n```\n")

        errors = self._run_validation()

        self.assertIn("README.md: missing required navigation link: plans/linux.md", errors)


class ActiveRouteTests(ValidatorFixture):
    def test_active_plan_needs_an_export_snapshot_link(self) -> None:
        self._replace("plans/linux.md", "- [Primary machine export](../exports/linux/primary-machine.md)\n", "")

        errors = self._run_validation()

        self.assertIn("plans/linux.md: active Setup Plan needs a link to an Inventory Export snapshot", errors)

    def test_export_index_needs_a_snapshot_link(self) -> None:
        self._replace("exports/linux/README.md", "- [Primary machine](./primary-machine.md)\n", "")

        errors = self._run_validation()

        self.assertIn("exports/linux/README.md: export index needs a link to an Inventory Export snapshot", errors)

    def test_active_plan_needs_a_current_inventory_record_for_its_entry_point(self) -> None:
        self._replace("plans/linux.md", "- [Linux apps](../catalog/linux-application-catalog.md)\n", "")

        errors = self._run_validation()

        self.assertIn("plans/linux.md: active Setup Plan needs a link to a current linux Inventory Record", errors)

    def test_active_plan_rejects_reference_inventory_records(self) -> None:
        self._write("catalog/linux-old.md", record("linux-old", "linux", status="reference"))
        self._append("plans/linux.md", "- [Old](../catalog/linux-old.md)\n")

        errors = self._run_validation()

        self.assertIn("plans/linux.md: active Setup Plan links reference Inventory Record: catalog/linux-old.md", errors)

    def test_legacy_entry_point_directory_at_root_is_rejected(self) -> None:
        self._write("windows/Applications.md", "# Windows apps\n")

        errors = self._run_validation()

        self.assertIn("windows/: legacy entry point directory at repository root; move it under reference/", errors)

    def test_empty_legacy_directory_is_ignored(self) -> None:
        (self.root / "linux").mkdir()

        self.assertEqual(self._run_validation(), [])


class RecordSchemaTests(ValidatorFixture):
    def test_plan_provisioning_adapter_is_root_relative(self) -> None:
        self._write(
            "plans/linux.md",
            plan("linux", extra_metadata="provisioning_adapter: ../environment/SetupLinux.sh\n", body=LINUX_PLAN_BODY),
        )

        errors = self._run_validation()

        self.assertIn(
            "plans/linux.md: provisioning_adapter escapes repository root: ../environment/SetupLinux.sh", errors
        )

    def test_plan_provisioning_adapter_must_exist(self) -> None:
        self._write(
            "plans/linux.md",
            plan("linux", extra_metadata="provisioning_adapter: environment/Missing.sh\n", body=LINUX_PLAN_BODY),
        )

        errors = self._run_validation()

        self.assertIn(
            "plans/linux.md: provisioning_adapter does not exist relative to repository root: environment/Missing.sh",
            errors,
        )

    def test_lifecycle_rules_apply_to_both_record_kinds(self) -> None:
        self._replace("plans/linux.md", "verified_on: 2026-08-15", "verified_on: soon")
        self._replace("catalog/linux-application-catalog.md", "verified_on: 2026-08-15", "verified_on: soon")

        errors = self._run_validation()

        self.assertIn("plans/linux.md: current plan needs an ISO verified_on date", errors)
        self.assertIn("catalog/linux-application-catalog.md: current resource needs an ISO verified_on date", errors)

    def test_automated_resource_needs_provisioning_adapter(self) -> None:
        self._replace("catalog/linux-application-catalog.md", "execution_mode: manual", "execution_mode: automated")

        errors = self._run_validation()

        self.assertIn("catalog/linux-application-catalog.md: automated resource needs provisioning_adapter", errors)

    def test_missing_plan_metadata_is_reported(self) -> None:
        self._replace("plans/windows.md", "supported: windows\n", "")

        errors = self._run_validation()

        self.assertIn("plans/windows.md: missing plan metadata: supported", errors)

    def test_resource_entry_points_must_be_known(self) -> None:
        self._replace("catalog/linux-application-catalog.md", "entry_points: linux", "entry_points: linux, beos")

        errors = self._run_validation()

        self.assertIn("catalog/linux-application-catalog.md: unknown entry point: beos", errors)

    def test_plan_resource_ids_are_checked_for_every_entry_point_and_shared_records(self) -> None:
        self._append("plans/linux.md", "Then apply `shared-missing` and `windows-missing`.\n")

        errors = self._run_validation()

        self.assertIn("plans/linux.md: unknown resource id: shared-missing", errors)
        self.assertIn("plans/linux.md: unknown resource id: windows-missing", errors)


class FlatpakInventoryTests(ValidatorFixture):
    def test_adapter_flatpak_missing_from_export_and_record(self) -> None:
        self._replace("environment/SetupLinux.sh", "  org.example.Editor\n", "  org.example.Editor \\\n  org.example.New\n")

        errors = self._run_validation()

        self.assertIn(
            "exports/linux/primary-machine.md: Flatpak installed by environment/SetupLinux.sh is missing from export: "
            "org.example.New",
            errors,
        )
        self.assertIn(
            "catalog/linux-application-catalog.md: Flatpak installed by environment/SetupLinux.sh has no "
            "Inventory Record row: org.example.New",
            errors,
        )

    def test_exported_flatpak_not_installed_by_adapter(self) -> None:
        self._replace("exports/linux/primary-machine.md", "- org.example.Editor\n", "- org.example.Editor\n- org.example.Typo\n")

        errors = self._run_validation()

        self.assertIn(
            "exports/linux/primary-machine.md: exported Flatpak is not installed by environment/SetupLinux.sh: "
            "org.example.Typo",
            errors,
        )


class LinkTests(ValidatorFixture):
    def test_reference_links_are_validated(self) -> None:
        self._append("reference/README.md", "- [Missing](../reference/missing.md)\n")

        errors = self._run_validation()

        self.assertIn("reference/README.md: broken local link: ../reference/missing.md", errors)

    def test_titled_and_angle_bracket_links_are_resolved(self) -> None:
        self._append(
            "reference/README.md",
            '- [Titled](./linux/source.md "Source doc")\n- [Angled](<./linux/source.md>)\n',
        )

        self.assertEqual(self._run_validation(), [])

    def test_links_inside_tilde_fences_are_ignored(self) -> None:
        self._append("reference/README.md", "~~~md\n- [Missing](./missing.md)\n~~~\n")

        self.assertEqual(self._run_validation(), [])

    def test_ignored_directories_are_not_scanned(self) -> None:
        self._write("node_modules/pkg/README.md", "- [Missing](./missing.md)\n")

        self.assertEqual(self._run_validation(), [])


class ValidateDocsCliTests(unittest.TestCase):
    def test_main_reports_failures_on_stderr(self) -> None:
        stdout, stderr = io.StringIO(), io.StringIO()
        with tempfile.TemporaryDirectory() as temp_dir, redirect_stdout(stdout), redirect_stderr(stderr):
            exit_code = validate_docs.main(["--root", temp_dir])

        self.assertEqual(exit_code, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("missing required navigation surface", stderr.getvalue())

    def test_main_passes_for_the_repository(self) -> None:
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            exit_code = validate_docs.main([])

        self.assertEqual(exit_code, 0)
        self.assertIn("Documentation validation passed.", stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
