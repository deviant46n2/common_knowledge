# Consilience template mapping — civic budget claim stress test

- **Date:** 26 November 2026
- **Status:** Conceptual mapping of a fictional civic claim to public Consilience nanopublication templates
- **Templates inspected:** theory claim, measured claim, data-quality finding, disagreement, claim correspondence
- **No nanopublications were created or published.**

## Purpose

Test whether the public Consilience claim-card and disagreement templates are genuinely limited to scientific papers or can serve as a starting point for a quantitative public-policy claim.

## Fictional case

County X's total appropriations rise from $100 million in FY2024 to $105 million in FY2025. A price index rises from 100 to 107.14 over the same period.

- Nominal appropriations increase by 5%.
- Inflation-adjusted appropriations decrease by approximately 2%.
- The statements are compatible because they refer to different measurement bases.

## Mapping

| Common Knowledge concept | Consilience template | Candidate fields / fit |
|---|---|---|
| Claim A: nominal appropriations rose 5% | Measured claim card | Exact source sentence; source document; subject = County X total appropriations; quantity/value = 105 million; unit = USD; axis = nominal appropriations; condition = FY2025 |
| Claim B: real appropriations fell 2% | Measured claim card | Subject = same appropriations series; quantity/value = 98 million in FY2024 dollars; unit = USD; axis = real appropriations; conditions include base year and price index; calculation provenance must be linked separately |
| Source data quality | Data-quality finding | Check run, records checked, records flagged, finding and dataset attribution |
| Claims A and B differ | Disagreement template or comparison-refused template | The disagreement template expects different values on the same dimension; here the dimensions are different (nominal vs real), so forcing a disagreement would be misleading |
| Claims A and B are related but not equivalent | Claim-correspondence template | Four-rung correspondence grade and explicit ceiling on what the grade licenses; potentially useful if the relation is carefully defined |
| Scope of a broader statement "the budget increased" | Theory claim or measured claim with conditions | The existing templates provide claim kind, axis, subject, conditions, and source location, but do not obviously provide a complete general scope model for jurisdiction, fiscal period, budget definition, and comparison basis |

## What the templates already solve

The public measured-claim template is more developed than a generic claim record. Its description specifies:
- an exact source sentence;
- a source document;
- a subject;
- a quantity on an axis;
- a QUDT numeric value and unit;
- a bound and the unit as written;
- conditions under which the sentence was reported;
- a stable claim IRI that can remain the same when a corrected card supersedes the previous one.

The disagreement template is also unusually specific. It asks for the dimension of disagreement, observable, instrument/technique, testability status, reason, assumption, margin, floor, and unit. The correspondence template uses a four-rung ladder and explicitly records what the grade does not license.

These are not hypothetical ideas; they are fields in public, published templates.

## What remains awkward for civic use

1. **Domain-specific dimensions:** "axis" and "claim kind" are flexible, but the template's current vocabulary is designed around scientific measurements. Public budgets need clear dimensions such as nominal/real, appropriations/expenditures, per-capita/total, jurisdiction, fiscal year, and price-index base year.
2. **Different dimensions are not necessarily disagreements:** the disagreement template is for claims that take different values on the same dimension. A nominal increase and real decrease should be represented as compatible statements with different bases, not as a disagreement.
3. **Source anchoring:** exact source sentence plus document is valuable, and the theory claim template includes document and page. The measured-claim description does not clearly specify a durable sentence selector, source-version identifier, or content hash. These should be tested in the actual form and RDF.
4. **Derived calculations:** the real-terms claim is derived from two source datasets and a formula. The claim card alone is not the calculation provenance; a separate activity/evidence record is needed.
5. **Ambiguity:** the broad statement "the budget increased" is not false, but it is underspecified. The templates do not appear to have a standard "insufficient scope" assessment status; this may need a new template or relation.
6. **Assessment authority:** the templates encode claim content and structured comparisons, but they do not by themselves establish who is qualified to assess a civic claim or how competing assessments should be reviewed.

## Result

The Consilience templates already solve several problems that we had independently identified:
- claim identity and correction;
- exact source sentence and source document;
- structured quantities, units, bounds, and conditions;
- disagreement dimensions and testability;
- graded correspondence and explicit limits on comparisons;
- data-quality findings.

This significantly narrows the amount of new modeling Common Knowledge may need. The main open questions are domain generalization, robust source-version/selector handling, derived-calculation provenance, and accessible public presentation.

## Recommendation

Do not create a competing generic claim-card vocabulary before asking the Consilience maintainers:
- whether the templates are intended to generalize beyond scientific literature;
- whether the vocabulary is stable and licensed for reuse;
- how source sentence/document/page anchors are represented in RDF;
- how corrected cards, conflicting assessments, and insufficiently scoped claims are handled;
- whether a civic-budget example would be a welcome interoperability test.

A Common Knowledge application could potentially reuse the claim-card and comparison pattern while adding public-policy scope, source anchoring, and a reader-facing explanation layer.
