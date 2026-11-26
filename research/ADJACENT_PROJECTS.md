# Adjacent Projects — Claims, Evidence, and Shared Knowledge

- **Research date:** 26 November 2026
- **Status:** Initial landscape assessment; not independently reviewed
- **Purpose:** Identify existing projects that overlap with Common Knowledge before we design or build a competing system.

## Why this matters

The initial technology survey was too narrow. It compared infrastructure components, but it did not yet map the projects already trying to create shared, structured records of claims, evidence, disagreement, and human/AI contributions.

This investigation found several close initiatives. Some are established research platforms; others are early schemas, pilots, or proposals. They are not interchangeable, and their reported adoption figures should not be treated as independently verified.

**The main implication is strategic:** Common Knowledge should not begin by inventing another publication network, claim/evidence schema, or graph store. We first need to establish whether a useful public-facing, general-knowledge, public-interest layer can build on or collaborate with these efforts.

## 1. Knowledge Space, Knowledge Pixels, and Nanoarguments

**Links**
- [Knowledge Space vision](https://w3id.org/knowledge-space/)
- [Knowledge Space version 1.0 (27 April 2026)](https://gist.github.com/tkuhn/a3842683b810f1e0dbc72a021083ea31)
- [Knowledge Pixels](https://knowledgepixels.com/)
- [Nanopublications](https://nanopub.net/)
- [Nanoarguments — NLnet project](https://nlnet.nl/project/Nanoarguments/)
- [Nanopublication ecosystem paper](https://knowledgepixels.com/nanopub-ecosystem-paper/)

### What exists

Knowledge Space is a detailed vision for an open, decentralized socio-technical ecosystem in which people and automated agents publish small, immutable, content-addressed knowledge records with provenance and optional signatures. It describes independent publishing/lookup and query services, collections, agent and service introductions, assessments, trust settings, key recovery, and trust-range algorithms.

The current nanopublication ecosystem is a concrete implementation of substantial parts of this vision:
- small RDF records with assertion, provenance, and publication metadata;
- cryptographic signatures and content-derived Trusty URIs;
- federated registries that replicate records;
- independent query services exposing SPARQL and reusable APIs;
- declarations and endorsements connecting agent identities to signing keys;
- a reproducible trust-propagation algorithm (IDEBT) used by registries to determine agent/key trust and publication quotas.

The ecosystem paper reports a snapshot from **4 May 2026** containing 79,672 nanopublications signed by 616 distinct agents. This is a dated project-reported snapshot, not a current live count or an independent audit.

The NLnet-funded **Nanoarguments** project began in April 2026. Its stated goal is a global, federated graph of scientific claims, evidence chains, and discussion. It builds on Nanodash, integrates with dokieli for in-document authoring, and plans a bidirectional ActivityPub connector so discussions can become persistent structured evidence records. NLnet lists the project as funded through the NGI0 Commons Fund.

### A particularly close proposal

On 2 October 2026, Knowledge Pixels founder Tobias Kuhn proposed **A shared open record of claims by humans and AI** on Manifund. Its stated scope explicitly includes scientific and other claims, provenance, checks and objections, correspondence between claims, support/rebuttal/qualification, AI model/configuration provenance, an agent library/MCP server, and extraction of argument structure from debates.

The proposal closed on 2 November 2026 without reaching its minimum: the page reports $0 raised against a $15,000 minimum and a $100,000 goal. This means that specific proposal was not funded. It does **not** mean the underlying work is absent: the nanopublication network, Nanodash, agent identity/delegation, the nanopub-skill, and the related NLnet-funded Nanoarguments project already exist.

### What overlaps with Common Knowledge

Very high conceptual overlap:
- human and AI contributions;
- small independently citable claims;
- provenance and source traceability;
- support, rebuttal, qualification, and disagreement;
- cross-linking claims made independently;
- open, decentralized publication and query;
- trust and identity separated from any single central authority.

### What is not yet the same thing

The funded Nanoarguments project is explicitly focused on scientific discourse. The broader human/AI claims proposal would extend to other domains, but its proposed knowledge-sharing layer and debate-extraction workflow were not funded through that campaign. The current network provides publication, signatures, replication, and querying; it is not, by itself, a complete public-facing process for evaluating arbitrary claims.

The Knowledge Space trust model primarily answers questions about agents, keys, and services. It must not be mistaken for proof that an assertion is true. The ecosystem's own paper describes trust in agents and services as a distinct layer.

### Risks and constraints

- Nanopublications are deliberately public, immutable, and widely replicable. Sensitive or rights-restricted material needs a different handling path.
- Online Nanodash signing keys are held server-side; command-line keys are held locally. These have different custody and recovery risks.
- Different ecosystem components have different licenses; do not assume one license covers all tools, vocabularies, templates, or data.
- The broader claim-sharing proposal is a clear potential collaborator or adjacent project, not a reason to build a parallel network without first talking to its authors.

**Assessment:** This is the closest existing infrastructure and strategic neighbor. Common Knowledge should investigate interoperability and collaboration before considering a new publication protocol or trust network.

## 2. MIRA and Discourse Graphs

**Links**
- [MIRA](https://mira.science/)
- [MIRA schema repository](https://github.com/MIRA-science/schema)
- [MIRA Evidence class](https://mira.science/schema/Evidence/)
- [Discourse Graphs](https://discoursegraphs.com/)
- [MIRA kickoff report](https://mira.science/blog/what-we-built-at-the-mira-kickoff/)

### What exists

MIRA (Modular Interoperable Research Attribution) is an open, early-stage schema for structuring research in progress. Its current schema includes:
- Question;
- Claim;
- Evidence;
- Study;
- Protocol;
- SourceDocument;
- Request;
- shared nodes, agents, and relation definitions.

It uses LinkML and publishes a JSON-LD transport context and generated SHACL shapes. The schema defines links such as `addresses`, `supports`, `opposes`, `grounds`, `follows`, and `sourceDocument`.

MIRA itself hosts no data. It is an interoperability layer intended to let different tools contribute to and query shared research graphs.

The MIRA website reports 100+ researchers writing weekly, 6,000+ signed research records, and 10+ life-science labs deployed. These are self-reported ecosystem figures; they should not be interpreted as proof that every record uses the current published schema or that the schema has been independently adopted at that scale.

### Fit and limitations

MIRA is a strong starting point for scientific discourse. It distinguishes claims from empirical evidence and connects evidence to studies, protocols, and source documents.

However, the current schema is research-specific:
- Evidence is defined as a specific empirical observation from a research method.
- It does not currently define a general source-passage selector for a quote, page, dataset row, cell, or time interval.
- It has `supports` and `opposes`, but no dedicated general assessment/review object or explicit `qualifies` relation in the current schema.
- Claim scope, definitions, uncertainty, and epistemic assessment methods are not fully specified as first-class structures.
- The current generated SHACL shapes include closed shapes for key classes, so extensions need to be made deliberately and kept interoperable.

The schema repository is marked as a working version. **No license file or repository license metadata was visible in the review.** Clarify licensing with maintainers before copying or embedding its schema or generated artifacts.

**Assessment:** MIRA is a serious candidate for a science-domain mapping or extension point, not yet a complete general-purpose knowledge model. A mapping of the same synthetic observation used in our other tests is recorded in [the MIRA mapping probe](experiments/2026-11-mira-mapping.md). It is worth discussing with its maintainers before designing an alternative.

## 3. SciOS: RRGI, the Minimum Viable Scientific Record, and a Git-based discourse graph

These are related but distinct artifacts and must not be conflated.

**Links**
- [SciOS](https://www.scios.tech/)
- [RRGI live graph](https://graph.scios.tech/)
- [RRGI workshop](https://workshop.scios.tech/)
- [Minimum Viable Scientific Record essay and graph](https://www.scios.tech/minimum-viable-scientific-record/)
- [Git-based discourse graph repository](https://github.com/jring-o/rdf)
- [Repository schema](https://github.com/jring-o/rdf/blob/main/SCHEMA.md)
- [Repository contribution guide](https://github.com/jring-o/rdf/blob/main/CONTRIBUTING.md)

### RRGI live graph

The public RRGI site describes a graph of signed records stored under authors' AT Protocol DIDs, indexed by an AppView, and pinned to IPFS. It presents a browser graph with research bundles and records that can be read, challenged, and extended. The page reported **532 records, 532 cold-stored, and six bundles** when inspected on 26 November 2026.

The live UI describes record types such as questions, claims, evidence, and sources, and relations such as supports, opposes, addresses, derived-from, contradicts, describes, grounds, follows, version-of, and equivalent-to. The MIRA kickoff report says RRGI adds endorsements that let researchers mark a claim as believed, verified, or qualified, and a Deltabay view that scores how evidence influences the credibility of answers to research questions. These appear to be RRGI/application-level capabilities rather than slots in the current published MIRA schema; the exact RRGI endorsement model still needs inspection. The site also describes a PDF extraction workflow. A separate workshop interface allows session participants to create drafts without accounts; the page says drafts remain private to the session.

The public site is a meaningful working prototype. However, a public API specification or source repository for the RRGI application was not located in this pass. The API root and common documentation paths returned 404 through the inspected browser interface. The reported record counts and storage behavior are site claims, not an independent audit.

### Minimum Viable Scientific Record (MVR)

A SciOS essay proposes a minimum viable scientific record and reports a decomposed corpus of:
- 153 source documents;
- 26,264 graph records;
- 21,422 extracted claims;
- 4,400 equivalence relations.

The essay describes source passages, provenance, persistent identifiers, typed relations, corrections, disputes, licensing, and machine-readable export. The JSONL corpus was too large for the available browser retrieval method, so its contents were not independently inspected in this pass. Treat the counts and implementation details as author-reported.

This is a research corpus and proposal, not the same thing as the smaller live RRGI graph.

### Git-based discourse graph

The public repository `jring-o/rdf` contains a third, distinct implementation: a whitepaper decomposed into individual Markdown nodes and linked through YAML frontmatter. Its current graph contains 349 nodes: questions, claims, evidence, methods, and sources.

Its contribution workflow is unusually simple:
- each node is a small standalone file;
- discussions attach to individual nodes;
- browser forms or Git can create a contribution;
- changes are submitted as pull requests;
- counterclaims and counter-evidence are new nodes linked with `opposes`, rather than overwriting the original;
- a graph linter checks schema, edges, reciprocal links, and body lengths.

The repository reports CC BY 4.0 for content and MIT for code. Its schema follows the Discourse Graphs Q/C/E/S model and adds Method. Check the provenance and rights of the upstream schema before reusing it.

### Fit and limitations

SciOS demonstrates several useful approaches:
- a public graph that people can inspect;
- signed, individually attributable contributions;
- source-passage-aware claim decomposition in a research corpus;
- explicit counterclaims and counter-evidence;
- lightweight Git-based review as an alternative to building a bespoke collaboration platform;
- an AT Protocol/IPFS architecture for personal data ownership and preservation.

The current graph schemas are science-oriented. A read-only inspection of selected Git-based graph nodes found that evidence is summarized and linked to a bibliographic Source node, but the sample did not include a DOI/URL or exact passage/table/row selector. Its `status` field is a contribution lifecycle state, not an epistemic verdict. The Git-based schema has no universal source-version/selector model, and its claim/evidence vocabulary is not yet a general epistemic assessment standard. The live RRGI app's API and source availability remain open questions. See the [read-only graph review](experiments/2026-11-scios-git-graph-review.md).

**Assessment:** One of the closest practical examples to the product workflow Common Knowledge is exploring. It should be tested as a product and potential collaborator, not treated as a complete general knowledge authority.

## 4. The Consilience

**Links**
- [The Consilience](https://theconsilience.io/)
- [GitHub repository](https://github.com/Anuja-Khatri/theconsilience-engine)
- [Published papers and validation materials](https://github.com/Anuja-Khatri/theconsilience-engine#published-papers)

### What exists

The Consilience is a specialized deterministic verification engine for comparing scientific claims across domains. Its documented pipeline:
- extracts typed claims from papers, including exact source sentences;
- compares structural commitments across different vocabularies using typed graph matching;
- applies explicit grading levels and ceilings on what a match does and does not license;
- assesses whether disagreements can be tested with existing instruments;
- records rejected comparisons with structural reasons.

Its design separates model-based extraction from code-based judgment: the model reads and types; deterministic code performs the verification.

A live query of the nanopublication assertion-template index on 25 November 2026 returned **six public Consilience templates**:
1. **Theory claim card:** a theory, claim statement, dimension of commitment, position on that dimension, and source locations (document and page). Each claim has its own IRI and can be superseded by a corrected card.
2. **Measured claim card:** exact source sentence, source document, subject, quantity/axis, QUDT value and unit, bounds and unit as written, conditions, and claim kind.
3. **Data-quality finding:** a check run over a dataset, how many records were flagged out of how many checked, and a finding framed as an observation about records rather than the people who produced them.
4. **Disagreement:** two claims taking different values on a dimension, with the dimension, observables, instruments, testability status, assumptions, margin/floor, unit, and reason.
5. **Claim correspondence:** two claims compared structurally and assigned a grade on a four-rung ladder from structural identity to thematic resonance, with explicit limits on what the grade licenses and an equivocation check.
6. **Comparison refused:** a structured record for declining a comparison rather than forcing a misleading equivalence.

These are real, published templates in the public nanopublication network, not merely proposed fields. They are authored by the Consilience project, not a universal Knowledge Pixels standard. The measured-claim and disagreement templates are especially relevant to the civic-budget stress test: they already model quantities, units, conditions, dimensions, and testability. The remaining question is how well their scientific vocabulary generalizes to public-policy claims and whether exact source locations are durable enough for our use. We mapped the same fictional budget example to these templates in [the Consilience civic-budget mapping probe](experiments/2026-11-consilience-civic-budget-mapping.md).

The author reports blind testing against the COGITATE adversarial collaboration: 2 of 3 predictions recovered after a disclosed re-review, with a 1,000-key permutation test yielding p=0.075, explicitly described as suggestive only. The repository reports a solo build and has a small public footprint at the time of review. Code is Apache-2.0; documentation is CC BY 4.0.

Template examples:
- [Theory claim card](https://w3id.org/np/RAmOdphN9C0EvbBzcUBHfii2z-EYmcPsTwP2mLr9SsOLk)
- [Measured claim card](https://w3id.org/np/RA2bWtxQfydQAEUp-qimU19xrw3XlXRmkgsvC7jTdh4LU)
- [Data-quality finding](https://w3id.org/np/RALu1b-aXtNNYykZ7Qrz04kx_NMVIapIfzvpFVrXRhbaM)
- [Disagreement](https://w3id.org/np/RAvlFcbPa5pxTNcz8r_uYIDAXRuieEgMgSnPlzBHibUjY)
- [Claim correspondence](https://w3id.org/np/RAB5yq6zMD127_oapC0cGKGoS5Ey5UaNVf94DRwWW83P4)

### Fit and limitations

This is not a general knowledge repository or a public evidence network. It is a specialized verifier for a narrow class of cross-domain scientific comparisons.

**Assessment:** Worth studying for deterministic checks, explicit verdict limits, testability, and published rejection reasons. It is not a replacement for Common Knowledge's contribution, provenance, or discovery layers.

## 5. Project Delphi / Science Oracle

**Links**
- [Science Oracle application](https://scienceoracle.com/)
- [Public graph](https://scienceoracle.com/graph)
- [PKG Viewer](https://pkg.scienceoracle.com/)
- [Ontology repository](https://github.com/fractastical/project-delphi-ontology)
- [Ontology reference](https://github.com/fractastical/project-delphi-ontology/blob/main/ONTOLOGY.md)
- [Publishing best practice](https://github.com/fractastical/project-delphi-ontology/blob/main/PUBLISHING.md)

### What exists

Project Delphi (formerly ProbKnow) has a live public application, Science Oracle, for source-traceable scientific Q&A and graph exploration. It describes a public research graph of claims, evidence, hypotheses, and assessments, with interfaces to ask questions, browse papers, explore hypotheses, and inspect nanopublications in a separate PKG Viewer.

The public application says that:
- answers are bounded by retrieved public graph sources, not web search or private research;
- supported statements, counterevidence, and gaps should be separated;
- citations should open source excerpts and, where available, original DOI publications;
- graph evidence confidence is aggregated from cited source scores with dependency adjustment and a coverage indicator;
- this confidence is not the probability that the generated answer is correct or a calibrated truth guarantee;
- absence of counterevidence in the retrieved set does not mean none exists.

The ontology repository is MIT-licensed and currently documents version 2.0. Its main modeling choices are particularly relevant:
- `Claim` is a subclass of `Hypothesis`: a hypothesis is a proposition represented without asserting it; a claim is a proposition a source states. The README explicitly describes a claim as a belief, not an asserted fact.
- `EvidenceItem` is separate from claims and assessments.
- `Assessment` is a separate n-ary evaluation with verdict, probability, confidence, reasons, evidence, and assessor attribution where available.
- `BayesianAssessment` carries Bayes factors and calibration information.
- `LLMClaimAssessment` records language-model evaluations.
- The assessor is a PROV-O SoftwareAgent; the model it runs is a separate `LanguageModel` entity, so two agents using the same model but different prompts/scaffolding can be distinguished.
- Other terms include scores, evidence weights, decibans, assessment types, calibration methods, p-values, statistical tests, and research domains.

The repository also contains a detailed 12-step publishing practice: source every assertion; publish each dataset as its own nanopublication; sign and test before production; require a human review sample and a second reviewer for high-stakes/public-facing claims; use two assessors from different providers in the documented audit path; record source hashes and generator versions; supersede/retract rather than overwrite; and maintain publication manifests.

### Public collection and openness

The README distinguishes three different things: the changing application dataset, the ontology/code repository, and the subset of records actually published to the nanopublication network. Not every application record is exported, signed, or published; public views do not constitute a complete export of private research.

The public domain-index endpoint returned 893 domain labels in a dated snapshot referenced by the README (11 October 2026). The README warns that this is not 893 equally populated or independently validated disciplines. The PKG Viewer displayed 6,241 imported/matched records during our 26 November inspection. These are dated UI observations, not an independent data audit or a complete corpus count.

### Hands-on UI result

Two read-only public Q&A tests were attempted, including one of the application's own starter questions. Both failed with the message that Delphi could not complete the answer and that no answer had been generated from unverified sources. No citations or excerpts were returned.

This is a single-session availability/UX observation, not evidence that the underlying claims or graph are wrong. The fail-closed behavior is good; the generic error did not distinguish an unavailable answer service from a genuine evidence gap. The homepage also notes that questions and responses are saved in the browser, including on shared devices.

See [the Science Oracle UI review](experiments/2026-11-science-oracle-ui-review.md).

### Fit and limitations

This is one of the closest existing scientific products to Common Knowledge's desired experience. It already has a public source-linked Q&A interface, graph exploration, explicit counterevidence/gaps, claim/evidence/assessment distinctions, model provenance, and a disciplined publication process.

It is nevertheless science-focused. The public domain index and application are organized around research domains; the current product is not a general civic, legal, historical, or public-policy knowledge service. The public corpus is also not a complete export of the full application dataset.

**Assessment:** Do not build another science-only source-linked Q&A and evidence graph without a compelling reason. Project Delphi is a strong technical and UX reference and a potential collaborator. Common Knowledge's possible distinction would need to be validated around general public knowledge, civic/legal/policy claims, a fully inspectable public corpus, and public-interest stewardship—not simply around claim/evidence graphs or AI assessments.

## 6. Open Research Knowledge Graph (ORKG)

**Links**
- [ORKG](https://orkg.org/)
- [ORKG Academy](https://academy.orkg.org/)
- [ORKG comparison course](https://academy.orkg.org/courses/comparison-course.html)
- [ORKG documentation](https://docs.orkg.org/)

### What exists

ORKG is an established scholarly knowledge graph focused on describing research papers and their contributions as structured, machine-readable data. Its central user-facing concepts include:
- structured paper contributions;
- comparisons that summarize and compare results across papers;
- community-maintained review/survey articles;
- lists and templates;
- a public API and exports including CSV, LaTeX, RDF, and PDF;
- stable DOI publication for comparisons.

The ORKG Academy documents human workflows for creating comparisons from papers, DOI lookups, and CSV imports, and describes AI-assisted support for structuring comparisons.

### Fit and limitations

ORKG is a mature reference for structured scholarly contribution authoring, templates, comparisons, and living reviews. Its core model is research-paper contributions and comparison tables, not a general public claim/evidence/disagreement system. An external knowledge-graph registry reports CC BY-SA 4.0 for ORKG data; verify current official terms before reusing data or building derivatives.

**Assessment:** A useful integration and UX reference for science, but not a complete foundation for general public knowledge.

## 6. Comparison: what is already covered?

| Capability | Knowledge Pixels / Nanoarguments | MIRA / Discourse Graphs | SciOS RRGI / MVR | The Consilience | Project Delphi | ORKG |
|---|---|---|---|---|---|
| Human and AI contributions | Agent identity and AI skill exist; broader claim workflow proposed | Human research collaboration; AI-assisted tools in ecosystem | AI extraction plus human review/endorsement in RRGI | AI extraction; deterministic code judges | AI-assisted structured contribution workflows |
| Atomic claims | Core nanopublication model supports it | First-class Claim | First-class Claim | Typed claims | Structured research contributions |
| Evidence relations | Nanoarguments aims at support/rebuttal/qualification | supports/opposes; evidence/claim links | supports/opposes/grounds and related edges | Evidence and claim structures | Research contribution properties/comparisons |
| Provenance and signatures | Strong: signed nanopubs, Trusty URIs, provenance | Signed records reported by MIRA ecosystem | Signed records in RRGI; provenance in graph models | Deterministic input/output hashes and source sentences | Contributor/provenance metadata; DOI publication |
| Exact source passages | Not yet a complete universal locator | No general selector in current schema | MVR reports source passages; live RRGI details need testing | Exact source sentence is part of extraction | Source papers linked; not a general passage-anchoring layer |
| Disagreement and correction | Nanoarguments and unfunded broader proposal target this | supports/opposes relations | counterclaims/opposes, endorsements, version relations | Structural mismatch/rejection and claim comparison | Comparisons/reviews, not a general objection network |
| General public knowledge | Broader proposal includes scientific and other claims | Primarily research | Primarily research | Scientific cross-domain comparison | Scholarly research |
| Public-facing product | Nanodash and related tools; broader knowledge-sharing UI proposed | Multiple research tools | Live public graph and workshop | Specialized verifier and demos | Mature public scholarly portal |
| Decentralized infrastructure | Strong, federated nanopublication network | Schema only; does not host | AT Protocol and IPFS in live RRGI | Not the main focus | Hosted institutional platform |
| Institutional/public-interest stewardship | Open network, but ecosystem stewardship is separate from Common Knowledge's mission | User/toolmaker stewardship | Project-specific | Solo project | Institutional research infrastructure |

## 7. What might still be distinct about Common Knowledge?

The overlap is substantial. We should not claim that Common Knowledge is the first project to propose a shared, evidence-linked record of claims by humans and AI.

Potentially distinctive work remains, but it needs validation:
1. **A general public knowledge service:** not limited to scientific literature or research projects; includes public policy, law, history, civic information, and other domains.
2. **An accessible public reading experience:** a person can inspect a claim's exact scope, definitions, evidence passages, counter-evidence, assessments, uncertainty, and revision history without understanding RDF, Git, or research metadata.
3. **A public-interest stewardship model:** long-term institutional independence, contributor rights, safety, preservation, and funding constraints that prevent capture or private enrichment.
4. **A clear epistemic assessment method:** distinguish what a source says, what an observation records, what an argument infers, and what a reviewer concludes; expose methods and uncertainty rather than reduce truth to popularity or agent reputation.
5. **Domain-aware source anchoring:** reliable links into legislation, court decisions, government datasets, archived web pages, scientific papers, and structured data—not only scholarly paper metadata.
6. **Political and civic usefulness without partisan identity:** a carefully bounded way to investigate public claims and policy without becoming a campaign or partisan fact-checking brand.

These are hypotheses, not established gaps. Knowledge Pixels' broader proposal already overlaps with some of them, so we need direct conversations and real user research before claiming differentiation.

## 8. Strategic recommendation

Before building another data model or publication backend:

1. **Contact Knowledge Pixels** to understand the current Nanoarguments roadmap, the status of the broader human/AI claims proposal, and whether a general public/civic application could interoperate or collaborate.
2. **Talk with MIRA/Discourse Graphs maintainers** about the schema's scope, licensing, extension model, and whether general knowledge domains are within their intended remit.
3. **Inspect SciOS RRGI hands-on** and ask about source availability, API, licensing, roadmap, and the intended relationship between MIRA and RRGI.
4. **Map ORKG's strengths and limitations** as an upstream scholarly contribution source.
5. **Choose one civic/public-knowledge use case** and test whether any of these systems can already support it with acceptable contributor and reader experiences. A fictional budget-comparison case is recorded in [the civic claim stress test](experiments/2026-11-civic-budget-claim-stress-test.md); it distinguishes nominal from real-terms claims and tests ambiguity, comparability, and assessment.

Do not create a competing protocol, trust network, universal ontology, or large graph store until this work is done.

The most plausible opportunity may be to build Common Knowledge as a public-interest application and stewarded knowledge service that reuses and connects existing open infrastructure—rather than trying to replace all of it.
