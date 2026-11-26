# Experience Principles and Visual Identity

- **Status:** Initial design direction for the prototype
- **Date:** 26 November 2026
- **Purpose:** Establish a coherent product feel before implementation; refine through use and feedback.

## 1. Design character

The product should feel like a **careful research instrument**, not a startup dashboard, compliance portal, or AI chatbot.

Desired qualities:
- Calm and focused.
- Precise without being intimidating.
- Scientifically literate but accessible.
- Transparent about evidence and uncertainty.
- Respectful of the researcher's existing work.
- Useful in a short session, with detail available when needed.

The interface should communicate: "Here is what we observed, here is why it matters, and here is what you can do next."

## 2. Visual direction

### Overall language

Use an editorial, instrument-like interface: strong typography, restrained color, clear hierarchy, generous spacing, and evidence presented as structured records.

Avoid:
- generic SaaS dashboard patterns;
- excessive gradients, glass effects, glowing AI motifs, or decorative animation;
- gamified scores, medals, or simplistic pass/fail ratings;
- dense walls of warnings;
- visual language that suggests the tool can certify scientific truth.

### Color roles

The initial palette should be semantic and restrained:
- **Ink / graphite:** primary text and structure.
- **Warm paper / off-white:** primary reading surface.
- **Muted blue-green / teal:** Common Knowledge's constructive, open, dependable accent.
- **Amber:** caution, incomplete evidence, or an actionable issue.
- **Muted red:** reserved for a clearly consequential problem, never ordinary incompleteness.
- **Neutral grey:** metadata, secondary information, and inactive states.

Color must never be the only way a finding's meaning is conveyed.

Exact color values are not locked. Test contrast in light and dark contexts before implementation.

## 3. Information architecture

The first report should be organized around the user's next decision, not around internal software modules.

Proposed sections:
1. **Project overview** — what was inspected, project location/name, inspection time, tool version, and scope.
2. **Attention needed** — the few highest-priority findings.
3. **What we found** — grouped findings with evidence and explanation.
4. **What is already in good shape** — positive observations without implying certification.
5. **Suggested next steps** — ordered, practical actions.
6. **Inspection limits** — checks not performed, uncertain interpretations, and unsupported project types.

Every finding should expose:
- stable finding ID;
- concise title;
- status and priority;
- observed evidence and its location;
- why the issue matters for handoff;
- confidence and limitations;
- suggested next action;
- relevant standard or existing tool, when applicable.

## 4. Interaction principles

- The first action should be obvious: choose a local project directory.
- Explain what will and will not be read before inspection.
- Do not execute project code or alter project files.
- Show progress only when a real operation is occurring.
- Let users expand a finding to inspect its evidence.
- Make the report useful without requiring an account or cloud connection.
- Provide a plain-text or portable report in addition to any rich interface.
- Keep advanced standards terminology available but explain it in ordinary language.

## 5. Voice and language

Use direct, neutral, helpful language.

Prefer:
- "We found no dependency declaration in the inspected locations."
- "This project references a data file that was not present at the recorded path."
- "We did not execute the workflow, so its runtime behavior is unknown."

Avoid:
- "Your research is not reproducible."
- "Your project failed certification."
- "AI verified your science."
- "100% reproducible" or equivalent claims.

## 6. Brand relationship

The product should be recognizably part of Common Knowledge, while remaining a useful standalone tool.

- Use the Common Knowledge name as the steward/creator identity.
- The product descriptor should explain its job before a separate product name is chosen.
- Use the founding motto and broader institutional language sparingly inside the tool; the interface is a working instrument, not a mission brochure.
- Do not invent a separate brand architecture before product-market and user evidence justify it.

## 7. Design validation

Before treating the visual identity as established:
- create a clickable or working report prototype from real fixture output;
- review it at laptop and narrow-screen widths;
- test keyboard navigation and screen-reader semantics;
- verify color contrast;
- ask at least a few target users to interpret findings without coaching;
- check whether the report feels helpful rather than judgmental or bureaucratic.

The first implementation should encode these principles simply. Do not build a design system before the product workflow is proven.
