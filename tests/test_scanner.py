from pathlib import Path
import tempfile
import unittest

from ck_preflight.scanner import inspect_project


class ScannerTests(unittest.TestCase):
    def test_fixture_reports_broken_link_and_numeric_mismatch(self):
        fixture = Path(__file__).parents[1] / "examples" / "synthetic-research-project"
        report = inspect_project(fixture)
        ids = [finding.finding_id for finding in report.findings]
        self.assertIn("CKP-LINK-001", ids)
        self.assertIn("CKP-CLAIM-001", ids)
        self.assertEqual(report.file_count, 7)

    def test_clean_project_has_no_findings(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text("# Small project\n", encoding="utf-8")
            report = inspect_project(root)
            self.assertEqual(report.findings, ())

    def test_missing_project_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            missing = Path(temp) / "missing"
            with self.assertRaises(ValueError):
                inspect_project(missing)


if __name__ == "__main__":
    unittest.main()
