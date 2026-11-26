# Workstream E — Multilingual Discovery and Inclusive Metadata

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Preliminary evidence review; language-community engagement remains essential
- **Workstream:** [E — Shared knowledge and preservation](README.md)

## 1. Language is part of knowledge access, not a user-interface feature

A digital knowledge system may technically accept Unicode text and offer a translated interface while still being inaccessible to many people. Discovery depends on whether metadata, labels, search terms, names, concepts, and source content are available in the languages people use.

Multilingual access also involves more than direct translation:
- Local concepts may not have exact equivalents in dominant languages.
- Dialects, scripts, transliteration, and orthographic variation matter.
- People and places may have multiple names and naming traditions.
- Search systems may perform unevenly across languages.
- Machine translation may distort context or cultural meaning.
- Some languages have little digital training data or specialist terminology.
- Community authority may govern whether and how a language resource is published.

A knowledge commons that treats English metadata as the default and other languages as optional enrichment risks reproducing existing inequalities.

## 2. UNESCO's Global Roadmap for Multilingualism in the Digital Era

UNESCO's 2025 Global Roadmap for Multilingualism in the Digital Era addresses the need for equitable representation and support for languages across digital platforms. It highlights language technologies such as machine translation, speech recognition, and natural-language processing, with attention to low-resource and endangered languages.

**Assessment:** Multilingual access is a structural digital-inclusion issue. The roadmap is an important policy signal, but implementation requires resources, language expertise, community participation, and support for languages that are not commercially attractive to technology providers.

## 3. Linked data and language-resource interoperability

A 2024 survey of multilinguality and linguistic linked open data (LLOD) describes both the potential and remaining challenges of publishing language resources as linked data. It identifies project-specific formats and limited interoperability as barriers to sharing and integration, while noting that linked data can help connect resources across languages.

The review also identifies limitations in representing rich morphological structures and fine-grained language varieties or dialects.

**Assessment:** Standards such as SKOS and linked-data vocabularies can help connect multilingual concepts and resources, but language tags alone do not solve cultural, semantic, or dialectal representation.

## 4. Wikidata language coverage: broad but uneven

A 2026 preprint analyzing more than 10 million statement bindings and over 6 million human entities reports substantial missingness in Wikidata's representation. Among the evaluated human entities, non-English descriptions covered 18.2% of items; it also reports geographic and demographic imbalances.

An earlier peer-reviewed survey of Wikidata language coverage found that labels and descriptions were distributed across many languages, but the median item had labels in only six languages. Coverage varied dramatically by language.

**Assessment:** A knowledge graph can support hundreds of languages while still leaving most individual entities without descriptions in many of those languages. The number of supported languages is not a sufficient measure of multilingual access.

**Limitations:** The 2026 analysis is a preprint and studies a particular set of properties and entity categories. The earlier coverage survey reflects an older state of Wikidata. Neither should be generalized to all knowledge graphs.

## 5. Inclusive metadata work is constrained by institutional resources

A 2026 study based on nine semi-structured interviews with metadata professionals at US R1 universities found broad interest in inclusive metadata but inconsistent implementation. Participants described constraints from legacy data, system limitations, project-based work, inadequate resources, and gaps in shared standards and cross-specialty coordination.

A 2025 study of multilingual academic retrieval across China and Sub-Saharan Africa describes a 13-language corpus and reports that Mandarin and English account for 64.6% of tokens, while nine African languages each contribute under 1.8%. Its system improved retrieval metrics in the studied corpus, but the distribution shows how a nominally multilingual dataset can remain highly imbalanced.

**Assessment:** Inclusive metadata requires institutional time, language expertise, coordination, and ongoing maintenance. Automated translation and retrieval may improve access but can also hide uneven coverage behind aggregate performance metrics.

## 6. Implications for Common Knowledge

Potential requirements to test:
1. Support language-tagged titles, descriptions, names, and concepts from the beginning.
2. Preserve original-language source descriptions alongside translations.
3. Distinguish human translations, community-approved translations, and machine-generated translations.
4. Record language variants, scripts, transliterations, and dialect information where appropriate.
5. Avoid automatically treating one language's label as the canonical name.
6. Make language coverage measurable at the resource and field level, not only at the platform level.
7. Allow communities to define preferred names, descriptions, and protocols.
8. Make machine-translated content visibly identifiable and correctable.
9. Avoid training or indexing protected language material without appropriate authority.
10. Fund ongoing metadata curation rather than treating translation as a one-time import task.

These are candidate requirements, not adopted policy.

## 7. Open questions

1. Which language communities and knowledge domains are absent from current repositories and knowledge graphs?
2. How can Common Knowledge measure multilingual coverage without reducing language communities to a score?
3. How should conflicting names, scripts, transliterations, and dialect variants be represented?
4. What level of human or community review is needed for machine translations?
5. How can low-resource language data be supported without extracting it from communities?
6. Which standards and APIs preserve language tags and original descriptions through export and aggregation?
7. How should search quality be tested across languages and resource types?
8. What financial and governance model can sustain multilingual curation?

Direct engagement with language communities, Indigenous knowledge holders, librarians, and metadata professionals is required before implementing language policies.

## Sources

See the November 2026 source register, entries E-30 onward.

## Change log

- **2026-11-26:** Added an initial review of multilingual digital access, linked language data, Wikidata language coverage, inclusive metadata practice, and multilingual academic retrieval.
