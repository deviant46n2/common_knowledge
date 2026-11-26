# Direct Competitors and Adjacent Research Projects

- **Reviewed:** 26 November 2026
- **Status:** Source-inspected desk review; not a full code audit or hands-on installation test
- **Purpose:** Record projects that materially overlap with possible Common Knowledge MVPs and identify where to integrate rather than duplicate.

## Executive summary

Four projects materially change the MVP landscape:

1. **Paper2Agent** demonstrates paper-to-agent conversion at significant scale in a Nature paper.
2. **ReCRATE** is a close, MIT-licensed implementation combining RO-Crate, method reuse, workflow execution, result comparison, domain profiles, and per-run provenance.
3. **agent-integrity-analysis** contains a working MIT-licensed numerical claim-to-evidence checker with a conservative evaluation on one AI-research benchmark.
4. **Trust, but verify, audit and attribute** proposes a human-in-the-loop verification methodology with example toolchains for mathematics and statistics.

A fifth project, **OpenDiscoveryTrace**, supplies a dataset and benchmark for evaluating process traces rather than only final research outputs. **SciClaimEval** supplies a cross-modal claim-verification dataset for scientific papers, but does not itself establish whether a claim is supported by the exact computational run that generated a result.

The implication is not that all product opportunities are closed. It is that the product cannot be framed as a generic research agent, workflow provenance recorder, or numerical claim checker. A defensible gap may exist in the interoperability and usability layer connecting research claims to standard, portable, inspectable evidence records across tools. This is still a hypothesis.

## 1. Paper2Agent

**Project:** [Paper2Agent](https://www.nature.com/articles/s41586-026-11044-y)  
**Code:** [jmiao24/Paper2Agent](https://github.com/jmiao24/Paper2Agent)  
**Publication:** Nature, 2026

### What it does

Paper2Agent converts a research paper and associated codebase into an interactive paper-specific agent. It uses a multi-agent pipeline to locate code, configure an environment, extract methodological tools, test and refine those tools, and package them as MCP servers. It also exposes static research materials as resources.

### Reported evaluation

The paper reports three evaluation corpora:
- 100 computational biology papers;
- 26 data- and discovery-focused papers;
- 10 non-biology computational papers.

Within the 100-paper computational biology sample, 74 were successfully agentified, producing 599 proposed tools, 593 of which passed automated validation. On 300 tutorial-derived questions, the Paper2Agent setup achieved 91.2 ± 1.6% accuracy, compared with 80.3 ± 2.3% for direct repository access using the same baseline model. The paper also reports results on non-biology computational and data/discovery-focused corpora.

These are study-specific evaluation results. They do not establish that arbitrary papers can be converted, that all generated tools are scientifically valid, or that open-ended scientific reasoning can be automated safely.

### Limitations relevant to Common Knowledge

The authors report that some repositories could not be agentified because of missing executable code, missing data or model artifacts, environment/dependency problems, and scripts that did not generalize. The paper explicitly retains human oversight for open-ended scientific reasoning.

### Product implication

Do not build a generic paper-to-agent converter. Study its interfaces, data model, and failure cases. A possible integration could allow downstream tools to consume Paper2Agent artifacts and attach more explicit, portable evidence records.

## 2. ReCRATE

**Project:** [biaperotto/recrate](https://github.com/biaperotto/recrate)  
**License:** MIT, as declared in its repository  
**Version declared in pyproject:** 0.1.0  
**Runtime declared:** Python 3.10+  
**Last repository commit observed:** 25 November 2026  
**Project's own status:** Proof of concept built at the Reinvent the Wheel hackathon in October 2026

### What it does

ReCRATE starts from a paper, RO-Crate, or WorkflowHub workflow and creates a research-method agent. Its documented workflow:
- finds or drafts a structured research object;
- identifies methods, inputs, outputs, parameters, and published results;
- runs the method on the original data where supported;
- compares results with published values or workflow test expectations;
- checks new input data against declared method requirements through domain profiles;
- records reproductions, follow-up checks, and reuses as Workflow Run RO-Crates;
- exposes capabilities through a CLI, local app, and MCP.

### Breadth documented in the repository

The README documents adapters for Galaxy, nf-core/Nextflow, CWL, Snakemake, and Jupyter. It also describes domain profiles for bioimaging and time series, with genomics, single-cell, and spatial-omics profiles marked as sketches. Examples include a nuclei segmentation workflow, penguin size analysis, StarDist, a workflow from WorkflowHub, and a synthetic demonstration.

The architecture distinguishes readiness from successful reproduction and uses a verdict ladder: materials found, runs, same numbers, and same conclusion. The last level requires a named person's judgment. It also documents sourced tolerances, append-only run records, and sandboxing.

### Limits stated by the project

Its README identifies itself as a proof of concept. It reports that some language environments use the researcher's interpreter rather than a pinned environment; some R/container work remains future work; some profiles are sketches or synthetic-only; GPU, cluster, very large/restricted data, and paid-API methods are described rather than run; and a 20–50-paper/workflow evaluation remains planned.

These are the project's own status statements, not independent verification.

### Product implication

ReCRATE is the closest project inspected so far to the earlier Common Knowledge research-packager/reproducibility-agent concept. It already covers much of the obvious product surface.

Recommended response:
- install and test it against representative workflows;
- map its input/output contracts and extension points;
- evaluate whether its Workflow Run RO-Crates can be consumed by other tools;
- identify concrete unmet user tasks rather than assumed feature gaps;
- consider an upstream contribution or interoperable companion if evidence supports it.

Do not copy or fork it simply to make a Common Knowledge-branded version. Its MIT license permits reuse subject to its terms, but technical, community, and attribution considerations still matter.

## 3. agent-integrity-analysis — numerical claim-to-evidence checker

**Project:** [mos3b-faqeeh/agent-integrity-analysis](https://github.com/mos3b-faqeeh/agent-integrity-analysis)  
**Paper:** [Beyond fabrication: Misattributed numbers in papers written by AI research agents](https://arxiv.org/abs/2610.38691)  
**License:** MIT for code, as declared in repository

### What it does

The repository contains a Python checker that:
- extracts numerical claims from a submission's LaTeX source, falling back to PDF text;
- indexes selected machine-generated result files;
- first checks whether a value appears in an execution artifact;
- then scores whether the context of the matching artifact corresponds to the paper's table row, column, caption, or sentence;
- calibrates against nearby numerical decoys;
- produces a CSV with the claim, matching evidence, provenance score, and conservative verdict.

The checker deliberately excludes code, prose, Markdown, figures, and TeX files from its evidence index. This prevents a number merely appearing in an agent's prose or source code from counting as evidence that the computation produced it.

### Reported evaluation

The authors report:
- 78 of 85 certified claims judged traceable (91.8%, exact 95% confidence interval 84–97%);
- 27 of 29 certified claims traceable on a confirmation sample;
- only about 23% of eligible claims certified;
- a large fraction of claims not certified were still traceable, so failure to certify is not evidence that a claim is false.

The repository documents sampling, weighting, annotation, and processing limitations in detail. Its weighted proportions are limited to eligible claims in selected submissions and are not population estimates for all AI-generated papers.

### Scope limitations

The tool is closely tied to the Into the Unknown benchmark's directory conventions, LaTeX/PDF manuscript extraction, and specific machine-generated result formats. Its current interface accepts a submission directory rather than a standard research object or workflow-run package.

### Product implication

A numerical claim-to-evidence checker is not a novel idea, and a useful implementation already exists. The possible Common Knowledge opportunity is to generalize the **interoperability contract and reviewer workflow**, not reproduce the paper's checker.

A product could potentially accept standard research packages and Workflow Run RO-Crates, map numerical claims to specific outputs/runs, and create a portable human-reviewed claim/evidence ledger. The checker is a reference implementation and baseline for comparison, not a blank-slate concept.

## 4. Trust, but verify, audit and attribute

**Paper:** [arXiv:2611.13042](https://arxiv.org/abs/2611.13042)  
**Date:** 9 November 2026

### What it proposes

A human-in-the-loop framework for checking AI-produced research results:
1. validated agent-usable tools with distinct grounds of trust check artifacts;
2. a fidelity audit checks whether the tool actually addressed the claim as stated;
3. humans make decisions at defined checkpoints;
4. a dialog report records human and AI contributions.

The authors describe implementations for mathematics and statistics and archive skill files and a complete example run on Zenodo.

### Important distinction

The paper is a methodology and example toolchain, not a general-purpose software product. It explicitly does not claim that the framework guarantees fidelity. Human decisions remain necessary, and a tool's passing verdict applies only to the artifact it actually checked.

### Product implication

Use this work to inform human decision points, claim freezing, fidelity checks, and contribution attribution. Do not claim to invent human-in-the-loop research verification.

## 5. OpenDiscoveryTrace

**Project:** [aayambansal/OpenDiscoveryTrace](https://github.com/aayambansal/OpenDiscoveryTrace)  
**Paper:** [OpenReview](https://openreview.net/forum?id=EHT3wVhCUZ)

OpenDiscoveryTrace provides 558 AI-scientist trajectories across 124 scientific tasks and seven models. Its schema records process-level information such as tool calls, observations, errors, revisions, and other step-level details. The authors report behavioral differences that output-only benchmarks miss.

It is a dataset and benchmark, not a general product for recording and reviewing arbitrary research projects. Its published trace schema includes model-thought fields; Common Knowledge should not assume that collecting private chain-of-thought is necessary or appropriate. Observable actions, inputs, outputs, configuration, tool calls, and human decisions are a safer and more defensible basis for audit records.

## 6. SciClaimEval

**Paper:** [SciClaimEval: Cross-modal Claim Verification in Scientific Papers](https://aclanthology.org/2026.lrec-1.864/)

SciClaimEval contains 1,664 annotated claim/evidence samples from 180 papers across machine learning, natural language processing, and medicine. It focuses on cross-modal evidence, including figures and tables.

This is important adjacent work, but its task is not the same as provenance checking. A claim may be semantically supported by a figure or table while still being attributed to the wrong run, dataset, or analysis. Conversely, a perfectly traceable result may not scientifically support the interpretation attached to it.

## 7. New empirical reporting guidance

A 2026 collaborative guideline paper, [Guidelines for empirical studies in software engineering involving large language models](https://link.springer.com/article/10.1007/s10664-026-10922-3), was developed by 22 researchers. It recommends declaring LLM role, model/version/configuration, system and prompt design, session traces, suitable baselines and metrics, open-model baselines where feasible, human validation, and limitations/mitigations.

The paper distinguishes interaction logs from runtime traces and notes that prompts, context files, tool schemas, and human-in-the-loop exchanges can materially affect results. It also recognizes privacy, confidentiality, and proprietary-system constraints on disclosure.

**Product implication:** a useful audit bundle should capture the static configuration and the observed runtime trace, not only the final answer or the model name. It should allow selective disclosure and redaction; full raw prompts and internal reasoning must not be public by default.

## 8. What this means for a Common Knowledge MVP

### Concepts we should not build from scratch
- Generic paper-to-agent conversion.
- Generic LLM observability or trace storage.
- Generic RO-Crate generation/validation.
- Generic workflow execution and result comparison.
- A generic AI-generated paper judge that returns a single pass/fail score.
- A new provenance ontology without a clear standards gap.

### A possible product gap to test

A local-first, standards-aware **research evidence handoff** tool that:
- accepts an existing research project and its output artifacts;
- imports workflow/run provenance from existing systems such as ReCRATE;
- extracts a narrow, explicitly supported set of claims (start with numerical claims in Markdown/LaTeX reports);
- links each claim to the specific output file, table/column/row, run, parameters, code revision, and input identity that support it;
- distinguishes value presence from contextual provenance;
- returns conservative statuses such as supported, traceable-but-unverified, ambiguous, untraced, and conflicting;
- lets a human confirm, reject, amend, or mark a claim as not machine-verifiable;
- exports a portable, versioned evidence ledger using existing standards where possible.

This product shape could complement ReCRATE and other workflow tools. It is not yet validated as a user need and may be too narrow, too complex, or already addressed by other implementations we have not found.

### Why this is more promising than a generic packager

It focuses on a consequential, measurable question: **does the reported claim actually correspond to the evidence and run it says it came from?** It can produce a clear before/after demonstration with intentionally misattributed results. It does not require Common Knowledge to host all research, run every workflow, or become an autonomous scientist.

### Main risks
- Claim extraction and context matching can produce false assurance.
- Numerical claims are easier than qualitative, causal, theoretical, or visual claims; scope must be explicit.
- A provenance link does not establish scientific validity.
- Existing checker implementations and emerging standards reduce novelty.
- User willingness to adopt a new reporting step is unknown.
- Sensitive data, unpublished manuscripts, and raw AI traces require strong local-first and disclosure controls.

## 8. FAIRSCAPE and the Evidence Graph Ontology (EVI)

**Project:** [FAIRSCAPE](https://fairscape.github.io/)  
**CLI:** [fairscape-cli](https://fairscape.github.io/fairscape-cli/)  
**Ontology:** [EVI](https://fairscape.github.io/EVI/)  
**Code:** [fairscape/fairscape](https://github.com/fairscape/fairscape) and [fairscape/EVI](https://github.com/fairscape/EVI)  
**License:** FAIRSCAPE is described by its project and papers as open source under MIT; EVI is published under CC BY 4.0.

### What it does

FAIRSCAPE packages research data, software, and computations as RO-Crates, records provenance, generates human- and machine-readable datasheets and evidence graphs, assesses AI-readiness, and supports publishing to repositories such as Dataverse and Zenodo.

Its CLI can create and manage RO-Crates, register datasets/software/computations, define or infer schemas, import selected data sources, generate HTML datasheets and evidence graphs, organize release packages, and publish packages.

FAIRSCAPE supports integrations or conversions involving Snakemake, Cromwell, Galaxy, MLflow, REDCap, Frictionless, Croissant, and Python. Its emphasis is biomedical research and AI-readiness, particularly work connected to NIH Bridge2AI.

### EVI's role

The Evidence Graph Ontology is an OWL 2 vocabulary extending W3C PROV-O to describe how a biomedical result was produced and what evidence bears on its correctness. It represents claims/findings, datasets, schemas, software, computations, and the relations between them. It can represent support and challenges to claims, not only a linear chain of execution.

This is a significant adjacent model for a claim/evidence layer. The current EVI release is 1.6 (August 2026); the ontology's own documentation describes it as a biomedical domain extension.

### Product implication

FAIRSCAPE and EVI substantially weaken any claim that Common Knowledge has discovered evidence graphs or research claim provenance. We should:
- inspect the FAIRSCAPE CLI and example crates;
- understand which parts are domain-specific versus reusable;
- evaluate EVI alongside W3C PROV, RO-Crate, Workflow Run RO-Crate, and nanopublications;
- determine whether a general cross-domain user problem remains;
- prefer adapters and interoperability rather than inventing another ontology.

A possible gap could remain in a lightweight local-first review workflow that consumes existing EVI/RO-Crate/Workflow Run RO-Crate records and helps authors/reviewers inspect claim-to-run traceability. But FAIRSCAPE already creates evidence graphs and visualizations, so that proposition requires direct comparison and user validation.

## Sources

- [Paper2Agent — Nature (2026)](https://www.nature.com/articles/s41586-026-11044-y)
- [Paper2Agent repository](https://github.com/jmiao24/Paper2Agent)
- [ReCRATE repository](https://github.com/biaperotto/recrate)
- [ReCRATE architecture](https://github.com/biaperotto/recrate/blob/main/docs/architecture.md)
- [ReCRATE input crate specification](https://github.com/biaperotto/recrate/blob/main/docs/crate-spec.md)
- [agent-integrity-analysis repository](https://github.com/mos3b-faqeeh/agent-integrity-analysis)
- [Beyond fabrication preprint](https://arxiv.org/abs/2610.38691)
- [Trust, but verify, audit and attribute](https://arxiv.org/abs/2611.13042)
- [OpenDiscoveryTrace repository](https://github.com/aayambansal/OpenDiscoveryTrace)
- [SciClaimEval](https://aclanthology.org/2026.lrec-1.864/)
- [LLM empirical software engineering guidelines](https://link.springer.com/article/10.1007/s10664-026-10922-3)
- [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/)

---
*This is a source-inspected desk review. Repository descriptions and self-reported evaluation results are attributed to their authors. No Common Knowledge user interviews, independent code audits, or hands-on comparative installations have yet been completed.*
