# Project Profile: Open Science Framework (OSF)

- **Snapshot:** 2026-11
- **Profile last verified:** 2026-11-26
- **Official website:** https://osf.io/
- **Operator:** Center for Open Science (COS), a nonprofit organization
- **Status:** Active platform undergoing a major product transition
- **Confidence:** High for the documented transition direction; medium for long-term outcomes, sustainability, and user impact

## Overview

The Open Science Framework (OSF) is an open-source platform operated by the Center for Open Science. Its current stated role is to help researchers create and connect transparent research records, including registrations and preprints, and link those records to related data, code, materials, publications, and other outputs hosted in OSF or external systems.

Historically, OSF Projects also served as general project collaboration, file-management, and data-storage spaces. This role is changing materially during the November 2026–February 2027 transition.

## Purpose and users

- **Intended problem:** Make research plans and outputs more transparent, discoverable, and connected.
- **Intended users:** Researchers, research communities, and institutions supporting open research.
- **Main use cases:** Study registration and preregistration; community-run preprint services; linking plans, outputs, and outcomes; discovery of connected research records.

## What it provides

According to current COS product and support documentation:
- Researchers can create registrations that provide a citable record of study plans.
- Research communities can operate preprint services using OSF infrastructure.
- Research records can link to data, materials, code, publications, and other outputs hosted in other repositories or systems.
- OSF provides search and discovery across public records and connected outputs.

**Important transition:** COS states that OSF will no longer function as a general project collaboration, data repository, or file-management space. The product is being refocused on registrations, preprints, and connections between research plans and outputs. COS's transition FAQ reports that the transition is taking place across November 2026 to February 2027; it also describes restrictions on creating new projects and components beginning 16 November 2026.

### Transition details verified 26 November 2026

- **16 November 2026:** OSF stopped allowing creation of new Projects and child Components through the interface or API. Existing Projects remain editable until the next transition date.
- **19 February 2027:** Existing public and private Projects are scheduled to become read-only. No further content or metadata changes will be possible through the Project workflow.
- **Public Projects:** COS says public Projects will remain findable, viewable, downloadable, and accessible at their existing URLs and DOIs, with COS continuing to manage storage and preservation.
- **Private Projects:** Current COS help guidance says private Projects will remain accessible after the transition to users who already have access on 19 February 2027. COS anticipates that private Projects may be removed in the future and targets at least 12 months' advance notice. Users cannot add new contributors after the read-only transition.
- **Registrations and Preprints:** These workflows are unaffected and continue to operate.
- **API:** Project-creation POST endpoints were disabled on 16 November 2026; project write/update APIs are scheduled to stop on 19 February 2027. Registry and Preprint APIs continue.
- **Product direction:** COS describes a more focused role for OSF around study plans, registrations, community-run Preprints, and links to outputs held in complementary services such as Zenodo.

**Source discrepancy:** Nature's 9 September 2026 report described a plan under which existing private files would be made public unless users removed them or made them public themselves. The later current COS transition FAQ and help guide say private Projects will remain private and accessible to existing authorized users after 19 February 2027, while future removal remains possible with advance notice. This profile follows the more recent, specific official COS guidance for the current policy and preserves the earlier report as historical evidence. Users should still check the live help pages for updates.

Researchers should consult current official transition guidance before relying on older tutorials or institutional guides.

## Technical design

- **Architecture:** Web-based open-source platform and shared infrastructure operated by COS.
- **Integrations:** Links research records to outputs hosted in external repositories and services; supports community-run preprint services.
- **Workflow:** Prospective study plans and registrations can be connected to outputs and reported outcomes.
- **Deployment:** Hosted service. Independent deployment and operational requirements were not assessed in this profile.
- **Interoperability:** Linking to external research outputs is central to the current product direction. The completeness and practical portability of these links require further investigation.

## Maturity and evidence of operation

OSF is an established platform with a long history of use. COS documentation describes current and planned functionality. Nature's 2026 reporting describes the platform's scale and the financial pressures behind the product transition.

This profile does not independently audit current uptime, security, source-code quality, accessibility, data export, or the completeness of migration arrangements.

## Openness

- **Source:** COS describes OSF as open source. The exact current license and repository state should be verified directly before reuse or deployment.
- **Research records:** Public registrations and preprints are central to the service's purpose.
- **Data:** OSF's role as a general data repository is being phased out; users should not assume that it remains suitable for new data storage.
- **Methods:** Registrations make planned methods and analyses more visible.
- **Interoperability:** The current direction emphasizes linking to external repositories and systems.
- **Portability:** Migration and export options, including the treatment of legacy project data, require detailed review.

## Governance and economics

- **Operator:** Center for Open Science, described in its support documentation as a nonprofit.
- **Funding and sustainability:** COS states that maintaining the broad OSF Projects scope would require approximately US$4–5 million per year for the next several years. It cites a combination of grant-funding challenges, increased activity-related costs, cloud services, security, integrations, software development, and accumulated technical debt. Nature's 9 September 2026 reporting also describes funding pressures and user impact. These are operator and journalism sources, not an independent financial audit.
- **Governance:** The organization's full governance structure and decision-making processes were not reviewed for this profile.
- **Contributor rights:** Not assessed in detail.
- **Continuity:** The 2026 transition demonstrates that a widely used research service can change scope when operating costs and funding become difficult to sustain.

## Strengths

- Established and recognizable infrastructure for registrations and preprints.
- Supports connections between research plans and outputs hosted in different systems.
- Provides a public record that can make research plans more transparent.
- Its transition is being documented by the operator, including user guidance and explanations.

## Limitations and risks

- It is no longer appropriate to describe OSF as a stable all-in-one project-management, collaboration, and data-storage service for new work.
- The transition creates migration and continuity questions for existing users and institutions.
- Private-project access and possible future removal require attention; users should not assume that read-only means permanently retained.
- API-dependent workflows need migration because project creation and write endpoints are being retired.
- Reliance on a central operator and external funding creates service-continuity risks.
- Linking outputs across services does not automatically guarantee that those outputs remain available, interoperable, or reproducible.
- The long-term effects of the transition on researchers and the wider open-science ecosystem are not yet established.

## Relevance to Common Knowledge

OSF is an important example of shared research infrastructure and a useful case study for:
- Connecting study plans to outputs across specialized repositories.
- Separating the functions of registration, preprints, project collaboration, and data preservation.
- The operational and financial burden of maintaining free-to-use research infrastructure.
- Migration, user trust, and continuity when a platform changes its scope.

It should not be treated as a simple template for Common Knowledge or as evidence that a new unified platform is needed. A more useful next step is to study which OSF functions researchers still need, where they will move, and how the new OSF role connects with other services.

## Assessment

**Documented fact:** COS is narrowing OSF's role during a transition beginning in November 2026, focusing on registrations, preprints, and linking research outputs.

**Assessment:** The transition reinforces the importance of modular infrastructure and sustainable operating models. It also creates a live opportunity to understand the practical costs of migration and the consequences of relying on a centralized service.

**Open questions:** What proportion of active users depend on each legacy feature? What migration paths and data exports are available? How will institutions adapt? What will be the effect on independent researchers and communities with limited infrastructure support? How will the refocused service be funded over time?

## Sources

- A-01 — COS, [The Open Science Framework](https://www.cos.io/products/osf).
- A-02 — COS Support, [OSF Projects Transition FAQs](https://help.osf.io/article/725-faqs).
- A-03 — COS, [OSF Product Roadmap](https://www.cos.io/product-roadmap?hsLang=en).
- A-04 — Nature, [Popular open-science platform to stop hosting data and code amid funding concerns](https://www.nature.com/articles/d41586-026-02598-y).
- A-05 — KU Leuven Research Data Management, [Open Science Framework](https://www.kuleuven.be/rdm/en/tools/osf).
- A-65 — COS, [OSF Changes](https://www.cos.io/osf-changes).
- A-66 — COS Support, [OSF Projects Transition](https://help.osf.io/article/727-osf-projects-transition).
- A-67 — COS Support, [OSF Projects Transition FAQs](https://help.osf.io/article/725-faqs).
- A-68 — COS Support, [OSF Projects API Impact](https://help.osf.io/article/744-osf-projects-api-impact).

## Change log

- **2026-11-26:** Created initial profile reflecting the OSF transition documented by COS in November 2026.
- **2026-11-26:** Expanded the profile with the exact November 2026–February 2027 transition timeline, API changes, public/private content distinctions, current funding rationale, and a documented discrepancy between earlier journalism and later official guidance. Added sources A-65 through A-68.
