"""Tests for the documentation validator in `validate_docs.py`."""

from __future__ import annotations

import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import validate_docs


class ValidateDocsTests(unittest.TestCase):
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

    def _write_repo(self) -> None:
        self._write(
            "README.md",
            "# Root\n\n"
            "- [Setup Plans](plans/README.md)\n"
            "- [Linux](plans/linux.md)\n"
            "- [macOS](plans/macos.md)\n"
            "- [Android](plans/android.md)\n"
            "- [Resource Catalog](catalog/README.md)\n"
            "- [Inventory Exports](exports/README.md)\n"
            "- [Reference](reference/README.md)\n",
        )
        self._write(
            "plans/README.md",
            "# Plans\n\n"
            "- [Linux](./linux.md)\n"
            "- [macOS](./macos.md)\n"
            "- [Android](./android.md)\n"
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
        self._write(
            "plans/linux.md",
            "---\n"
            "id: linux-setup-plan\n"
            "title: Linux setup plan\n"
            "entry_point: linux\n"
            "status: current\n"
            "supported: Linux\n"
            "verified_on: 2026-08-15\n"
            "---\n\n"
            "- [Catalog](../catalog/README.md)\n"
            "- [Exports](../exports/linux/README.md)\n"
            "- [Reference](../reference/README.md)\n",
        )
        self._write(
            "plans/macos.md",
            "---\n"
            "id: macos-setup-plan\n"
            "title: macOS setup plan\n"
            "entry_point: macos\n"
            "status: current\n"
            "supported: macOS\n"
            "verified_on: 2026-08-15\n"
            "---\n\n"
            "- [Catalog](../catalog/README.md)\n"
            "- [Exports](../exports/macos/README.md)\n"
            "- [Reference](../reference/README.md)\n",
        )
        self._write(
            "plans/android.md",
            "---\n"
            "id: android-setup-plan\n"
            "title: Android setup plan\n"
            "entry_point: android\n"
            "status: current\n"
            "supported: Android\n"
            "verified_on: 2026-08-15\n"
            "---\n\n"
            "- [Catalog](../catalog/README.md)\n"
            "- [Exports](../exports/android/README.md)\n"
            "- [Reference](../reference/README.md)\n",
        )
        self._write(
            "plans/windows.md",
            "---\n"
            "id: windows-setup-plan\n"
            "title: Windows setup plan\n"
            "entry_point: windows\n"
            "status: reference\n"
            "supported: Windows\n"
            "verified_on: pending\n"
            "---\n\n"
            "- [Windows Applications](../windows/Applications.md)\n",
        )
        self._write(
            "exports/linux/README.md",
            "# Linux exports\n\n"
            "- [Linux Plan](../../plans/linux.md)\n"
            "- [Catalog](../../catalog/README.md)\n",
        )
        self._write(
            "exports/macos/README.md",
            "# macOS exports\n\n"
            "- [macOS Plan](../../plans/macos.md)\n"
            "- [Catalog](../../catalog/README.md)\n",
        )
        self._write(
            "exports/android/README.md",
            "# Android exports\n\n"
            "- [Android Plan](../../plans/android.md)\n"
            "- [Catalog](../../catalog/README.md)\n",
        )
        self._write(
            "catalog/example.md",
            "---\n"
            "id: linux-example\n"
            "title: Example\n"
            "entry_points: linux\n"
            "execution_mode: manual\n"
            "status: current\n"
            "supported: Linux\n"
            "verified_on: 2026-08-15\n"
            "source_docs: linux/source.md\n"
            "---\n",
        )
        self._write("linux/source.md", "# Source\n")
        self._write("windows/Applications.md", "# Windows apps\n")

    def _run_validation(self, root: Path | None = None) -> list[str]:
        return validate_docs.collect_errors(root or self.root)

    def test_validation_passes_for_valid_role_navigation(self) -> None:
        self.assertEqual(self._run_validation(), [])

    def test_validation_passes_through_a_symlinked_root(self) -> None:
        link_parent = tempfile.TemporaryDirectory()
        self.addCleanup(link_parent.cleanup)
        link = Path(link_parent.name) / "repo"
        link.symlink_to(self.root, target_is_directory=True)

        self.assertEqual(self._run_validation(link), [])

    def test_validation_rejects_missing_required_navigation_link(self) -> None:
        self._write(
            "README.md",
            "# Root\n\n"
            "- [Setup Plans](plans/README.md)\n"
            "- [Linux](plans/linux.md)\n"
            "- [macOS](plans/macos.md)\n"
            "- [Resource Catalog](catalog/README.md)\n"
            "- [Inventory Exports](exports/README.md)\n"
            "- [Reference](reference/README.md)\n",
        )

        errors = self._run_validation()

        self.assertIn("README.md: missing required navigation link: plans/android.md", errors)

    def test_validation_rejects_windows_link_in_active_navigation(self) -> None:
        self._append("README.md", "- [Windows](plans/windows.md)\n")

        errors = self._run_validation()

        self.assertIn("README.md: forbidden Windows link in active navigation: plans/windows.md", errors)

    def test_navigation_examples_in_code_fences_do_not_satisfy_contract(self) -> None:
        self._write(
            "README.md",
            "# Root\n\n"
            "- [Setup Plans](plans/README.md)\n"
            "- [Linux](plans/linux.md)\n"
            "- [macOS](plans/macos.md)\n"
            "- [Resource Catalog](catalog/README.md)\n"
            "- [Inventory Exports](exports/README.md)\n"
            "- [Reference](reference/README.md)\n\n"
            "```md\n"
            "- [Android](plans/android.md)\n"
            "```\n",
        )

        errors = self._run_validation()

        self.assertIn("README.md: missing required navigation link: plans/android.md", errors)

    def test_reference_links_are_validated(self) -> None:
        self._append("reference/README.md", "- [Missing](../reference/missing.md)\n")

        errors = self._run_validation()

        self.assertIn("reference/README.md: broken local link: ../reference/missing.md", errors)

    def test_titled_and_angle_bracket_links_are_resolved(self) -> None:
        self._append(
            "reference/README.md",
            '- [Titled](../linux/source.md "Source doc")\n- [Angled](<../linux/source.md>)\n',
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


class AndroidMigrationTests(unittest.TestCase):
    def _read(self, relative_path: str) -> str:
        path = validate_docs.DEFAULT_ROOT / relative_path
        self.assertTrue(path.exists(), f"{relative_path} does not exist")
        return path.read_text(encoding="utf-8")

    def _front_matter(self, relative_path: str) -> dict[str, str]:
        return validate_docs.parse_front_matter(self._read(relative_path))

    def test_android_plan_links_to_canonical_application_catalog(self) -> None:
        text = self._read("plans/android.md")
        self.assertIn("[Android application catalog](../catalog/android-application-catalog.md)", text)

    def test_android_plan_links_to_inventory_export(self) -> None:
        text = self._read("plans/android.md")
        self.assertIn("[Primary device export](../exports/android/primary-device.md)", text)

    def test_android_plan_does_not_reference_legacy_applications(self) -> None:
        text = self._read("plans/android.md")
        self.assertNotIn("../android/Applications.md", text)

    def test_android_export_index_links_to_primary_device(self) -> None:
        text = self._read("exports/android/README.md")
        self.assertIn("[Primary device](./primary-device.md)", text)

    def test_android_catalog_is_current(self) -> None:
        metadata = self._front_matter("catalog/android-application-catalog.md")
        self.assertEqual(metadata.get("status"), "current")
        self.assertRegex(metadata.get("verified_on", ""), r"\d{4}-\d{2}-\d{2}")

    def test_legacy_android_applications_moved_to_reference(self) -> None:
        legacy_path = validate_docs.DEFAULT_ROOT / "android" / "Applications.md"
        reference_path = validate_docs.DEFAULT_ROOT / "reference" / "android" / "Applications.md"
        self.assertFalse(legacy_path.exists(), "legacy android/Applications.md should no longer exist")
        self.assertTrue(reference_path.exists(), "reference/android/Applications.md should exist")


class LinuxMigrationTests(unittest.TestCase):
    def _read(self, relative_path: str) -> str:
        path = validate_docs.DEFAULT_ROOT / relative_path
        self.assertTrue(path.exists(), f"{relative_path} does not exist")
        return path.read_text(encoding="utf-8")

    def test_linux_plan_links_to_inventory_export(self) -> None:
        text = self._read("plans/linux.md")
        self.assertIn("[Primary machine export](../exports/linux/primary-machine.md)", text)

    def test_linux_plan_does_not_reference_legacy_navigation_roots(self) -> None:
        text = self._read("plans/linux.md")
        self.assertNotIn("../linux/", text)
        self.assertNotIn("./linux/", text)

    def test_linux_export_index_links_to_primary_machine(self) -> None:
        text = self._read("exports/linux/README.md")
        self.assertIn("[Primary machine](./primary-machine.md)", text)

    def test_legacy_linux_files_moved_to_reference(self) -> None:
        legacy_dir = validate_docs.DEFAULT_ROOT / "linux"
        reference_dir = validate_docs.DEFAULT_ROOT / "reference" / "linux"
        self.assertFalse(legacy_dir.exists(), "legacy linux/ directory should no longer exist")
        self.assertTrue(reference_dir.exists(), "reference/linux/ directory should exist")
        self.assertTrue((reference_dir / "Applications.md").exists())
        self.assertTrue((reference_dir / "Desktop-Setup.md").exists())


if __name__ == "__main__":
    unittest.main()
