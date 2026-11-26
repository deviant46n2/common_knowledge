# Roadmap

This roadmap is a practical sequence, not a promise to build every part of the long-term vision. The immediate goal is a demonstrable piece of software that makes the Common Knowledge idea tangible.

## Current direction

Build an **inspectable, evidence-linked knowledge system**, beginning with one small, complete, useful slice.

The first slice should let someone create or inspect a structured knowledge record and understand:
- exactly what is being stated, including scope and context;
- which sources or observations support, challenge, or qualify it;
- who or what contributed the record and how;
- what is known, uncertain, disputed, or not yet checked;
- how the record and its evidence have changed over time;
- how the information can be exported and independently inspected.

This is a product hypothesis, not a settled data model or architecture. Research must determine what existing systems already provide and where a new contribution would be justified.

## Near-term sequence

### 1. Focused research — current priority

Investigate the smallest set of standards, tools, and real workflows needed to make a defensible first product decision.

- Compare existing knowledge bases and structured statement systems.
- Examine how they represent sources, evidence, provenance, disagreement, versions, and corrections.
- Identify relevant open standards and practical implementation libraries.
- Look for real user problems that are not already adequately served.
- Talk to people who curate, verify, publish, or rely on knowledge records as soon as there is a concrete workflow to discuss.

**Output:** a short comparison, an initial record-model proposal, and a clearly stated gap—or a recommendation to build on an existing system.

### 2. Build one vertical slice

Implement the smallest end-to-end workflow that tests the chosen gap. A possible shape is one bounded collection of knowledge records with a human-readable view, structured evidence links, visible history, and portable machine-readable export.

Do not build a universal knowledge graph, global search engine, social network, AI agent platform, distributed database, or governance system as a prerequisite.

**Output:** a working demonstrator with example records, tests, documentation, and explicit limitations.

### 3. Test with people outside the project

Ask people to use the demonstrator without coaching. Observe whether they can understand a record, trace its evidence, recognize uncertainty, identify changes, and export or reuse the information.

Compare it with their current tools and workflows. Record confusion, missing features, and negative feedback. Mission enthusiasm is not evidence of product usefulness.

**Output:** an independent evaluation and a decision to continue, narrow, integrate upstream, or stop.

### 4. Invite contributors around something real

Once the software demonstrates practical value, invite domain experts, researchers, developers, librarians, archivists, and other interested people to inspect and improve it.

Keep contribution rights and expectations clear. Develop community processes with the people who arrive rather than designing a detailed governance constitution in advance.

### 5. Grow the commons in response to demonstrated needs

Only as real use requires it, develop broader capabilities for federation, preservation, multilingual access, AI collaboration, community stewardship, and institutional continuity.

The long-term system should not depend on one company, model, database, institution, or founder. That is a design goal to test incrementally, not an excuse to overbuild the first version.

## Working rules

- Build on existing standards and infrastructure wherever practical.
- Distinguish evidence from interpretation and source claims.
- Never equate a confidence label or community vote with truth.
- Preserve disagreement and correction history.
- Treat privacy, consent, safety, rights, and community control as design constraints.
- Prefer reversible experiments and small working demonstrations.
- Keep documentation proportional to what people need to build, use, review, or contribute.

## Not current priorities

A public marketing website, formal institutional governance, a universal ontology, a global data-ingestion pipeline, distributed compute, and a large-scale AI research system are not prerequisites for the first demonstrator.
