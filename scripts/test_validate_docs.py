from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("validate-docs.py")
SPEC = importlib.util.spec_from_file_location("validate_docs", MODULE_PATH)
validate_docs = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validate_docs)


class ValidateDocsNavigationContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.original_root = validate_docs.ROOT
        validate_docs.ROOT = self.root
        self._write_repo()

    def tearDown(self) -> None:
        validate_docs.ROOT = self.original_root
        self.temp_dir.cleanup()

    def _write(self, relative_path: str, content: str) -> None:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

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

    def _run_validation(self) -> list[str]:
        return validate_docs.collect_errors()

    def test_validation_passes_for_valid_role_navigation(self) -> None:
        self.assertEqual(self._run_validation(), [])

    def test_validation_rejects_missing_required_navigation_link(self) -> None:
        readme = self.root / "README.md"
        readme.write_text(
            "# Root\n\n"
            "- [Setup Plans](plans/README.md)\n"
            "- [Linux](plans/linux.md)\n"
            "- [macOS](plans/macos.md)\n"
            "- [Resource Catalog](catalog/README.md)\n"
            "- [Inventory Exports](exports/README.md)\n"
            "- [Reference](reference/README.md)\n",
            encoding="utf-8",
        )

        errors = self._run_validation()

        self.assertIn("README.md: missing required navigation link: plans/android.md", errors)

    def test_validation_rejects_windows_link_in_active_navigation(self) -> None:
        readme = self.root / "README.md"
        readme.write_text(
            readme.read_text(encoding="utf-8") + "- [Windows](plans/windows.md)\n",
            encoding="utf-8",
        )

        errors = self._run_validation()

        self.assertIn("README.md: forbidden Windows link in active navigation: plans/windows.md", errors)

    def test_navigation_examples_in_code_fences_do_not_satisfy_contract(self) -> None:
        readme = self.root / "README.md"
        readme.write_text(
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
            encoding="utf-8",
        )

        errors = self._run_validation()

        self.assertIn("README.md: missing required navigation link: plans/android.md", errors)

    def test_reference_links_are_validated(self) -> None:
        reference = self.root / "reference/README.md"
        reference.write_text(
            reference.read_text(encoding="utf-8") + "- [Missing](../reference/missing.md)\n",
            encoding="utf-8",
        )

        errors = self._run_validation()

        self.assertIn("reference/README.md: broken local link: ../reference/missing.md", errors)


if __name__ == "__main__":
    unittest.main()
