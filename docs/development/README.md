# Development Notes

This document is intentionally lightweight while the first product is still being researched.

## Current source of truth

- The running code and tests show what is implemented.
- [Product Direction](../../product/PRODUCT_DIRECTION.md) describes the current product hypothesis, not implemented capability.
- [Prototype Plan](../../product/PROTOTYPE_PLAN.md) describes the next research and build sequence.
- [Prototype Status](../../product/PROTOTYPE_STATUS.md) records the earlier preflight experiment; it is not the current product status.
- [Roadmap](../../ROADMAP.md) records project-level priorities.

When documents conflict, do not silently guess. Identify the conflict and update the relevant document.

## Working habits

- Keep changes small and understandable.
- Inspect existing code and tests before changing behavior.
- Add tests for behavior changes and run them where practical.
- Report exactly what was tested and what was not.
- Prefer established formats and libraries over custom infrastructure.
- Make data flows, permissions, and external services explicit.
- Do not execute untrusted project code or send project data to remote services without a clear need and authorization.
- Keep user data portable and avoid unnecessary collection.
- Preserve meaningful history; explain corrections rather than silently rewriting records.
- Do not choose or change the project's software, data, or contributor licenses without explicit approval.

## Documentation rule

Write documentation when it helps someone build, run, inspect, test, or contribute to the current software. Keep it current and proportional. Do not create empty specifications, requirement catalogs, or architecture documents before there is a real design to describe.

For consequential technical choices, record the problem, alternatives, evidence, decision, and trade-offs in a short decision note. Routine reversible experiments do not need formal records.

## Verification language

Distinguish:
- **Proposed:** an idea being considered.
- **Implemented:** code exists.
- **Tested:** a stated test was run with its result recorded.
- **User-tested:** people outside the building effort tried it.
- **Released:** a version was published for use.

A passing test proves only the behavior it exercises. Do not describe software as validated based only on internal tests or a successful demo.
