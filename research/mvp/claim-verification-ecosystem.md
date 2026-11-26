# Claim Verification and Research-Agent Tool Ecosystem

- **Reviewed:** 26 November 2026
- **Status:** Source-inspected desk research; not an independent evaluation
- **Purpose:** Determine whether a claim-to-evidence or research-agent workflow is a defensible Common Knowledge MVP.

## Executive conclusion

The claim-to-evidence space is now too populated for Common Knowledge to justify building a generic checker or research-agent workflow without a sharply evidenced gap.

The ecosystem includes:
- general reproducibility certificates (ReproCert);
- manuscript/source/result claim checking (reproducible-science);
- paper-to-artifact reproduction workflows (Research Paper Reproduction for Codex);
- end-to-end AI-assisted research scaffolds (autoresearch);
- paper lifecycle agent skills;
- research method agents (ReCRATE, Paper2Agent);
- workflow execution with provenance (FlowProof);
- evidence graphs and packaging (FAIRSCAPE/EVI);
- benchmark datasets for scientific agent behavior and claim verification (OpenDiscoveryTrace, Into the Unknown, AutoMat, SciClaimEval).

A Common Knowledge product in this area would need to solve a specific integration or usability problem that these tools do not already handle. Merely combining their feature lists is not enough.

## 1. ReproCert

**Repository:** [AETHERXGLOBAL/reprocert](https://github.com/AETHERXGLOBAL/reprocert)  
**License:** Apache-2.0  
**Declared release:** stable v1.0.0  
**Package:** aetherx-reprocert, Python 3.11+

ReproCert turns a declared technical claim into a command, observed evidence, explicit checks, and a machine-readable certificate. Examples include benchmark thresholds, pytest/JUnit results, reproducible builds, data-quality assertions, and AI/research workflows.

It supports CLI initialization, execution, verification, and GitHub Actions. It distinguishes PASS, FAIL, INCONCLUSIVE, and ERROR. Its own documentation explicitly says that a passing certificate does not establish scientific truth, benchmark fairness, or software security. Its technical evaluation pack offers an external engineer a bounded installation/execution/verification path without a hosted account.

**Implication:** A generic claim-to-evidence certificate generator is already available. Common Knowledge would need a demonstrably missing research-specific workflow or integration, not recreate the certificate engine.

## 2. reproducible-science

**Repository:** [anon-submission-account/reproducible-science](https://github.com/anon-submission-account/reproducible-science)  
**License:** MIT, as declared in repository  
**Runtime:** Python 3.11+

The suite provides:
- preregistration/plan freezing against a commit and content hash;
- input sealing and recorded run outputs;
- claims that point to exact values and locations in result files;
- manuscript quotation checks against cited source passages;
- unified verification with separate outcomes for mismatch, missing evidence, checks that did not run, and source errors.

It emphasizes deterministic, offline checks, separation of facts from policy verdicts, and distinct statuses rather than a single pass/fail result. Its functions are split into separately installable packages.

**Implication:** A broad local-first research claim checker already exists with several features we had considered. Its package design and output contracts should be inspected before any Common Knowledge implementation.

## 3. Research Paper Reproduction for Codex

**Repository:** [FullFighting/reproduce-research-paper](https://github.com/FullFighting/reproduce-research-paper)  
**License:** MIT, as declared in repository  
**Declared release:** v1.4.0

This evidence-first Codex skill reads a paper, maps claims to official code/data/commands, prepares a reviewable reproduction plan, runs only after explicit approval, extracts metrics from run-generated artifacts, compares typed values under declared policies, and produces an evidence bundle with logs, hashes, provenance, and claim-scoped reports.

The repository reports 15 public claim checks passing its own benchmark and describes a deterministic runtime, isolated execution, resource budgets, secret-safe defaults, and independent verification. Those are project-reported figures and capabilities, not an independent Common Knowledge evaluation.

**Implication:** Even paper-to-artifact claim verification has feature-rich open-source implementations. We should test them rather than assume the gap is that no one has built a usable workflow.

## 4. autoresearch

**Repository:** [aznikline/autoresearch](https://github.com/aznikline/autoresearch)

autoresearch describes a 12-stage pipeline from idea through literature, hypothesis, experiment, analysis, paper draft, and export. It includes an evidence ledger, code/config hashes, protocol fingerprints, multi-metric experiment tracking, claim verification, human review gates, venue contracts, and domain-specific methodology skills.

Its README explicitly states that it is not an autonomous paper generator and that novelty, real data, real compute, and peer review remain human responsibilities. It reports a worked example with 40 trials and keeps submission readiness false where blockers remain.

**Implication:** A general AI-assisted research lifecycle scaffold is already being explored. Common Knowledge should avoid competing with it as a broad research agent or paper factory.

## 5. Agent skills for the research-paper lifecycle

[research-paper-lifecycle-skills](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills) describes 42 agent skills covering source discovery, writing, citation checks, result verification, artifact preparation, submission, rebuttal, and presentation. [open-research-skills](https://github.com/gxCaesar/open-research-skills) includes an evidence-and-claims handoff reference with explicit distinctions among observed, failed, not-run, and inferred evidence.

These are not complete hosted software platforms, but demonstrate how quickly reusable agent workflows and open skill libraries are emerging.

**Implication:** A generic prompt/skill collection is unlikely to be differentiated. Any Common Knowledge agent integration should have a concrete software capability or validated workflow behind it.

## 6. Existing evaluations of research-rigor tools and scientific agents

### “Use as directed?” — 2026 tool comparison

Eckmann et al. compared 11 automated tools across nine research-rigor criteria using 1,500 open-access PubMed Central manuscripts and human-curated labels. The authors found that some criteria had a clear best tool, while for others combining tools outperformed any single tool. The paper identifies differences in tool definitions, input preprocessing, paper sections examined, domain, algorithm, accessibility, and desired sensitivity.

The authors emphasize validation on domain-relevant human-curated data and regular re-evaluation when tools or underlying LLMs change.

**Implication:** Tool evaluation itself is valuable, but a broad biomedical rigor-tool benchmark already exists. A Common Knowledge benchmark would need a different target—such as cross-tool provenance interoperability or specific AI-agent failure modes—and should not duplicate this study.

### AutoMat

[AutoMat](https://jhu-clsp.github.io/AutoMat/) is a benchmark for evaluating whether LLM-based agents can reproduce claims from computational materials-science papers. It targets recovery of underspecified procedures, navigation of specialized toolchains, and determining whether resulting evidence supports a claim.

**Implication:** Domain-specific benchmarks for agentic scientific reproduction are also appearing. Any benchmark proposal must explain what failure modes and users it adds beyond AutoMat, OpenDiscoveryTrace, and Into the Unknown.

## 7. Provisional market map

| Capability | Existing projects | Implication for Common Knowledge |
|---|---|---|
| Claim → command → evidence → certificate | ReproCert | Do not build a generic certificate engine |
| Claim → exact artifact location/value | reproducible-science | Do not build a generic claim/result checker |
| Paper → reproduction plan → run → report | Research Paper Reproduction for Codex | Do not build a generic paper reproduction agent |
| Idea → literature → experiments → paper workflow | autoresearch | Do not build an all-in-one AI scientist scaffold |
| Paper → executable method agent | Paper2Agent, ReCRATE | Integrate; do not clone |
| AI agent → reproducible pipeline execution | FlowProof | Integrate; avoid generic execution server |
| Research data/software/computation → evidence graph | FAIRSCAPE/EVI | Reuse existing models and tools |
| Research workflow run → portable provenance | Workflow Run RO-Crate | Use the standard; avoid proprietary run format |
| Research-rigor checks across manuscripts | ScreenIT tools and 2026 comparison | A broad rigor checker is not a new category |
| Scientific-agent process evaluation | OpenDiscoveryTrace, Into the Unknown, AutoMat | Any new benchmark needs a narrow, distinct research question |

## 8. What might remain open

The first-pass review suggests three possible gaps, none yet validated:

1. **Cross-tool interoperability:** converting and validating evidence records across existing research agents, workflow engines, certificates, RO-Crates, and evidence graphs without losing meaning.
2. **A low-friction user workflow:** helping a researcher use a small number of existing tools together, with clear explanations and a portable final artifact, rather than asking them to understand each tool's ecosystem.
3. **Independent conformance testing:** testing whether integrations actually preserve the semantics they claim to preserve—for example, whether a run certificate, Workflow Run RO-Crate, and manuscript claim still point to the same code, inputs, outputs, and run after export/migration.

These are only promising questions. There may already be tools we have not found. The next phase should investigate the exact handoffs between projects and test them on a controlled fixture.

## Sources

- [ReproCert repository](https://github.com/AETHERXGLOBAL/reprocert)
- [reproducible-science repository](https://github.com/anon-submission-account/reproducible-science)
- [Research Paper Reproduction for Codex](https://github.com/FullFighting/reproduce-research-paper)
- [autoresearch](https://github.com/aznikline/autoresearch)
- [research-paper-lifecycle-skills](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills)
- [open-research-skills](https://github.com/gxCaesar/open-research-skills)
- [Use as directed? A comparison of software tools intended to check rigor and transparency of published work (2026)](https://doi.org/10.1371/journal.pone.0342225)
- [AutoMat benchmark](https://jhu-clsp.github.io/AutoMat/)
- [OpenDiscoveryTrace](https://github.com/aayambansal/OpenDiscoveryTrace)
- [Into the Unknown](https://arxiv.org/abs/2610.19159)
- [Beyond fabrication](https://arxiv.org/abs/2610.38691)

---
*This review is based on public documentation and source inspection. Project capabilities and self-reported benchmarks have not been independently verified by Common Knowledge.*
