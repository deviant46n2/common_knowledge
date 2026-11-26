# Workstream C — Preliminary Comparative Synthesis

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Preliminary synthesis; workstream remains in progress
- **Workstream:** [C — Scientific reproducibility and research integrity](README.md)

## 1. Main finding: trust is a chain, not a badge

A research result is supported by a chain of decisions and artifacts: question, design, participants or observations, inputs, methods, code or interpretive process, analysis, outputs, interpretation, publication, and subsequent correction.

Different frameworks address different links in this chain:
- FAIR and FAIR4RS improve discovery, access conditions, interoperability, and reuse of data and software.
- TOP and Registered Reports address transparency and some incentives around research design, analysis, and publication.
- RO-Crate and PROV-O help describe research objects and provenance.
- BagIt and PREMIS address package integrity and preservation metadata.
- Binder, Whole Tale, Code Ocean, and workflow systems support execution and computational context.
- Reporting guidelines address completeness for particular research designs.
- COPE, Crossref, and research-integrity frameworks address correction, publication ethics, and responsible practice.

No one component establishes that a scientific claim is true. A robust system needs to preserve the evidence and context needed for independent scrutiny.

## 2. Findings grounded in the current sample

### 2.1 Sharing is necessary in some cases, but insufficient for computational reproducibility

The 2022 Trisovic et al. study found substantial execution failures in a sample of Dataverse replication packages. The 2023 biomedical notebook study likewise found dependency installation and execution failures. The 2026 clinical prediction model review found code availability remained uncommon in its specific sample and that repositories often lacked documentation, dependency specification, or licenses.

**Assessment:** A link to code is not a reproducibility guarantee. A record should distinguish code existence, accessible code, documented code, licensed code, environment capture, successful execution, and independent verification.

### 2.2 Execution success is not scientific validation

A script may execute and still produce an incorrect output, use invalid data, implement an inappropriate model, or fail to support the paper's interpretation. Conversely, a valid analysis may not run in a clean automated environment because it depends on licensed software, secure data, specialized hardware, manual steps, or unavailable services.

**Assessment:** Any “reproducible” label must state the exact verification scope, environment, data, version, and result. Do not collapse re-execution, reanalysis, replication, and scientific validity into one score.

### 2.3 Reproducibility expectations must respect research methods

The qualitative research sources show that full public release of raw data may be methodologically inappropriate, ethically unsafe, or inconsistent with participant consent. The 2026 scoping review identifies practical barriers including confidentiality, consent, misuse, context, approvals, researcher distress, and cost.

**Assessment:** The common record should be open about methods and access conditions, but should not mandate public release of all raw data. Qualitative research may support transparency through reflexivity, positionality, analytic documentation, contextual description, and controlled secondary access rather than repeatability of a fixed analysis.

### 2.4 Integrity requires fair process and a correctable record

The Singapore Statement, ALLEA Code, National Academies report, and COPE guidance emphasize honesty, accountability, stewardship, institutional environments, fair process, and correction. Crossref's 2026 API incident demonstrates that even metadata infrastructure used to track retractions can fail operationally.

**Assessment:** Common Knowledge should preserve corrections and publication-status history, but it should not become an unqualified misconduct tribunal. Allegations, evidence of unreliability, honest error, methodological disagreement, and confirmed misconduct are distinct categories.

### 2.5 Preservation is part of reproducibility

Research software, dependencies, data, and execution environments can become unavailable even when an article and code repository remain online. RO-Crate, BagIt, PREMIS, OAIS, and CoreTrustSeal address complementary pieces of description, integrity, and custody.

**Assessment:** A reproducibility record should identify what is archived, who is responsible for it, what rights permit preservation and migration, and what dependencies remain external. Containers and checksums help, but do not guarantee long-term execution or institutional continuity.

## 3. Candidate minimum record and verification model

The [working research-record proposal](research-record.md) defines a common core plus optional modules for different research types. The current evidence supports keeping that model proportional and layered.

A useful record should distinguish at least these artifact states:

| State | What it establishes | What it does not establish |
|---|---|---|
| Described | The artifact is identified and contextualized | That it can be accessed or used |
| Deposited | A copy or record is held in a named repository | That it is preserved indefinitely |
| Accessible | A defined audience can retrieve it under stated conditions | That it is reusable or complete |
| Licensed | Reuse terms are stated for the artifact | That the depositor had authority to grant all rights |
| Documented | Methods, dependencies, context, or use instructions are supplied | That the documentation is correct |
| Validated | A defined schema or package check passed | That the scientific content is valid |
| Re-executed | A computational procedure ran under a stated environment | That it reproduced the reported result or is scientifically correct |
| Reanalyzed | Another analyst examined the same evidence | That a new study will obtain the same result |
| Replicated | New observations or data tested a finding | That all methods and assumptions of the original were valid |
| Audited | A defined process was checked against explicit criteria | That all possible errors were found |

These states are not a simple quality ladder. A study may be audited but not replicated, or may be re-executed without independent review of its scientific assumptions.

## 4. Candidate design principles

These are hypotheses for pilot testing, not adopted Common Knowledge policy.

1. **Methods are first-class records:** Preserve protocols, decisions, instruments, and deviations, not only papers and outputs.
2. **Software is a research artifact:** Record versions, licenses, dependencies, and execution instructions.
3. **Access conditions are explicit:** Public, registered, controlled, embargoed, and unavailable materials should be distinguished, with reasons and responsible stewards.
4. **Verification scope is stated:** Every verification result names the object, version, method, environment, and limitations.
5. **Exploratory and confirmatory work are distinguishable:** Preregistration is useful where suitable, but exploration and serendipity remain legitimate.
6. **Research-type differences are respected:** Do not impose quantitative reproducibility norms indiscriminately on qualitative, historical, interpretive, community-led, or theoretical work.
7. **Correction history is preserved:** Never silently overwrite the record when claims, data, code, or publication status change.
8. **Integrity process is fair:** Separate correction from punishment and evidence from allegation.
9. **Preservation is assigned:** Every public preservation promise identifies a custodian, scope, and continuity plan.
10. **Burden is proportional:** A common record should be feasible for small independent teams and expandable for high-risk or regulated work.

## 5. Gaps in this investigation

- Discipline-specific replication and reproducibility practices beyond psychology, clinical prediction, and computational research.
- Qualitative, humanities, Indigenous, and community-led research beyond selected data-sharing literature.
- National and institutional research-integrity procedures outside the reviewed frameworks.
- Empirical evaluations of Registered Reports and TOP adoption across disciplines.
- Long-term execution and preservation studies comparing containers, workflow platforms, and archives.
- Practical accessibility and burden for small or under-resourced teams.
- Direct researcher, repository manager, participant, and community interviews.
- Independent review of the platforms and standards identified so far.

## 6. What would change this assessment?

The common-record hypothesis should be revised if testing shows that it imposes excessive burden, fails to capture essential disciplinary context, or creates incentives to disclose material that should remain protected. The next phase should pilot the record with contrasting research types and ask contributors which fields materially help later readers.

## 7. Next research actions

1. Test the research-record proposal with a small computational project and a qualitative or community-based project.
2. Expand evidence on research integrity procedures and Registered Reports beyond the initial sources.
3. Investigate long-term software and environment preservation with real archived projects.
4. Consult researchers and repository professionals about the cost and usability of the proposed record.
5. Revise the proposal and prepare a bounded baseline report only after these gaps are addressed.

## Sources

See the [November 2026 source register](../../sources.md), entries C-01 onward.

## Change log

- **2026-11-26:** Added a preliminary synthesis connecting reproducibility standards, empirical execution evidence, qualitative data-sharing ethics, integrity processes, and preservation. Workstream C remains in progress.
