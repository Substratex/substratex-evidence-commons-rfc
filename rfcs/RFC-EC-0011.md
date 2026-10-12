# RFC-EC-0011 — RES / EGC / Evidence Commons Boundary

**Status:** Draft  
**Target:** ECS 1.0  
**Namespace:** `urn:substratex:evidence-commons:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®


## 1. Division of responsibility

### Runtime Evidence Standard (RES)
Defines evidence formation and evidence lifecycle semantics, including identity, source relationship, support class, missingness, method relationship, scope, lineage, challenge state, issuance, export, and preservation metadata.

### Evidence-Governed Computation (EGC)
Evaluates what claims may be admitted from evidence and governs bounded projection, surface binding, and egress closure.

### Evidence Commons Standard (ECS)
Governs how evidence artifacts and their governed metadata move between custodians and systems: admission, disclosure, publication, comparison, challenge, aggregation, preservation, federation, and Commons governance.

## 2. No subsumption

ECS does not redefine RES evidence semantics.

ECS does not reproduce EGC claim-admissibility logic.

An ECS implementation MAY carry EGC metadata and SHOULD preserve it without amplification.

## 3. Handoff

An RES artifact entering a Commons SHOULD preserve:

- stable evidence/artifact identity;
- evidence standard/version;
- provenance/lineage;
- support classes/statuses;
- missingness;
- method/version;
- scope;
- challenge/supersession state;
- integrity references;
- disclosure posture or disclosure prerequisites;
- preservation metadata where present.

## 4. Non-RES artifacts

A Commons MAY admit non-RES artifacts as exploratory or under another explicitly declared evidence profile.

Such admission MUST NOT be represented as RES conformance.

## 5. EGC continuity

Where an artifact includes EGC claim contracts, admitted claims, claim status, or surface-binding references, ECS federation and preservation MUST NOT silently strengthen, strip, or rewrite those authority semantics.


---

Copyright © 2026 Arjay Asadi. Documentation licensed under CC BY-SA 4.0 unless otherwise marked.
