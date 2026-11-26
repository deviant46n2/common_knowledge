# WorkflowHub — Project Profile

- **Category:** Computational workflow registry and collaboration infrastructure
- **Snapshot:** November 2026
- **Status:** Initial profile; operator documentation reviewed, independent evaluation still needed
- **Primary site:** https://www.workflowhub.eu/

## What it is

WorkflowHub is a registry for describing, sharing, publishing, and discovering scientific computational workflows. It aims to support reuse across disciplines and workflow systems, rather than being only an execution engine for one scientific domain.

Its public documentation describes support for open standards and formats including Common Workflow Language (CWL), RO-Crate, Bioschemas, and the GA4GH Tool Registry Service API. It also supports workflow teams and collaboration, version management, collections, and links to external workflow services and repositories.

## What role it fills

WorkflowHub addresses a layer that is easy to overlook when mapping research infrastructure: the workflow itself as a citable, discoverable, reusable research object. A dataset or paper may be archived while the sequence of computational steps that transformed inputs into results remains difficult to find, inspect, or rerun.

## Strengths and potentially relevant design choices

- Focuses on discovery and reuse of workflows, not only storage of papers or datasets.
- Uses established standards and machine-readable descriptions to improve interoperability.
- Allows workflows to remain associated with their own communities and repositories.
- Connects workflow descriptions to execution and monitoring services rather than claiming to replace them.

## Limitations and open questions

- A registry entry does not guarantee that a workflow is executable, maintained, secure, or scientifically valid.
- Interoperability depends on metadata quality, version pinning, dependency capture, and the durability of linked resources.
- The profile does not yet assess adoption outside the communities represented in the registry, governance, long-term funding, or independent user experience.
- Workflow formats and standards may be unevenly supported across scientific fields.

## Relevance to Common Knowledge

WorkflowHub is evidence that reusable research infrastructure can be modular: a shared registry can connect workflows without owning every execution environment or dataset. Common Knowledge should study this pattern before considering any custom workflow catalog or orchestration layer.

## Sources

- [WorkflowHub](https://www.workflowhub.eu/) — operator description and current registry.
- [FAIRDOM overview of WorkflowHub](https://fair-dom.org/fairdom-in-use/workflowhub) — additional description of collaboration, FAIR workflow metadata, RO-Crate, and integrations.

## Assessment

**Preliminary assessment:** A useful example of standards-oriented, federated workflow discovery. Its existence strengthens the case for investigating integration and provenance across existing services before building new infrastructure.
