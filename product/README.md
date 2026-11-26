# Product Development

**Status:** Working prototype direction established; initial static-inspection slice implemented.  
**Started:** 26 November 2026

This directory is the working home for Common Knowledge's first product. It is intentionally separate from the wider institutional roadmap: the first product should demonstrate useful capability without pretending to be the whole commons.

## Working direction

Build a **local-first research project preflight and handoff tool**. Its initial job is to help someone understand whether a computational research project is ready to be inspected, handed to a collaborator, or reused—and to give them concrete, evidence-linked next steps when it is not.

The first target to investigate is a computational Python project. The first prototype should inspect files and declared configuration without executing project code.

This is the direction for the first prototype, not an irrevocable product commitment. We will change or abandon it if hands-on comparison and user evidence show that existing tools already solve the problem well or that the problem is not important to users.

## Product documents

- [Product direction and initial user promise](PRODUCT_DIRECTION.md)
- [Experience principles and visual identity](EXPERIENCE_AND_VISUAL_IDENTITY.md)
- [Prototype plan and acceptance gates](PROTOTYPE_PLAN.md)
- [Prototype status and run instructions](PROTOTYPE_STATUS.md)

## Current status

- [x] Select a working direction for the first prototype.
- [x] Define a narrow initial user and task hypothesis.
- [x] Establish experience and visual-design principles.
- [x] Create a synthetic research project fixture with known conditions.
- [x] Implement an initial static-inspection slice and HTML/JSON report.
- [ ] Execute the automated test suite in a clean environment.
- [ ] Test relevant existing tools against the same fixture.
- [ ] Test with people who did not build it.
- [ ] Decide whether to continue, narrow, integrate upstream, or stop.

## Product integrity

The tool must not imply that project organization, metadata completeness, successful execution, or a clean report proves that research is scientifically valid. It should report observable conditions, evidence, uncertainty, and limitations. It must not execute a project's code in the initial prototype.

No software, documentation, data, or contributor license is selected by this document. Licensing decisions remain separate and require an explicit project decision.
