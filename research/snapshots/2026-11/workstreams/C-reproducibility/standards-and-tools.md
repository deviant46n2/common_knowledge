# Workstream C — Standards and Tools for Reproducible Research

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Preliminary technical landscape; not an implementation recommendation
- **Workstream:** [C — Scientific reproducibility and research integrity](README.md)

## 1. Why a layered view is necessary

No single format, platform, or checklist makes research reproducible. The practical record spans several different concerns:

1. **Description:** What is this research object, who created it, and what does it contain?
2. **Provenance:** Which agents and activities produced, transformed, reviewed, or corrected each object?
3. **Packaging and integrity:** Can files be transferred, inventoried, and checked for accidental change?
4. **Execution:** Can computational steps be rerun in a sufficiently specified environment?
5. **Reporting:** Does the account disclose the design and methods appropriate to the study type?
6. **Publication status:** Has the scholarly record been corrected, updated, or retracted?
7. **Preservation:** Can another institution or person retain and interpret the record after a service disappears?

These layers overlap, but are not substitutes for one another. A provenance graph does not prove an analysis is correct. A container image does not guarantee long-term execution. A checksum detects changed bytes, not whether the content is scientifically valid. A reporting checklist improves completeness but cannot replace expert judgment.

## 2. Provenance and research-object description

### RO-Crate

RO-Crate is a community-developed specification for describing research objects using linked-data concepts and Schema.org terms. It can describe a dataset, its constituent files, contextual entities, people, organizations, software, and actions. The current specification page identifies version 1.3 as the current long-term release; 1.2 is described as stable, while community work is directed toward a modularized version 2.

Its provenance guidance can record creation and update actions, agents, instruments such as software, times, and relationships between old and new versions. RO-Crate can be combined with packaging and fixity approaches such as BagIt, OCFL, and Git rather than replacing them.

**Assessment:** A promising interoperability layer for research packages, particularly where workflows, data, software, and publications need to travel together. It is metadata, not a complete archive, execution system, or guarantee of preservation. Adoption, tooling maturity, and usability need further evaluation.

### W3C PROV-O

PROV-O is a W3C Recommendation that expresses the PROV data model as an OWL ontology. Its core concepts are **Entity**, **Activity**, and **Agent**. These can describe what was used, what happened, what was generated, and who or what was responsible. The model can be extended for domain-specific needs.

**Assessment:** A general provenance vocabulary useful for cross-system exchange and conceptual alignment. Its flexibility is valuable, but implementation profiles and practical conventions are needed to ensure that two systems record comparable information. The standard does not itself collect provenance or establish that a recorded account is complete or truthful.

### BagIt

BagIt (RFC 8493) is a hierarchical file packaging convention for transferring and storing digital content with metadata tags and payload manifests. It supports cryptographic checksums to detect corruption or unexpected changes. The RFC is informational, not an Internet Standards Track specification.

**Assessment:** A useful, relatively simple packaging and fixity building block. It can help verify that a received package matches its manifest, but does not describe the scientific meaning of files, establish provenance, guarantee storage redundancy, or ensure future software can interpret the contents.

## 3. Computational environments and execution

### Binder and repo2docker

Project Jupyter's Binder stack uses BinderHub and repo2docker to build interactive computational environments from Git repositories. repo2docker translates repository configuration into Docker images and defines a reproducible execution-environment specification. A public BinderHub service is available at mybinder.org.

**Assessment:** An accessible route from version-controlled notebooks and code to an executable environment, with an open-source stack that can be deployed independently. A public hosted service should not be mistaken for an archival guarantee; availability, resource limits, dependency pinning, external data, and long-term image retention remain separate concerns.

### Whole Tale

Whole Tale describes a “Tale” as a composite research object containing data, code, software environment, configuration, metadata, and provenance. Its documentation describes running research code in an external system, recording execution, and publishing artifacts to repositories such as Zenodo or Dataverse with persistent identifiers.

**Assessment:** Particularly relevant as an example of connecting execution environments to repository publication rather than treating them as separate silos. Its own documentation and stated capabilities are primary evidence; current service operations, adoption, maintenance, and long-term funding require independent verification.

### Code Ocean

Code Ocean uses “Capsules” to bundle code, data, environment, metadata, and results. Its documentation describes Git-backed change history, reproducibility panels, and release capsules intended to preserve a run-only version separate from the actively edited project. Its Open Science Library documentation describes staff checks for computational reproducibility and quality before publication.

**Assessment:** A useful commercial-platform example of packaging, execution, version history, and workflow-level verification. It should be compared with open-source and institutionally hosted alternatives. Vendor claims such as “guaranteed reproducibility” must be evaluated against the exact scope of verification, supported environments, data rights, access terms, and exit/export paths.

## 4. Reporting standards are discipline- and design-specific

The EQUATOR Network maintains a searchable catalogue of health research reporting guidelines. Examples include CONSORT for randomized trials, PRISMA for systematic reviews, and STROBE for observational studies. The catalogue also includes extensions and other study types; the appropriate guideline depends on the actual design and question.

The existence of a checklist does not mean a study is valid, and reporting guidelines are not interchangeable. They help authors disclose the information readers need to understand and assess a particular design. Common Knowledge should link to established, maintained discipline-specific guidance rather than invent one universal scientific reporting checklist.

## 5. Preregistration and Registered Reports

The Center for Open Science describes Registered Reports as a publishing format in which peer review occurs before outcomes are known. A Stage 1 protocol may receive in-principle acceptance, with final publication dependent on conducting the approved work and meeting pre-specified quality criteria rather than obtaining a desired result. COS lists more than 300 journals offering the format in some form on the page accessed for this snapshot.

**Potential strengths:** Reduces some forms of publication bias and undisclosed analytic flexibility; gives methodological quality attention before results are known; can support publication of null or unexpected results.

**Limitations and cautions:** It is not suitable or necessary for every research question. Exploratory work remains important and should be labeled honestly rather than prohibited. Protocols can be amended for defensible reasons, but deviations should be disclosed. Stage 1 review does not guarantee competent execution, sound measurement, or valid interpretation. The format adds review workload and may interact differently with disciplines and funding cycles.

**Assessment:** A valuable option in suitable hypothesis-driven research, not a universal gatekeeping rule. Preserve the distinction between confirmatory and exploratory work.

## 6. Corrections, retractions, and the changing scholarly record

Crossref's Retraction Watch documentation states that Crossref acquired the Retraction Watch database in September 2023 and makes it available through the REST API and a downloadable CSV repository. Retraction records are collected from publisher sites and other discovery methods; corrections and expressions of concern are included but are less comprehensive than retractions.

A particularly instructive operational event occurred in September–November 2026: Crossref reported that Retraction Watch updates had not been added to its REST API since 24 September, affecting around 1,300 retractions. The CSV remained available, and Crossref reported a fix and monitoring on 25 November 2026.

**Assessment:** This is a concrete reminder that scholarly metadata is dynamic infrastructure with failure modes. Common Knowledge should not rely on one API as the sole source of publication status. It should retain source, retrieval time, update type, identifiers, and links to authoritative publisher notices; periodically reconcile feeds; and preserve a correction history rather than overwriting the earlier state.

A retraction is not a complete explanation of why a work was withdrawn, and a correction is not necessarily evidence of misconduct. Retraction metadata should be represented neutrally and with links to the notice and relevant context.

## 7. Preliminary interoperability implications

A plausible layered architecture for research records would combine, where useful:

- Persistent identifiers and domain metadata for discoverability.
- RO-Crate or an equivalent research-object description for packaging context.
- PROV-compatible provenance for agents, activities, inputs, outputs, and derivations.
- BagIt or another fixity-capable archival package for transfer integrity.
- Version-controlled code and explicit computational environments for executable analyses.
- Study-design-specific reporting guidelines.
- Linked publication-status records for corrections, expressions of concern, and retractions.
- Independent preservation and export arrangements.

This is a candidate interoperability pattern, not a selected Common Knowledge architecture. Each component needs assessment for maturity, adoption, licensing, implementation burden, accessibility, and long-term support.

## 8. Open questions for the next pass

1. How well do RO-Crate, PROV-O, BagIt, and repository-specific metadata interoperate in real workflows?
2. Which tools can validate a package automatically, and what exactly do their validators test?
3. How often do Binder, Whole Tale, and Code Ocean environments remain runnable after years, not just immediately after publication?
4. What are the practical exit paths from hosted computational platforms?
5. Which reporting frameworks cover qualitative, humanities, community-led, Indigenous, and mixed-methods research?
6. How should research objects represent unavailable or restricted inputs without falsely claiming full reproducibility?
7. What correction and retraction feeds are authoritative, complete, and independently reconcilable?

## Sources

See the [November 2026 source register](../../sources.md), entries C-07 onward.

## Change log

- **2026-11-26:** Added an initial comparison of provenance, packaging, computational execution, reporting, Registered Reports, and correction infrastructure.
