# RFC-EC-0002 — Artifact Admission

**Status:** Draft  
**Target:** ECS 1.0  
**Namespace:** `urn:substratex:evidence-commons:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®


## 1. Purpose

Artifact admission determines whether an evidence artifact may enter a Commons and under what restrictions.

## 2. Admission inputs

An admission evaluator MUST inspect, at minimum where applicable:

- artifact identity;
- declared evidence standard and version;
- schema identity;
- source/disclosure posture;
- provenance references;
- integrity/fixity metadata;
- conformance claims;
- challenge and supersession state known at submission;
- publication request;
- legal/consent declaration where required by policy.

## 3. Dispositions

An Admission Record SHALL use exactly one disposition:

- `admitted`
- `admitted_restricted`
- `exploratory`
- `quarantined`
- `refused`
- `withdrawn`

## 4. Comparable admission

An artifact MUST NOT be represented as standards-comparable merely because it was admitted.

Admission and comparability are distinct evaluations.

## 5. Exploratory admission

A Commons MAY retain non-conformant or non-RES material as `exploratory` provided:

- the status is explicit;
- it is excluded from standards-conformant aggregate claims by default;
- it cannot masquerade as a conformant artifact.

## 6. No silent repair

A node MUST NOT silently invent missing provenance, source, method, conformance, or disclosure metadata in order to admit an artifact.

Any normalization MUST be distinguishable from supplied evidence metadata.


---

Copyright © 2026 Arjay Asadi. Documentation licensed under CC BY-SA 4.0 unless otherwise marked.
