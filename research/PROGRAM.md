# Common Knowledge Research Program

**Status:** Active, focused research  
**Current focus:** Evidence-linked knowledge records and the systems that already support them  
**Method:** [Research methodology](methodology.md)

## Purpose

Research exists to make concrete product and engineering decisions better. It should help us understand what already works, what people still struggle with, which standards can be reused, and whether Common Knowledge has a worthwhile contribution to make.

This is not an attempt to map every adjacent field before building anything. Research should be bounded, source-based, and capable of changing the product direction.

## Current research questions

1. How do existing systems represent statements, sources, evidence, provenance, uncertainty, disagreement, and revision history?
2. Which open standards and data formats allow records to move between tools?
3. Which parts of the candidate workflow are already well served, and where do users encounter real friction?
4. What is the smallest useful end-to-end demonstrator that can test a meaningful gap?
5. What rights, privacy, safety, and stewardship constraints affect the records and evidence?

The first research cycle is documented in [Focused Research](FOCUSED_RESEARCH.md).

## Current priorities

### 1. Knowledge representation and evidence relationships

Investigate practical models for statements, claims, observations, source documents, evidence excerpts, assessments, qualifiers, and typed relationships such as supports, contradicts, qualifies, or derives from.

Do not assume every useful record is a binary claim or that one universal ontology is achievable or desirable.

### 2. Provenance, attribution, and history

Investigate how to identify who or what contributed information, how a record was derived or transformed, how versions are preserved, and how corrections can be inspected without erasing prior history.

### 3. Existing platforms and implementation choices

Compare a small number of real systems. Prioritize primary documentation, source code, export formats, and hands-on tests. Look for opportunities to extend or interoperate with existing projects rather than duplicate them.

### 4. People and actual workflows

As soon as a concrete workflow can be shown, speak with people who create, curate, verify, maintain, or rely on structured knowledge. Ask about current tasks, workarounds, failure cases, and what they would need to trust or reuse a record. Do not treat enthusiasm for the mission as product validation.

### 5. Rights, safety, and access

Identify the minimum requirements for attribution, licensing, privacy, consent, sensitive information, community-governed knowledge, and restricted access. Openness is a default, not an override of people's rights.

## Background research

The November 2026 snapshot and its seven workstreams remain useful background material. They are not seven equal active priorities. Use them selectively when a concrete product or technical question calls for deeper investigation.

## Research practice

- Prefer primary specifications, official documentation, source repositories, and published evaluations.
- Record exact sources, versions, dates, and the claims they support.
- Separate documented facts, observed behavior, interpretation, hypotheses, and recommendations.
- Test software where practical; a feature page is not proof of operational behavior.
- State what was not examined and where coverage is weak.
- Include critical evidence and existing solutions that weaken a preferred idea.
- Do not claim interviews, independent review, or user validation that have not occurred.
- Keep research notes concise enough to inform a decision.

## Decision rule

If an existing project already solves the need, consider using it, extending it, or contributing upstream. Build new infrastructure only where a real user need and a meaningful gap are demonstrated.
