# Project Delphi — published assessment record review

- **Date:** 26 November 2026
- **Status:** Read-only inspection of one signed public nanopublication through Nanodash
- **Record:** [Gemini 4 Argon on buehler-2007-fracture-review-02](https://w3id.org/np/RA-8seOVkMr9taBsJb_jNIdOh_uVF5g4rBVaJvXHaFtfA)
- **No records were created or edited.**

## Purpose

Inspect one actual Project Delphi assessment record to see how the ontology's Claim, EvidenceItem, Assessment, SoftwareAgent, LanguageModel, and provenance concepts appear in a published artifact.

## Record inspected

The nanopublication is labelled:

> Gemini 4 Argon on buehler-2007-fracture-review-02: partially-resolvable, resolvability 0.56

It was published on 8 November 2026 and is signed with RSA by a human publisher identified through ORCID. Its publication metadata declares CC BY 4.0 and the `buehler-protein-materials` domain.

## What the assessment actually says

The assessment concerns a claim extracted from a 2007 review about fracture mechanics in biological protein materials compared with metals and ceramics.

The assessment description says that published mechanical data and structural databases support the broad qualitative comparison, but that the claim is only partially resolvable until a specific quantitative descriptor is chosen.

- **Main verdict:** `partially-resolvable`
- **Main score:** 0.56
- **Assessor self-confidence:** 0.77
- **Proposed test:** Compare quantitative fracture descriptors such as flaw-tolerance length scales, normalized work of fracture, strain-at-failure, and bond-breaking mechanism across protein materials and crystalline metals/ceramics.

This is a **resolvability assessment**: it evaluates whether the claim can be tested with available data. It is not a verdict that the claim is 56% true.

## Evidence and sub-assessments

The assessment links two candidate datasets:
- RCSB Protein Data Bank, for atomic structures of hierarchical protein building blocks;
- Materials Project, for elastic and cleavage properties of metals and ceramics.

It also records two evidence-against points:
1. Some continuum metrics may show mathematical similarities between protein materials and nanocrystalline metals/ceramics despite mechanistic differences.
2. The source claim is qualitative and does not specify the quantitative fracture metric that separates the material classes.

Five rubric sub-assessments are recorded:
- analysis feasibility: 0.65;
- data adequacy: 0.55;
- data existence: 0.65;
- discriminating power: 0.50;
- operationalizability: 0.45.

The candidate datasets are proposed inputs for a future test, not direct proof of the original claim. This is an important distinction.

## Assessment plan and provenance

The assessment is linked to an assessment plan through PROV-O's qualified association / had-plan pattern. The plan URL is pinned to a GitHub commit and points to a project README.

The assessing agent is a `prov:SoftwareAgent` identified as the Project Delphi dataset-resolvability assessor using Gemini 4 Argon. The model is represented separately as a `delphi:LanguageModel` with identifier `gemini-4-argon-medium`.

The publication itself is attributed to a human ORCID identity and signed with RSA. Thus the record distinguishes:
- the agent that performed the assessment;
- the language model used by that agent;
- the human publisher/signing identity;
- the assessment plan;
- the nanopublication's creation and license metadata.

The linked raw assessment JSON path in the cited GitHub repository returned 404 through the public GitHub API in this review. This may reflect an unavailable repository/path or access restriction; it prevented independent inspection of the raw model input/output batch and prompt. The public nanopublication and its rendered fields were accessible.

## Why this is useful for Common Knowledge

1. **Different questions need different assessments.** "Is this claim true?" and "Can this claim be tested with currently available data?" are not the same question. Project Delphi represents resolvability separately.
2. **Scores need typed meanings.** A 0.56 resolvability score, 0.77 assessor confidence, a rubric score, and a calibrated probability are different things. The UI must never flatten them into one "truth score."
3. **Assessment provenance is a first-class record.** The method/plan, assessor agent, model/version, human publisher, timestamp, and evidence links are inspectable.
4. **Evidence against should be preserved.** The record includes counter-considerations and a proposed test rather than only a positive summary.
5. **Candidate data is not evidence of the conclusion.** A dataset that could test a claim is not the same as an observed result from that dataset.
6. **Public publication is not full reproducibility by itself.** The nanopublication is signed and public, but one linked raw input path was not retrievable during this review.

## Limitations

- This is one assessment record, not a full audit of Project Delphi's public graph.
- The claim nanopublication and underlying source paper were not independently inspected here.
- The raw assessment batch and prompt were not retrieved.
- The candidate datasets were not queried or analyzed.
- No conclusion is drawn about whether the assessment's scores are calibrated or correct.

## Design lesson

A public knowledge system should not display a single confidence number without naming what it measures. It may need separate, explicitly typed records for:
- claim support/contradiction;
- evidence quality;
- source reliability;
- data availability;
- testability/resolvability;
- assessor confidence;
- calibrated probability (only where a method justifies it).

This record is a concrete example of that separation.


## Older published claim/evidence inventory sample

The ontology repository also publishes `nanopubs/live-inventory-2026-10-14.csv`. I parsed this file and found 183 unique nanopublications in this inventory:
- 161 Bayesian-assessment statements;
- 11 claim-statement records;
- 8 evidence-item records;
- 1 testable-hypothesis record;
- 1 hypothesis-statement record;
- 1 agent-introduction record.

This is a curated inventory dated 14 October 2026, not a count of the whole Science Oracle graph or all records in the public nanopublication network.

One example, claim `B2013-C1`, concerns the effect of H,K-ATPase inhibition on planarian head regeneration. Its inventory entries include:
- the source DOI `10.1242/dev.086900`;
- experimental context: Schmidtea mediterranea, H,K-ATPase RNAi, head size versus blastema size, 4–14 days post-amputation;
- an evidence item referencing **Fig. 4B–C**;
- a reported p-value of 0.0001;
- a two-sample comparison of head-size percentage at 14 dpa;
- a computed Vovk–Sellke maximum p-ratio of 26.014298;
- a weight-of-evidence value of 0.9975.

A separate Bayesian assessment record uses "Vovk–Sellke p-value calibration" and a weight-of-evidence value of 0.9977.

This provides more precise evidence structure than a bare paper citation: it records a figure, experimental context, statistical test, p-value, and a named calibration method. It still does not preserve the exact figure image/panel, source page excerpt, source file version/hash, or underlying raw measurements in the inspected records. The figure label is a useful locator but not a complete evidence anchor.

The repository's `nanopubs/README.md` also documents an ontology migration: some signed 1.x templates remain published while new 2.0 versions are being generated but are not yet signed/published. This is a live example of schema evolution and compatibility work. The 14 October inventory is explicitly a legacy per-statement wave; it should not be treated as representative of every current 2.0 record.

**Interpretation:** Project Delphi already demonstrates a rich, evidence-linked scientific graph, including statistical evidence and typed assessments. But its public records can be fragmented into multiple atomic nanopublications, and the published inventory is still evolving across ontology versions. A reader-facing application and a stable migration/export story are therefore essential.
