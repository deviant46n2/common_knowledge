# Workstream C — A Practical Research Record: Minimum Common Core

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Working proposal for research and pilot testing; not a universal standard
- **Workstream:** [C — Scientific reproducibility and research integrity](README.md)

## Purpose

This document proposes a small common core of information that helps people understand, inspect, preserve, and correct a research contribution. It is deliberately not a universal methods checklist. Experimental, observational, computational, qualitative, historical, theoretical, and community-led research need different methods-specific records.

The aim is proportionality: a small independent project should be able to record its work without an institutional bureaucracy, while a high-risk clinical or human-subject study should meet the additional requirements of its field, ethics review, and law.

## A. Minimum common core for any research contribution

### 1. Identity and scope
- Stable project or contribution identifier, if available.
- Title and concise description.
- Research question, objective, or purpose.
- Relevant discipline, domain, and keywords.
- Status: proposed, active, completed, paused, withdrawn, or superseded.

### 2. People, organizations, and responsibility
- Contributors and their roles, using identifiers where available and consented.
- Responsible contact or steward.
- Funding, material support, and relevant affiliations.
- Conflicts of interest and their management.
- AI systems or automated tools that materially contributed, with version/provider/configuration where known and meaningful.

### 3. Methods and decision history
- Study or inquiry design and rationale.
- Materials, instruments, sources, procedures, and analytical methods.
- Sampling or selection approach, inclusion/exclusion rules, and known coverage limitations.
- Preregistered or planned methods, if any.
- Material deviations, amendments, and reasons.
- Distinction between confirmatory, exploratory, and retrospective analysis where relevant.

### 4. Evidence and inputs
- Data, source materials, specimens, observations, documents, or other inputs.
- Origin and acquisition dates or periods.
- Data dictionary, units, formats, and relevant metadata.
- Access conditions, consent, license, and restrictions.
- Missingness, exclusions, transformations, and known quality limitations.
- If an input cannot be shared, a clear description of the restriction and a route for legitimate controlled access where possible.

### 5. Analysis and outputs
- Code, scripts, notebooks, protocols, models, or other materials needed to understand the work.
- Software, tool, and dependency versions where relevant.
- Computational environment and execution instructions for computational work.
- Parameters, random seeds, logs, and intermediate outputs when material to interpretation.
- Main findings, uncertainty, limitations, and alternative explanations.
- Negative, null, inconclusive, or failed results where relevant to the stated question.

### 6. Provenance and versioning
- Links among inputs, procedures, analyses, and outputs.
- Version identifiers or dated snapshots for important artifacts.
- Who made material changes, when, and why.
- Persistent identifiers and checksums where feasible.
- Clear links to prior versions, derivative work, and related publications.

### 7. Ethics, rights, and safety
- Ethics review or exemption status where applicable.
- Consent and participant/community governance conditions.
- Privacy, confidentiality, and data minimization measures.
- License and reuse conditions for each major artifact.
- Restrictions on sensitive data, locations, knowledge, or methods, with a brief justification.
- Safety or environmental considerations relevant to the work.

### 8. Review, correction, and closure
- Internal review, peer review, independent verification, or audit status, without conflating them.
- Known limitations and unresolved questions.
- Corrections, retractions, expressions of concern, disputes, or superseding versions.
- Preservation location, export route, and responsible custodian if known.
- Date of last substantive update.

## B. Add-on modules by research type

The common core should be extended with modules appropriate to the work, not forced into one template.

| Research type | Additional records to consider |
|---|---|
| Experimental | Protocol, randomization, blinding, controls, sample-size rationale, instrument calibration, intervention fidelity, preregistration |
| Observational | Sampling frame, recruitment, measurement validity, confounding, missing data, weighting, temporal/geographic coverage |
| Computational | Source code, exact dependencies, operating system, hardware assumptions, environment lockfile/container, command sequence, tests, logs, data lineage |
| Clinical / human subjects | Trial registration, protocol amendments, ethics approvals, consent, adverse events, outcome definitions, participant flow, privacy controls |
| Systematic review | Search strategies, databases, dates, screening criteria, deduplication, extraction forms, risk-of-bias method, synthesis protocol |
| Qualitative | Positionality/reflexivity, recruitment context, interview or observation guide, coding process, analytic memos, consent and quotation protections |
| Historical / archival | Source provenance, collection identifiers, archival context, transcription conventions, uncertainty, translation choices, rights and access limits |
| Community-led / Indigenous | Community authority, collective consent and governance, data sovereignty, benefit-sharing, culturally appropriate access, protocols for restricted knowledge |
| Field / ecological | Site and time metadata, instruments, calibration, sampling effort, observer effects, sensitive-species location controls, permits |

This table is illustrative and incomplete. Each discipline and community may require additional or different practices.

## C. Evidence states must be explicit

A research record should distinguish at least:

- **Reported:** stated by the contributor; not independently checked.
- **Documented:** supported by linked records or artifacts.
- **Re-executed:** computational procedure rerun by another person or environment.
- **Reanalyzed:** independent analysis of the same underlying evidence.
- **Replicated:** new observations or data collected to test a finding.
- **Audited:** reviewed against a defined audit scope and criteria.
- **Corrected:** a prior record has been amended, with history retained.
- **Retracted / withdrawn:** status changed, with reason and source linked where available.

These are not a single quality ladder. A successful computational rerun does not establish external validity; a replication does not necessarily verify every element of the original data pipeline. Every verification claim should state its scope, method, environment, and limitations.

## D. Minimum provenance chain

For a computational result, a useful basic chain is:

**Input(s) → Activity / procedure → Software and parameters → Output(s) → Interpretation / claim**

For each link, record the responsible human or software agent where possible, version or identifier, time, and relevant relationships. This maps conceptually to PROV's Entity–Activity–Agent model and can be expressed with suitable tools such as RO-Crate and PROV-O.

A research record should not imply that every step is machine-verifiable. Human decisions, tacit expertise, unavailable inputs, and interpretive judgments need to be described honestly.

## E. Proportionality and legitimate limits

The common core is a starting point, not a compliance barrier. Requirements should scale with:
- Potential harm and sensitivity.
- Complexity and cost of verification.
- Research type and established disciplinary standards.
- Rights and expectations of participants and knowledge-holding communities.
- Available resources and the consequences of non-reproducibility.

Do not require public release of personal, confidential, Indigenous, security-sensitive, or otherwise protected data. Where open release is not appropriate, record metadata, access conditions, governance authority, and a responsible access pathway where feasible.

## F. Pilot questions

Before adopting this record model, test it with:
1. A small computational study using public data.
2. An observational project with uneven sampling.
3. A qualitative or community-based contribution.
4. A project with sensitive or controlled-access data.

Ask contributors what is burdensome, what is missing, what can be automated, and which fields are genuinely useful to later readers. Revise the model based on evidence rather than assuming that more metadata always means better science.

## Sources and foundations

This working proposal draws on FAIR, FAIR4RS, TOP 2025, RO-Crate, W3C PROV-O, BagIt, computational research platforms, and discipline-specific reporting guidance. See source register entries C-01 through C-14 and the [standards and tools landscape](standards-and-tools.md).

## Change log

- **2026-11-26:** Drafted a proportional common-core research record and optional research-type modules for testing.
