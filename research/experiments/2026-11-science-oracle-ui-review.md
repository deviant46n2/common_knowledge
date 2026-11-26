# Project Delphi / Science Oracle — public product and UI review

- **Date:** 26 November 2026
- **Status:** Read-only review of the public website, PKG Viewer, ontology, and publishing guide; one live question test
- **No account was created; no records were imported, saved, or published.**

## Product inspected

- [Science Oracle](https://scienceoracle.com/)
- [Public graph](https://scienceoracle.com/graph)
- [Paper browser](https://scienceoracle.com/papers)
- [Hypothesis browser](https://scienceoracle.com/hypotheses)
- [PKG Viewer](https://pkg.scienceoracle.com/)
- [Ontology repository](https://github.com/fractastical/project-delphi-ontology)

## What the product says it does

Science Oracle describes itself as a source-traceable research workspace. It:
- searches a public scientific knowledge graph, not the open web or private research;
- provides answers bounded by retrieved sources;
- separates supported statements, counterevidence, and evidence gaps;
- links citations to source excerpts and, where available, original DOI publications;
- exposes confidence based on the graph evidence scores of cited sources, accounting for dependencies, with a separate coverage indicator;
- explicitly says this confidence is not the probability that the AI wording is correct or a calibrated truth guarantee;
- says missing counterevidence does not mean none exists.

The site also states that the latest question and response are saved in the browser, including on shared devices. This is a relevant privacy consideration for any public research interface.

## Live question test

A read-only question was submitted through the public "Ask the Oracle" form:

> What evidence in the public graph supports or challenges the hypothesis that bioelectric signaling influences planarian regeneration?

The app entered a loading state, then returned:

> "Could not complete this question. Delphi could not complete this answer. Please retry. No answer has been generated from unverified sources."

A retry produced the same failure. No answer, sources, counterevidence, or evidence gaps were returned.

**Interpretation:** This is a single availability/UX failure, not evidence that the knowledge graph or its records are wrong. The fail-closed behavior is preferable to fabricating an answer from unverified sources. However, the interface did not distinguish "no relevant evidence in this collection" from "the answer service failed," which is an important product distinction.

## Public collection observations

- The public domain index endpoint returned 893 domain labels in a dated snapshot referenced by the repository README (11 October 2026). The README explicitly warns that this is not 893 equally populated or independently validated disciplines.
- The PKG Viewer described itself as searching every record already imported into that workspace. Its table displayed 6,241 matched/imported records at the time of inspection, including Project Delphi rubric assessments and LLM assessments.
- The repository README makes an important distinction between the changing application dataset, the ontology/code repository, and records actually published to the nanopublication network. Not every application record is exported, signed, or published; public views do not constitute a full export of private research.

These are snapshots of the public interface at the time of review, not a complete data audit.

## Ontology review

The current ontology is v2.0. Key modeling choices:
- `Claim` is a subclass of `Hypothesis`: a hypothesis is a proposition represented without asserting it; a claim is one that a source states. The README calls a claim "a belief, not an asserted fact."
- `EvidenceItem` is separate from claims and assessments.
- `Assessment` is an n-ary evaluation of a hypothesis/claim, with verdict, probability, confidence, reasons, evidence, and assessor attribution as applicable.
- `BayesianAssessment` carries Bayes factors and calibration information.
- `LLMClaimAssessment` identifies assessments produced by software agents running language models.
- The assessor is a PROV-O SoftwareAgent; the model is a separate `LanguageModel` entity. This allows two agents using the same model but different prompts/scaffolding to be distinguished.
- Other fields include scores, evidence weights, decibans, assessment type, calibration method, p-values, statistical tests, and domains.
- Claims are linked to source works using PROV-O derivation; the vocabulary reuses FaBiO, PROV-O, SKOS, Dublin Core, QUDT, and other standards where appropriate.

This is a much more developed assessment model than the generic MIRA schema or the simple SciOS Git graph. It is still designed for scientific research and the application has a curated science-domain index, not a general civic/public knowledge corpus.

## Publishing workflow

The repository's `PUBLISHING.md` documents a rigorous 12-step build/audit/publish/remediate loop. Notable controls:
- source every assertion;
- publish every dataset as its own nanopublication with provenance and confidence;
- use the test registry before production;
- inspect for dummy data and invalid placeholders before signing;
- require two assessors from different providers for the documented audit path, with assessor distinct from builder;
- require human review before production and a second reviewer for high-stakes/public-facing claims;
- preserve source hashes and generator versions;
- supersede or retract rather than overwrite;
- maintain publication manifests;
- never commit signing keys or API tokens.

These are strong operational patterns. They are documented project practices; this review did not independently run their pipeline or verify every published record.

## Licensing and openness

The public ontology repository includes an MIT license. The README distinguishes the open vocabulary/code/examples from the larger application dataset, which is not fully included in the repository and may contain private research. Not every application record is published to the public nanopublication network.

This is a significant difference from Common Knowledge's aspiration for an openly inspectable public knowledge corpus by default. It may be a reasonable privacy boundary for a research application, but Common Knowledge would need a clearer public/private separation and bulk export/preservation policy.

## Findings for Common Knowledge

1. **A live public application already exists** for source-linked scientific Q&A, claim/hypothesis graphs, evidence, uncertainty, and AI assessments. We should not build another science-only version of this without a clear reason.
2. **The ontology is a strong reference** for separating source-stated claims, hypotheses, evidence items, assessments, agents, and language models.
3. **The publishing process is unusually explicit** about independent audits, human review, test-to-production promotion, source completeness, and remediation.
4. **Confidence must be carefully presented.** The product itself distinguishes graph evidence confidence from the probability that the generated answer is correct.
5. **The application is not a fully open corpus.** Its public views and published nanopubs are not a complete export of all application records.
6. **Its domain is science.** It does not yet provide a general civic, legal, historical, or public-policy knowledge service.
7. **The first live Q&A test failed closed.** We need more than one test before judging availability or answer quality, but the error UX is a useful lesson.

## Next checks

- Test one of the app's domain-specific starter questions to see whether the public Q&A path is generally operational.
- Inspect one published claim, one evidence item, and one LLM assessment in full, including source passage and provenance.
- Compare the ontology's claim/evidence/assessment model with the Consilience templates and MIRA mapping.
- Ask the maintainer about public data export, source passage anchoring, non-science domains, and interoperability.
- Do not reuse the ontology as Common Knowledge's schema without first evaluating whether its science-specific assumptions fit our scope.


## Second live question test

A separate run selected the first available starter question from the public dropdown:

> What does the public evidence show about NASICON-based sensors with carbonate electrodes exhibit Nernstian EMF response to CO2 across 200–100,000 ppm at 350–500°C, and what remains uncertain?

This also failed. The app displayed the same "Could not complete this question" / "No answer has been generated from unverified sources" message three times. No citations, excerpts, support, counterevidence, uncertainty, or gaps were returned.

**Updated interpretation:** Two distinct public queries failed, including one supplied by the application's own starter-question list. This suggests the public answer path was unavailable or malfunctioning during the test window. It does not establish that public mode is inherently unsupported, and it does not tell us whether the underlying graph contains relevant evidence. The system correctly avoided fabricating an answer, but the generic error did not distinguish service failure from an evidence gap.
