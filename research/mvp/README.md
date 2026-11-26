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
- [Development documentation and source-of-truth policy](../../docs/development/README.md)

## Current preliminary conclusion

The broad research workspace, generic research package generator, and generic software-metadata generator spaces are already populated by mature platforms, standards, and specialist tools. A basic RO-Crate generator or CodeMeta/CITATION.cff helper is not a defensible product proposition by itself.

Two narrower areas warrant deeper investigation:

1. **Research handoff and reproducibility diagnostics:** help a researcher or research software engineer identify and fix practical gaps that make a project difficult for another person to understand, inspect, run where possible, cite, or preserve. This must offer more than a checklist or metadata generator.
2. **Research-specific auditability for AI-assisted work:** connect agent/LLM execution traces to research inputs, code, datasets, outputs, decisions, and claims in a portable, reviewable record. Generic AI observability is mature; the potential gap is research-specific provenance and evidence linkage.

The OSF Projects transition creates a real but time-bounded migration need for some active projects. It is not currently a strong core-product candidate: OSF provides export guidance, says completed public projects generally need no action, and is developing additional API-based export tools.

No MVP has been selected. The next cycle should compare the two leading opportunity areas in more depth, inspect implementations, and seek direct evidence from people doing the work.

## Change log

- **2026-11-26:** Established MVP-specific research area and recorded first-pass competitor and opportunity findings. Conclusions remain provisional.
