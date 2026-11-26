"""Static, local-only checks for a narrow class of research project handoff issues."""

from __future__ import annotations

import csv
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit


MARKDOWN_LINK = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
# Experimental v0 syntax: a bold numeric result described as a difference and
# linked to a CSV with metric,value,unit columns.
LINKED_DIFFERENCE_CLAIM = re.compile(
    r"(?:difference|effect|estimate)[^\n.]*?\*\*"
    r"(?P<value>-?\d+(?:\.\d+)?)\s*(?P<unit>[A-Za-zµμ%]+)\*\*"
    r"[^\n.]*?\]\((?P<target>[^)]+\.csv)(?:\s+[^)]*)?\)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Finding:
    finding_id: str
    title: str
    priority: str
    summary: str
    evidence: str
    recommendation: str
    limitation: str


@dataclass(frozen=True)
class InspectionReport:
    project_name: str
    project_root: str
    file_count: int
    python_file_count: int
    markdown_file_count: int
    csv_file_count: int
    findings: tuple[Finding, ...]
    checks_performed: tuple[str, ...]
    checks_not_performed: tuple[str, ...]

    def to_dict(self) -> dict:
        result = asdict(self)
        result["findings"] = [asdict(item) for item in self.findings]
        return result


def _inside(root: Path, candidate: Path) -> bool:
    try:
        candidate.relative_to(root)
        return True
    except ValueError:
        return False


def _local_target(root: Path, source: Path, destination: str) -> Path | None:
    destination = destination.strip().strip("<>").split("#", 1)[0].split("?", 1)[0]
    parsed = urlsplit(destination)
    if parsed.scheme or parsed.netloc or not destination:
        return None
    target = (source.parent / unquote(destination)).resolve()
    if not _inside(root, target):
        return None
    return target


def _markdown_files(root: Path) -> list[Path]:
    ignored = {".git", ".venv", "venv", "__pycache__", "node_modules"}
    return sorted(
        path for path in root.rglob("*.md")
        if not any(part in ignored for part in path.relative_to(root).parts)
    )


def _check_broken_links(root: Path, markdown_files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for source in markdown_files:
        try:
            lines = source.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError):
            continue
        for line_number, line in enumerate(lines, start=1):
            for match in MARKDOWN_LINK.finditer(line):
                destination = match.group(1).split(maxsplit=1)[0]
                target = _local_target(root, source, destination)
                if target is None or target.exists():
                    continue
                relative_source = source.relative_to(root).as_posix()
                findings.append(Finding(
                    finding_id="CKP-LINK-001",
                    title="A local document link points to a missing file",
                    priority="attention",
                    summary=f"The link target '{destination}' does not exist in this project.",
                    evidence=f"{relative_source}:{line_number} links to {destination}",
                    recommendation="Restore the referenced artifact, correct the link, or explain why the reference is no longer available.",
                    limitation="This check resolves ordinary relative Markdown links only; it does not inspect links embedded in every possible document format.",
                ))
    return findings


def _check_linked_difference_claims(root: Path, markdown_files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for source in markdown_files:
        try:
            lines = source.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError):
            continue
        for line_number, line in enumerate(lines, start=1):
            match = LINKED_DIFFERENCE_CLAIM.search(line)
            if not match:
                continue
            target = _local_target(root, source, match.group("target"))
            if target is None or not target.is_file():
                continue
            try:
                with target.open(newline="", encoding="utf-8") as stream:
                    rows = list(csv.DictReader(stream))
            except (OSError, UnicodeError, csv.Error):
                continue
            matching = [
                row for row in rows
                if row.get("metric", "").strip().lower() == "mean_difference"
            ]
            if len(matching) != 1:
                continue
            row = matching[0]
            try:
                claimed_value = float(match.group("value"))
                evidence_value = float(row["value"])
            except (KeyError, TypeError, ValueError):
                continue
            claimed_unit = match.group("unit").strip().lower()
            evidence_unit = row.get("unit", "").strip().lower()
            if claimed_unit != evidence_unit or abs(claimed_value - evidence_value) <= 1e-9:
                continue
            source_rel = source.relative_to(root).as_posix()
            target_rel = target.relative_to(root).as_posix()
            findings.append(Finding(
                finding_id="CKP-CLAIM-001",
                title="A linked numerical difference does not match its result table",
                priority="high",
                summary=(
                    f"The report states {claimed_value:g} {claimed_unit}, while "
                    f"{target_rel} records {evidence_value:g} {evidence_unit} "
                    "for mean_difference."
                ),
                evidence=f"{source_rel}:{line_number} -> {target_rel} (mean_difference)",
                recommendation="Check whether the report cites the intended run and update either the claim or its evidence reference.",
                limitation=(
                    "Experimental narrow check: recognizes a bold numeric difference/effect/estimate "
                    "on one Markdown line linked to a CSV with metric,value,unit columns. "
                    "It does not interpret arbitrary prose or establish that the underlying analysis is valid."
                ),
            ))
    return findings


def inspect_project(project_path: str | Path) -> InspectionReport:
    root = Path(project_path).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise ValueError(f"Project path is not a directory: {root}")

    ignored = {".git", ".venv", "venv", "__pycache__", "node_modules"}
    files = sorted(
        path for path in root.rglob("*")
        if path.is_file() and not any(part in ignored for part in path.relative_to(root).parts)
    )
    markdown_files = _markdown_files(root)
    findings: list[Finding] = []

    if not any(path.name.lower() in {"readme.md", "readme.rst", "readme.txt"} for path in files):
        findings.append(Finding(
            finding_id="CKP-DOC-001",
            title="No project README was found",
            priority="attention",
            summary="The inspected project has no conventional README file at any depth.",
            evidence="Project file inventory",
            recommendation="Add a short entry point explaining the research question, project structure, data, methods, and how another person can inspect the work.",
            limitation="A README may exist under a nonstandard name or in an external project page that this local inspection cannot see.",
        ))

    findings.extend(_check_broken_links(root, markdown_files))
    findings.extend(_check_linked_difference_claims(root, markdown_files))

    return InspectionReport(
        project_name=root.name,
        project_root=str(root),
        file_count=len(files),
        python_file_count=sum(path.suffix == ".py" for path in files),
        markdown_file_count=len(markdown_files),
        csv_file_count=sum(path.suffix.lower() == ".csv" for path in files),
        findings=tuple(findings),
        checks_performed=(
            "Local file inventory (excluding common environment and version-control directories)",
            "Conventional README presence",
            "Relative local links in Markdown files",
            "Narrow experimental linked numerical-difference check for CSV result tables",
        ),
        checks_not_performed=(
            "No project code, notebooks, shell commands, or workflows were executed",
            "No scientific method, statistical validity, or conclusion was assessed",
            "No runtime dependency or environment installation was tested",
            "No external URLs or remote services were contacted",
            "No privacy, consent, license compatibility, or data-governance review was performed",
            "No claim outside the narrow documented Markdown/CSV pattern was checked",
        ),
    )
