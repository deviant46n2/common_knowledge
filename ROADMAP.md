# Roadmap

This roadmap describes how Common Knowledge will move from its founding idea to a useful, independently testable product and, only then, toward a wider commons. It is a sequence of evidence and working outcomes, not a fixed schedule or a promise to build every capability listed here.

The near-term priority has changed: **Common Knowledge should demonstrate practical value before asking people to commit substantial time to the project.** We will continue researching, but research should now be focused on selecting and building a useful MVP rather than completing an exhaustive survey of the field.

The product-discovery work is recorded in [MVP Discovery](research/MVP_DISCOVERY.md). The wider evidence base remains in the [seven-workstream research program](research/PROGRAM.md) and [November 2026 field snapshot](research/snapshots/2026-11/README.md).

## How to read this roadmap

- **Useful product before recruitment:** invite people to try and improve something real, not merely join an ambitious idea.
- **Evidence before commitment:** product candidates are hypotheses until existing tools and real user workflows have been examined.
- **Build only what is missing:** reuse mature projects, standards, and infrastructure wherever they serve the need.
- **Standalone value:** the first product should be useful without a Common Knowledge network or community already existing.
- **Trust and portability:** make outputs inspectable and exportable; do not create unnecessary lock-in.
- **People before scale:** learn from users and maintainers before expanding infrastructure.
- **Revisit openly:** update the roadmap when evidence, collaborators, or practical constraints warrant it.

## Phase 1 — Discover a real problem and select the MVP

**Current priority**

Identify a specific problem experienced by a reachable group of people, determine why existing tools do not adequately solve it, and define a small product that Common Knowledge can credibly build.

Work includes:

- Compare real workflows and capabilities of existing research tools, not just their feature lists.
- Prioritize the parts of Workstreams A, C, and E that inform interoperability, reproducibility, and preservation for candidate products.
- Investigate B or D only where distributed infrastructure or AI materially affects the chosen problem.
- Speak with independent researchers, research software engineers, students, librarians, data stewards, and maintainers.
- Seek concrete examples, workarounds, failures, and criticisms; do not treat enthusiasm for the mission as evidence of product demand.
- Define a target user, job, scope, non-goals, success measures, risks, and existing components to reuse.

**Outputs**

- A documented comparison of leading product candidates and existing alternatives.
- Evidence from real user workflows and problem-discovery conversations.
- A one-page MVP product brief.
- A documented selection decision and explicit reasons for rejecting alternatives.

**Move forward when:** one bounded problem is sufficiently validated, the proposed solution offers a meaningful gap over existing tools, and a small team can build and test it.

## Phase 2 — Build a useful vertical slice

Build the smallest complete version of the selected product that delivers a useful result from beginning to end.

Work includes:

- Prefer local-first operation and established, interoperable formats where appropriate.
- Reuse existing open-source libraries, services, and standards rather than recreating them.
- Keep the first workflow narrow and understandable.
- Include installation instructions, sample material, automated tests, a working demonstration, and clear limitations.
- Protect sensitive data and respect rights, consent, and community control.
- Avoid building accounts, hosting, distributed compute, social features, or a universal platform unless the validated use case requires them.

**Outputs**

- A working MVP that an external person can install or use.
- A reproducible demonstration using representative examples.
- Tests, documentation, and an honest account of limitations and failure modes.
- A public issue tracker with specific, actionable improvement opportunities.

**Move forward when:** the core workflow works reliably enough for external evaluation and the product delivers a useful result without requiring the future Common Knowledge ecosystem.

## Phase 3 — Validate with independent users

A successful demonstration is not proof of a useful product. People outside the founding effort must be able to evaluate it.

Work includes:

- Observe first-time users installing and completing the core task.
- Measure time to first useful result, failure rates, setup burden, and output accuracy.
- Ask whether the result is genuinely useful, trustworthy, and worth using again.
- Compare against the user's existing workflow and tools.
- Test export, portability, and independent inspection.
- Record negative results and revise or abandon the product hypothesis if evidence warrants it.

**Outputs**

- An independent usability and technical evaluation.
- A prioritized list of improvements and unresolved risks.
- A revised product scope based on evidence.
- A clear public demonstration and case study, with participant permission where needed.

**Move forward when:** people outside Common Knowledge can use the product, understand its limits, and identify concrete value over their previous workflow.

## Phase 4 — Attract contributors around demonstrated value

Once there is something useful to inspect and try, invite people to help improve it.

Work includes:

- Publish contributor guidance and specific starter tasks.
- Invite independent technical and domain review.
- Welcome bug reports, integrations, documentation, accessibility work, testing, and security review.
- Make contribution expectations, attribution, licensing, and decision processes clear.
- Seek maintainers and community-facing collaborators so the founder does not become a permanent bottleneck or public representative.
- Continue user discovery as the product evolves.

**Outputs**

- A small, active group of users and contributors.
- A contribution process with clear rights and responsibilities.
- Independent review and a visible record of product changes.
- A realistic maintenance and support plan.

**Move forward when:** the product has demonstrated repeat use and a contributor group can improve and maintain it without relying entirely on the founder.

## Phase 5 — Establish durable stewardship and expand the commons

Develop the broader organizational and technical structures in proportion to demonstrated needs.

Work includes:

- Define transparent decision-making and a path for resolving disagreements.
- Clarify contributor attribution, rights, licensing, and responsibilities.
- Establish research-integrity, review, correction, and appeals processes appropriate to the work.
- Develop data stewardship practices that respect privacy, consent, security, and community rights.
- Make funding, conflicts of interest, compensation, and institutional relationships transparent.
- Design governance to resist capture by any founder, donor, company, government, or political faction.
- Plan for continuity, independent oversight, and succession beyond the founding team.
- Connect additional projects, repositories, tools, datasets, and communities where interoperability solves real problems.
- Explore federated or distributed infrastructure only where it improves resilience, access, or participant control.

These practices should be developed with qualified contributors and, where necessary, professional legal and domain-specific advice. No particular legal form or technical architecture is predetermined.

**Outputs**

- Draft governance and participation policies shaped with contributors.
- Clear licensing, data-handling, funding, and conflict-of-interest practices.
- A continuity and accountability plan.
- A tested path for additional projects and interoperable services.

**Move forward when:** the commons can support multiple useful projects with credible accountability, sustainable maintenance, and distributed stewardship.

## Candidate first product directions

Three connected hypotheses are currently under investigation:

1. A local-first research handoff/readiness tool that helps people prepare existing computational projects for inspection, reuse, and preservation.
2. A research-specific audit layer that connects AI/agent traces to inputs, methods, code, outputs, and human decisions.
3. A claim-to-evidence verifier that checks whether numerical statements in a report correspond to the correct result, metric, experiment, and run.

These are **not selected MVPs**. Existing projects already cover substantial parts of this space, including Renku, Galaxy, Code Ocean, Whole Tale, RO-Crate tooling, Paper2Agent, ReCRATE, and a benchmark-specific numerical claim checker. Common Knowledge should investigate integration and contribution opportunities before considering a competing implementation.

The [MVP Discovery brief](research/MVP_DISCOVERY.md) and [MVP research index](research/mvp/README.md) record the current comparison, direct competitor review, technical hypotheses, and test plan.

## What is deliberately not a first priority

Common Knowledge is not currently committing to:

- Building a universal research platform from scratch.
- Creating a new distributed-computing network before a real workload requires one.
- Replacing universities, journals, libraries, repositories, or existing open-science projects.
- Deploying autonomous AI researchers without clear limits, evaluation, and accountability.
- Building a social network or membership system before there is a useful product.
- Incorporating a particular legal entity before the mission, jurisdiction, and governance needs are understood.
- Scaling membership, infrastructure, fundraising, or public attention as ends in themselves.

## Measures of progress

Progress should be judged by useful outcomes rather than attention or repository activity. Relevant measures include:

- A real user problem documented with concrete examples.
- A defensible gap compared with existing tools.
- Time for a new user to reach a first useful result.
- Successful completion of the core workflow.
- Accuracy and actionability of product outputs.
- Independent use, inspection, export, and verification.
- Repeat use and user-reported value.
- Maintenance burden, security, privacy, and accessibility.
- Contributions accurately attributed and fairly governed.
- Funding and decision-making remaining transparent and resistant to capture.
- The work remaining useful without depending on one founder or institution.

## Long-term direction

The long-term ambition remains a durable, globally accessible commons through which people can contribute to, examine, preserve, and build upon humanity's shared knowledge.

The first product is not the whole commons. It is the first practical proof that Common Knowledge can make something genuinely useful, trustworthy, and open to improvement.

---

This roadmap is a living document. Changes should be explained openly, especially when they alter the project's priorities, commitments, or relationship with its founding principles.
