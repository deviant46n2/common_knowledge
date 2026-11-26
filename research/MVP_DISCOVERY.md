# MVP Discovery Brief

- **Established:** 26 November 2026
- **Status:** Active product-discovery document; hypotheses, not commitments
- **Purpose:** Focus Common Knowledge's research on selecting and building a useful first product that can earn trust and attract collaborators.

## 1. Strategic shift

Common Knowledge should not begin by asking strangers to join an ambitious project that has not yet demonstrated practical value. The first public invitation should be to use, inspect, test, or improve something that already works.

This changes the near-term priority from completing a broad ecosystem survey to **evidence-led MVP discovery and delivery**. The seven research workstreams remain useful, but they should now be investigated selectively according to whether they help us:

1. identify a specific, consequential user problem;
2. establish that existing tools do not already solve it adequately;
3. define a small product that can solve part of it independently;
4. build and evaluate that product with the resources available;
5. make the result credible, safe, portable, and maintainable.

Research should continue alongside development. It should not become an indefinite gate that delays a useful prototype.

## 2. What the MVP must prove

The MVP is not a miniature version of the eventual global commons. It is a working product that demonstrates one useful capability and provides a credible foundation for further work.

Minimum requirements:

- **Standalone utility:** a person can use it without joining a network, contributing compute, or believing in the wider mission.
- **Real user and task:** the product serves an identifiable person doing a real job.
- **Demonstrable outcome:** a user can see what it did and judge whether it helped.
- **Low adoption friction:** setup and first success should be achievable by a technically capable newcomer using clear instructions.
- **Evidence and transparency:** methods, limitations, test results, dependencies, and known risks are documented.
- **Portability:** users can export their work and are not trapped in a Common Knowledge service.
- **Proportional scope:** no custom distributed network, universal platform, or elaborate account system unless the chosen problem requires it.
- **Responsible defaults:** protect private, sensitive, restricted, and community-governed material; do not make all research data public by default.

The MVP should be useful before it is popular. It should not depend on network effects to deliver its first unit of value.

## 3. Initial product opportunity space

These are candidates for investigation, not decisions.

| Candidate | Potential user and job | Why it might matter | Main risk / existing alternatives |
|---|---|---|---|
| Research artifact packager and readiness checker | A researcher or research-software engineer wants to make a computational project understandable, portable, and easier to inspect | Could turn a messy project folder or repository into a structured, inspectable research package with an actionable quality report | RO-Crate tools, research templates, Renku, Galaxy, Code Ocean, Whole Tale, and workflow-specific tools already cover parts of this |
| Portable research-project record | A small research team wants a durable record of question, methods, inputs, outputs, contributors, rights, and changes | Could bridge fragmented tools without replacing them | Risk of becoming another project-management template or metadata burden |
| Research workflow / provenance audit | A team wants to understand whether another person can inspect or re-run a computational result | Could expose missing dependencies, undocumented steps, inaccessible inputs, and unverifiable claims | Execution environments are complex; a successful run does not establish scientific validity |
| Federated research discovery | A researcher wants to find related projects and evidence across repositories and disciplines | Strong long-term commons fit | Requires data integration, ranking, rights-aware metadata, and enough indexed content; hard to make compelling as a first product |
| Human–AI research audit trail | A researcher wants transparent records of AI-assisted research | Timely and relevant to Common Knowledge's human–AI goals | Rapidly changing field, substantial privacy and security questions, and risk of overclaiming what logs prove |

### Early hypothesis worth testing

A particularly promising *shape* is a small, local-first tool that examines a computational research project and produces:

1. a human-readable report describing what is present, missing, unclear, or not verifiable;
2. a portable, standards-based package of project metadata and selected artifacts;
3. explicit provenance, rights, access conditions, versions, and limitations where available;
4. actionable recommendations rather than a simplistic reproducibility score.

This could complement existing repositories and workflow systems rather than replace them. It must be tested against existing tools before being selected. In particular, RO-Crate is an established packaging standard, and `ro-crate-py` already provides libraries and CLI functions to create and consume crates. Common Knowledge should reuse standards and mature libraries rather than invent another metadata format.

## 4. What the current evidence says

### Existing infrastructure is substantial

- **Renku** already connects code, data, compute, environments, workflows, and people, including GitHub and external data sources. A general-purpose research workspace would therefore face a mature and ambitious comparator.
- **Galaxy** combines analysis workflows, execution, training, community support, and provenance. Rebuilding its domain-specific capabilities would be wasteful.
- **Code Ocean**, **Whole Tale**, **Binder**, **Nextflow**, **Snakemake**, **DVC**, and other tools cover important pieces of executable research and computational reproducibility.
- **RO-Crate** provides a community-developed way to describe and package research objects. The official tools directory lists libraries, graphical editors, validators, and domain-specific applications. The existence of these tools means “generate an RO-Crate” alone is not a sufficient product proposition.
- **OSF's Projects transition** is a current ecosystem change: new Projects and components stopped being creatable on 16 November 2026, and existing Projects are scheduled to become read-only on 19 February 2027. OSF Registrations and Preprints continue. This creates migration and workflow questions for some users, but Common Knowledge should not assume it should build an OSF replacement.

### Evidence-based implications

1. **Do not build another all-in-one research workspace by default.** Renku and other platforms already pursue this.
2. **Do not mistake a standard for a product.** RO-Crate is useful infrastructure; the user-facing value must be a workflow, integration, explanation, validation, or outcome that is currently difficult.
3. **Do not claim to certify reproducibility.** Distinguish metadata completeness, package validity, accessibility, environment capture, successful re-execution, independent verification, replication, and scientific validity.
4. **Make export and interoperability central.** A tool that helps users leave with a portable record can earn trust without owning their research.
5. **Investigate concrete pain around transitions and fragmented workflows.** OSF's transition is a timely discovery prompt, not proof of demand for a new platform.
6. **Choose a narrow initial research type.** Computational projects are easier to inspect and test with software, but the design must not imply that all valid research is computational or that qualitative and community-led work should be forced into the same template.

## 5. Target users to investigate first

Prioritize people who can both experience the problem directly and evaluate a technical prototype:

- independent researchers and small research groups;
- research software engineers and computational researchers;
- graduate students and early-career researchers;
- research data stewards and librarians;
- maintainers of open scientific workflows and repositories.

Do not treat these groups as interchangeable. A research software engineer may value automation and machine-readable provenance; a researcher may value low-friction setup and a clear report; a data steward may care most about rights, metadata, preservation, and migration.

Initial discovery should seek concrete recent examples, not general approval of Common Knowledge. Ask what the person tried to do, what failed or took too long, what tools they used, what workarounds they adopted, and what they would trust a new tool to handle.

## 6. MVP selection criteria

Score candidates qualitatively against these questions; do not create false precision with a numeric ranking before evidence exists.

- **Pain:** Is the problem frequent, consequential, and currently expensive or frustrating?
- **Reach:** Can we identify real users and a practical way to reach them?
- **Gap:** Is there a demonstrable unmet need after accounting for existing tools?
- **First-use value:** Can a new user get a useful result in one short session?
- **Buildability:** Can a very small team build a credible first version?
- **Testability:** Can success and failure be measured with representative examples?
- **Trust:** Can we make the product safe, transparent, and honest about its limits?
- **Fit:** Does it advance the long-term commons without requiring the entire commons to exist?
- **Maintenance:** Can the product be maintained without unsustainable infrastructure or support costs?

A candidate should not be selected merely because it is technically interesting or aligns elegantly with the long-term vision.

## 7. Proposed discovery and build sequence

### Step 1 — Narrow the landscape research

For each leading candidate:
- inspect primary documentation and live product capabilities;
- install and try the relevant open-source tools where practical;
- compare real user workflows, not only feature lists;
- inspect licenses, maintenance activity, deployment requirements, and exit/export paths;
- identify a specific task that remains difficult.

Prioritize A, C, and E for product-relevant interoperability, reproducibility, and preservation evidence. Use B only where a candidate actually needs distributed infrastructure. Use D where AI is part of the proposed product. Use F to avoid avoidable governance and contributor-rights mistakes. Workstream G supplies direct user evidence throughout.

### Step 2 — Conduct problem discovery

Aim initially for roughly 8–15 focused conversations or equivalent asynchronous exchanges across several roles. This is a planning range, not a representative sample or a quota. Ask participants to walk through real recent workflows and, where possible, show non-sensitive examples. Seek skeptics and people who already use mature alternatives.

No interviews or user validation should be claimed until they have actually occurred.

### Step 3 — Write a one-page product brief

Specify:
- primary user;
- concrete job and current pain;
- existing alternatives and why they are insufficient for this case;
- exact MVP workflow;
- explicit non-goals;
- success measures;
- privacy, rights, and security boundaries;
- what will be reused rather than rebuilt.

### Step 4 — Build a working vertical slice

Deliver one complete path from input to useful output. Prefer local-first operation and established formats where possible. Include sample data, automated tests, installation instructions, a short demonstration, and known limitations.

### Step 5 — Test with people outside the project

A successful demo is not the same as a useful product. Observe whether new users can install it, complete the task, understand the output, trust the boundaries, and decide whether it saves effort. Record failures and revise.

### Step 6 — Invite contributors around demonstrated work

Once the product is usable, publish a clear contribution guide and specific issues. Ask for independent evaluation, bug reports, integrations, documentation, accessibility review, and domain expertise. The invitation should point to something a person can actually try.

## 8. Candidate first demonstration and measures

If the research-packager hypothesis survives comparison and user discovery, a bounded demonstration could use:
- one small, openly licensed computational research repository;
- one messy or incomplete example that exposes real gaps;
- one complete example with documented inputs, code, environment, outputs, and limitations.

Potential measures:
- time to first useful report;
- percentage of findings that users judge accurate and actionable;
- number of false positives and false assurances;
- successful export and independent inspection;
- successful re-execution only where explicitly supported;
- setup failures and support burden;
- user-reported time saved and willingness to use it again.

The tool must never present a green checkmark as proof that research is scientifically correct.

## 9. Immediate research priorities

1. Compare Renku, Galaxy, Code Ocean, Whole Tale, Binder, DVC, workflow systems, and research templates against the candidate user tasks.
2. Test `ro-crate-py`, RO-Crate graphical tools, and validators directly; document what they already do well and what is still missing.
3. Review the OSF transition from the perspective of actual user workflows, without presuming that displaced users need another general-purpose platform.
4. Examine the current research-record proposal and reduce it to fields that are useful, actionable, and proportionate for a first product.
5. Prepare a concise problem-discovery interview script and recruit a small, varied set of willing reviewers when the user is ready to conduct outreach.
6. Select one product hypothesis only after the comparison and user evidence are sufficient.

## 10. Decision rule

**Do not build a platform because Common Knowledge needs a platform. Build a tool because a real person has a real problem that the tool can solve better than the available alternatives.**

The first product is a demonstration of the commons in practice: useful, inspectable, portable, honest about uncertainty, and open to improvement. It is not the final architecture of Common Knowledge.

## Sources and further reading

- [OSF Projects Transition](https://help.osf.io/article/727-osf-projects-transition)
- [OSF transition details](https://help.osf.io/article/759-details-of-osf-projects-transition)
- [OSF guide to choosing a repository](https://help.osf.io/article/735-choosing-a-repository)
- [Renku: What is Renku?](https://docs.renkulab.io/en/0.57.2/introduction/what-is-renku.html)
- [Renku 2.0](https://renkulab.io/)
- [Galaxy project](https://galaxyproject.org/)
- [RO-Crate tools and resources](https://www.researchobject.org/ro-crate/tools.html)
- [RO-Crate specification](https://www.researchobject.org/ro-crate/)
- [ro-crate-py](https://github.com/ResearchObject/ro-crate-py)
- [Recording provenance of workflow runs with RO-Crate (2024)](https://doi.org/10.1371/journal.pone.0309210)
- [Reproducibility of Computational Research Community of Practice resources](https://reproducibility.rcc.uchicago.edu/resources/)
- [Workstream A comparative synthesis](snapshots/2026-11/workstreams/A-open-science/comparative-synthesis.md)
- [Workstream C research-record proposal](snapshots/2026-11/workstreams/C-reproducibility/research-record.md)
- [Workstream C comparative synthesis](snapshots/2026-11/workstreams/C-reproducibility/comparative-synthesis.md)
- [Workstream E comparative synthesis](snapshots/2026-11/workstreams/E-knowledge-preservation/comparative-synthesis.md)

---
*This brief records an initial product-discovery direction as of 26 November 2026. It is not evidence of user validation, a final product choice, or a commitment to a particular architecture.*
