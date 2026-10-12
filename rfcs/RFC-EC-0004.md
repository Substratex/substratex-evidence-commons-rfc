# RFC-EC-0004 — Publication and Access Classes

**Status:** Draft  
**Target:** ECS 1.0  
**Namespace:** `urn:substratex:evidence-commons:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®


## 1. Publication classes

An ECS Publication Record SHALL declare one:

- `public`
- `restricted`
- `research`
- `organizational`
- `exploratory`
- `withdrawn`

## 2. Separation from disclosure

Publication class governs access/exposure. Disclosure posture governs what evidentiary material is available.

A `public` artifact may still be `metadata_only`.  
A `restricted` artifact may contain `complete_source`.

## 3. Publication transitions

Transitions SHALL be recorded as events rather than overwriting prior publication history.

## 4. Withdrawn state

A withdrawn artifact MUST NOT be newly presented as active Commons evidence.

Where lawful and technically possible, its identity, withdrawal reason category, and historical lineage SHOULD remain resolvable.

## 5. Access enforcement

Access mechanisms are implementation-defined. ECS requires only that the declared publication class and actual access policy not conflict without an explicit policy override record.


---

Copyright © 2026 Arjay Asadi. Documentation licensed under CC BY-SA 4.0 unless otherwise marked.
