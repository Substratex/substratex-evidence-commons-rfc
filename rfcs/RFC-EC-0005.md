# RFC-EC-0005 — Comparability

**Status:** Draft  
**Target:** ECS 1.0  
**Namespace:** `urn:substratex:evidence-commons:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®


## 1. Principle

Similarity is not comparability.

A Commons MUST NOT treat two artifacts as standards-comparable without an explicit comparison purpose and compatibility assessment.

## 2. Dimensions

A Comparability Assessment SHALL evaluate, where relevant:

- schema/version compatibility;
- evidence-horizon compatibility;
- method/version compatibility;
- source-qualification compatibility;
- coordinate-system compatibility;
- claim-definition compatibility;
- disclosure compatibility;
- population/context compatibility;
- validation-state compatibility;
- challenge/supersession state.

## 3. Outcomes

- `comparable`
- `conditionally_comparable`
- `non_comparable`
- `indeterminate`

## 4. Conditional comparison

A conditionally comparable result SHALL state the conditions and dimensions under which comparison is permitted.

## 5. Missing information

Unknown compatibility SHALL NOT be converted to compatibility.

If a required dimension cannot be assessed, the outcome MUST be `indeterminate` or `non_comparable` according to the comparison contract.

## 6. Disclosure asymmetry

Artifacts with different disclosure postures MAY be comparable for some purposes, but the assessment MUST state any verification asymmetry.

## 7. Comparability does not establish validity

A comparable pair may share the same invalid method. Comparability establishes compatibility for a declared analytical purpose, not scientific correctness.


---

Copyright © 2026 Arjay Asadi. Documentation licensed under CC BY-SA 4.0 unless otherwise marked.
