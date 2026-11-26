# MVP Research

- **Established:** 26 November 2026
- **Status:** Active investigation
- **Purpose:** Identify the strongest feasible first product through evidence about user problems, existing tools, technical gaps, and demonstrable value.
- **Parent brief:** [MVP Discovery](../MVP_DISCOVERY.md)
- **Roadmap:** [Project roadmap](../../ROADMAP.md)

## Research principles

1. Investigate user problems, not just interesting technologies.
2. Compare actual capabilities and workflows, not marketing descriptions alone.
3. Prefer primary documentation, source code, papers, release records, and direct tests.
4. Record existing solutions even when they weaken a preferred idea.
5. Distinguish demonstrated capabilities from advertised or planned capabilities.
6. Treat candidate assessments as provisional; explain uncertainty.
7. Do not claim user validation until conversations or observed tests have occurred.
8. Prefer integration and standards reuse over creating competing formats or platforms.
9. Preserve dated findings and decision history.
10. Converge toward a product brief and testable MVP, not an exhaustive encyclopedia.

## Current documents

- [Candidate landscape and initial comparison](candidate-landscape.md)
- [Technical opportunities and integration hypotheses](technical-opportunities.md)
- [Direct competitor source review](direct-competitors.md)
- [Claim verification and research-agent ecosystem](claim-verification-ecosystem.md)
- [Hands-on experiments and user discovery plan](discovery-experiments.md)
- [Development documentation and source-of-truth policy](../../docs/development/README.md)

## Current preliminary conclusion

The broad research workspace, generic research package generator, and generic software-metadata generator spaces are already populated by mature platforms, standards, and specialist tools. A basic RO-Crate generator or CodeMeta/CITATION.cff helper is not a defensible product proposition by itself.

Three related areas now warrant deeper investigation:

1. **Research handoff and reproducibility diagnostics:** help a researcher or research software engineer identify and fix practical gaps that make a project difficult for another person to understand, inspect, run where possible, cite, or preserve. This must offer more than a checklist or metadata generator.
2. **Research-specific auditability for AI-assisted work:** connect agent/LLM execution traces to research inputs, code, datasets, outputs, decisions, and claims in a portable, reviewable record. Generic AI observability is mature; the potential gap is research-specific provenance and evidence linkage.
3. **Claim-to-evidence verification:** conservatively trace numerical statements in a manuscript or report to the specific output, metric, experiment, and run that supports them, with human review for ambiguous or unsupported cases. A recent benchmark-specific checker demonstrates the feasibility of a narrow version; any Common Knowledge implementation would need a broader, interoperable input contract and must avoid duplicating existing work.

A major new finding is that **ReCRATE** is an active MIT-licensed proof of concept that already combines RO-Crate, workflow execution, result comparison, domain-specific input checks, and append-only Workflow Run Crates. **Paper2Agent** has also been evaluated at scale and published in Nature. These projects substantially raise the bar for any overlapping product. We should investigate integration, contribution, and interoperability before considering a competing implementation.

The OSF Projects transition creates a real but time-bounded migration need for some active projects. It is not currently a strong core-product candidate: OSF provides export guidance, says completed public projects generally need no action, and is developing additional API-based export tools.

No MVP has been selected. The first comparison has now identified substantial existing products in all three areas, including several stable claim-verification and research-agent tools. The next cycle should focus less on adding more names to the landscape and more on hands-on interoperability tests, user workflow evidence, and whether a genuinely unmet integration problem exists.

## Change log

- **2026-11-26:** Established MVP-specific research area and recorded first-pass competitor and opportunity findings. Conclusions remain provisional.
