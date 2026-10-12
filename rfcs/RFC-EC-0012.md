# RFC-EC-0012 — Conformance Profiles and Test Requirements

**Status:** Draft  
**Target:** ECS 1.0  
**Namespace:** `urn:substratex:evidence-commons:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®


## 1. Profiles

### ECS-Artifact
Tests artifact envelope identity, evidence-profile declaration, provenance, disclosure, integrity, challenge state, and versioning.

### ECS-Admission
Tests admission evaluation, disposition, refusal/quarantine/exploratory semantics, and no-silent-repair.

### ECS-Disclosure
Tests disclosure posture, redaction history, verification limits, and publication/disclosure separation.

### ECS-Comparison
Tests explicit purpose, compatibility dimensions, outcome, conditions, and no unknown→compatible promotion.

### ECS-Aggregation
Tests contract identity, membership, duplicate control, comparability requirements, challenge handling, and boundary statements.

### ECS-Preservation
Tests identity, provenance, challenge state, redaction history, fixity, and migration continuity.

### ECS-Federation
Tests node identity, transfer record, origin/custody distinction, duplicate detection, and round-trip continuity.

### ECS-Full
Requires all required profiles.

## 2. Test families

A conformance suite SHOULD include:

1. schema validity;
2. stable identity;
3. unknown disclosure rejection;
4. disclosure non-inflation;
5. publication/disclosure independence;
6. challenge propagation;
7. supersession retention;
8. withdrawal propagation;
9. comparability rejection;
10. conditional comparability;
11. duplicate-copy non-independence;
12. aggregation membership traceability;
13. preservation round trip;
14. federation custody continuity;
15. redaction-history retention;
16. RES/EGC metadata preservation;
17. malicious metadata isolation;
18. schema-version distinction.

## 3. Reporting

Conformance reports SHALL identify:

- implementation;
- implementation version;
- ECS version;
- profiles evaluated;
- corpus version;
- pass/fail counts;
- skipped tests;
- deviations;
- environment;
- timestamp;
- report integrity reference where available.

## 4. Certification boundary

A conformant report MUST NOT use conformance to imply SubstrateX certification, source truth, scientific validity, legal admissibility, safety, or security.


---

Copyright © 2026 Arjay Asadi. Documentation licensed under CC BY-SA 4.0 unless otherwise marked.
