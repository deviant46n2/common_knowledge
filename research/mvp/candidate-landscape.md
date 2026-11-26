# MVP Candidate Landscape — First Comparative Pass

- **Snapshot date:** 26 November 2026
- **Status:** Preliminary desk research; not a systematic review and not user-validated
- **Purpose:** Eliminate weak product propositions early and identify candidate gaps worth testing.
- **Related:** [MVP Discovery](../MVP_DISCOVERY.md)

## Executive assessment

The first pass changes our initial hypothesis. Research packaging, research metadata, and computational reproducibility are not empty spaces. There are established standards, mature platforms, specialist tools, and newer utilities that already cover many obvious features.

The opportunity is therefore unlikely to be “build a better general research workspace” or “generate an RO-Crate.” A defensible MVP needs to solve a specific job that existing tools leave difficult, fragmented, expensive, or inaccessible.

Three connected areas currently deserve the most investigation:

- **A. Research handoff / readiness diagnostics:** an approachable workflow that helps a project owner prepare an existing research project for another person to inspect, understand, run where possible, cite, and preserve.
- **B. Research-specific auditability for AI-assisted work:** a portable evidence record connecting AI/agent execution traces to scientific inputs, methods, data, code, outputs, decisions, and claims.
- **C. Claim-to-evidence verification:** a conservative tool that checks whether numerical statements in a report are attributable to the correct output, metric, experiment, and run, rather than merely finding the same number somewhere in a project directory.

These are opportunity hypotheses, not selected products. We need direct user evidence and hands-on tool testing before commitment.

## Candidate comparison

| Candidate | Existing landscape | Initial assessment | Disposition |
|---|---|---|---|
| General-purpose research collaboration workspace | OSF, Renku, Galaxy, institutional repositories, lab notebooks, project-specific systems | High build and maintenance burden; duplicates broad existing functionality | Reject as first MVP |
| Generic research artifact / RO-Crate generator | RO-Crate ecosystem lists 100+ related tools, libraries, editors, validators, workflow integrations, and domain profiles | Standards generation alone is not differentiated | Reject as standalone MVP; reuse standards |
| Research software metadata generator | CodeMeta, CITATION.cff, CodeMeta tools, cffinit, SMECS, rs-metadata, Codefair, institutional FAIR software tooling | Clear need exists, but specialist tools already serve it | Do not build another generator |
| Computational reproducibility platform | Renku, Whole Tale, ReproZip, Code Ocean, Binder, workflow engines, containers, CI systems | Important need, but comprehensive execution environments are complex and competitive | Do not build a platform; investigate narrower handoff/diagnostic workflow |
| Research handoff / readiness diagnostic | Checklists, FAIR software guidance, metadata validators, workflow tools, and reproducibility platforms each cover parts | Potential gap in low-friction, evidence-based diagnosis plus actionable remediation across existing tools | Keep as leading candidate; investigate deeply |
| OSF export/migration assistant | OSF API, osfclient, manual file/wiki/metadata/log export guidance; OSF says more API export tools are being made available | Concrete short-term need for some active projects, but many users need no migration and existing public records remain accessible | Explore as bounded utility or integration, not assumed core product |
| Generic AI research agent | AI Scientist, Co-Scientist, Robin, many agent frameworks and scientific domain agents | Crowded, fast-moving, expensive to evaluate, and prone to overclaiming scientific capability | Do not build an autonomous scientist as first MVP |
| Generic AI agent observability | OpenTelemetry GenAI conventions, MLflow, Langfuse, Phoenix, Opik, OpenLLMetry, OpenInference | Tracing, dashboards, costs, and debugging are already served by broad tooling | Reuse instrumentation and storage |
| Research-specific AI workflow audit record | Recent research identifies a gap between polished final outputs and inspectable process artifacts; generic tracing does not itself establish scientific provenance or validate claims | Potentially meaningful niche if connected to research objects, methods, data lineage, result selection, and evidence | Keep as leading candidate; investigate deeply |
| Federated research discovery network | Repository APIs, identifiers, knowledge graphs, metadata standards, institutional discovery tools | Long-term value depends on scale, rights, and metadata quality; hard to deliver first-use value without coverage | Defer |

## 1. General research workspace: too broad for a first product

Renku combines a web platform and command-line client, GitLab-based repositories and CI, Jupyter sessions, datasets, environment management, workflow capture, provenance, and a knowledge graph. Whole Tale supports external execution, environment configuration, workflow-run capture, and publication to research archives. Galaxy provides a mature scientific analysis and workflow ecosystem.

A new Common Knowledge workspace would have to compete on a broad set of capabilities while taking responsibility for hosting, security, storage, user support, migration, and continuity.

**Conclusion:** connect existing tools and make a narrow task easier before attempting to host the research lifecycle.

## 2. Generic research packaging: standards and tools already exist

RO-Crate is a community-developed standard for describing research objects and their provenance. Its official tools directory lists a broad ecosystem, including:
- Python, JavaScript, Ruby, R, Rust, and .NET libraries;
- browser-based editors and viewers;
- validators and profile-specific validators;
- workflow and run-provenance integrations;
- converters, archive integrations, and domain-specific applications.

The directory includes Crate-O, NovaCrate, RO-Crate Playground, ro-crate-py, workflow-run tooling, and many domain-specific implementations. The list is not a quality assessment: projects vary in maturity, maintenance, and scope.

**Conclusion:** use RO-Crate where it fits. Generating a valid crate is a component, not a complete product proposition.

## 3. Generic research software metadata: a crowded subproblem

Existing tools already reduce metadata authoring effort:
- **CodeMeta** provides a machine-readable software metadata vocabulary and ecosystem of generators, converters, and harvesters.
- **CITATION.cff** gives software a human-readable citation record and is rendered by GitHub.
- **SMECS** harvests metadata from GitHub/GitLab repositories, provides a curation interface, and exports CodeMeta.
- **rs-metadata** generates and validates CodeMeta and CITATION.cff, checks consistency with repository/package metadata, and integrates with CI through a GitHub Action.
- **Codefair** is listed by the CodeMeta project as a GitHub coding assistant that generates CodeMeta.
- Institutional FAIR research software checklists and guidance cover repository structure, testing, dependencies, documentation, licensing, persistent identifiers, and citation.

A product that merely scans a repository and creates metadata files would duplicate existing work.

**Conclusion:** if we build around repository inspection, the differentiator must be a broader user job and actionable evidence, not metadata generation.

## 4. Reproducibility and research handoff: real need, many partial solutions

A 2025 cross-domain study of computational reproducibility reported frequent barriers among its surveyed participants: missing information needed to execute experiments (79%), unavailable data (63%), unavailable code (63%), and failed installation (50%). The study also found low awareness of existing reproducibility frameworks in its sample. These percentages must not be generalized to all researchers without examining sampling and methods.

A separate 2026 survey of 133 completed responses reported that lack of time was a major perceived barrier to sharing data and preparing code documentation. It explicitly identifies its sample as self-selected and engaged with open science, so it is evidence of reported experience in that sample, not a population estimate.

The ecosystem already offers:
- **ReproZip:** captures execution-related files, binaries, dependencies, and environment information for packaging computational experiments; its documented tracing workflow is Linux-oriented.
- **Whole Tale:** supports environment configuration, recorded execution, and publishing computational research artifacts.
- **Renku:** connects data, code, environments, workflows, and provenance.
- **Binder/BinderHub:** launches interactive computational environments from code repositories; BinderHub requires deployment infrastructure.
- **Code Ocean:** provides a hosted capsule-based platform for code, data, environments, and results.
- **Workflow engines:** Snakemake, Nextflow, CWL, Galaxy, and others describe and execute domain-specific pipelines.
- **DVC and version-control approaches:** help track data, code, and pipelines.
- **Research software checklists:** guide people through metadata, documentation, testing, licenses, citation, and preservation.

The remaining potential gap may be between these specialized tools and the person who simply needs to prepare an existing project for handoff. A user may not know which tools to use, what matters for their particular project, which gaps actually block reuse, or how to fix them without spending days on manual documentation.

**Potential product shape:** inspect a local directory or repository; identify project type and available evidence; test only safe, clearly scoped properties; explain what is missing and why it matters; propose fixes; and generate a portable handoff record. This must not claim to certify scientific validity or guarantee reproducibility.

Open questions:
- Is this pain sufficiently frequent and important to justify another tool?
- Which user has the strongest need and ability to adopt it?
- Are users struggling with discovery of existing tools, integration between them, or lack of time/incentive?
- Could a small diagnostic workflow add meaningful value beyond checklists and current metadata tooling?
- Which project types are suitable for a first version without overgeneralizing?

## 5. OSF transition: real, bounded, and not a reason to replace OSF

OSF announced that no new Projects or child Components could be created from 16 November 2026 and that existing Projects become read-only on 19 February 2027. Registrations and Preprints continue. Public projects remain accessible, findable, and downloadable; OSF recommends that users with completed public projects that need no updates take no action.

Migration is a multi-part process. Files, project metadata, wikis, and activity logs are handled separately. OSF documents browser-based export and osfclient for files; its support documentation says additional API-based export tools are being made available. The API remains available for reading project data, while write functions are being retired.

**Conclusion:** there may be value in testing a unified export/inspection workflow for active projects, especially one that preserves component structure, metadata, wiki content, logs, access context, and links. But first check OSF's own tools and user needs. A one-off migration utility could be useful, but it is not yet a strong foundation for the long-term Common Knowledge product.

## 6. Generic AI research agents: do not start by building an AI scientist

The 2026 scientific-agent landscape includes end-to-end research systems, domain-specific hypothesis-generation systems, and expert-in-the-loop scientific reasoning engines. Recent evaluations show substantial capability, but also persistent problems with execution, novelty checks, integrity, evidence grounding, and claims that are not supported by recorded work.

A 2026 benchmark study using unpublished follow-up directions from domain scientists reported that none of 135 submissions from nine frontier agents satisfied all required conditions, and 114 failed an integrity check, often because claims described work not actually performed or reported numbers that contradicted recorded evidence. This is a specific benchmark, not a universal estimate of agent performance.

**Conclusion:** an autonomous scientist would be a poor first product: broad scope, difficult evaluation, high compute costs, and substantial risk of presenting plausible outputs as validated research. Common Knowledge can support human–AI research without trying to automate the whole research lifecycle.

## 7. Generic agent observability: reuse it

Generic agent tracing and observability is already a substantial ecosystem. OpenTelemetry GenAI conventions and tools such as MLflow, Langfuse, OpenInference, OpenLLMetry, and others can capture model calls, tool calls, latency, token use, and execution traces. These systems help developers debug and evaluate agents.

However, a trace of software execution is not automatically a research record. It does not necessarily describe the scientific question, source datasets, method, benchmark-selection rationale, result-selection process, analysis decisions, human review, or the relationship between a manuscript claim and its underlying evidence.

**Potential gap:** research-specific packaging and interpretation of traces, using existing observability systems as inputs rather than replacing them.

This needs deeper testing. OpenDiscoveryTrace and other emerging datasets show that structured process traces are already an active research area; Common Knowledge must not assume it is the first to recognize the problem.

## 8. Provisional opportunity ranking

This is qualitative triage, not a numerical score.

| Opportunity | User pain evidence | Existing competition | Standalone demo potential | Current confidence |
|---|---|---|---|---|
| Research handoff / readiness diagnostics | Moderate; supported by reproducibility studies and documentation barriers | High but fragmented across tools and checklists | High if a clear before/after workflow exists | Medium-low |
| Research-specific AI workflow audit record | Emerging, with recent research identifying an evidence and traceability gap | Generic observability is high; research-specific integration appears less consolidated | High with a working AI experiment and evidence-linked report | Medium-low |
| OSF export/migration helper | Concrete for active users affected by workflow changes | OSF guidance, API, osfclient, and announced export tooling | High for a narrow import/export demonstration | Medium |
| Generic metadata generator | Established need | Very high | High | High confidence it is not differentiated |
| General research platform | Broad need | Very high | Low; needs network and infrastructure | High confidence it is too broad |

## 9. What to investigate next

### Priority 1 — Hands-on research handoff tools
- Install and run ReproZip against representative projects.
- Test Whole Tale's public workflow and documented limitations.
- Test Renku's local client and a small example repository.
- Compare Binder, DVC, workflow-engine reports, and standard packaging outputs.
- Inspect how each tool handles missing data, external data, dependencies, secrets, licensing, provenance, and export.
- Determine which functions can safely run without executing untrusted research code.

### Priority 2 — AI research workflow audit
- Inspect OpenTelemetry GenAI conventions and open trace formats.
- Run a small instrumented agent workflow using an existing observability stack.
- Examine how to link trace records to code commits, datasets, workflow definitions, parameters, and outputs.
- Test a portable export using RO-Crate and/or W3C PROV.
- Determine which data must never be logged or automatically published.
- Compare against OpenDiscoveryTrace and research-agent audit approaches.

### Priority 3 — OSF transition
- Inspect the current OSF export tools, API, and osfclient.
- Map exactly which parts of an OSF project are and are not exported by existing utilities.
- Look for evidence of user difficulty from library support materials and user discussions.
- Do not build migration functionality until the remaining gap is clear.

### Priority 4 — Direct user discovery
Seek people who recently prepared a research project for publication, transfer, collaboration, review, or reproduction. Ask them to show the workflow and friction, using non-sensitive material. Include people who already use Renku, Whole Tale, Code Ocean, OSF, GitHub, and workflow systems.

## 10. Decision gate

Select an MVP only when we can write a credible answer to all of these:

1. Who is the first user?
2. What specific task are they trying to complete?
3. What do they do today?
4. What exactly fails, takes too long, or remains inaccessible?
5. Which existing tools have we tested?
6. Why is our proposed workflow meaningfully better?
7. What is the smallest complete product that solves the task?
8. What can we demonstrate with representative inputs?
9. How will we measure usefulness and avoid false assurances?
10. Can the product be built, secured, documented, and maintained with available resources?

Until these questions have defensible answers, all candidate concepts remain provisional.

## Sources

### Research packaging, workflows, and reproducibility
- [RO-Crate official tools and resources](https://www.researchobject.org/ro-crate/tools/)
- [Renku documentation: What is Renku?](https://docs.renkulab.io/en/0.57.2/introduction/what-is-renku.html)
- [Whole Tale documentation](https://wholetale.readthedocs.io/en/stable/)
- [ReproZip documentation](https://docs.reprozip.org/en/latest/)
- [BinderHub documentation](https://binderhub.readthedocs.io/en/latest/)
- [Code Ocean user guide](https://docs.codeocean.com/user-guide)
- [Computational reproducibility framework study, Future Generation Computer Systems (2025)](https://doi.org/10.1016/j.future.2025.107924)
- [Exploratory Insights into Barriers and Open Practices for Computational Reproducibility (2025/2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13560004/)
- [Reproducibility debt: insights from practitioners (2026)](https://link.springer.com/article/10.1007/s10664-026-10973-6)

### Research software metadata and FAIR practices
- [CodeMeta tools directory](https://codemeta.github.io/tools/)
- [rs-metadata documentation](https://lumc-dcc.github.io/rs-metadata/)
- [SMECS paper](https://doi.org/10.14279/eceasst.v85.2708)
- [FAIR research software checklist](https://fair-toolbox.github.io/framework/checklist.html)
- [FAIR4RS biomedical research software guidelines](https://www.nature.com/articles/s41597-023-02463-x)

### OSF transition
- [OSF Projects transition](https://help.osf.io/article/727-osf-projects-transition)
- [OSF transition details](https://help.osf.io/article/759-details-of-osf-projects-transition)
- [OSF download and export guidance](https://help.osf.io/article/745-download-and-export-content)
- [OSF metadata, wiki, and logs export guidance](https://help.osf.io/article/746-download-individual-osf-wikis-metadata-and-logs)
- [OSFClient download guide](https://help.osf.io/article/742-using-osfclient-to-download-project-files)
- [OSF API v2 documentation](https://developer.osf.io/)

### AI research and auditability
- [Accelerating scientific discovery with Co-Scientist, Nature (2026)](https://www.nature.com/articles/s41586-026-10644-y)
- [Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap (2026)](https://arxiv.org/abs/2608.05179)
- [Into the Unknown: Benchmarking AI agents on open scientific research problems (2026)](https://arxiv.org/abs/2610.19159)
- [OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows (2026)](https://arxiv.org/abs/2609.09203)
- [The More You Automate, the Less You See: Hidden Pitfalls of AI Scientist Systems (2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13663820/)
- [Designing reproducible large-language-model-assisted scientific analyses (2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13576654/)
- [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- [Agent observability prior-work survey, AAIF working group](https://github.com/aaif/wg-observability-and-traceability/blob/main/working-documents/PRIOR-WORK.md)

---
*This comparison records a first-pass landscape review. It is not a systematic review, hands-on evaluation, or user validation. Tool capabilities and project status change; high-impact assumptions must be rechecked before product selection.*
