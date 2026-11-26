# Workflow Provenance and Interoperability Ecosystem

- **Reviewed:** 26 November 2026
- **Status:** Desk research from standards documentation and primary sources; no hands-on tool execution yet.
- **Purpose:** Assess whether Common Knowledge should build a research handoff, provenance, validation, or interoperability product.

## 1. Executive conclusion

Workflow provenance is not an empty space. The RO-Crate community has developed a mature set of standards and tools for describing research objects, workflow definitions, workflow tests, and workflow executions. Multiple workflow systems already export these records.

The current profile collection includes:
- **RO-Crate 1.3** as the base research-object packaging standard;
- **Workflow RO-Crate 1.1** for packaging workflow definitions;
- **Workflow Testing RO-Crate 0.1** for describing workflow test suites and CI test instances;
- **Workflow Run RO-Crate 0.6** with Process Run, Workflow Run, and Provenance Run profiles for execution provenance.

The 0.6 release (7 September 2026) aligns with RO-Crate 1.3 and Workflow RO-Crate 1.1. It changes several IRI mappings and is not backward compatible with some older RO-Crate 1.1 / Workflow RO-Crate 1.0 mappings. Version-aware import and validation therefore matter.

Existing tools cover validation, conversion, inspection, re-execution, comparison of run outputs, and continuous workflow testing. A generic crate validator, workflow-run recorder, or reproducibility comparator would duplicate established work.

## 2. Standards and profiles

### RO-Crate

RO-Crate is a lightweight, JSON-LD-based approach to packaging research data with metadata and relationships. Profiles constrain the vocabulary and required structure for particular purposes.

### Workflow RO-Crate

Describes a computational workflow as a research object, including workflow definitions, software, authorship, licenses, test data, and related resources.

### Workflow Testing RO-Crate

Extends Workflow RO-Crate with metadata for test suites, test services, and test instances. LifeMonitor uses it to connect workflow metadata to CI services such as GitHub Actions, Jenkins, and Travis CI, then expose test outcomes through an API and dashboard.

### Workflow Run RO-Crate

Captures execution provenance and associated inputs, outputs, code, and metadata. The profile collection offers increasing levels of detail:
- Process Run Crate for one or more tools contributing to a computation;
- Workflow Run Crate for coordinated execution driven by a ComputationalWorkflow;
- Provenance Run Crate for internal step-level details.

The 2024 PLOS ONE paper reports implementation in six workflow systems and a conversion tool, with interoperability across heterogeneous workflow management systems as a primary motivation.

### ARC Workflow Run RO-Crate

A newer profile aligns computational workflow runs with ISA-based laboratory provenance. It multi-types workflow definitions as both ComputationalWorkflow and LabProtocol, and workflow runs as both CreateAction and LabProcess, so experimental and computational processes can be represented in one coherent crate.

**Implication:** Do not invent a general provenance model. Use existing profiles and determine whether a real use case requires an extension.

## 3. Existing tools

| Tool | Function | Important boundary |
|---|---|---|
| **rocrate-validator / roc-validator** | Validates base RO-Crate and declared profiles, including RO-Crate 1.3, Workflow, Workflow Testing, Process Run, Workflow Run, and Provenance Run Crates | Checks conformance to profile rules; does not establish scientific correctness |
| **runcrate** | Python library and CLI to report on Workflow Run RO-Crates, convert CWLProv bundles, and re-run workflows from crates | Re-execution still depends on compatible workflow runner, data access, environment, and security controls |
| **Tonkaz** | Compares two RO-Crates containing expected and actual workflow provenance, including selected biological feature values; reports levels of reproducibility | Domain-focused on biological analysis outputs; selects recognized file types/EDAM terms; does not score the entire workflow |
| **LifeMonitor** | Aggregates and monitors workflow test status over time across CI services; uses Workflow Testing RO-Crate | Focuses on workflow maintenance and test health, not manuscript claim validation |
| **Snakemake RO-Crate report plugin** | Produces a Provenance Run Crate after a Snakemake workflow run | Workflow-specific integration |
| **WfExS-backend** | Runs Nextflow, CWL, and Galaxy workflows, including in trusted research environments, and describes executions as Workflow Run RO-Crates | Service/backend deployment and resource/security requirements |
| **StreamFlow** | Workflow management for hybrid HPC/cloud environments with Workflow Run RO-Crate export for CWL runs | Execution and infrastructure complexity |
| **Galaxy** | Imports/exports RO-Crates for datasets and workflow executions | Mature domain-specific analysis platform |
| **ReCRATE** | Uses research method agents and records executions as Workflow Run RO-Crates | Proof of concept; some profiles and execution classes remain incomplete |
| **FlowProof** | Exposes bioinformatics pipeline execution and provenance through MCP | Early project focused on bioinformatics |

### Tonkaz: an important existing result-comparison tool

The Tonkaz paper describes comparing expected and actual workflow-run RO-Crates. It first checks checksums; where outputs differ, it compares selected biological feature values under a configurable tolerance. The paper explicitly avoids a universal workflow-level score because reproducibility criteria vary by use case. The structured result is left to workflow developers to interpret.

**Implication:** Comparing outputs across runs is not a new idea. A Common Knowledge product would need to solve a more specific problem than “compare two workflow crates.”

### LifeMonitor: ongoing health, not just one-time validation

LifeMonitor monitors workflow tests over time and surfaces changes in workflow operation. It uses Workflow Testing RO-Crate to describe the workflow, test suite, CI service, and test instance. This addresses a real preservation issue: workflows decay when APIs, software versions, URLs, and external resources change.

**Implication:** A useful handoff product should distinguish a one-time package validation from ongoing workflow maintenance. Common Knowledge should not build another general workflow monitor.

## 4. The possible remaining gap

The standards and tools cover much of the technical substrate:
- a crate can describe a research object;
- a workflow crate can describe a workflow;
- a run crate can describe execution;
- a testing crate can describe recurring checks;
- validators can test profile conformance;
- runcrate can inspect, convert, and re-execute;
- Tonkaz can compare selected outputs;
- LifeMonitor can monitor test status;
- FAIRSCAPE/EVI can model evidence graphs and findings;
- reproducible-science can export claim checks as an experimental RO-Crate profile.

The unresolved question is whether these outputs work together in a real user's end-to-end task. A potential gap is **semantic interoperability across tools**, especially whether claim-level records, workflow runs, data/software identifiers, licenses, and evidence links survive packaging, export, conversion, and independent inspection.

This is not yet proven to be a product opportunity. It may be sufficiently handled by existing tools, community profiles, and maintainers' work.

## 5. Proposed hands-on interoperability experiment

Use a small, openly licensed synthetic computational project with a known result and a report containing explicit numerical claims.

Create or obtain outputs from:
1. a workflow runner that emits Workflow Run RO-Crate;
2. reproducible-science claim-check export;
3. ReproCert certificate output;
4. where feasible, a FAIRSCAPE/EVI evidence graph.

Then:
- validate each crate with roc-validator;
- inspect and report on run crates with runcrate;
- compare two runs using Tonkaz or an equivalent supported workflow;
- verify that claims still reference the correct run, metric, artifact, and location after export;
- move the bundle to a clean environment and inspect it without the original service;
- deliberately introduce a version mismatch, missing artifact, wrong-run value, and stale claim;
- record which errors each tool detects, which it misses, and how clear its report is.

Do not execute unknown external research code during this experiment. Use synthetic fixtures or official demo projects in a disposable, resource-limited environment after reviewing their execution behavior.

## 6. Product implications

- A generic RO-Crate validator is already available.
- A generic workflow run recorder is already represented by a broad ecosystem.
- A generic workflow test monitor already exists.
- A generic workflow output comparator already exists in Tonkaz.
- A generic research evidence graph already exists in FAIRSCAPE/EVI.
- A generic claim-check RO-Crate export is already emerging in reproducible-science.

A viable Common Knowledge MVP would need to be a genuinely missing user-facing workflow, a meaningful integration that preserves information between existing tools, or an independent conformance test that current maintainers and users actually need.

Do not choose an interoperability product just because interoperability is philosophically aligned with Common Knowledge. Demonstrate a real break in an actual workflow first.

## Sources

- [RO-Crate tools and resources](https://www.researchobject.org/ro-crate/tools/)
- [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/)
- [Workflow Run RO-Crate profile collection](https://www.researchobject.org/workflow-run-crate/profiles/)
- [Workflow Run RO-Crate changelog](https://www.researchobject.org/workflow-run-crate/profiles/changelog.html)
- [Recording provenance of workflow runs with RO-Crate (2024)](https://doi.org/10.1371/journal.pone.0309210)
- [RO-Crate Validator documentation](https://rocrate-validator.readthedocs.io/en/latest/)
- [rocrate-validator repository](https://github.com/crs4/rocrate-validator)
- [runcrate usage](https://www.researchobject.org/runcrate/usage.html)
- [Tonkaz reproducibility scale paper](https://doi.org/10.1093/gigascience/giad031)
- [LifeMonitor](https://lifemonitor.eu/)
- [Workflow Testing RO-Crate](https://crs4.github.io/workflow-testing-ro-crate/)
- [ARC Workflow Run RO-Crate (2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13526443/)
- [Snakemake RO-Crate report plugin](https://github.com/snakemake/snakemake-report-plugin-rocrate)

---
*This document is based on public standards documentation and published research. No hands-on Common Knowledge interoperability tests have been completed.*
