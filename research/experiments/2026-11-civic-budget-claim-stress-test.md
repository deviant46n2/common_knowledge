# Civic budget claim stress test — scope, comparability, and assessment

- **Date:** 26 November 2026
- **Status:** Fictional conceptual test; no real government claim or budget data
- **Purpose:** Test whether candidate record models can preserve scope and explain apparent disagreement in a public-policy claim.

## Fictional case

County X has the following fictional budget figures:

| Measure | FY2024 | FY2025 |
|---|---:|---:|
| Total nominal appropriations | $100 million | $105 million |
| Price index (FY2024 = 100) | 100.00 | 107.14 |

Two statements are made:

- **Claim A:** "County X's total appropriations increased by 5% in FY2025 compared with FY2024."
- **Claim B:** "County X's total appropriations decreased by 2% in real terms in FY2025 compared with FY2024."

Both are correct under their stated measurement bases:
- Nominal change: `(105 / 100) - 1 = +5%`.
- Real change: `(105 / 100) / (107.14 / 100) - 1 ≈ -2%`.

The claims are not contradictory. They describe the same budget using different bases. A third statement—"The budget increased"—is ambiguous until the speaker defines whether they mean nominal or inflation-adjusted appropriations, actual expenditures, per-capita spending, or a particular program.

All figures and entities are fictional. This test is about representation, not a factual claim about a real jurisdiction.

## Why this is a useful test

A simplistic claim database might store two sentences and label them as contradictory. A careful knowledge system needs to preserve:
- the metric being compared (appropriations, not expenditures);
- jurisdiction (County X);
- fiscal period (FY2024 to FY2025);
- unit and currency;
- nominal versus real basis;
- price index and reference year;
- calculation method;
- source versions and exact table rows;
- the distinction between an ambiguous statement and a false one.

This is a common pattern in public debate: two statements can be individually correct but not comparable, or a broad statement can omit the definition that makes it interpretable.

## Candidate record structure

### Claims

- **C1:** Total nominal appropriations rose 5% from FY2024 to FY2025.
- **C2:** Total real appropriations fell approximately 2% over the same period, using the stated price index.
- **C3:** "County X's budget increased" — ambiguous without a metric and adjustment basis.

### Evidence

- **E1:** The adopted budget table provides FY2024 and FY2025 total appropriations.
- **E2:** The price-index dataset provides the FY2024 and FY2025 index values.
- **E3:** A reproducible calculation activity derives the real-terms comparison from E1 and E2.

### Assessment

- **A1:** C1 and C2 are compatible because they use different adjustment bases.
- **A2:** C3 is underspecified and cannot be assessed until its metric, period, and basis are defined.
- The assessment records its method, formula, assumptions, author/reviewer, evidence, date, and limitations.

## Mapping to existing systems

| System | What it can represent now | What is missing or awkward |
|---|---|---|
| Wikibase | Statements with qualifiers for time, unit, and context; references can store source metadata; ranks can distinguish statement status | A complete multi-claim comparison/assessment workflow is not native; exact evidence-row anchors need a convention or linked entities; ranks are not evidence quality |
| MIRA | Questions, claims, evidence, studies, protocols, support/opposition, and source documents | No first-class claim-scope dimensions, adjustment basis, assessment/review object, or explicit compatibility/qualification relation in the current schema |
| Nanopublications / Knowledge Space | Each claim, evidence record, calculation, and assessment can be a separate signed, citable contribution with provenance | The vocabulary and reader-facing comparison semantics need to be agreed; publication format alone does not tell readers whether claims are compatible |
| SciOS Git-based graph | Separate claim/evidence/source nodes, counterclaims, methods, and pull-request review | The sample schema has no structured scope fields or source selectors; prose can explain the basis but is harder to query consistently |
| SciOS RRGI | Live graph types include claims, evidence, questions, sources, and typed relations; public graph supports extension | The public API/schema details and civic-domain suitability need direct confirmation |
| ORKG | Structured numeric comparisons, methods, results, and tabular views across research papers | Designed for scholarly research contributions, not general public claims and contested civic statements |

## Design lessons

1. **A claim is not just a sentence.** It needs enough scope to identify what is being asserted, about whom/what, where, when, and under which definitions.
2. **Comparability is a separate question from truth.** Two claims may be compatible, contradictory, overlapping, or not comparable. These relationships should not be collapsed into a single true/false verdict.
3. **Ambiguity is not falsity.** An underspecified statement should be marked as underspecified, with the missing scope made visible.
4. **Assessments need their own provenance.** The calculation, reviewer, method, evidence set, and limitations are part of the assessment record.
5. **The source evidence must be inspectable.** A reader should be able to open the budget table and the price-index rows used in the calculation, not merely see a bibliography.
6. **The UI should explain why claims differ.** A useful public interface should show "nominal" versus "real" next to the numbers and explain that both statements can be correct.

## Current conclusion

This case is a better test of Common Knowledge's intended civic usefulness than a binary fact-checking example. It suggests that a distinctive contribution may lie in the accessible representation of claim scope, comparability, evidence, and independent assessment—while reusing existing graph and publication infrastructure.

This is a hypothesis only. The next validation should involve real public-budget documents and users who work with public finance, journalism, or civic accountability.
