# Workstream C — Initial Field Overview: Scientific Reproducibility and Research Integrity

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Preliminary orientation; not a systematic review
- **Workstream:** [C — Scientific reproducibility and research integrity](README.md)

## 1. Why this field matters

Common Knowledge cannot simply collect papers, datasets, and code and assume that the resulting archive is trustworthy. Research claims need to be inspectable, methods need to be understandable, evidence needs to be traceable, and errors need to be correctable.

Reproducibility and integrity are not just software features. They depend on research design, measurement, sampling, statistical analysis, data stewardship, incentives, peer review, publication practices, and the ability of independent people to scrutinize results.

## 2. Terms that must not be conflated

Terminology varies between disciplines and communities. This project will use the following working distinctions, while recording field-specific definitions when they differ.

- **Computational reproducibility:** Re-running an analysis using the same data, code, and sufficiently equivalent computational environment to obtain the same or materially consistent outputs.
- **Replicability:** Conducting a new study or analysis to test whether a finding holds under new data, observations, or experimental runs. Some fields use “reproducibility” for this meaning; definitions must be stated.
- **Robustness:** Examining whether conclusions persist under reasonable alternative assumptions, analytical choices, model specifications, or data-processing decisions.
- **Generalizability / transportability:** Assessing whether results apply to other populations, settings, times, or conditions.
- **Transparency:** Making research decisions, methods, materials, data-access conditions, code, analysis plans, and limitations inspectable to the extent ethically and legally possible.
- **Research integrity:** Conducting and communicating research responsibly, including honest reporting, appropriate attribution, ethical treatment of participants, sound data management, disclosure of conflicts, and correction of the record.

A result can be computationally reproducible but scientifically wrong. A finding can fail to replicate for legitimate reasons, including contextual differences, measurement changes, low power, or a false original claim. Replication outcomes require interpretation rather than a binary “science works / science fails” label.

## 3. Foundational frameworks and evidence

### FAIR principles

The FAIR principles describe data and other research objects as Findable, Accessible, Interoperable, and Reusable. They emphasize persistent identifiers, rich metadata, standard retrieval protocols, machine-actionable formats, clear licenses, provenance, and domain-relevant standards.

FAIR does not mean that all data must be publicly downloadable. The principles explicitly allow authentication and authorization where necessary, and metadata can remain accessible even when underlying data are restricted or unavailable.

FAIR is a high-level set of guiding principles, not one implementation standard or a guarantee of scientific validity.

### FAIR for research software

The FAIR4RS principles adapt the FAIR approach to software. They stress persistent identification of versions, software metadata, standard retrieval, interoperability, license clarity, provenance, and the distinction between software that can be found and software that is actually usable and reusable.

This matters because software is often part of the scientific method, not merely a supplementary artifact.

### TOP Guidelines

The updated Transparency and Openness Promotion (TOP 2025) framework organizes research practices, verification practices, and verification studies. The 2026 peer-reviewed update describes seven research practices, two verification practices, and four verification-study types.

Important distinction: disclosure, sharing, and third-party certification are different levels of implementation. A paper saying data are unavailable is transparent about the restriction but does not make the data reusable. A journal policy requiring sharing does not prove that the shared material is complete or executable.

### Replication evidence

The 2015 Reproducibility Project: Psychology attempted replications of 100 studies and reported that replication effects were, on average, about half the magnitude of original effects; 36% of replications were statistically significant. These results were influential, but they should not be reduced to the claim that “most science is false.” The project concerned a sample of published psychology studies, and replication success depends on design, power, context, and the definition of replication.

The wider lesson is that the scientific record benefits from independent verification, realistic uncertainty, adequate power, and incentives for reporting results that do not confirm initial hypotheses.

## 4. Research lifecycle: where integrity and reproducibility can fail

| Stage | Relevant records and practices | Common failure modes |
|---|---|---|
| Question and design | Research question, protocol, hypotheses, sampling plan, power justification, ethics review | HARKing, underpowered design, undisclosed deviations, unexamined assumptions |
| Data collection | Instruments, calibration, provenance, consent, sampling frame, inclusion/exclusion criteria | Missing context, selective measurement, unrecorded exclusions, privacy risks |
| Data management | Data dictionary, metadata, formats, access conditions, license, versioning | Incomplete metadata, inaccessible formats, unclear rights, loss of context |
| Analysis | Code, software versions, dependencies, parameters, logs, notebooks, environment | Manual steps, hidden preprocessing, dependency drift, undisclosed analytic flexibility |
| Interpretation | Uncertainty, alternative explanations, limitations, robustness checks | Overclaiming, selective reporting, unsupported causal claims |
| Publication | Methods, citations, data/code links, conflicts, preregistration links, peer review | Publication bias, inaccessible supplements, incomplete reporting |
| Post-publication | Corrections, expressions of concern, retractions, replications, commentary | Silent changes, poor correction links, stigma around negative results |
| Preservation | Persistent identifiers, archival packages, mirrors, succession plans | Broken links, lost software, unavailable dependencies, institutional closure |

## 5. Preliminary observations

1. **FAIR and reproducibility overlap but are not synonyms.** Findable and interoperable data help, but scientific reproduction also requires adequate methods, software, context, and expertise.
2. **Accessibility must include legitimate controlled access.** Sensitive human data, Indigenous knowledge, and security-sensitive datasets may require restricted access. The goal is inspectability and accountable access, not indiscriminate disclosure.
3. **Research software deserves first-class treatment.** A paper and dataset are often insufficient without exact software versions, dependencies, scripts, and execution context.
4. **Preregistration is useful but not universal.** It can distinguish planned analyses from exploratory ones, but it is not equally suitable for every research design and does not prevent all bias or error.
5. **Verification is broader than replication.** Reanalysis, code review, data audits, robustness checks, multiverse analysis, many-analyst studies, and independent replication answer different questions.
6. **Research incentives matter.** Practices that improve reliability can be undermined when careers reward novelty, positive results, speed, and publication volume over careful verification and correction.
7. **Correction is part of science, not an embarrassment to hide.** The record should preserve the history of claims, corrections, retractions, and unresolved disagreement.

## 6. Initial tools, standards, and organizations to map

- FAIR Guiding Principles for research data.
- FAIR4RS Principles for research software.
- TOP Guidelines and Registered Reports.
- DataCite, Crossref, ORCID, ROR, and repository metadata.
- RO-Crate, W3C PROV, BagIt, and research workflow provenance.
- Code Ocean, Whole Tale, Binder, Jupyter, Galaxy, and workflow execution environments.
- Reproducibility networks, replication projects, and metascience groups.
- COPE, Committee on Publication Ethics; research integrity offices and national frameworks.
- Retraction Watch and Crossref Retraction Watch data.
- Reporting guidelines such as CONSORT, PRISMA, STROBE, ARRIVE, and discipline-specific equivalents.

This is a discovery list, not an endorsement or an assertion that the tools are interchangeable.

## 7. Questions for the next research pass

1. Which definitions of reproducibility and replicability are used by major disciplines, and where do they conflict?
2. What is the minimum reproducibility record for computational research, experimental research, observational research, and qualitative research?
3. How do FAIR and FAIR4RS translate into practical repository and software requirements?
4. What does TOP 2025 change in practice, and how are journals implementing it?
5. What do Registered Reports improve, and what limitations remain?
6. How should research involving sensitive, Indigenous, or community-controlled data be independently scrutinized without violating rights?
7. How should Common Knowledge preserve corrections, retractions, disputes, negative findings, and version histories?
8. Which practices are feasible for small independent teams rather than only well-funded institutions?

## 8. Scope and limitations

This overview is a starting map, not a systematic review. It is initially weighted toward cross-disciplinary open-science frameworks and examples from psychology and computational research. It does not yet represent the full diversity of biomedical, clinical, physical, social, humanities, qualitative, Indigenous, or community-based research methods.

## Sources

See the [November 2026 source register](../../sources.md), entries C-01 onward.

## Change log

- **2026-11-26:** Created the initial field overview and registered foundational sources on FAIR, FAIR4RS, TOP 2025, and replication evidence.
