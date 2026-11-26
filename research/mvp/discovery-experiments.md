# MVP Research — Hands-on Experiments and User Discovery Plan

- **Established:** 26 November 2026
- **Status:** Proposed investigation plan; not yet executed
- **Purpose:** Convert desk research into reproducible comparisons and real user evidence before selecting an MVP.

## 1. Research questions

The next investigation should answer:

1. Which job is painful enough that a real person will adopt a new tool?
2. Which existing project already solves most of it?
3. What is the smallest useful gap between current tools?
4. Can Common Knowledge demonstrate that gap with a narrow, reliable vertical slice?
5. Can the product be built as an integration or extension rather than a competing platform?
6. What would make a user trust its output and return to use it?

## 2. Candidate workflows to compare

### Workflow A — Prepare a computational research project for handoff

**User job:** “I need to give this project to another researcher, reviewer, collaborator, or future version of myself so they can understand what was done and run or inspect it.”

Representative toolchain to test:
- plain Git repository plus README and dependency manifest;
- CodeMeta and CITATION.cff generation/validation;
- ReproZip;
- Renku;
- Whole Tale;
- Binder;
- RO-Crate creation and validation;
- ReCRATE where the project has a published method or workflow.

Record:
- installation and setup time;
- how much user knowledge is required;
- what gets captured automatically;
- what remains manual;
- missing external data and dependencies;
- output portability;
- how clearly gaps are explained;
- whether a newcomer can complete the handoff without help.

### Workflow B — Verify an AI-assisted computational research run

**User job:** “I need to show which model, prompts/configuration, tools, inputs, code, and outputs produced this result, and what a human checked.”

Representative toolchain to test:
- one small AI-assisted research workflow;
- OpenTelemetry GenAI instrumentation or an established trace SDK;
- one existing observability backend, such as MLflow or Langfuse;
- RO-Crate / Workflow Run RO-Crate export;
- ReCRATE if the workflow is represented as a supported computational method.

Record:
- which events are captured by default;
- which artifacts require manual links;
- what is lost across model/provider boundaries;
- how human decisions and corrections are represented;
- whether the trace can be exported and inspected without the original service;
- privacy risks and redaction effort;
- whether a reviewer can reconstruct the run's key actions.

### Workflow C — Check whether report claims match run evidence

**User job:** “I need to know whether the numerical claims in this report actually came from the correct experiment, metric, dataset, and run.”

Representative toolchain to test:
- the published agent-integrity-analysis checker on its intended benchmark format;
- a synthetic project with multiple runs, metrics, and deliberate decoy values;
- a ReCRATE run crate and result table;
- a Markdown or LaTeX report containing claims, tables, captions, and references to run IDs.

Record:
- claim extraction coverage;
- correct evidence-link rate;
- false certification rate;
- proportion of claims conservatively left unresolved;
- ability to distinguish wrong-run values from absent values;
- human review time;
- quality of the exported audit report.

Do not optimize for the largest number of green checks. The key measure is precision of positive claims and clarity about what remains unknown.

## 3. Controlled synthetic test fixture

Create a small, openly licensed example research project with a known ground truth. It should contain:
- a stated research question and method;
- a small dataset with clear provenance;
- versioned analysis code;
- at least two experiment runs;
- at least two metrics;
- result tables with explicit schema and units;
- a final Markdown report;
- an RO-Crate / Workflow Run RO-Crate representation where supported;
- a complete mapping of each report claim to its true evidence source.

Then deliberately introduce known defects:
1. copy a correct number from the wrong run;
2. report the wrong metric while using a plausible number;
3. report a value with incorrect units;
4. use a rounded value that should still match;
5. include a claim with no supporting output;
6. include a supported claim whose evidence is inaccessible or restricted;
7. change the report after the run without updating the evidence reference;
8. include a value that appears in code or prose but not in an execution artifact.

Expected result: the tool should identify the right evidence or state that it cannot verify the claim. It must not label unsupported claims as false by default.

## 4. Evaluation metrics

### Technical correctness
- **Positive predictive value / precision:** among claims marked supported, how many are actually supported by the correct evidence?
- **Coverage:** what share of eligible claims can be checked?
- **False certification rate:** how often does the tool incorrectly mark a wrong-run or wrong-metric value as supported?
- **Abstention quality:** does it correctly distinguish ambiguous/unavailable evidence from false claims?
- **Traceability completeness:** can each positive finding identify the exact artifact, run, metric, and context?
- **Determinism:** do the same inputs and versions produce the same findings?
- **Portability:** can another person inspect the evidence package without the original service?

### User value
- Time to first useful result.
- Time required to prepare a project for handoff.
- Time required to review a report's claims.
- Number of issues found that users agree are important.
- Number of incorrect or irrelevant warnings.
- User ability to explain what each status means.
- Whether the user would use the tool again on a real project.

### Operational feasibility
- Installation burden.
- Runtime and memory requirements.
- Dependencies and platform constraints.
- Need for cloud services or API keys.
- Security risk from untrusted project content.
- Maintenance burden and integration complexity.

## 5. User discovery plan

No Common Knowledge interviews have yet been conducted. The following is a proposed plan, not evidence of completed outreach.

### Participants to seek

- research software engineers who support computational research;
- researchers who recently prepared a replication package or moved a project between tools;
- computational researchers who use Python/R/Jupyter or workflow engines;
- AI-for-science researchers and developers of research agents;
- research data stewards and librarians;
- journal/repository artifact evaluators where accessible.

Aim for a varied first set of roughly 8–15 conversations or asynchronous walkthroughs. This is a planning range, not a representative sample or a quota. A smaller number of detailed workflow observations can be more useful than many generic opinions.

### Interview method

Ask participants to walk through one recent, real task. Avoid asking whether they like Common Knowledge or whether a hypothetical tool sounds useful.

Questions:
1. Tell me about the last time you needed someone else to inspect, run, reproduce, or reuse a research project.
2. What were you trying to accomplish, and what triggered the task?
3. What files, tools, repositories, or services did you use?
4. Which part took the most time or required the most expertise?
5. What information was missing or difficult to trust?
6. What workaround did you use?
7. What happened when another person tried to use the project?
8. Which existing tools did you evaluate or reject, and why?
9. What would you not trust a new tool to do automatically?
10. Could you show a non-sensitive example of the workflow or its output?
11. How would you know that a new tool had genuinely improved the task?
12. What would make you use it again?

For AI-assisted research specifically:
- Which model/provider and tools were used?
- What exact artifacts and run information are currently retained?
- How are results mapped to manuscript claims?
- How are incorrect, superseded, or discarded runs represented?
- Which information cannot be disclosed?
- What does a reviewer actually need to see?

### Ethical and privacy safeguards

- Explain the purpose and voluntary nature of the conversation.
- Do not ask for confidential manuscripts, unpublished datasets, credentials, or private agent traces.
- Ask permission before recording or quoting.
- Store only the minimum notes needed.
- Anonymize findings unless explicit permission supports attribution.
- Do not present one participant as representing a discipline or institution.
- Seek appropriate ethics advice before conducting publishable human-subject research or generalizable studies.

## 6. Stop / proceed criteria

Proceed with a candidate only if:
- the problem is described consistently by people who experience it;
- current tools leave a concrete, observed gap;
- a newcomer can get a useful result from a narrow first workflow;
- success and failure can be tested with known examples;
- the product can be safe and honest about uncertainty;
- it can integrate with rather than displace established infrastructure.

Reject or defer a candidate if:
- user interest is mostly enthusiasm for the Common Knowledge mission;
- the product only duplicates a mature tool;
- the useful result requires a large network or hosted service before first use;
- positive results cannot be verified independently;
- the product must ingest sensitive data or execute untrusted code without a proportionate safety design;
- maintenance and support costs exceed the likely value.

## 7. Expected outputs from this research cycle

1. Reproducible notes from hands-on tool comparisons.
2. A small synthetic fixture with known ground truth and documented defects.
3. A candidate scorecard with qualitative evidence and confidence.
4. A record of actual user interviews or walkthroughs, if conducted.
5. One selected problem statement and one-page MVP brief, or an explicit decision to continue discovery.
6. A draft implementation roadmap only after the problem and scope are sufficiently supported.

---
*This is a plan for future experiments and discovery. No tests, interviews, or user validations described here have yet been performed.*
