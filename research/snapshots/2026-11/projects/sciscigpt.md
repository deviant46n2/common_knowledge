# Project Profile: SciSciGPT

- **Snapshot:** 2026-11
- **Profile last verified:** 2026-11-26
- **Project website:** https://sciscigpt.com/
- **Code:** https://github.com/Northwestern-CSSI/SciSciGPT
- **Research paper:** https://doi.org/10.1038/s43588-025-00906-6
- **Status:** Open-source research prototype and domain-specific collaborator
- **Confidence:** High for published architecture and stated resources; independent evaluation of current service and user experience remains open

## Overview

SciSciGPT is an AI collaborator designed for the science of science: the study of how science itself develops, including scholarly networks, research topics, publication patterns, and scientific innovation.

The published system combines a scholarly data repository, a multi-agent architecture with specialist roles, and a conversational web interface for iterative analysis and research prototyping.

## Documented architecture

The 2025/2026 paper describes three main components:
1. A database repository containing scholarly data and a curated corpus of science-of-science publications.
2. A multi-agent system in which a research manager delegates tasks to specialist agents.
3. A conversational interface supporting iterative clarification, analysis, and visualization.

The paper describes open-source implementation and data resources, including a GitHub repository and Zenodo archive.

## Relevance to Common Knowledge

SciSciGPT is a useful example of a domain-specific human–AI collaborator that connects:
- Curated research literature.
- Structured scholarly data.
- Specialist AI agents.
- Analytical workflows.
- Human interaction and iterative refinement.

It may be particularly useful as a model for domain-specific research assistants rather than a universal autonomous research agent.

## Limitations and open questions

- Its demonstrated domain is science of science, not all research disciplines.
- Published case studies do not establish general scientific reliability.
- Agent roles and internal workflow are system-specific and need independent evaluation.
- The public interface's current operational status, access terms, and service dependencies require verification.
- Independent reproduction of its published analyses should be assessed.
- How does the system record source provenance, data transformations, human interventions, and agent decisions?

## Assessment

**Documented fact:** SciSciGPT is an open-source prototype multi-agent collaborator for science-of-science workflows, with a scholarly data repository and conversational interface.

**Assessment:** Its domain specialization and structured data foundation are valuable design signals. Common Knowledge should study its auditability, data provenance, and independent reproducibility before drawing architectural conclusions.

**Open question:** Can its workflow and data architecture be reused or adapted in a portable, model-agnostic way without depending on its particular data sources or hosted interface?

## Sources

See source register entry D-06.

## Change log

- **2026-11-26:** Created profile from the peer-reviewed Nature Computational Science paper and linked code/data resources.
