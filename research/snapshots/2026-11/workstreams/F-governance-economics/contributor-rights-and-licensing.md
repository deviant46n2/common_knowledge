# Workstream F — Contributor Rights, Licensing, and Intellectual-Property Stewardship

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Preliminary legal-architecture analysis; not legal advice or a license selection
- **Workstream:** [F — Governance, economics, and institutional design](README.md)

## 1. One project may contain several kinds of intellectual property

Common Knowledge may create or steward software, documentation, research reports, datasets, databases, scientific articles, protocols, metadata, knowledge graphs, images, trademarks, and community-held or third-party materials. These categories do not necessarily share the same rights or licensing needs. A single repository-level license can be misleading if it appears to cover material with different owners, rights, or obligations.

## 2. Different works need different legal tools

### Software

Creative Commons explicitly recommends against applying CC licenses to software. It recommends established software licenses recognized by the Free Software Foundation or Open Source Initiative, because software licenses address source-code distribution, modification, and often patent rights.

The Open Source Definition requires free redistribution, source-code access, permission to create derived works, and no discrimination against people or fields of endeavor. An OSI-approved license permits commercial use and cannot prohibit use by a political organization, military actor, or particular research field.

### Documentation and other creative works

Creative Commons licenses can be appropriate for documentation, educational material, images, and other copyrightable content. CC BY 4.0 requires attribution and allows adaptation and commercial reuse. CC BY-SA adds a share-alike requirement for adaptations. CC0 is a public-domain dedication tool rather than an ordinary attribution license.

A CC license is generally not revocable for uses already authorized under its terms. The licensor must have authority to apply it.

### Data and databases

Open Data Commons provides database-specific tools:
- ODbL: attribution and share-alike for databases.
- ODC-By: attribution for databases.
- PDDL: public-domain dedication and license.

Database structure and database contents may have different rights. A database containing third-party text, images, or personal information may require separate permissions for those contents. Database rights also vary across jurisdictions.

FAIR or publicly accessible does not mean public-domain, unrestricted, or cleared for all reuse.

### Identifiers and license metadata

SPDX provides standardized identifiers and machine-readable license information for software, data, hardware, and documentation. SPDX identifiers can help systems detect and preserve license information during packaging and exchange.

## 3. Open-source licensing and anti-weaponization create a real tension

The Open Source Definition prohibits restricting use by field of endeavor. A project cannot claim an OSI-approved open-source license while forbidding downstream use for political campaigning, commercial products, military research, or other specified fields.

This does not mean the institution must support harmful activity. The legal and technical tools must be distinguished:
- An open-source license grants broad rights to recipients of the software.
- Hosted services can have acceptable-use rules, access controls, and safety policies.
- The institution can choose which projects it funds, hosts, or endorses.
- Data access and reuse can be restricted by rights, consent, privacy, security, or community protocols.
- Governance can prevent the institution itself from becoming a partisan instrument.

But a downstream user may still use an open-source copy in ways the institution opposes, subject to other applicable law. A use-restrictive license may express a policy preference but would not be OSI open source and could reduce compatibility and adoption.

**Assessment:** If Common Knowledge wants genuinely open-source software and political independence, anti-weaponization cannot be guaranteed by adding a field-of-use restriction to the software license. It must be pursued through institutional governance, funding rules, service policies, transparent research standards, and rights-aware data stewardship.

## 4. Contributor agreements: DCO and CLA are not the same

### Developer Certificate of Origin (DCO)

A DCO is a lightweight certification that a contributor has the right to submit a contribution under the project's existing license. It is commonly recorded with a Signed-off-by line in a commit message.

The DCO does not itself transfer copyright to the project. It provides a provenance and contributor-rights assertion. It does not resolve every question about employer ownership, patents, third-party code, or contributions from contractors.

### Contributor License Agreement (CLA)

A CLA defines additional rights granted to the project or its steward. The Apache Software Foundation's Individual CLA, for example, grants the Foundation and recipients broad, perpetual, worldwide, non-exclusive, royalty-free copyright and patent licenses for covered contributions, while contributors retain their copyright and may use their original contributions elsewhere.

A CLA can clarify rights and reduce legal uncertainty, but asks contributors to make contractual representations and may create friction for casual contributors. Corporate ownership, employment agreements, patents, and third-party materials still need attention.

## 5. Contributor agency and institutional stewardship

A contributor policy should explain:
- Who owns the contribution.
- Which license applies when it is submitted.
- Whether the contributor grants additional rights to the institution.
- Whether the contributor can reuse their own work elsewhere.
- How employer-owned work is handled.
- How third-party and AI-generated material must be disclosed.
- Whether the institution can relicense contributions.
- How attribution and moral rights are treated.
- What happens to contributions if the project or institution closes.
- How contributors can raise licensing or attribution disputes.

Avoid asking contributors to assign broad ownership rights unless there is a clear, justified need. Where a license grant is sufficient, it may better preserve contributor agency.

## 6. Current repository implications

A public GitHub repository is not automatically open source. GitHub's documentation states that, without a license, default copyright rules apply; other users may view and fork the repository through GitHub's platform terms, but do not receive general permission to reuse, redistribute, or create derivative works outside those terms.

For Common Knowledge:
- Decide the scope of the license before inviting substantive external contributions.
- Distinguish original documentation from future software, datasets, and third-party material.
- Avoid a blanket license notice that accidentally covers material the project does not own.
- Add a clear contribution policy before accepting significant code or research contributions.
- Do not change the current repository's license as part of this research pass; license selection remains a separate explicit decision.

## 7. Candidate policy principles

1. Contributors retain ownership of their original work unless a clearly justified and explicit agreement says otherwise.
2. Licenses are selected by material type and rights context.
3. The project does not claim rights over material it does not own or have authority to license.
4. Every contribution has traceable provenance and an explicit license basis.
5. Software, documentation, data, and media have distinct license treatment.
6. Third-party and AI-generated material is disclosed and reviewed before inclusion.
7. Attribution is preserved where required and where contributors request it.
8. Contributor agreements are proportionate and understandable.
9. Community-held knowledge is not relicensed or redistributed without appropriate authority.
10. The project distinguishes open-source licensing from acceptable-use rules for services it operates.

These are candidate principles for legal review and community discussion, not adopted policies.

## 8. Open questions

1. Should software use a permissive or copyleft license, and what trade-offs matter for federation and institutional adoption?
2. Should documentation use CC BY 4.0 or CC BY-SA 4.0?
3. Which data should use CC0, ODC-By, ODbL, restricted access, or another rights framework?
4. How should third-party content, scholarly articles, and research datasets be handled?
5. Is a DCO sufficient for early contributions, or is a CLA needed for particular classes of contribution?
6. How should employer-owned and contractor-created contributions be handled?
7. How can open-source software be combined with service-level safety and acceptable-use policies without misrepresenting what the license can control?
8. What protections can be offered for contributors whose work is used in ways they oppose?
9. How should trademarks and project identity be stewarded separately from software rights?
10. What happens to licensing and contributor rights during a merger, fiscal-host transition, or dissolution?

## Sources

See the November 2026 source register, entries F-14 onward.

## Change log

- **2026-11-26:** Added analysis of software, documentation, data/database licensing, DCO/CLA approaches, contributor agency, and the tension between open-source licensing and field-of-use restrictions.
