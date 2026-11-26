# Workstream C — Empirical Evidence on Reproducibility and Data Sharing

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Selected empirical examples; not a systematic review or field-wide prevalence estimate
- **Workstream:** [C — Scientific reproducibility and research integrity](README.md)

## 1. Why empirical evidence matters

Standards and platform documentation explain what systems are intended to do. Empirical studies help reveal what happens when people try to reuse code, execute analyses, or share research materials in practice.

The studies below are not directly comparable: they examine different disciplines, samples, research artifacts, time periods, and definitions of success. Their value is in identifying failure modes and showing why simple indicators—such as a repository link or a “data available” statement—are insufficient.

## 2. Computational code availability and execution

### Large-scale research-code execution study (2022)

Trisovic, Lau, Pasquier, and Crosas examined more than 2,000 replication datasets from Harvard Dataverse containing over 9,000 R files published from 2010 to 2020. They attempted to execute the code in clean environments.

They reported:
- 74% of R files failed to complete without error in the initial execution.
- After a limited automatic code-cleaning process, 56% still failed.
- At dataset level, 45% of datasets had at least one automatically re-executable R file under the study's criteria.

The authors identify issues such as hard-coded paths, library dependencies, encoding, and execution order. They explicitly caution that successful re-execution is necessary but not sufficient for reproducibility: code can run and still produce a different or incorrect result.

**Limitations:** The study examined a particular repository sample, R files, and execution protocol. Timeouts and dependencies on other languages or execution order complicate interpretation. These numbers should not be generalized to all science or all code.

### Biomedical Jupyter notebook execution study (2023)

A study of notebooks associated with biomedical publications identified 27,271 notebooks from 2,660 GitHub repositories associated with 3,467 publications. Of the notebooks with declared dependencies that were selected for attempted execution, only a subset could have all dependencies installed and be rerun. Among those rerun, 1,203 completed without errors; 879 reproduced outputs identical to the original notebook, while 324 produced different results.

**Limitations:** This is a specific biomedical publication corpus and an automated execution procedure. Notebooks may rely on external resources, manual steps, or state not captured by dependency files. The results should not be treated as a universal failure rate.

### Clinical prediction model code availability (2026)

A 2026 scoping review of clinical prediction model studies citing TRIPOD or TRIPOD+AI reported that only 12.2% of studies reported accessible code. The authors also examined repositories and found that code availability did not consistently include documentation, dependency specification, or licensing features that support reuse.

**Limitations:** This sample is specific to clinical prediction-model studies and the review's inclusion criteria. The study used AI-assisted methods, so its screening and extraction procedures should be evaluated when interpreting results. It is not an estimate of code availability across all clinical or scientific research.

**Combined assessment:** Public code is a starting point, not proof of reuse or reproducibility. A useful record needs a versioned repository, explicit license, documentation, dependency/environment specification, data access conditions, and a tested execution path where feasible.

## 3. Qualitative data sharing requires different methods and safeguards

### Conceptual and ethical analysis (2024)

Lamb and colleagues argue that rigid expectations to publish complete qualitative datasets can be inappropriate for many qualitative methods. In some approaches, interpretation is situated and reflexive rather than a process expected to produce one uniquely reproducible result. Full transcripts can also expose participants even after obvious identifiers are removed, especially when the sample is small or contextual details are distinctive.

The authors do not argue that qualitative data should never be reused. They discuss secondary analysis where consent, context, access controls, and researcher reflexivity are adequate. They recommend planning for future data sharing during consent design and considering controlled-access repositories rather than requiring all data to be publicly downloadable.

**Limitations:** This is a focused commentary in health psychology, not a universal account of qualitative methods. Qualitative traditions differ, and the authors' position should be considered alongside other perspectives.

### Scoping review of qualitative interview-data sharing barriers (2026)

Gowie and colleagues' 2026 scoping review identified 110 sources and grouped barriers to sharing interview and focus-group data into seven themes: confidentiality, consent, data misuse, context, external approvals, researcher distress, and time and financial constraints. The authors emphasize that strategies are diverse and have not been systematically evaluated, and caution against one-size-fits-all sharing expectations.

**Limitations:** The review maps suggested strategies and barriers; it does not establish that each proposed strategy is effective. Its inclusion criteria focus on interview and focus-group transcripts, and the evidence base includes different source types.

**Combined assessment:** Transparency and rigor do not require every underlying artifact to be public. For qualitative work, a responsible record may include methodological context, positionality/reflexivity, sampling, analytic decisions, consent scope, access conditions, and a controlled-access route where appropriate. In some projects, public release of raw transcripts would be unethical or epistemologically inappropriate.

## 4. What these findings mean for a common research record

A minimum record should not treat code, data, and full transcripts as interchangeable attachments. It should ask:

- What artifact is needed to understand or verify the claim?
- What level of verification is appropriate for the research design?
- What is the actual license and access condition?
- Can the artifact be used without missing dependencies, undocumented steps, or unavailable context?
- Does sharing create risks of re-identification, misuse, or harm?
- What can be shared publicly, what can be shared under controlled access, and what should not be shared?
- What is the distinction between re-execution, reanalysis, replication, and interpretive transparency?

A data availability statement should explain what is available, where, under what conditions, and why any materials are unavailable or restricted. “Available on request” should not be treated as equivalent to a durable, governed access mechanism.

## 5. Practical requirements suggested by the evidence

For computational research:
1. Preserve a versioned source repository or archived release.
2. Include a clear license and contribution/attribution information.
3. Document dependencies and environment configuration.
4. Provide execution instructions and input/output descriptions.
5. Capture parameters, seeds, and external data dependencies when material.
6. Test execution in a clean environment and record the result, environment, date, and limitations.
7. Preserve the exact artifact used for publication, not only the latest development branch.

For qualitative and sensitive research:
1. Plan consent and future sharing before data collection.
2. Document the research context, sampling, positionality, and analytic process.
3. Assess re-identification and contextual risks, not just direct identifiers.
4. Distinguish public metadata, public excerpts, controlled-access materials, and non-shareable materials.
5. Record who has authority to approve access and what uses are permitted.
6. Provide for withdrawal or restriction where required by consent, ethics, or law.
7. Avoid imposing quantitative notions of reproducibility where they conflict with the research design.

These are evidence-informed suggestions for testing, not a universal compliance standard.

## 6. Open questions

1. How should automated reproducibility checks report partial success, missing dependencies, and data-access barriers?
2. What is a meaningful minimum execution test for code with nondeterministic or hardware-dependent outputs?
3. How can long-term environments be preserved when containers depend on unavailable services, licensed software, or specialized hardware?
4. What are best practices for qualitative data access that respect consent, context, and community authority?
5. How can platforms support secondary qualitative analysis without treating it as replication?
6. Which forms of evidence should be public when raw data cannot be shared?
7. How can evaluation frameworks avoid penalizing researchers whose methods or communities require restricted data?

## Sources

See the [November 2026 source register](../../sources.md), entries C-23 onward.

## Change log

- **2026-11-26:** Added selected empirical evidence on research-code execution, biomedical notebooks, clinical prediction model code availability, and qualitative data sharing. These examples are not a systematic review or field-wide prevalence estimates.
