# Workstream D — Preliminary Comparative Synthesis

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Preliminary synthesis; workstream remains in progress
- **Workstream:** [D — Human–AI research collaboration](README.md)

## 1. Main finding: scientific capability and scientific accountability must develop together

Current AI systems can contribute across many research tasks, and integrated agents can complete substantial portions of a research workflow. But successful task completion and polished manuscripts do not establish scientific validity.

The evidence reviewed includes:
- A domain-specific open-source research collaborator (SciSciGPT).
- An end-to-end AI Scientist system evaluated in machine-learning research.
- A randomized comparison of human-only, AI-assisted, and AI-led teams verifying quantitative social-science results.
- A controlled analysis showing hidden methodological failures in autonomous AI scientist systems.
- Publisher policies emphasizing human accountability, transparency, and confidentiality.
- CRediT as a structured taxonomy for human research contributions.

These sources support a cautious, task-specific view rather than a general claim that AI can or cannot do science.

## 2. Findings grounded in the current sample

### 2.0 Human–AI collaboration is task-dependent, not automatically synergistic

A preregistered 2024 meta-analysis of 106 experiments and 370 effect sizes found that human–AI combinations were, on average, better than humans alone but worse than the best of humans or AI alone. Decision tasks showed average performance losses; content-creation tasks were more promising. Combinations were more successful when the human alone outperformed the AI, and less successful when the AI alone was stronger.

**Assessment:** Common Knowledge should evaluate division of labor and task allocation, not assume that adding a human reviewer or AI assistant creates synergy. Measure the best standalone baseline, combined performance, time, and cost.

### 2.1 More autonomy does not automatically produce better research

The PNAS reproducibility experiment found similar reproduction rates for human-only and AI-assisted teams (94% and 91%) in its specific setting, while AI-led teams achieved 37%. Human-only teams identified more major coding errors.

**Assessment:** Human–AI collaboration may preserve much of the performance of expert teams, but delegating verification to AI with minimal human oversight can reduce reliability. This is evidence from one task family, not a universal law.

### 2.2 End-to-end workflow demonstrations are meaningful but narrow

The AI Scientist's 2026 Nature paper demonstrates a substantial automated workflow, but only one of three submitted workshop papers was accepted and the authors document errors in ideas, implementation, experimental rigor, and citations.

**Assessment:** The system is a real research-engineering milestone. It is not evidence that autonomous research agents are ready to replace domain expertise or peer review.

### 2.3 Final manuscripts can conceal workflow failures

The 2026 PNAS analysis found benchmark-selection problems, undocumented synthetic data or subsampling, and other methodological issues in two AI scientist systems. The flaws were not reliably visible in the final manuscript; workflow artifacts improved auditing.

**Assessment:** A paper-only record is insufficient for AI-generated research. Data lineage, code, benchmark selection, logs, and intermediate artifacts need to be preserved when they materially affect claims.

### 2.4 Attribution and accountability are separate

CRediT provides a structured vocabulary for human contributions but does not define authorship eligibility. Publisher policies vary, but the reviewed policies consistently retain human responsibility for accuracy and integrity and emphasize disclosure and confidentiality.

**Assessment:** Common Knowledge should record AI systems as tools or workflow participants with explicit task descriptions, while naming accountable human contributors and their roles. A model cannot assume the responsibilities of a human author.

### 2.5 Auditability must be designed into the workflow

An audit record cannot be reconstructed reliably after the fact if a system never captured its inputs, outputs, data transformations, model identity, tool calls, and human interventions.

**Assessment:** Research agents should emit structured, versioned workflow records as part of normal operation. The record should be proportionate to risk and should protect confidential material rather than publishing raw traces indiscriminately.

## 3. Candidate design principles

These are hypotheses for technical and community testing, not adopted Common Knowledge policy.

1. **Human accountability is explicit:** Every consequential research contribution has a responsible human or institution.
2. **AI participation is disclosed:** Record material AI use in proportion to its influence and risk.
3. **Autonomy is declared:** Identify whether AI was assistive, specialist, a workflow participant, delegated, or autonomous.
4. **Workflow evidence is preserved:** Capture inputs, source versions, model/tool identity, actions, outputs, failures, and human decisions where material.
5. **Claims are auditable:** Link statements to sources, data, methods, code, and results.
6. **Benchmarks are governed:** Record why benchmarks and metrics were chosen, and preserve pre-specified criteria where appropriate.
7. **Data transformations are visible:** Disclose generated, filtered, subsampled, or otherwise transformed data.
8. **Verification is independent where possible:** Separate the system that produced a claim from the system or person that evaluates it.
9. **Confidentiality is protected:** Do not expose unpublished, personal, or sensitive information through external tools without authority.
10. **Attribution is accurate:** Use contributor-role vocabularies for humans and a distinct record for AI systems.
11. **Corrections remain visible:** Preserve the history of outputs, claims, and publication status.
12. **Evaluation is task-specific:** Do not treat benchmark performance or workflow completion as general scientific competence.

## 4. Candidate audit model

The [proposed AI research audit record](AI-research-audit-record.md) is a first draft. It connects:
- Project identity and human responsibility.
- Task and autonomy specification.
- Model and execution context.
- Input and source lineage.
- Workflow traces and tool calls.
- Results, evaluation, and interpretation.
- Human review and accountability.
- Privacy, security, and correction history.

It needs practical testing with real workflows before adoption. Some information may need controlled access or redaction.

## 5. Gaps in this investigation

- Domain-specific systems in biology, chemistry, medicine, materials science, field research, and laboratory robotics.
- Qualitative, humanities, and community-led research.
- Comparative evaluations of multiple models and agent architectures on the same research tasks.
- Cost, energy, access, and labor implications.
- Model/provider transparency and reproducibility for hosted systems.
- Legal and institutional questions around AI-generated research, data, and intellectual contributions.
- Direct researcher and reviewer interviews.
- The full text and analysis of the 24 November 2026 PNAS comment on autonomous AI scientist pitfalls.

## 6. What would change this assessment?

The current cautious assessment should change if independent, preregistered, cross-domain evaluations show that AI-led systems consistently match or exceed expert human teams on scientifically meaningful tasks, including error detection, robustness, and transparent reporting—not merely manuscript generation.

Conversely, a blanket prohibition on autonomous research would be premature if bounded agentic workflows prove useful, auditable, and safe in specific contexts.

## 7. Next research actions

1. Retrieve and assess the full text of the 24 November 2026 PNAS comment.
2. Expand system profiles beyond AI Scientist and SciSciGPT, including domain-specific scientific agents.
3. Test the proposed audit record on a small AI-assisted literature review and a code/experiment workflow.
4. Compare current agent benchmarks for task completion, scientific validity, and workflow auditability.
5. Consult researchers, editors, and research-integrity specialists about disclosure and accountability.
6. Produce a bounded field synthesis only after these gaps are addressed.

## Sources

See the [November 2026 source register](../../sources.md), entries D-01 onward.

## Change log

- **2026-11-26:** Added a preliminary synthesis of capability, autonomy, workflow auditability, attribution, and human accountability. Workstream D remains in progress.
