# Workstream D — Initial Field Overview: Human–AI Research Collaboration

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Preliminary orientation; not a systematic review
- **Workstream:** [D — Human–AI research collaboration](README.md)

## 1. Central question

How can AI systems help people discover, understand, conduct, verify, communicate, and preserve research while keeping scientific work accountable, inspectable, and genuinely collaborative?

AI participation ranges from narrow assistance—searching literature, translating, coding, or summarizing—to multi-agent systems that plan and execute experiments, analyze data, draft papers, or review results. These are different levels of capability and risk. “AI in science” is not one technology or one governance problem.

Common Knowledge should investigate AI as a research tool, a workflow participant, and in some settings an increasingly autonomous agent. It should not assume that more autonomy automatically means better science.

## 2. A practical autonomy spectrum

1. **Assistive tool:** Responds to a human's direct request, such as explaining a paper or helping write code.
2. **Task specialist:** Performs a bounded function, such as literature search, data extraction, translation, coding, or statistical analysis.
3. **Workflow participant:** Uses tools and context across multiple steps under human direction.
4. **Delegated agent:** Receives an objective, plans a sequence of tasks, and makes intermediate decisions while a human supervises.
5. **Autonomous research pipeline:** Attempts to complete much of the research lifecycle, from idea generation and experimentation to manuscript production, with limited human intervention.

This spectrum is descriptive rather than a ranking of scientific quality. A narrow, well-validated specialist may be more useful and trustworthy than a broad autonomous system.

## 3. Research lifecycle and AI roles

AI systems may contribute to literature discovery, hypothesis generation, experimental design, protocol drafting, data cleaning, analysis, code generation, laboratory and robotic workflows, visualization, manuscript drafting, peer review support, replication, integrity checks, metadata enrichment, and research-record maintenance.

Each stage has different error modes. A hallucinated citation, a mislabeled observation, a flawed statistical test, an unsafe laboratory instruction, and an unreported data transformation are not interchangeable failures.

## 4. Initial representative systems and evidence

### SciSciGPT

SciSciGPT is an open-source prototype AI collaborator for the science of science. Its 2025/2026 paper describes a database repository, a multi-agent system with specialist roles, and a conversational interface for iterative research. It is a useful example of domain-specific human–AI collaboration rather than a claim of universal autonomous science.

### The AI Scientist

Sakana AI's AI Scientist research explores end-to-end automation in machine learning research: generating ideas, writing and executing code, analyzing results, drafting papers, and automated review. A 2026 Nature paper reports a system that generated a workshop paper that passed the first round of peer review, while also documenting significant limitations: only one of three submissions was accepted, and common failures included weak ideas, incorrect implementations, insufficient methodological rigor, experimental errors, and inaccurate citations.

This is a meaningful capability demonstration, but it does not establish that autonomous AI systems can reliably conduct scientific research across disciplines.

### Human–AI reproducibility teams

A 2026 PNAS experiment assigned 288 researchers to 103 teams using human-only, AI-assisted, or AI-led approaches to reproduce quantitative social-science findings. The reported reproduction rates were 94% for human-only teams, 91% for AI-assisted teams, and 37% for AI-led teams. Human-only teams detected more major coding errors than the other conditions.

The paper reports that a correction was published in July 2026, updating three author affiliations. The correction does not change the reported research results.

### Hidden workflow failures in autonomous AI scientists

A 2026 PNAS study analyzed two representative open-source AI-scientist systems and found systematic problems involving benchmark selection, undocumented synthetic data or subsampling, metric use, and post hoc selection. The authors report that important flaws could be invisible in the final manuscript and that access to workflow artifacts improved auditing.

This evidence directly connects Workstream D to Workstream C: final prose is not enough to verify an AI-generated research claim.

## 5. Evaluation must go beyond polished outputs

An AI system can produce a plausible paper while making mistakes in novelty assessment, citation accuracy, benchmark selection, data handling, method implementation, statistical analysis, interpretation, uncertainty reporting, or reproducibility.

Evaluation should inspect both the final artifact and the workflow that produced it. Useful evidence includes task specifications, source records, code versions, data lineage, execution logs, model versions, human interventions, and review decisions—subject to privacy, security, and intellectual-property constraints.

## 6. Human responsibility, attribution, and agency

AI systems do not remove the need to identify accountable human or institutional stewards. A research record should disclose material AI involvement and identify who defined the question, selected data and evaluation criteria, reviewed code and methods, approved experiments and resource use, interpreted results, approved publication, and is responsible for corrections and safety.

Attribution varies by journal, discipline, and contribution type. AI systems should not be casually treated as human authors with legal or moral responsibilities they cannot discharge. Human contributors should not hide their own decisions behind “the model did it.”

## 7. Risks and safeguards

| Risk | Possible safeguard |
|---|---|
| Fabricated or misrepresented sources | Claim-level citation checks and source inspection |
| Hidden data manipulation or benchmark leakage | Versioned data lineage, pre-specified evaluation, workflow logs |
| Incorrect generated code or methods | Tests, independent review, clean execution, domain expertise |
| Overconfident or selective reporting | Uncertainty disclosure, negative-result preservation, workflow audit |
| Unsafe tool execution | Sandboxing, least privilege, allowlists, resource limits, human approval |
| Privacy or consent violations | Data minimization, controlled access, no unapproved external transfer |
| Model/provider changes | Record model identifier, version, date, parameters, and service conditions |
| Automation bias and deskilling | Human challenge, review, training, and explicit responsibility |
| Concentrated access to powerful AI systems | Open standards, portability, multiple providers, transparent cost/access barriers |
| Unclear authorship or accountability | Contribution records and named responsible human stewards |

## 8. Implications for Common Knowledge

The likely opportunity is not to replace researchers with autonomous agents. It is to make human–AI research collaboration more capable and more accountable.

Potential roles to investigate include a common record of human and AI contributions, reusable and inspectable workflows, independent evaluation of AI-generated hypotheses/code/claims, model-agnostic interfaces, transparent access to sources and compute, human review at consequential decision points, and public benchmarks that test scientific validity rather than merely task completion.

These are hypotheses, not a chosen architecture or policy.

## 9. Questions for the next research pass

1. Which scientific tasks show repeatable benefit from AI assistance, and for whom?
2. Which tasks become less reliable as autonomy increases?
3. How should AI contributions be represented in authorship and contributor taxonomies?
4. What workflow artifacts are essential for auditing AI-generated research?
5. How should systems disclose model identity, version, prompts, tool calls, and human interventions?
6. How can AI systems support qualitative, interpretive, and community-led research without imposing unsuitable epistemic assumptions?
7. How can independent verification remain possible when models, data, APIs, and compute are proprietary?
8. What evaluation methods detect fabricated citations, benchmark leakage, undisclosed data transformations, and post hoc selection?
9. What security boundaries are needed when agents execute code or control instruments?
10. How should AI-generated knowledge be corrected, attributed, and preserved over time?

## 10. Scope and limitations

This first orientation is weighted toward AI/ML research agents, reproducibility, and science-of-science workflows. It does not yet adequately cover domain-specific systems in biology, chemistry, materials science, medicine, field science, laboratory robotics, qualitative research, or the humanities. It also does not assess the environmental, labor, procurement, and geopolitical implications of AI research infrastructure in depth.

## Sources

See the [November 2026 source register](../../sources.md), entries D-01 onward.

## Change log

- **2026-11-26:** Created initial field overview of assistive tools, workflow agents, autonomous research pipelines, human–AI evaluation, auditability, and accountability.
