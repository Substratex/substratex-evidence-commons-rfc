# Evidence Commons Standard (ECS)

**RFC Specification for Portable, Challengeable, Comparable, Preservable, and Federated Computational Evidence**

**Target:** ECS 1.0  
**Status:** Request for Comment / Standards Track  
**Namespace:** `urn:substratex:evidence-commons:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®

Evidence Commons Standard (ECS) defines the interoperability and governance layer for evidence after it leaves its originating system.

Its constitutional principle is:

> **The artifact is durable; the interface is not.**

ECS specifies how evidence artifacts may be admitted, disclosed, published, compared, challenged, aggregated, preserved, transferred between custodians, and governed without converting portability into stronger evidentiary authority.

## Architectural position

```text
Runtime Evidence Standard (RES)
defines evidence formation, identity, status, lineage,
challenge state, issuance, export, and preservation
                    ↓
Evidence-Governed Computation (EGC)
governs claim admissibility, bounded projection,
surface binding, and egress closure
                    ↓
Evidence Commons Standard (ECS)
governs exchange, publication, discovery, comparison,
challenge, aggregation, federation, and preservation
across systems and custodians
```

ECS does **not** require one central website, database, or institution. A conforming Commons may be public, organizational, research-oriented, regulatory, sector-specific, or federated.

## What ECS standardizes

1. Commons Artifact Admission
2. Disclosure and Privacy
3. Publication and Access Classes
4. Comparability
5. Challenge, Counterevidence, Review, Supersession, and Withdrawal
6. Aggregation
7. Preservation
8. Federation and Interchange
9. Commons Governance
10. Conformance

## What ECS does not standardize

ECS does not:

- define the scientific validity of a metric or method;
- create evidence authority that was absent upstream;
- certify source truth or source authenticity by default;
- infer hidden state, intent, consciousness, private reasoning, or causality;
- require a specific scientific instrument, interface, model provider, storage vendor, or deployment topology;
- require a single canonical Commons operator;
- make aggregation equivalent to generality, causality, truth, or safety;
- replace RES evidence formation or EGC claim governance.

## Artifact admission classes

A Commons may admit evidence under one of the following admission dispositions:

- `admitted`
- `admitted_restricted`
- `exploratory`
- `quarantined`
- `refused`
- `withdrawn`

Only artifacts that satisfy the compatibility and conformance requirements of a comparison or aggregation contract may participate in standards-conformant comparison or aggregation.

## Disclosure postures

ECS 1.0 defines:

- `complete_source`
- `redacted_source`
- `derived_evidence_only`
- `metadata_only`
- `withheld_restricted`

Disclosure posture describes what is available for inspection. It does not itself determine truth or validity.

## Publication classes

ECS 1.0 defines:

- `public`
- `restricted`
- `research`
- `organizational`
- `exploratory`
- `withdrawn`

Publication class and disclosure posture are independent dimensions.

## Conformance profiles

- **ECS-Artifact** — portable Commons artifact envelope
- **ECS-Admission** — admission evaluation and disposition
- **ECS-Disclosure** — disclosure, privacy, and redaction semantics
- **ECS-Comparison** — explicit comparability assessment
- **ECS-Aggregation** — governed aggregate production
- **ECS-Preservation** — preservation and history retention
- **ECS-Federation** — repository-to-repository custody transfer
- **ECS-Full** — all required profiles

Passing public fixtures establishes only declared ECS conformance. It is not SubstrateX certification.

## Repository layout

```text
rfcs/             normative RFC series
schemas/          JSON Schema 2020-12 interchange schemas
vocabulary/       controlled machine-readable vocabularies
conformance/      profiles, fixtures, expected outcomes, reports
examples/         end-to-end examples
mappings/         RES, EGC, PROV, OpenLineage, VC/C2PA mappings
scripts/          reference validation utilities
```

## Standards-track RFCs

See [`RFC_INDEX.md`](RFC_INDEX.md).

## Licensing

Specifications and documentation: **CC BY-SA 4.0**  
Reference software, validators, tests, and tooling: **PolyForm Perimeter 1.0.1**

See [`LICENSE.md`](LICENSE.md).

---

Copyright © 2026 Arjay Asadi. All rights reserved except as expressly licensed.
