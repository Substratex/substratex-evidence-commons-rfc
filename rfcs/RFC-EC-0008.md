# RFC-EC-0008 — Preservation

**Status:** Draft  
**Target:** ECS 1.0  
**Namespace:** `urn:substratex:evidence-commons:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®


## 1. Principle

Preservation must retain the evidence relationship, not merely the visible conclusion.

## 2. Preservation record

A Preservation Record SHALL identify:

- preserved artifact;
- preservation event identity;
- custodian;
- fixity/integrity reference;
- preservation time;
- storage or package representation;
- disclosure posture;
- challenge state;
- redaction history reference;
- migration/version history;
- prior preservation event where applicable.

## 3. Required fidelity

A preservation operation MUST NOT silently discard:

- artifact identity;
- upstream provenance;
- disclosure posture;
- known challenge/dispute state;
- supersession or withdrawal state;
- integrity scope;
- version identity;
- boundary/limitation metadata required by the artifact profile.

## 4. Migration

Format migration MAY occur, but MUST create a preservation event and MUST distinguish:

- source representation;
- target representation;
- migration tool/method;
- transformation scope;
- validation result.

## 5. Fixity

ECS does not require one digest algorithm. The algorithm and digest scope MUST be declared.

## 6. Redaction history

A later redaction MUST NOT be presented as though the artifact had always existed in that state. Redaction events SHALL be historically distinguishable.


---

Copyright © 2026 Arjay Asadi. Documentation licensed under CC BY-SA 4.0 unless otherwise marked.
