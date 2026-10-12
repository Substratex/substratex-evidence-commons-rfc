# RFC-EC-0001 — Commons Architecture

**Status:** Draft  
**Target:** ECS 1.0  
**Namespace:** `urn:substratex:evidence-commons:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®


## 1. Constitutional principle

> **The artifact is durable; the interface is not.**

A Commons SHALL attach legitimacy, identity, disclosure, challenge state, and custody history to artifacts and governed records, not to the transient interface through which they are viewed.

## 2. Architecture

ECS defines a federatable evidence-commons layer. It does not require a central operator.

A conforming Commons may consist of one or more independent **Commons Nodes**.

## 3. Core objects

ECS 1.0 defines:

- Commons Artifact Envelope
- Admission Record
- Disclosure Profile
- Publication Record
- Comparability Assessment
- Challenge
- Counterevidence
- Review
- Supersession
- Withdrawal
- Aggregation Record
- Preservation Record
- Federation Transfer
- Custody Event
- Conformance Report

## 4. Core invariants

A conforming implementation SHALL preserve the following invariants:

1. **Artifact identity continuity** — transfer does not silently create a new origin.
2. **No authority creation by custody** — storage or republication does not create evidentiary authority.
3. **Disclosure fidelity** — redaction and withholding remain explicit.
4. **Challenge retention** — open challenges remain attached or discoverable.
5. **Non-destructive revision** — correction and supersession do not erase history.
6. **Comparability is declared** — comparison is never inferred from superficial similarity.
7. **Aggregation is contract-bound** — aggregate membership is governed by explicit inclusion rules.
8. **Replication is not independence** — copied artifacts are not independent observations.
9. **Publication is not validation** — public availability does not establish truth or scientific validity.
10. **Federation preserves custody lineage** — receiving nodes distinguish origin from custody.
11. **Withdrawal is state, not erasure** — withdrawn identity remains historically resolvable where lawful.
12. **Interfaces have no independent evidence authority** — display does not strengthen an artifact.

## 5. Topology independence

Conformance depends on preserved semantics, not whether components run in a browser, server, local application, institutional repository, distributed object store, or federated service.


---

Copyright © 2026 Arjay Asadi. Documentation licensed under CC BY-SA 4.0 unless otherwise marked.
