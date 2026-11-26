"""Command-line entry point."""

from __future__ import annotations

import argparse
from pathlib import Path

from .report import write_reports
from .scanner import inspect_project


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="ck-preflight",
        description="Statically inspect a local research project and write an evidence-linked report.",
    )
    parser.add_argument("project", type=Path, help="Path to the local project directory")
    parser.add_argument("--output", type=Path, required=True, help="Report directory outside the inspected project")
    args = parser.parse_args()

    try:
        report = inspect_project(args.project)
        html_path, json_path = write_reports(report, args.output)
    except (OSError, ValueError) as error:
        parser.error(str(error))

    print(f"Inspected: {report.project_name}")
    print(f"Files: {report.file_count}")
    print(f"Findings: {len(report.findings)}")
    print(f"HTML report: {html_path}")
    print(f"JSON report: {json_path}")
    print("No project code was executed.")
    return 0
