# Workstream B — Workload Fit, Data Locality, and Resource Economics

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Working analysis; requires workload-specific measurement
- **Workstream:** [B — Distributed and federated infrastructure](README.md)

## 1. Start with the workload, not the network

A distributed system is useful only if the work can be divided, scheduled, moved, verified, and recombined at acceptable cost and risk.

Before selecting an architecture, characterize each candidate workload:
- How many independent jobs exist?
- How long does each job run?
- How much CPU, GPU, memory, disk, and network bandwidth does it need?
- How much data must move to each worker?
- Can work be interrupted and resumed?
- Are outputs deterministic, numerically tolerant, or stochastic?
- How expensive is independent verification?
- Does the data contain personal, confidential, licensed, export-controlled, or community-governed material?
- What latency and turnaround time are acceptable?
- Does the workload require specialized hardware, software, or interconnects?

## 2. Workload classes and likely fit

| Workload class | Typical characteristics | Potential fit | Main concerns |
|---|---|---|---|
| Parameter sweeps / Monte Carlo | Many independent runs, bounded inputs/outputs | Strong candidate for BOINC or HTC | Random seeds, statistical validation, data movement |
| Model evaluation batches | Many independent prompts/examples or model runs | Possible candidate for volunteer/HTC pools | Model licensing, GPU compatibility, nondeterminism, data privacy |
| Embarrassingly parallel simulations | Independent tasks with limited communication | Strong candidate for volunteer or institutional HTC | Result verification, heterogeneous numerical behavior |
| Large-scale data preprocessing | Parallelizable but often data-heavy | Depends on data locality and storage bandwidth | Network cost, sensitive data, reproducibility |
| Tightly coupled simulation | Frequent low-latency communication among processes | Usually HPC cluster or specialized federation | Interconnect latency, synchronized scheduling |
| Interactive research computing | User expects immediate response | Usually dedicated or elastic service | Latency, session state, predictable capacity |
| Sensitive human-subject analysis | Data cannot be broadly copied | Controlled institutional environment or compute-to-data | Access governance, privacy, audit, legal restrictions |
| Large model training | High GPU, memory, storage, and network demands | Specialized multi-GPU/HPC infrastructure | Interconnect, checkpointing, power, licensing, data governance |
| Archival storage | Long-lived data with retention requirements | Managed repositories or preservation networks | Custody, redundancy, retrieval, funding, rights |

This table is an initial engineering heuristic, not a universal benchmark. Real performance must be measured using representative tasks and hardware.

## 3. Why volunteer compute is not free compute

A volunteer contributes resources but still bears costs:
- Electricity and cooling.
- Hardware wear and opportunity cost.
- Internet bandwidth and data caps.
- Storage space and local support.
- Security and privacy exposure.
- Time spent installing, maintaining, and troubleshooting clients.

The coordinating project also bears costs:
- Coordinator servers, databases, and bandwidth.
- Software signing, build pipelines, and release engineering.
- Job packaging and compatibility testing.
- Result validation and duplicate execution.
- Monitoring, incident response, and participant support.
- Data storage, retention, and deletion.
- Recruitment, documentation, and community management.

A realistic cost model should record both cash expenses and donated in-kind resources. A workload that is “free” only because costs are hidden or shifted to volunteers may be neither fair nor sustainable.

## 4. Data locality can determine whether distribution is practical

Moving a dataset to a worker can cost more than the computation itself. Data may also be too large, licensed, sensitive, or governed by restrictions that make copying inappropriate.

Potential patterns include:
- **Move compute to data:** run jobs near an institutional or community-controlled dataset.
- **Move small inputs to workers:** suitable when data are public and each job needs a small subset.
- **Distribute derived or synthetic data:** useful for testing and some evaluation, but not a substitute when the original data carry essential properties.
- **Use secure enclaves or controlled execution:** potentially relevant for sensitive data, but requires threat-model and implementation review.
- **Keep data local and share only aggregate outputs:** may reduce exposure, but output leakage and inference risks still need assessment.

A distributed system should not assume that every contributor's machine is an acceptable destination for research data.

## 5. Scheduling and fairness

A scheduler makes policy choices, even when those choices are automated:
- Which jobs receive priority?
- How are scarce GPUs allocated?
- Are contributors compensated, credited, or simply acknowledged?
- How are idle or intermittent workers treated?
- How are geographic, hardware, and bandwidth inequalities reflected?
- Can participants set caps and preferred workload types?
- Can a project prevent one institution or donor from dominating resource allocation?

A fair scheduler may need explicit priorities, quotas, reservation mechanisms, transparent accounting, and appeals. “First come, first served” is itself a policy and may favor well-connected or high-capacity participants.

## 6. Practical implications for a Common Knowledge pilot

The first distributed-compute pilot should:
1. Select a real, bounded research question.
2. Define a reproducible baseline on one known machine.
3. Split the work into independent jobs only where scientifically valid.
4. Use public, non-sensitive data.
5. Record hardware and environment assumptions.
6. Define application-specific validation before recruiting workers.
7. Measure end-to-end time, including packaging, transfer, queueing, failed jobs, verification, and result aggregation.
8. Compare against local execution and an institutional cluster where possible.
9. Publish the actual resource and energy assumptions, not only peak throughput.
10. Stop if distribution adds complexity without meaningful benefit.

## 7. BOINC Central as a potential hosted pilot route

BOINC Central's current guidelines are unusually concrete. It supports scientific or nonprofit work using open-source software, publicly available non-sensitive input/output data, and large numbers of independent jobs. Typical jobs should run from minutes to about a day and fit the resource profile of home computers. The hosted service uses BUDA and Docker-based application packaging, with a web interface for batch submission and output retrieval.

This lowers the barrier compared with operating a new BOINC project, but it does not remove the need for a suitable workload, application-specific validation, security review, and reproducible baseline. It also introduces a dependency on the Berkeley-operated service and its capacity.

**Assessment:** Before considering a custom Common Knowledge volunteer network, test whether a bounded research workload could run through BOINC Central or an existing institutional HTC service. Confirm current eligibility, queue time, GPU requirements, data rules, and support directly.

## 8. Open questions

1. What candidate Common Knowledge research tasks are sufficiently parallel and independently verifiable?
2. How much time and bandwidth would data staging require?
3. Which workloads could use CPUs, and which genuinely require GPUs?
4. What is the measured overhead of validation for each candidate workload?
5. How should donated compute be valued and acknowledged without creating harmful competition?
6. What scheduling rules balance scientific priority, fairness, and contributor control?
7. How can the project support low-bandwidth and older devices without excluding them?
8. When is an existing institutional HTC/HPC service more appropriate than a volunteer network?

## Sources

See the [November 2026 source register](../../sources.md), entries B-01 through B-11.

## Change log

- **2026-11-26:** Added a first workload-fit and resource-economics framework to guide later technical experiments and avoid premature distributed-compute design.
