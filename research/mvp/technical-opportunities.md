# Technical Opportunities and Integration Hypotheses

- **Established:** 26 November 2026
- **Status:** Preliminary technical investigation
- **Purpose:** Identify reusable standards and technical building blocks for the two leading MVP opportunity areas without prematurely fixing an architecture.

## 1. Design stance

Common Knowledge should not invent a new research metadata format, provenance vocabulary, workflow engine, or AI observability backend unless evidence shows that existing standards cannot meet a necessary requirement.

Prefer local-first processing where feasible; established interchange formats; explicit user control over data and logs; deterministic checks before probabilistic interpretation; read-only inspection before write or execution permissions; inspectable and exportable outputs; adapters to existing tools; and a clear distinction between observed evidence, inferred findings, and unknowns.

## 2. Research handoff / readiness diagnostic

### Potential input
- Local project directory.
- Git repository or repository URL, with explicit choice of local clone or remote inspection.
- Later: exports from OSF or other repositories.

### Potential outputs
1. Human-readable report of observed project contents and gaps.
2. Machine-readable findings with rule IDs, evidence locations, confidence, and remediation.
3. Optional generated metadata files or documentation suggestions, reviewed by the user before writing.
4. Optional RO-Crate package, using an established library.
5. Manifest of files, checksums, provenance, and known access restrictions where appropriate.

### Existing building blocks to evaluate

| Component | Candidate standard/tool | Why relevant | Caution |
|---|---|---|---|
| Research object packaging | RO-Crate | Interoperable description of research objects and provenance | Profiles and domain requirements vary; valid syntax is not scientific completeness |
| Python RO-Crate library | ro-crate-py | Existing creation/consumption library | Verify current support, validation options, and compatibility |
| Workflow provenance | W3C PROV; Workflow RO-Crate; workflow-specific exporters | Connect entities, activities, agents, and executions | Generic provenance can be incomplete or verbose |
| File integrity | SHA-256 checksums; BagIt where appropriate | Detect accidental change and support transfer validation | A checksum proves byte identity, not authenticity, correctness, or preservation quality |
| Software metadata | CodeMeta; CITATION.cff | Software description, authorship, citation, identifiers | Do not duplicate or contradict package metadata |
| Research software practice | FAIR4RS and community checklists | Establish proportionate expectations | Checklist completion is not evidence of scientific validity |
| Environment capture | Lockfiles, containers, Nix/Conda, ReproZip, workflow engines | Record or reconstruct runtime conditions | No single method works for every language, hardware, data access model, or OS |
| Execution | Binder, Whole Tale, Renku, workflow engines | Re-run workflows in appropriate environments | Running untrusted code introduces security and resource risks |

### Candidate checks

**Presence and structure**
- README or equivalent project description exists.
- Expected source, data, documentation, and output directories are identifiable.
- Repository has a version-control history.
- License and citation metadata are present or their absence is clearly reported.
- Project has a stated entry point or execution instructions.

**Metadata and consistency**
- CITATION.cff and CodeMeta parse and validate when present.
- Names, versions, authors, identifiers, and repository URLs agree across records where comparable.
- Dependency manifests are detected and parsed.
- Data files have available descriptions, units, and provenance information where relevant.

**Execution readiness**
- Declared runtime and dependency information exists.
- A documented command or workflow entry point is available.
- Sample or test data is present or access instructions are documented.
- A bounded test command can be run only after user consent and in an isolated environment.
- Expected outputs or assertions exist to compare against.

**Transfer and preservation**
- File inventory and checksums can be generated.
- Large, external, ignored, or linked files are identified.
- Symlinks, Git LFS pointers, submodules, external storage, and inaccessible dependencies are reported.
- Rights and access conditions are surfaced where machine-readable evidence exists.
- Export contents can be reopened and independently inspected.

**Interpretation**
- Each result says exactly what was checked, how, and what it does not establish.
- Unknown is not converted into failure.
- Absence of evidence is not reported as evidence of misconduct or invalid science.
- A green status must never imply scientific validity or guarantee reproducibility.

### Major safety constraints
- Never execute repository code automatically during a passive scan.
- Treat repository contents, README instructions, scripts, notebooks, and metadata as untrusted input.
- Do not upload project files, environment variables, credentials, prompts, logs, or datasets to a remote service without explicit informed user action.
- Detect and avoid collecting common secret patterns where practical; explain that secret scanning is imperfect.
- Avoid traversing outside the selected project root through symlinks.
- Respect .gitignore and provide explicit controls for included/excluded paths.
- Do not bundle private, licensed, sensitive, or community-controlled data merely because it is locally available.
- Provide a dry-run and clear file manifest before creating archives or modifying files.
- Keep destructive changes out of the MVP.

## 3. Research-specific AI workflow audit

### Problem hypothesis

An AI/agent trace shows software execution, but a scientific reviewer needs to understand the relationship between the research question, evidence, methods, data, code, model/tool actions, decisions, outputs, and claims.

Generic observability systems can capture calls, tool interactions, timing, tokens, and execution traces. Research auditability needs additional semantics and a durable export.

### Potential architecture shape
- Accept traces from existing systems through OpenTelemetry or documented native export formats.
- Link trace records to source-control commit IDs, datasets or dataset identifiers, workflow definitions, parameters, and output artifact checksums.
- Record model/provider identity, version, relevant configuration, and tool versions when available.
- Record human interventions and approval points.
- Link reported findings to artifacts and runs that support them.
- Export a portable record, potentially using RO-Crate plus suitable provenance structures.
- Generate a human-readable audit report with missing links, contradictions, and unknowns.
- Keep raw prompts, private datasets, credentials, chain-of-thought, and other sensitive material out of public exports by default.

### Research-specific risks
- A trace can be complete while the science is wrong.
- A log may contain sensitive personal, institutional, or unpublished information.
- A model/provider may not disclose exact model version or internal behavior.
- Capturing chain-of-thought is neither necessary nor a safe default; capture observable inputs, outputs, actions, parameters, and decisions appropriate to audit needs.
- Trace completeness varies across agent frameworks and tools.
- A human can intervene outside the instrumented system, leaving gaps.
- A final manuscript claim may not map cleanly to one run or artifact.
- The product must not imply that logged actions were valid or that every relevant action was captured.

### Potential initial use case

A deliberately small AI-assisted computational experiment with a defined research question, a fixed openly licensed dataset, versioned analysis code, one instrumented AI agent, recorded tool calls and outputs, a human review/correction step, and a final report with claims linked to evidence.

The demonstration should deliberately include a failure (for example, an unsupported claim or output mismatch) and show whether the audit record helps a reviewer find it.

## 4. Standards and specifications to verify

- **RO-Crate:** research object packaging and profiles.
- **W3C PROV:** provenance model for entities, activities, and agents.
- **OpenTelemetry GenAI semantic conventions:** trace attributes and events for model and agent operations.
- **OpenInference:** complementary trace conventions and instrumentation ecosystem.
- **CodeMeta:** research software metadata.
- **CITATION.cff:** software citation metadata.
- **BagIt:** packaging and payload manifest conventions for transfer and fixity.
- **FAIR4RS:** findability, accessibility, interoperability, and reuse principles for research software.
- **Workflow RO-Crate / Provenance Run Crate:** structured descriptions of workflows and executions.

The product must select profiles and combinations based on the actual use case. Listing standards is not an architecture.

## 5. Comparative technical experiments to run

### Experiment A — Repository inspection
- Select three public computational research repositories of different sizes and maturity.
- Run existing metadata tools and FAIR checklists.
- Record installation burden, runtime, findings, false positives, and manual effort.
- Compare what a novice can understand without specialist support.
- Do not treat one repository or one discipline as representative.

### Experiment B — Research packaging
- Create an RO-Crate using existing tooling for a small known project.
- Validate it with at least one independent validator/viewer.
- Export, move, unpack, and inspect it on a separate environment.
- Record which project details are not preserved or cannot be represented.
- Compare with a simple archive plus README, CITATION.cff, CodeMeta, and checksums.

### Experiment C — Execution and reproducibility
- Test ReproZip, Whole Tale, Renku, and Binder on suitable example workflows.
- Separate setup success, execution success, output equivalence, and scientific validity.
- Record platform constraints, data-access assumptions, and maintenance burden.
- Never execute unknown code outside a disposable, resource-limited environment.

### Experiment D — AI workflow provenance
- Instrument a minimal agent workflow using OpenTelemetry or an established observability SDK.
- Export the trace and link it to commit, inputs, outputs, and evaluation artifacts.
- Produce a human-readable report and a portable research package.
- Intentionally introduce one traceability defect and test whether the report reveals it.
- Compare generic observability output against the research audit record requirements.

## 6. What remains undecided

- Whether the first product should focus on general computational research handoff or AI-assisted research auditability.
- Whether the initial interface should be a CLI, local web UI, GitHub Action/App, or combination.
- Which research domain and project type should define the first supported workflow.
- Which export format/profile is appropriate.
- Whether execution should be excluded from the first release.
- Whether AI-assisted interpretation adds enough value to justify cost, privacy, and reliability risks.
- Which existing libraries and services are safe, maintained, and appropriately licensed.

Do not resolve these questions in architecture documents until comparative experiments and user discovery justify a decision.

## Sources
- [RO-Crate tools and resources](https://www.researchobject.org/ro-crate/tools/)
- [W3C PROV overview](https://www.w3.org/TR/prov-overview/)
- [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- [OpenInference](https://github.com/Arize-ai/openinference)
- [CodeMeta tools](https://codemeta.github.io/tools/)
- [FAIR4RS principles](https://doi.org/10.1038/s41597-022-01710-x)
- [BagIt specification](https://datatracker.ietf.org/doc/html/rfc8493)
- [Designing reproducible LLM-assisted scientific analyses (2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13576654/)
- [The More You Automate, the Less You See (2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13663820/)
- [OpenDiscoveryTrace (2026)](https://arxiv.org/abs/2609.09203)

---
*This document records technical hypotheses and test plans, not a selected design or implemented architecture.*
