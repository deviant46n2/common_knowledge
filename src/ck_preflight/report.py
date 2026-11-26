"""Portable HTML and JSON report rendering."""

from __future__ import annotations

import html
import json
from pathlib import Path

from .scanner import InspectionReport


def write_reports(report: InspectionReport, output_dir: str | Path) -> tuple[Path, Path]:
    destination = Path(output_dir).expanduser().resolve()
    if destination == Path(report.project_root) or Path(report.project_root) in destination.parents:
        raise ValueError("Choose an output directory outside the inspected project.")
    destination.mkdir(parents=True, exist_ok=True)

    json_path = destination / "preflight-report.json"
    html_path = destination / "preflight-report.html"
    json_path.write_text(json.dumps(report.to_dict(), indent=2), encoding="utf-8")
    html_path.write_text(render_html(report), encoding="utf-8")
    return html_path, json_path


def render_html(report: InspectionReport) -> str:
    findings_html = []
    for finding in report.findings:
        findings_html.append(
            '<article class="finding">'
            f'<div class="finding-meta"><span>{html.escape(finding.finding_id)}</span>'
            f'<span class="priority {html.escape(finding.priority)}">{html.escape(finding.priority)}</span></div>'
            f'<h3>{html.escape(finding.title)}</h3>'
            f'<p>{html.escape(finding.summary)}</p>'
            f'<p class="evidence"><strong>Evidence</strong> · {html.escape(finding.evidence)}</p>'
            f'<p><strong>Suggested next step</strong> · {html.escape(finding.recommendation)}</p>'
            f'<p class="limitation"><strong>Limit</strong> · {html.escape(finding.limitation)}</p>'
            '</article>'
        )
    if not findings_html:
        findings_html.append(
            '<div class="empty"><h3>No findings from the checks performed</h3>'
            '<p>This is not a certification or proof of research validity. Review the inspection limits below.</p></div>'
        )

    checks = "".join(f"<li>{html.escape(item)}</li>" for item in report.checks_performed)
    limits = "".join(f"<li>{html.escape(item)}</li>" for item in report.checks_not_performed)
    count = len(report.findings)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Research project preflight · {html.escape(report.project_name)}</title>
<style>
:root {{ color-scheme: light; --ink:#202b2b; --muted:#657372; --paper:#f6f5ef; --surface:#fffefa; --line:#dce1dc; --teal:#286a66; --amber:#a76722; --red:#9b403a; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--paper); color:var(--ink); font:16px/1.55 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
header {{ background:var(--ink); color:#f7f7f0; padding:2.5rem max(1.25rem,calc((100vw - 920px)/2)); }}
.eyebrow {{ color:#a8c8c1; text-transform:uppercase; letter-spacing:.12em; font-size:.76rem; font-weight:700; }}
h1 {{ margin:.45rem 0 .25rem; font-size:clamp(1.8rem,4vw,2.7rem); line-height:1.12; font-weight:650; }}
header p {{ color:#d0d9d4; margin:.5rem 0 0; }}
main {{ max-width:920px; margin:2rem auto 4rem; padding:0 1.25rem; }}
.summary {{ display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:.75rem; margin-bottom:2rem; }}
.metric {{ background:var(--surface); border:1px solid var(--line); border-radius:12px; padding:1rem; }}
.metric strong {{ display:block; font-size:1.65rem; line-height:1.2; }}
.metric span {{ color:var(--muted); font-size:.85rem; }}
h2 {{ font-size:1.25rem; margin:2rem 0 .8rem; }}
.finding,.empty,.panel {{ background:var(--surface); border:1px solid var(--line); border-radius:12px; padding:1.1rem 1.2rem; margin:.75rem 0; }}
.finding h3,.empty h3 {{ margin:.5rem 0; font-size:1.05rem; }}
.finding p {{ margin:.5rem 0; }}
.finding-meta {{ display:flex; justify-content:space-between; color:var(--muted); font: .78rem ui-monospace,monospace; }}
.priority {{ text-transform:uppercase; letter-spacing:.08em; font-weight:700; }}
.priority.high {{ color:var(--red); }} .priority.attention {{ color:var(--amber); }}
.evidence {{ background:#f1f3ed; padding:.55rem .7rem; border-radius:7px; overflow-wrap:anywhere; }}
.limitation {{ color:var(--muted); font-size:.9rem; }}
.panel ul {{ margin:.35rem 0; padding-left:1.25rem; }}
footer {{ color:var(--muted); font-size:.85rem; border-top:1px solid var(--line); padding-top:1rem; margin-top:2rem; }}
@media(max-width:620px) {{ .summary {{ grid-template-columns:repeat(2,minmax(0,1fr)); }} header {{ padding:2rem 1.25rem; }} }}
</style>
</head>
<body>
<header>
  <div class="eyebrow">Common Knowledge · Research project preflight</div>
  <h1>{html.escape(report.project_name)}</h1>
  <p>A local, static inspection of project handoff signals. No project code was executed.</p>
</header>
<main>
  <section class="summary" aria-label="Project inventory">
    <div class="metric"><strong>{report.file_count}</strong><span>Files inspected</span></div>
    <div class="metric"><strong>{report.python_file_count}</strong><span>Python files</span></div>
    <div class="metric"><strong>{report.markdown_file_count}</strong><span>Markdown files</span></div>
    <div class="metric"><strong>{count}</strong><span>Findings</span></div>
  </section>
  <h2>Findings and next steps</h2>
  {''.join(findings_html)}
  <h2>Checks performed</h2>
  <section class="panel"><ul>{checks}</ul></section>
  <h2>What this report does not establish</h2>
  <section class="panel"><ul>{limits}</ul></section>
  <footer>Inspection scope: {html.escape(report.project_root)} · Common Knowledge prototype 0.1.0</footer>
</main>
</body>
</html>
"""
