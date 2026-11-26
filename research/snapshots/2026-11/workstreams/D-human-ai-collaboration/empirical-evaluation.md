# Workstream D — Empirical Evaluation of AI Research Agents

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Selected evidence from three studies and one current scholarly exchange; not a systematic review
- **Workstream:** [D — Human–AI research collaboration](README.md)

## 1. Why evaluate workflows rather than demonstrations?

A system that produces a paper-like manuscript has completed a visible output task. That does not establish that it selected an appropriate question, used valid data, implemented its methods correctly, avoided selective reporting, or produced a claim that survives independent scrutiny.

The recent evidence points toward a distinction between **workflow completion** and **scientific validity**. Evaluation must inspect intermediate decisions and artifacts, not just the final manuscript.

## 2. AI Scientist: end-to-end capability with important limitations

The 2026 Nature paper *Towards End-to-End Automation of AI Research* describes a system that generates research ideas, searches literature for novelty, writes and executes code, analyzes experiments, drafts a manuscript, and uses an automated reviewer.

The paper reports that one of three submitted workshop papers was accepted. It also documents recurring failures:
- Ideas can be naive or underdeveloped.
- Implementations may not correctly realize the proposed method.
- Methodological rigor can be insufficient.
- Experimental execution can contain errors.
- Citations may be inaccurate or hallucinated.
- Manuscript presentation can contain inconsistencies.

**Assessment:** The work demonstrates a real, integrated research workflow in a narrow machine-learning setting. It does not demonstrate reliable end-to-end scientific discovery at the level of leading human research, nor broad transfer across disciplines.

## 3. Human–AI reproduction: assistance versus delegation

The 2026 PNAS study assigned 288 researchers to 103 teams and compared three approaches to reproducing quantitative social-science findings:
- Human-only teams: 94% reproduction rate.
- AI-assisted teams: 91%.
- AI-led teams with minimal human oversight: 37%.

Human-only teams identified significantly more major coding errors. AI-assisted teams performed similarly to human-only teams on most outcomes, but did not demonstrate a measurable overall advantage in the study.

**Interpretation:** In this specific setting, AI assistance did not outperform human-only work, while AI-led work performed substantially worse. AI may still be useful for screening or scale-constrained tasks, but this experiment supports retaining substantive human expertise in critical verification.

**Limitations:** Results are specific to the task, research domain, teams, and systems used. They do not establish a universal ceiling for AI assistance or future models. The article received an affiliation correction in July 2026; the correction did not change the results.

## 4. Hidden methodological failures in autonomous AI scientists

The 2026 PNAS study by Luo, Kasirzadeh, and Shah examines two representative open-source AI-scientist systems. It identifies four classes of risk:
- Inappropriate benchmark selection.
- Data leakage.
- Metric misuse.
- Post hoc selection bias.

The study reports that both systems could silently generate synthetic data or subsample supplied data without documenting these choices in the final manuscript. It found that manuscript-only review was insufficient to detect important flaws and that access to code and workflow traces improved auditing.

**Assessment:** This is especially relevant to a shared research commons. A paper can look methodologically coherent while the underlying workflow contains decisions that change the evidence. Logs, code, dataset versions, and decision history are part of the research record, not optional technical debris.

**Limitations:** The controlled analysis concerns two systems and selected settings. It does not establish the prevalence of each failure across all AI research agents.

## 5. A current scholarly exchange

On 24 November 2026, Loisel and Goodman published a PNAS comment titled *The AI Scientist in the Mirror: Shared Flaws, Joint Remedies*, responding to the October 2026 PNAS study of hidden pitfalls.

The bibliographic record confirms the comment and its relationship to the earlier article. The full text was not available in the source material reviewed for this pass, so this report does not summarize or endorse its arguments. It is recorded as a follow-up source to retrieve and assess in the next research cycle.

This is a deliberate evidence boundary: a relevant title and citation are not enough to claim knowledge of an article's argument.

## 6. Evaluation dimensions for Common Knowledge

A useful AI research evaluation should assess at least:

| Dimension | Question |
|---|---|
| Research question | Is the question meaningful, scoped, and genuinely open? |
| Literature grounding | Are sources real, relevant, and accurately represented? |
| Novelty | Is novelty checked against relevant prior work, not just model memory? |
| Design | Are methods appropriate to the question and discipline? |
| Data provenance | Are inputs, transformations, synthetic data, and exclusions disclosed? |
| Benchmark integrity | Were evaluation criteria selected before results were known? |
| Implementation | Does the code actually implement the stated method? |
| Execution | Can the workflow be rerun in a documented environment? |
| Analysis | Are statistics, metrics, uncertainty, and comparisons appropriate? |
| Reporting | Are negative results, deviations, and limitations included? |
| Independent verification | Can another person inspect or reproduce key claims? |
| Human accountability | Who made and approved consequential decisions? |
| Workflow auditability | Are intermediate artifacts available for review? |

A single composite score could hide critical failure. Results should be reported by dimension and include the scope and evidence for each judgment.

## 7. Implications for Common Knowledge

Potential design requirements:
1. Store workflow artifacts alongside manuscripts and results.
2. Record benchmark and metric choices before experimentation where appropriate.
3. Preserve original inputs and disclose generated or transformed data.
4. Require claim-to-source traceability for literature-derived claims.
5. Make human interventions and approvals visible.
6. Support independent re-execution and review.
7. Separate agent task-completion metrics from scientific-quality evaluation.
8. Preserve failed runs and discarded experiments when they materially affect interpretation.
9. Allow evaluators to inspect the complete process under appropriate privacy and security controls.
10. Record corrections and post-publication commentary as part of the evolving scientific record.

These are candidate requirements for pilot testing, not a final AI policy.

## 8. Open questions

1. What is the smallest workflow trace that lets an independent reviewer detect data manipulation or benchmark leakage?
2. How should novelty checks be audited?
3. Which decisions should require human approval before an agent proceeds?
4. How should an evaluation distinguish agent capability from human scaffolding and tool access?
5. Can a system be evaluated without exposing confidential data or proprietary prompts?
6. How should results be reported when a model/provider changes between runs?
7. What forms of human expertise are most important for different scientific domains?
8. How should the 24 November 2026 PNAS comment be incorporated once the full text is reviewed?

## Sources

See the [November 2026 source register](../../sources.md), entries D-01 through D-11.

## Change log

- **2026-11-26:** Added a comparative evaluation of AI Scientist, human–AI reproducibility teams, and workflow-audit findings. Recorded a newly published PNAS comment without interpreting its inaccessible full text.
