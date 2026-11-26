# Civic Fact-Checking and Public-Claim Infrastructure

- **Research date:** 26 November 2026
- **Status:** Initial landscape review; selected source and API checks performed
- **Purpose:** Understand what already exists for political/public claims, fact-check discovery, community review, and temporal facts.

## Why this is a separate workstream

Common Knowledge's public-facing ambition includes claims made by politicians, public officials, companies, and other public actors. The scientific knowledge-graph projects are not the whole landscape. There are already fact-checking organizations, claim-detection systems, fact-check archives, and temporal fact ledgers.

These systems generally do **not** provide a universal evidence-linked knowledge graph. But they solve important adjacent problems and should be integrated or learned from rather than duplicated.

## 1. Factiz — open archive of published fact-checks

**Links**
- [Factiz archive](https://factiz.org/)
- [About Factiz](https://factiz.org/about/)
- [Global fact-check database](https://factiz.org/global-fact-check-database/)
- [Sources and licences](https://factiz.org/sources/)
- [Platform design](https://factiz.org/platform/)
- [Source code](https://github.com/factiz-org/factiz)
- [Resolver protocol v0.1](https://github.com/factiz-org/factiz/blob/main/docs/PROTOCOL.md)

### What exists

Factiz is a public archive of existing newsroom fact-checks. Its 23 November 2026 edition reports 106,277 claims, 109,074 fact-checks, 266 newsrooms, and 49–50 claim languages (the README and site differ by one language); the interface is available in 15 languages. 829 claims were checked by two or more newsrooms.

A page groups checks of the same claim across newsrooms and languages. Each newsroom's verdict stays attributed to that newsroom, in its own words, with a link to the original article. Factiz explicitly says it does not decide truth for the archive and does not show a percentage of truth.

The archive uses records that may be republished:
- Google Data Commons ClaimReview feed, CC BY 4.0;
- EUvsDisinfo, with the reuse conditions it lists;
- Factiz's own Radar checks, CC BY 4.0.

Every record names its source and license. The site states that it does not include every fact-check: many newsrooms do not openly license their work.

Factiz Radar is separate from the archive's aggregation role. It checks a few widely circulating claims per week, using AI-drafted checks and review by a human editor who did not write the check. Unknowns can be published as unknown, with a request for help.

### Resolver protocol

The Factiz repository contains a draft resolver protocol (v0.1) that asks one narrow question:

> Has this claim already been checked, by whom, and what was the outcome?

It is not a truth oracle, moderation API, or identity layer. Its key requirements include:
- no probability-of-truth field;
- no claim match below the resolver's declared threshold;
- distinguish a human fact-check match from a resolver's own assessment;
- do not store or forward the original artifact; retain only a fingerprint, except for an explicit-consent dispute route;
- name each newsroom, verdict, date, and link;
- express consensus as a count, not a truth percentage;
- identify the fingerprint model/version and refuse cross-version comparisons;
- publish thresholds and matching variants so clients can inspect the conditions of the result.

The protocol is a **draft and not yet adopted**. It is designed to sit alongside ClaimReview rather than replace it. It proposes a stable cross-language `claim_id` and artifact fingerprint as the missing link between checks.

### Maturity and limitations

- Code is AGPL-3.0; resolver protocol is CC BY 4.0; the conformance test is MIT.
- The repository reports 9,595 passing tests as of 24 November 2026, but this is the project's own test report. Its benchmark is explicit about remaining false matches and the limits of synthetic test pairs.
- The archive has no public query API yet; the site says an API and browser extension are planned. The resolver protocol is draft.
- A clean self-hosted site is not yet easy: the README says there is no small sample edition in the repository and the corpus-building lab is needed.
- The archive preserves the newsroom's verdict and link, not a structured evidence graph of the article's supporting passages, source documents, methods, and counterevidence.

**Assessment:** The strongest existing reference for *finding out whether a public claim has already been fact-checked*. It aligns with the principle that a lookup service should report who checked a claim and what they concluded, not invent its own universal truth percentage. Common Knowledge could interoperate with Factiz rather than re-create its archive.

## 2. AsOf — temporal fact ledger

**Links**
- [AsOf](https://asof.is/)
- [About and verification rules](https://asof.is/about)
- [Live API](https://asof.is/v1/health)
- [MCP connector](https://asof.is/)

### What exists

AsOf describes itself as a temporal fact ledger: each record is one claim about a subject, with a fact/value, valid dates, sources, and a confidence score. When a fact changes, the old claim is closed and linked to the new one rather than overwritten.

Its documented verification rules:
- two independent sources agreeing -> status `valid`;
- one source -> `unverified`;
- conflicting sources -> both claims remain and are flagged;
- primary regulatory filings or official status dashboards can be asserted on their own under stated confidence conditions;
- sources include the passage that states the value where one was read;
- corrections are queued for human review.

It distinguishes valid, unverified, disputed, and superseded claims. It exposes a REST API and an MCP server. Open snapshots are planned, not yet available according to its About page. The project says its initial coverage is search/AI and technology, with public companies and broader domains to follow.

### Live API probe

A read-only API request for Google as of 1 January 2016 returned historical claims with source records, quotes/excerpts, source types, publication/retrieval dates, valid-from/valid-to, recorded-at dates, confidence, and supersession links. A separate `known_by` query returned the subset known to the ledger by a specified date.

The live health endpoint reported:
- 44,532 claims;
- 13,986 sources;
- 502 entities;
- 10,888 valid, 103 unverified, 33,539 superseded, 2 flagged;
- 6,747 held rather than asserted;
- zero orphaned claims, dangling supersession pointers, or valid claims without sources.

These are live service-reported counts, not an independent data audit.

### Fit and limitations

AsOf is a strong example of temporal claim storage, source passage capture, supersession, and explicit held/unverified states. Its `as_of` (when a fact was true) and `known_by` (when the ledger knew it) distinction is particularly useful.

It is not a general evidence/argument graph:
- it focuses on entity facts and changing values rather than arbitrary claims, arguments, and independent assessments;
- its confidence score is based on source support rules, not a calibrated probability of truth;
- "two independent sources" and "primary source" are policy rules that still require careful source-independence and reliability judgments;
- no public code repository or full public data snapshot was found in this review;
- the public product is AI-retrieval-first and currently focused on technology/AI entities, not civic discourse.

Its stated data licensing (facts, descriptive text CC BY 4.0, Wikipedia-derived text CC BY-SA) should be checked at the level of each source and database before reuse; this is not legal advice.

**Assessment:** A useful model for temporal facts, source passages, corrections, and machine-readable retrieval. It is a narrow, independently operated product, not a general public knowledge commons.

## 3. Full Fact — claim monitoring and editorial fact-checking

**Links**
- [Full Fact AI](https://fullfact.org/ai/)
- [Full Fact](https://fullfact.org/)

### What exists

Full Fact is a registered UK charity and non-profit company. Its AI tools monitor online news, live TV, podcasts, and social media; split material into sentences; identify checkable claims; classify claim types and topics; and match repeated claims to previous checks.

Full Fact defines a claim as the checkable part of a sentence and distinguishes quantitative, causal, predictive, and other claim types. It uses AI to prioritize and match claims, but expert fact-checkers investigate and publish the actual verdict. It uses ClaimReview markup so fact-checks can travel beyond its own website.

Full Fact reports its tools are used by 40+ fact-checking organizations in 30 countries and three languages, processing about a third of a million sentences on a typical weekday. These are organization-reported figures. The tools are available to other organizations through a paid license.

### Fit and limitations

Full Fact demonstrates a mature human-plus-AI workflow for identifying important public claims, detecting repetition, and helping journalists work at scale. It also shows why claim detection and claim adjudication should be separate.

It is not a general public knowledge graph, and its AI tools are a licensed service rather than an open-source public database.

**Assessment:** A strong potential collaborator and upstream source of claim-monitoring expertise. Common Knowledge should learn from its editorial methodology and use ClaimReview-compatible outputs rather than attempt to replace professional fact-checking organizations.

## 4. Cofacts — community fact-checking and open data

**Links**
- [Cofacts](https://en.cofacts.tw/)
- [About Cofacts](https://en.cofacts.tw/about)
- [Open data repository](https://github.com/cofacts/opendata)
- [Hugging Face dataset](https://huggingface.co/datasets/Cofacts/line-msg-fact-check-tw)
- [Public GraphQL API](https://api.cofacts.tw/)

### What exists

Cofacts is a Taiwanese civic-technology project that began in 2016. It combines a messaging chatbot with a collaborative fact-checking database. People report suspicious messages; volunteers add responses; other contributors review responses and provide feedback. AI replies can appear before a human fact-check is available, and the API keeps AI replies separate from human replies.

The project emphasizes different views and says that fact-checking responses are not necessarily correct or complete; editors review contributions to select higher-quality responses. Its public API and open dataset support reuse by researchers, journalists, civic developers, and other applications. The latest open-data snapshot in the repository during this review was 22 November 2026.

Cofacts' public data terms specify CC BY-SA 4.0, while the API/open-data generator code is MIT-licensed. API use has application credentials and data-use terms; it should not be scraped or reused outside those terms.

Cofacts Association was established in Taiwan in 2023 to sustain the community. Research on the platform notes its strengths in speed and community participation, while also identifying limits: no formalized verification standards, optional training, no prior vetting of volunteer skills, potential conflicts of interest, and limited access to advanced forensic tools.

### Fit and limitations

Cofacts is a valuable model for community participation, transparent disagreement, AI-assisted triage, human review, open data, and a non-commercial civic-tech organization. It is focused on rumors and messages circulating in Taiwan (especially closed messaging platforms), not a general-purpose knowledge graph or universal public reference.

**Assessment:** A useful community and institutional case study, especially for contributor workflow and public-interest sustainability. It also demonstrates why openness needs clear verification practices, reviewer support, and safeguards against low-quality or conflicted contributions.

## 5. ClaimReview, Fact Check Explorer, and claim-detection tools

### ClaimReview

ClaimReview is a Schema.org markup vocabulary used by publishers to describe fact-check articles. It provides structured claim text, claimant, reviewer/publisher, verdict, date, and article URL. It is a useful interoperability format for fact-check publishers, but not a complete claim/evidence graph.

Factiz's protocol review identifies missing cross-language claim identity, artifact representation, and controlled verdict normalization as practical gaps. It recommends building alongside ClaimReview rather than replacing it.

Google's support for fact-check rich results in Search has been phased down, but Fact Check Explorer remains a discovery surface. ClaimReview is still useful as a publisher-side interchange format.

### Claim detection

Full Fact and ClaimBuster illustrate a separate technical problem: identifying check-worthy statements in large streams of speech and text. Claim detection is not fact verification. A claim classifier can help prioritize work, but cannot establish whether a statement is true.

### Ecosystem context

The Duke Reporters' Lab tracks fact-checking organizations and projects. Its 2026 census reports a changing ecosystem with new projects and closures, highlighting that long-term funding and organizational independence are real constraints for public-interest fact-checking.

## 6. What these systems leave open

Across these projects, several patterns recur:
- Factiz aggregates published newsroom verdicts but does not expose a structured graph of all underlying evidence.
- AsOf stores dated, sourced entity facts but does not provide a general argument/disagreement model or a complete public data export.
- Full Fact and similar organizations identify and investigate claims, but their outputs are editorial fact-checks rather than an open, composable knowledge base.
- Cofacts enables community participation and open data, but its own documentation and external research identify the need for stronger formal verification standards and reviewer support.
- ClaimReview helps publishers describe fact checks but does not provide a universal record of claims, evidence passages, competing assessments, and corrections.

Potential Common Knowledge work remains, but it must be framed carefully:
1. Connect claims to precise source passages, data rows, legal sections, and versions.
2. Preserve multiple assessments, counterevidence, and disagreements rather than flattening them into one verdict.
3. Distinguish claim scope, ambiguity, comparability, source reliability, evidence quality, testability, and conclusion.
4. Integrate fact-check archives and professional fact-checkers rather than replacing them.
5. Provide a public-facing, cross-domain interface and durable open exports.
6. Build reviewer support and public-interest stewardship that can sustain careful work without relying on a single founder or one model.

## 7. Recommended next step

Use a single real public claim that has already been fact-checked by multiple newsrooms. Compare:
- the original claim and context;
- each newsroom's own verdict and article;
- the exact sources and passages those articles rely on;
- whether different verdicts reflect different evidence, scope, or methods;
- what Factiz and ClaimReview can already provide;
- what additional structure Common Knowledge would add.

This would test whether Common Knowledge can contribute something genuinely new to the civic information ecosystem without duplicating the work of existing fact-checkers.
