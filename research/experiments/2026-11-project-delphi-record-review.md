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
