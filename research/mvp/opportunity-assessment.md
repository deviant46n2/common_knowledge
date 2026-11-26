# MVP Opportunity Assessment — Preliminary Synthesis

- **Assessment date:** 26 November 2026
- **Status:** Preliminary desk-research synthesis; no MVP selected
- **Research cutoff:** 26 November 2026
- **Purpose:** Turn the first landscape investigation into a clear product decision process and avoid building a duplicate of existing infrastructure.

## Executive conclusion

The original candidate—a general research project inspector/packager—was a reasonable starting hypothesis, but the research has shown that its obvious feature set is already distributed across a substantial and rapidly developing ecosystem.

There are mature standards and tools for:
- research project collaboration and execution;
- metadata, citation, and FAIR software practices;
- RO-Crate creation, validation, and preservation;
- workflow definitions and execution provenance;
- workflow testing and long-term monitoring;
- reproducibility comparisons;
- claim-to-evidence verification;
- AI-assisted research and paper-to-agent conversion;
- evidence graphs and research audit trails.

Several projects are new and still early, but they are real implementations with code, tests, documentation, and public examples. Common Knowledge should not treat “early” as meaning “nonexistent.”

**Current recommendation: do not build a new general-purpose research platform, metadata generator, research packager, workflow runner, claim checker, AI scientist, or generic agent skill collection.**

The most defensible path currently is to investigate a **narrow, user-facing integration problem across existing research tools**. The likely shape is a local-first tool or plugin that helps a researcher complete one real workflow and produces an inspectable, portable result. But even this is only a hypothesis: the standards and tools may already solve the problem adequately.

A useful first product may therefore be an extension, adapter, or integration around an existing project rather than an entirely new application. That is a valid Common Knowledge product if it delivers standalone value and can be maintained responsibly.

## 1. What the landscape has taught us

### 1.1 Research workspaces are already well served

Renku, Galaxy, OSF (within its changing service scope), Whole Tale, and specialist environments already cover significant parts of research collaboration, data, code, workflows, execution, and publication.

A new all-in-one workspace would inherit a large operational burden before it could offer differentiated value.

### 1.2 Packaging and metadata are not empty spaces

RO-Crate 1.3, CodeMeta, CITATION.cff, FAIR4RS, and many associated tools cover research-object description, software metadata, citation, validation, and preservation.

The official RO-Crate tools directory lists a broad and growing ecosystem, including libraries, editors, validators, workflow integrations, converters, and agent skills.

A generic crate generator or repository metadata helper is not a defensible MVP.

### 1.3 Workflow provenance and reproducibility already have a standards ecosystem

Workflow Run RO-Crate 0.6 and related profiles describe workflows, tests, executions, inputs, outputs, and provenance. Existing tools include roc-validator, runcrate, Tonkaz, LifeMonitor, workflow-system plugins, ReCRATE, FlowProof, and FAIRSCAPE.

A generic workflow recorder, validator, monitor, or result comparator would overlap with existing work.

### 1.4 Claim-to-evidence verification is now an active product area

The landscape includes ReproCert, reproducible-science, Research Paper Reproduction for Codex, agent-integrity-analysis, autoresearch, and other agent skills. Some already provide deterministic local checks, portable reports, run-linked evidence, and RO-Crate export.

A generic claim checker or evidence ledger is not a new idea. The reproducible-science project even defines an experimental RO-Crate 1.3 profile for claim-check records.

### 1.5 AI-assisted research is moving quickly

Paper2Agent, ReCRATE, FlowProof, autoresearch, OpenDiscoveryTrace, AutoMat, and other projects cover paper-to-agent conversion, workflow execution, process traces, reproducibility, and scientific-agent evaluation.

Common Knowledge should not build an autonomous scientist or broad research agent as its first product.

### 1.6 Evidence graphs already exist

FAIRSCAPE and the Evidence Graph Ontology (EVI) provide research data/software/computation packaging and evidence graphs, especially in biomedical and Bridge2AI contexts.

A new evidence ontology or graph viewer would need a very clear unmet need.

## 2. Candidates we should not pursue as standalone MVPs

| Product proposition | Why it is weak as a first MVP |
|---|---|
| General research collaboration platform | Too broad; existing platforms already have users, integrations, and substantial operating infrastructure |
| Generic research package generator | RO-Crate and its tool ecosystem already provide standards and implementations |
| Generic metadata / citation generator | CodeMeta, CITATION.cff, rs-metadata, SMECS, Codefair, and related tools cover this |
| General reproducibility platform | Renku, Whole Tale, ReproZip, Galaxy, workflow engines, and related systems already provide major capabilities |
| Generic workflow provenance recorder | Workflow Run RO-Crate and multiple implementations already exist |
| Generic workflow reproducibility comparator | Tonkaz and other workflow-specific tooling already compare outputs |
| Generic claim-to-evidence checker | ReproCert, reproducible-science, and Research Paper Reproduction for Codex already cover much of this |
| Generic AI research agent | Crowded, difficult to validate, resource-intensive, and prone to overstating scientific authority |
| Generic research agent skill collection | Many public skill libraries already cover the paper lifecycle and research workflows |
| Generic research repository MCP server | Existing repository MCP servers and paper/workflow agents cover substantial pieces; first-use demand remains uncertain |
| General research rigor checker | A 2026 comparison already evaluated 11 tools across nine criteria and 1,500 manuscripts |

These are not claims that every existing product is complete or universally adequate. They are reasons not to duplicate their advertised core functions without a specific user problem and direct comparison.

## 3. Remaining opportunity hypotheses

### Hypothesis A — A genuinely low-friction research handoff workflow

A researcher has an existing project and needs to hand it to a collaborator, reviewer, future maintainer, or repository. The hard part may be deciding which tools and checks to use, interpreting their results, and assembling a clear portable handoff.

Potential value:
- guide a user through the right existing tools for their project type;
- make gaps and unknowns understandable;
- preserve rights, licenses, provenance, and external dependencies;
- create one inspectable handoff report;
- avoid replacing the user's repository or workflow engine.

Risk: this may still be a thin wrapper around tools that users already know how to use. User discovery must establish that integration and guidance are a real pain, not just a convenient feature.

### Leading product shape to test: local-first research preflight and handoff

The most promising *shape* to test is not a new validator or research package generator. It is a small, local-first tool that helps a researcher complete the handoff task by orchestrating existing tools and explaining their outputs.

A first version might:
- inspect one supported type of computational research project without executing its code;
- identify existing metadata, dependencies, workflow definitions, test commands, run records, and evidence artifacts;
- detect which established validators or checkers are relevant and available;
- invoke safe read-only validation commands only with user approval;
- produce one clear report with evidence locations, missing links, known limitations, and next actions;
- optionally export a small index/manifest of the existing project without copying restricted data.

This is a product hypothesis, not a selected design. The first version must do more than aggregate checklists or shell out to other tools. It must make the workflow meaningfully easier for a defined user, and the output must be more actionable than the separate tool reports.

A reasonable first supported scope could be computational Python projects, but only if research software engineers and researchers confirm that this is a valuable first user group. It should not claim to cover all research types.

### Hypothesis B — Cross-tool evidence interoperability

A research project may produce multiple records: a ReproCert certificate, a reproducible-science claim-check export, a Workflow Run RO-Crate, an EVI evidence graph, and manuscript artifacts. It is not yet clear whether these records preserve the same relationships when moved between tools.

Potential value:
- inspect and compare the semantics of different evidence formats;
- identify missing or broken links among claims, runs, files, code revisions, and datasets;
- test round-trip export and independent inspection;
- produce a clear compatibility report;
- provide adapters where a real incompatibility exists.

Risk: standards and validators already address much of this. The product must demonstrate an actual break in a real workflow before we build it.

### Hypothesis C — An integration or extension for an existing project

Instead of creating a new system, Common Knowledge could contribute a missing capability to ReCRATE, FlowProof, FAIRSCAPE, reproducible-science, ReproCert, or another existing project.

Potential value:
- deliver something useful sooner;
- inherit existing users, domain knowledge, and technical foundations;
- avoid duplicating infrastructure;
- build a track record through a concrete upstream contribution.

Risk: the project owner and community must welcome the contribution; Common Knowledge should not assume control over another project's direction or assets. The contribution must still be independently useful and properly attributed.

### Hypothesis D — A narrow research-integrity test or conformance suite

There may be a need to test whether tools preserve evidence relationships and report their limitations correctly, rather than merely checking that a package conforms to a schema.

Potential value:
- controlled fixtures with known ground truth;
- test cases for wrong-run attribution, missing artifacts, stale metadata, version mismatch, and unsupported claims;
- reusable CI tests for tool developers;
- transparent precision, coverage, and abstention reporting.

Risk: existing benchmarks and validators already cover adjacent tasks. A new suite needs a distinct, defensible target and interested maintainers.

## 4. Preliminary recommendation

Prioritize the following investigation order:

1. **Local-first research preflight and handoff:** test whether a guided tool that orchestrates existing validators and explains the results solves a real, frequent user problem.
2. **Cross-tool evidence interoperability:** test whether claims, runs, files, identifiers, and rights survive real export and handoff workflows.
3. **Upstream contribution opportunities:** if a concrete gap belongs inside an existing project, prefer a contribution or adapter over a competing product.
4. **Integrity conformance tests:** pursue only if the first tests reveal semantic failures not caught by current validators and benchmarks.

Do not choose a product based on conceptual alignment alone. If hands-on tests show that existing tools already work together adequately, reject the integration hypothesis and return to user problem discovery.

## 5. Next research cycle — hands-on, not more directory building

### Test fixture

Create one small, openly licensed computational project with:
- a stated research question and method;
- a small dataset with known provenance;
- versioned code and dependencies;
- two distinct runs;
- result tables with metrics, units, and identifiers;
- a Markdown or LaTeX report with explicit numerical claims;
- known intentional defects: wrong-run value, wrong metric, missing artifact, stale claim, changed file, and ambiguous evidence.

### Test existing tools

Use safe official examples and a disposable environment to test:
- ReproCert;
- reproducible-science, including its RO-Crate export;
- ReCRATE;
- FlowProof's mock backend and, only if safe, its documented example;
- FAIRSCAPE CLI and example crates;
- rocrate-validator;
- runcrate;
- Tonkaz where its supported file types apply;
- LifeMonitor's Workflow Testing RO-Crate flow.

Do not run arbitrary public research repositories or execute untrusted scripts on the host. Start with mock backends and known official fixtures. Any real workflow execution must be explicitly scoped and isolated.

### Compare outputs

For each tool, record:
- exact version and commit;
- input format and assumptions;
- command sequence and environment;
- outputs and schemas;
- claim/run/artifact relationships represented;
- checksums and identity fields;
- license and rights representation;
- errors and unknowns;
- round-trip and independent-reader results;
- installation and first-use burden.

### User evidence

After the first reproducible demonstration exists, conduct a small number of focused workflow walkthroughs with researchers, RSEs, and tool maintainers. Ask them to show a recent task and its friction; do not ask them to join Common Knowledge or endorse the mission.

## 6. Decision gate for selecting the MVP

We should not move to a strategic implementation roadmap until we can state:

1. **User:** who has the first problem?
2. **Job:** what exact task are they trying to complete?
3. **Pain:** what failed, took too long, or required specialist help?
4. **Alternatives:** which existing tools did we test, not merely read about?
5. **Gap:** what concrete step remains unsolved?
6. **Product:** what is the smallest complete workflow that solves it?
7. **Proof:** what representative example demonstrates the result?
8. **Safety:** what data, execution, privacy, and rights boundaries apply?
9. **Adoption:** can a newcomer install/use it without personal assistance?
10. **Maintenance:** can a small team maintain it sustainably?

If any answer is vague, continue research or reduce scope.

## 7. What would make the MVP attractive

A useful first product should:
- work without a Common Knowledge account or network;
- provide a useful result in one short session;
- integrate with tools people already use;
- be local-first where sensitive research data is involved;
- produce transparent, inspectable output;
- state exactly what it verified and what it did not;
- support export and independent inspection;
- have sample projects and automated tests;
- be easy for an external maintainer to integrate;
- welcome contributions around specific, real issues.

The first invitation to contributors should be: “Here is a tool you can install and use. Here is the problem it solves. Here is the evidence that it works. Here is one concrete way to improve it.”

## 8. Evidence limitations

- This assessment is based on public documentation, papers, source inspection, and repository metadata.
- No Common Knowledge user interviews have been conducted.
- No competitor has been independently security-audited.
- No hands-on comparative installation or interoperability experiment has been completed.
- Project feature descriptions and self-reported benchmark results are attributed to their authors.
- Lack of visible issues, stars, or community activity is not proof that a project has no users or value.
- This assessment is not a final product decision.

## Sources and linked research

- [MVP research index](README.md)
- [Candidate landscape](candidate-landscape.md)
- [Direct competitors and adjacent research projects](direct-competitors.md)
- [Claim verification and research-agent ecosystem](claim-verification-ecosystem.md)
- [Workflow provenance and interoperability ecosystem](workflow-interoperability.md)
- [Technical opportunities and integration hypotheses](technical-opportunities.md)
- [Hands-on experiments and user discovery plan](discovery-experiments.md)

---
*This is the current best synthesis of the evidence reviewed on 26 November 2026. It is deliberately provisional and should be revised after hands-on tests and user workflow evidence.*
