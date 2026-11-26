# Workstream E — Preliminary Comparative Synthesis

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Preliminary synthesis; workstream remains in progress
- **Workstream:** [E — Shared knowledge and preservation](README.md)

## 1. Main finding: a commons is a federation of responsibilities, not just a shared database

The reviewed systems solve different parts of the knowledge lifecycle:
- Repositories and archives hold primary resources.
- Metadata registries and aggregators make resources discoverable.
- Identifier systems disambiguate works, people, organizations, and versions.
- Vocabularies and ontologies help express concepts and relationships.
- Presentation standards make complex digital objects usable.
- Preservation networks protect digital content against loss and corruption.
- Community archives and governance frameworks define who may describe, access, preserve, or reuse knowledge.

These functions should not be conflated or assumed to belong to one institution. A federated commons may coordinate relationships among existing stewards without taking custody of every resource.

## 2. Findings grounded in the current sample

### 2.1 Interoperability requires mappings and provenance, not just a common format

Dublin Core, SKOS, BIBFRAME, DataCite, PROV, RO-Crate, and Europeana's Data Model serve different purposes. Europeana's approach shows how an aggregator can map diverse provider schemas into a shared model while retaining distinctions between the provided object, digital representations, and descriptions. Its documentation also recognizes multiple descriptions and provenance for enrichment.

**Assessment:** Common Knowledge should not require all contributors to replace their systems with one schema. It should test mapping layers that preserve the source record, record the transformation, and expose the normalized view as a derived representation.

### 2.2 Discovery is not custody or preservation

OAI-PMH exposes metadata for harvesting; it does not transfer arbitrary content. DPLA's public description links metadata records back to contributor-held items. Crossref and DataCite provide persistent identifiers and metadata, not guarantees that the underlying content remains available. IIIF supports interoperable presentation, not archival custody.

**Assessment:** A discovery layer must state whether it stores metadata, content, preservation copies, or only links. It should not imply that a linked object is preserved by the aggregator.

### 2.3 Persistent identifiers solve naming problems, not all continuity problems

DOIs, ORCID iDs, and ROR IDs help identify outputs, people, and organizations. They support linking and disambiguation, but depend on metadata maintenance and responsible resolution services. BIBFRAME's Work–Instance–Item distinction shows why entity granularity matters.

**Assessment:** A knowledge record should distinguish the abstract work, a particular edition or version, a digital file or manifestation, and a locally held copy. It should preserve identifier types rather than flattening every identifier into a generic URL field.

### 2.4 Preservation requires people, policy, funding, and technical operations

PREMIS, BagIt, OAIS, CoreTrustSeal, LOCKSS, and CLOCKSS cover different parts of preservation. Fixity checks and replicated copies help detect and repair corruption. OAIS and CoreTrustSeal emphasize organizational responsibilities and trustworthy repository characteristics. CLOCKSS demonstrates a governed dark archive with trigger-based access.

**Assessment:** “We have backups” is not an adequate preservation policy. A durable commons needs named custodians, rights to preserve and migrate, funding, procedures, independent verification, and a succession plan.

### 2.5 Open by default must be constrained by rights and community authority

FAIR, CARE, Local Contexts, Mukurtu, and UNESCO documentary-heritage guidance collectively show that data usability and community rights must be considered together. CARE emphasizes collective benefit and authority to control; Local Contexts enables communities to communicate protocols; Mukurtu supports granular access and multiple community narratives; UNESCO recognizes cultural custodianship and legitimate access restrictions.

**Assessment:** Preservation, discovery, access, and reuse permissions should be separate fields and decisions. Public availability does not imply consent for every future use, and a technically accessible file is not necessarily ethically open.

### 2.6 Knowledge records must preserve plural sources and contested descriptions

Wikidata's sourcing guidance places responsibility on editors to cite supporting sources and permits multiple sourced values with qualifiers. Europeana's model can retain multiple provider descriptions, including contradictions. Mukurtu supports multiple community records for material.

**Assessment:** Common Knowledge should not silently collapse disagreement into one canonical statement. It should preserve source-specific claims, attribution, dates, context, and the reason a normalized view selects or prioritizes one value.

## 3. Candidate design principles

The following are hypotheses for technical and community testing, not adopted platform requirements.

1. **Federation before centralization:** connect existing stewards and systems before building a universal repository.
2. **Source records remain identifiable:** preserve original metadata and links separately from normalized or enriched records.
3. **Mappings are inspectable:** record schema versions, transformation rules, and responsible agents.
4. **Claims are source-linked:** attach provenance and citations to individual claims or statements where feasible.
5. **Plurality is representable:** allow multiple sourced descriptions, interpretations, and values.
6. **Rights travel with records:** licenses, restrictions, consent conditions, and community protocols must survive export and aggregation.
7. **Preservation is explicit:** distinguish link, metadata copy, content copy, and managed archival preservation.
8. **Access is layered:** separate preservation permission, metadata discovery, content access, and reuse.
9. **Community authority is real:** do not collect, label, publish, or reuse community-controlled knowledge without appropriate authority and relationships.
10. **Portability is a design requirement:** provide export, independent verification, and migration paths.
11. **Uncertainty remains visible:** record entity-match confidence, source disagreements, stale metadata, and known gaps.
12. **Human stewardship is infrastructure:** sustainable services require people, training, governance, and support—not only software.

## 4. Gaps in this investigation

This first pass is weighted toward scholarly metadata and library-sector standards. It is not yet a balanced global survey. Significant gaps include:
- Community archives beyond the examples reviewed.
- Indigenous-led systems and direct consultation with knowledge-holding communities.
- Multilingual metadata and search in under-resourced languages.
- Accessibility for people with disabilities and low-bandwidth settings.
- National libraries and archives outside North America and Europe.
- Oral histories, living traditions, non-textual knowledge, and locally governed collections.
- Software and web archiving, born-digital works, and dynamic research artifacts.
- Long-term costs, staffing, governance, and independent audits of preservation providers.
- Actual interoperability tests and migration exercises rather than documentation-only comparison.

## 5. What would change this assessment?

The federation hypothesis should be revised if practical tests show that existing systems cannot exchange the needed metadata, rights, provenance, and version information without unacceptable loss or cost. The next phase should therefore include small interoperability experiments and conversations with repository managers, librarians, archivists, researchers, and community stewards.

## 6. Next research actions

1. Profile representative digital preservation and community-archive projects, including their funding, governance, and continuity arrangements.
2. Examine multilingual discovery, accessibility, and metadata quality across different regions.
3. Test a small crosswalk among Dublin Core, DataCite, Schema.org, PROV, and RO-Crate using real sample records.
4. Test how source records, conflicting values, rights statements, and corrections survive aggregation and export.
5. Conduct direct, consent-based conversations with community archives and knowledge stewards before proposing platform features.
6. Produce a bounded field synthesis only after these gaps are addressed.

## Sources

See the [November 2026 source register](../../sources.md), entries E-01 onward.

## Change log

- **2026-11-26:** Added a preliminary synthesis across metadata, identifiers, aggregation, preservation, community rights, and documentary heritage. Workstream E remains in progress.
