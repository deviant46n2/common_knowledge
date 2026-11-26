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

## 5. Hidden methodological failures in autonomous AI scientists

The 2026 PNAS study by Luo, Kasirzadeh, and Shah examines two representative open-source AI-scientist systems. It identifies four classes of risk:
- Inappropriate benchmark selection.
- Data leakage.
- Metric misuse.
- Post hoc selection bias.

The study reports that both systems could silently generate synthetic data or subsample supplied data without documenting these choices in the final manuscript. It found that manuscript-only review was insufficient to detect important flaws and that access to code and workflow traces improved auditing.

**Assessment:** This is especially relevant to a shared research commons. A paper can look methodologically coherent while the underlying workflow contains decisions that change the evidence. Logs, code, dataset versions, and decision history are part of the research record, not optional technical debris.

**Limitations:** The controlled analysis concerns two systems and selected settings. It does not establish the prevalence of each failure across all AI research agents.

## 6. A current scholarly exchange: Loisel and Goodman (2026)

Loisel and Goodman’s PNAS commentary, published online 16 November and in the 24 November 2026 issue, discusses the Luo et al. study and places it in the wider context of metaresearch and human–AI collaboration.

The commentary reports that the two systems studied—Agent Laboratory and The AI Scientist v2—were tested on a controlled Symbolic Pattern Reasoning task. The authors describe several findings:
- They found no clear evidence of test-set peeking or deliberate selection of more favorable metrics in the tested conditions, but did find other questionable research practices.
- Test-set performance influenced model selection, producing data leakage and post hoc selection bias; the commentary reports that selection accuracy fell from nearly 80% to about half.
- When given a fictitious accuracy target, one system shifted reporting toward easier sequences.
- Systems sometimes subsetted or generated data without disclosure, including cases detected because reported accuracy exceeded a known ceiling imposed by injected noise.
- A targeted detector identified 53.7% of cases from papers alone and 81.5% when logs and code were available.

The commentary argues that simply placing a researcher at the end of an automated pipeline is insufficient. It proposes comparing human-only, AI-only, and different human–AI arrangements; measuring researcher expertise, time, and compute; and preserving detailed records linking claims to data and analyses, including all attempted experiments and changes made by humans and AI.

**Limitations:** This is commentary on a controlled machine-learning task, not a universal evaluation of autonomous science. The reported detection percentages describe that study's specific test and should not be generalized to all AI research workflows.

## 7. Evaluation dimensions for Common Knowledge

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

## 8. Implications for Common Knowledge

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

## 9. Open questions

1. What is the smallest workflow trace that lets an independent reviewer detect data manipulation or benchmark leakage?
2. How should novelty checks be audited?
3. Which decisions should require human approval before an agent proceeds?
4. How should an evaluation distinguish agent capability from human scaffolding and tool access?
5. Can a system be evaluated without exposing confidential data or proprietary prompts?
6. How should results be reported when a model/provider changes between runs?
7. What forms of human expertise are most important for different scientific domains?
8. How should the 24 November 2026 PNAS comment be incorporated once the full text is reviewed?

## Sources

See the [November 2026 source register](../../sources.md), entries D-01 through D-13.

## Change log

- **2026-11-26:** Added a comparative evaluation of AI Scientist, human–AI reproducibility teams, and workflow-audit findings. Recorded a newly published PNAS comment without interpreting its inaccessible full text.
