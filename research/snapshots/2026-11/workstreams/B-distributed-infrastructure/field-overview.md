# Workstream B — Initial Field Overview: Distributed and Federated Infrastructure

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Preliminary orientation; not a systematic review
- **Workstream:** [B — Distributed and federated infrastructure](README.md)

## 1. Central question

How can people and institutions contribute, share, coordinate, and govern computing, storage, networking, and other infrastructure without creating unacceptable security, reliability, privacy, or power-concentration risks?

The word “distributed” covers very different systems. A volunteer computing network, a university high-throughput cluster federation, a peer-to-peer content network, a multi-cloud scheduler, and a decentralized storage market do not solve the same problem. They have different trust assumptions, economic models, workload types, and operational responsibilities.

Common Knowledge should not treat decentralization as an end in itself. The question is which forms of distribution improve resilience, accessibility, user agency, and scientific capability for a real workload.

## 2. Core distinctions

- **Distributed computing:** Work is executed across multiple computers or sites.
- **Volunteer computing:** Individuals or organizations donate spare resources to projects, often using personal devices.
- **High-throughput computing (HTC):** Systems maximize the rate of completing many jobs, often with independent or loosely coupled workloads.
- **High-performance computing (HPC):** Systems optimize tightly coupled parallel computation and low-latency communication, often requiring specialized interconnects and coordinated scheduling.
- **Federation:** Independently operated systems coordinate through shared protocols, identities, policies, or interfaces while retaining some local autonomy.
- **Multi-cluster orchestration:** Software coordinates workloads or services across multiple clusters, often under one organization's or operator's control.
- **Peer-to-peer networking:** Participants communicate directly or through relays without relying on one fixed central server for every interaction.
- **Distributed storage:** Data is replicated, erasure-coded, or otherwise spread across nodes or providers.
- **Content addressing:** Data is identified by a cryptographic digest or content identifier rather than only by a location-based URL.
- **Decentralization:** Control, decision-making, or operational dependency is distributed. A technically distributed system can still have centralized governance, funding, identity, or control.

## 3. Main infrastructure layers

1. **Resource discovery and identity:** How workers, clusters, storage providers, and organizations find and authenticate one another.
2. **Scheduling and allocation:** How jobs are assigned based on capacity, locality, cost, priority, availability, and policy.
3. **Execution and isolation:** How workloads are packaged, sandboxed, monitored, and terminated.
4. **Data movement and storage:** How inputs and outputs are transferred, cached, replicated, and retained.
5. **Trust and verification:** How systems handle malicious, faulty, compromised, or unreliable nodes and results.
6. **Monitoring and accounting:** How resource use, failures, costs, energy, and contribution are measured.
7. **Governance and incentives:** Who sets policy, pays for operations, resolves disputes, and controls software and data.
8. **Resilience and continuity:** How systems survive node churn, outages, provider exit, attacks, and institutional failure.

## 4. Initial representative systems

### Volunteer and public-resource computing

**BOINC** is designed for high-throughput scientific computing using heterogeneous, intermittently available, and untrusted consumer devices. Its architecture distributes jobs to worker clients; projects can replicate jobs and validate results. Project-specific validators and assimilators are often required.

BOINC documentation explicitly identifies result falsification, malicious executable distribution, server compromise, participant privacy, and abuse of volunteer hosts as security risks.

### Institutional and campus federation

**HTCondor** supports high-throughput computing across a single cluster, related campus clusters, cloud resources, and national or international federations. It represents a more institutionally managed model, often with credentials, access points, schedulers, and defined administrative control.

### Multi-cluster orchestration

**Kubernetes SIG Multicluster** works on Kubernetes-native ways for workloads and metadata to cross cluster boundaries. This is useful for understanding multi-cluster coordination, but it is not the same thing as open volunteer computing: participating clusters may still be administered by a single organization or trusted operators.

### Peer-to-peer networking

**libp2p** is a suite of protocols and implementations for building peer-to-peer applications, including addressing, secure connections, discovery, relaying, and pub/sub. Its own specifications repository describes the specifications as incomplete and under active development.

### Content-addressed storage

**IPFS** identifies content by content identifiers and allows nodes to retrieve content from peers. Its documentation is explicit that content addressing does not guarantee persistent availability: cached content can be garbage-collected, and continued availability requires pinning or other retention arrangements. Pinning services introduce service-provider and funding dependencies.

These systems are not interchangeable and do not collectively form a ready-made Common Knowledge architecture.

## 5. Early technical and governance lessons

1. **Workload shape determines architecture.** Independent parameter sweeps, model evaluation, and batch analysis may suit HTC or volunteer computing. Tightly coupled simulation may require HPC infrastructure and low-latency interconnects.
2. **Untrusted workers require validation.** Redundant execution, statistical checks, signed outputs, trusted execution, or application-specific verification may be necessary. No one technique works for every workload.
3. **Code distribution is a security boundary.** Volunteers need assurance that workloads cannot access personal files, credentials, or unrelated resources. Sandboxing and code signing reduce risk but do not eliminate it.
4. **Data movement can dominate compute.** Large, sensitive, or licensed datasets may be unsuitable for arbitrary volunteer nodes. Compute-to-data or controlled institutional execution may be preferable.
5. **Distributed does not mean persistent.** Peer caching and replication require active operators, storage capacity, monitoring, and incentives.
6. **Federation does not eliminate governance.** Identity, trust, dispute resolution, funding, and control can remain centralized even when computation or storage is distributed.
7. **Volunteer resources are not free.** Electricity, bandwidth, hardware wear, support, security, and coordination have real costs.
8. **Participant agency matters.** Contributors should understand what their machines will run, what resources can be used, what data may leave their devices, and how to pause or withdraw.

## 6. Relevance to Common Knowledge

A distributed infrastructure layer could eventually help coordinate donated or institutional compute and storage. But it should only be considered after identifying concrete research workloads, their data sensitivity, verification needs, resource requirements, and operational costs.

The first question is not “How do we build a global compute network?” It is “Which real research tasks are blocked by lack of suitable resources, and what is the smallest safe and useful way to support them?”

## 7. Questions for the next research pass

1. Which research workloads are genuinely suitable for volunteer computing, and which are not?
2. What are the security and privacy guarantees of BOINC, HTCondor, and emerging federation systems?
3. How do projects validate results when workers are unreliable or adversarial?
4. What is the trade-off between redundant computation, cryptographic verification, trusted hardware, and application-specific checks?
5. How are compute resources discovered, benchmarked, allocated, and fairly accounted for?
6. How do storage networks guarantee retention, repair, and retrieval rather than merely content addressing?
7. Which systems allow independent operators to participate without requiring a single trusted administrator?
8. What happens when a coordinator, identity provider, funding source, or major storage provider disappears?
9. How can contributors control resource limits, workload permissions, data access, and withdrawal?
10. Which workloads can run near sensitive data instead of moving data to volunteer devices?

## 8. Scope and limitations

This first orientation is weighted toward BOINC, HTCondor, Kubernetes multi-cluster coordination, libp2p, and IPFS. It does not yet comprehensively cover HPC schedulers, grid computing, scientific workflow federation, decentralized storage economics, confidential computing, trusted execution environments, distributed AI inference, energy accounting, or global network access inequalities.

## Sources

See the [November 2026 source register](../../sources.md), entries B-01 onward.

## Change log

- **2026-11-26:** Created initial field overview and mapped representative volunteer compute, institutional HTC, multi-cluster orchestration, peer-to-peer networking, and content-addressed storage systems.
