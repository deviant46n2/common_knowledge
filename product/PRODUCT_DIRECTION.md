# Product Direction — Research Project Preflight

- **Status:** Working direction for prototype development
- **Date:** 26 November 2026
- **Decision type:** Reversible product hypothesis; not a final MVP selection

## 1. Product in one sentence

A local-first tool that helps a researcher inspect the handoff-readiness of a computational project, understand concrete weaknesses in its research record, and prepare a more inspectable handoff using existing standards and tools.

## 2. Initial user hypothesis

**Primary user to investigate:** a computational researcher or research software engineer who maintains a small-to-medium Python-based research project and needs to share it with a collaborator, reviewer, future maintainer, or repository.

This is a starting hypothesis, not a claim that this group has validated demand.

Likely adjacent users include graduate researchers, research data stewards, librarians, and maintainers of research software. Do not design the first release for all of them simultaneously.

## 3. The job to be done

"When I need someone else to understand or reuse my computational research project, help me find the practical gaps and prepare a trustworthy handoff without making me learn and operate a collection of disconnected tools."

The product should answer:
- What is actually present in this project?
- What important information or relationships are missing or unclear?
- Which findings are supported by direct evidence, and where is that evidence?
- Which established tools or standards can address a finding?
- What should I do next, and what remains unknown?

## 4. Product promise

**Make the state of a research project understandable and actionable before it is handed to someone else.**

The tool should be useful to the project owner, not merely produce a compliance score for an evaluator.

## 5. First prototype boundary

### In scope for the first prototype

- Inspect one local project directory.
- Start with computational Python projects.
- Read files and declared configuration only.
- Identify a bounded set of project characteristics: repository structure, README/instructions, dependency declarations, environment files, tests, workflow definitions, data/artifact references, citation metadata, license declarations, and existing provenance or research-object records.
- Report each finding with a stable identifier, severity or priority, explanation, evidence location, confidence/limitations, and a practical next step.
- Distinguish "not found" from "not applicable", "not checked", and "could not determine".
- Produce a readable report that can be saved and shared.
- Include a small synthetic example so the behavior can be independently reproduced.
- Reuse existing validators and metadata tools where comparison demonstrates they add value.

### Explicitly out of scope initially

- Executing project code, notebooks, shell commands, or workflow definitions.
- Uploading project contents or telemetry to a service.
- Requiring a Common Knowledge account or network connection.
- Hosting, collaboration, comments, social features, or a central project registry.
- Claiming to verify scientific truth, correctness of conclusions, or general reproducibility.
- Supporting every language, discipline, repository host, or workflow engine.
- Replacing RO-Crate, CodeMeta, CITATION.cff, workflow engines, repositories, or existing validators.
- Automatically changing or rewriting a user's project.

## 6. Product differentiation hypothesis

The product is not intended to be another generic checklist, metadata generator, validator, or research package builder.

Its possible differentiation is the **guided handoff workflow**:
1. inspect the actual project;
2. identify which checks are relevant;
3. connect findings to concrete evidence in the project;
4. explain implications in plain language;
5. recommend the next useful action;
6. assemble a concise, portable handoff report.

This differentiation is unproven. The hands-on comparison must test whether existing tools already deliver it adequately. If the product is only a thin wrapper, do not ship it as a standalone product.

## 7. Trust model

- Local-first by default.
- No project code execution in the initial prototype.
- No network calls during inspection unless a future, explicit feature requires them.
- No silent file modifications.
- No collection of project contents or telemetry.
- Findings must be traceable to observed evidence.
- No single "research quality" score.
- Never present absence of detected problems as proof of scientific validity.
- Show tool versions, checks performed, checks not performed, and known limitations.
- Treat sensitive, personal, controlled, or community-governed data with care; do not copy data into reports or exports by default.

## 8. First success criteria

The prototype is worth continuing only if it can demonstrate all of the following:

1. A newcomer can point it at a sample project and obtain a useful report without executing that project's code.
2. Findings are accurate against a fixture with known conditions.
3. Findings identify specific evidence locations and explain why they matter.
4. The report separates observed facts, inferences, recommendations, and unknowns.
5. It adds meaningful convenience or insight beyond running the relevant existing tools separately.
6. The output is understandable to a researcher who is not a research-infrastructure specialist.
7. It is straightforward to inspect, test, and reproduce.

Quantitative targets should be set after the fixture and baseline tool comparisons exist, not invented in advance.

## 9. Decision rule

Continue with this direction only if hands-on testing establishes a concrete gap and the prototype demonstrates a better user workflow. Otherwise, narrow the task, contribute upstream, build an adapter, or reject the idea. Common Knowledge's mission is more important than preserving this particular product hypothesis.
