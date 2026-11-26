# Workstream B — Trust, Validation, and Verifiable Storage

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Preliminary technical analysis; not a security audit
- **Workstream:** [B — Distributed and federated infrastructure](README.md)

## 1. The trust problem is not one problem

Distributed infrastructure must address at least four distinct questions:

1. **Worker integrity:** Did the worker execute the assigned workload as expected?
2. **Result validity:** Is the returned output correct for the task?
3. **Data confidentiality and integrity:** Could a worker, coordinator, or network participant read or alter protected inputs and outputs?
4. **Storage commitment and retrieval:** Is data still stored, and can authorized users actually retrieve it when needed?

A cryptographic signature can authenticate who produced a message without proving that the message is true. A sandbox can limit access without proving that the computation is correct. A storage proof can attest that a provider holds data without proving that a client can retrieve it at acceptable speed. These properties need separate mechanisms and evidence.

## 2. BOINC: application-specific validation of untrusted workers

BOINC's documentation assumes volunteer hosts may be unreliable because of hardware faults, floating-point differences, or deliberate falsification. It provides several result-validation strategies rather than a universal mechanism.

### Single execution with application-specific checks

A job can run once and a validator can inspect the result for known properties, such as conservation laws in a simulation. This avoids duplicate compute but is only useful where the application has a reliable way to detect incorrect outputs.

### Replicated execution

A job can run on multiple hosts, with agreement among outputs used as evidence of validity. This introduces compute overhead and numerical-comparison problems. Different processors, GPUs, compilers, and math libraries can produce small or significant floating-point differences. Exact bitwise comparison may require constraining the execution environment and can reduce performance; tolerance-based comparison is only appropriate when the application is numerically stable.

### Adaptive replication

BOINC documents adaptive replication as a way to reduce the overhead of checking every result. It tracks validated results by host and application version and selectively replicates more work for less-trusted hosts. Its documentation says default replication can spend at least 50% of total CPU time on result validation, while adaptive replication aims for a much lower overhead, potentially 5–10%.

These are implementation targets and project documentation, not independent performance guarantees. Adaptive trust is not the same as proof of correctness: it relies on historical host behavior, randomized checks, and the quality of the application validator.

**Assessment:** BOINC demonstrates that result validation must be designed around each scientific workload. Common Knowledge should not assume that generic consensus, majority voting, or duplicated execution automatically establishes correctness.

## 3. Security boundaries and participant agency

BOINC's security guidance identifies attacks against both sides of the volunteer relationship:
- A worker may return fabricated results or falsify credit.
- A compromised project server may distribute malicious executables.
- A project workload may intentionally or accidentally damage a volunteer's machine.
- Project files and participant information may be exposed.
- Network traffic and project servers can be attacked.

BOINC describes mitigations such as code signing, upload certificates, account-based sandboxing, and resource limits, while explicitly noting residual risks and responsibilities. It warns that projects need sufficient security expertise and operational resources.

**Assessment:** A volunteer compute system creates a reciprocal trust relationship. Participants trust the project not to abuse their devices; researchers trust remote workers not to falsify results. A credible platform needs clear workload disclosure, sandboxing, permission limits, resource controls, signed releases, update procedures, incident response, and the ability to pause or withdraw.

## 4. Filecoin: verifiable storage commitments

Filecoin documents two core storage proofs:

- **Proof of Replication (PoRep):** used when a storage provider initially commits to store data, creating a provider- and time-specific encoded replica.
- **Proof of Spacetime (PoSt):** repeated proofs that the provider continues to store the committed data over time.

The protocol uses challenges against randomly selected parts of stored data and cryptographic proofs. The Filecoin documentation describes storage deals with explicit terms such as data size, price, duration, and collateral, and penalties for failure to submit required proofs.

**Assessment:** This is a useful example of cryptographic mechanisms enforcing a storage commitment across providers without trusting one central operator to report all storage status.

**Important distinction:** Proof that a provider is retaining data is not the same as proof of fast or reliable retrieval by an end user. Filecoin documentation distinguishes storage providers from retrieval providers. Retrieval availability, latency, bandwidth, encryption, access control, and user experience need separate assessment. Proofs also do not decide whether content is lawful, ethical, correctly described, or worth preserving.

## 5. A layered verification model

| Property | Candidate mechanism | Main limitation |
|---|---|---|
| Message authenticity | Digital signatures and authenticated channels | A signed message can still be false |
| Workload authenticity | Signed builds and release artifacts | Does not prove safe behavior or correct results |
| Execution isolation | Sandboxing, containers, OS permissions, resource quotas | Isolation depends on implementation and threat model |
| Result correctness | Application-specific validators, invariants, test vectors | Only checks what the validator can express |
| Independent agreement | Replicated execution and comparison | Correlated failures, collusion, nondeterminism, and extra cost |
| Storage commitment | Cryptographic proof of replication/time | Does not guarantee retrieval performance or ethical custody |
| Data confidentiality | Encryption, access control, compute-to-data | Key management, endpoint exposure, and side channels remain |
| Auditability | Logs, provenance, signed receipts, independent audits | Logs can be incomplete, forged, or unavailable |

No single mechanism covers the whole table. Security and correctness should be described as explicit properties with evidence and limitations, not summarized by a generic “trustless” or “verified” badge.

## 6. Implications for Common Knowledge

Before any distributed compute pilot, the project should define:
- The exact task and scientific purpose.
- Whether the workload is deterministic and how outputs will be checked.
- What code is executed, who reviewed it, and how updates are authenticated.
- Which files, network services, devices, and permissions the workload can access.
- Whether data are public, sensitive, licensed, or subject to participant/community restrictions.
- What resource limits and participant controls exist.
- How invalid, suspicious, or inconsistent results are handled.
- How contributors can report abuse, withdraw, or delete local data.
- What is logged and retained, and for how long.
- Who is responsible for incident response and security updates.

A safe early pilot should use public, non-sensitive data and bounded, independently checkable jobs. It should not require volunteers to trust opaque code or expose private datasets to arbitrary nodes.

## 7. Open questions

1. Which validation strategies work for stochastic AI workloads, floating-point simulations, and model evaluation?
2. How can independent results be checked when exact agreement is not expected?
3. What attacks can defeat majority voting or adaptive host reputation?
4. What are the practical isolation guarantees of BOINC sandboxes and container-based workers on Linux, Windows, and macOS?
5. How should compute-to-data work when data cannot be moved to volunteers?
6. What is the relationship between storage proof, actual retrieval, and long-term preservation?
7. How can participants inspect workload source, permissions, and resource usage before contributing?
8. How can security incidents and project misuse be reported and independently reviewed?

## Sources

See the [November 2026 source register](../../sources.md), entries B-09 onward.

## Change log

- **2026-11-26:** Added initial analysis of BOINC result validation and security boundaries and Filecoin verifiable storage proofs. This is a technical landscape, not a security audit or architecture recommendation.
