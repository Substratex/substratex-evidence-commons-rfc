# RFC-EC-0009 — Federation and Interchange

**Status:** Draft  
**Target:** ECS 1.0  
**Namespace:** `urn:substratex:evidence-commons:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®


## 1. Purpose

Federation allows Commons Nodes to exchange evidence artifacts while preserving origin identity and custody provenance.

## 2. Node identity

A federating node SHALL expose a stable node identifier for transfer records.

## 3. Federation transfer

A Federation Transfer SHALL identify:

- transfer identity;
- source node;
- destination node;
- artifact identity;
- transfer mode;
- transferred representation;
- custody intent;
- disclosure posture;
- integrity reference;
- transfer time;
- prior custody reference where applicable.

## 4. Transfer modes

ECS 1.0 defines:

- `copy`
- `custody_transfer`
- `mirror`
- `reference_only`
- `preservation_replica`

## 5. Origin versus custody

Receiving an artifact does not make the receiving node its evidentiary origin.

Nodes SHALL distinguish:

- origin identity;
- current custodian;
- previous custodians;
- local import event.

## 6. Duplicate detection

A node SHOULD detect artifacts with the same stable origin identity and MUST NOT count replicated copies as independent evidence solely because they arrived from different nodes.

## 7. Namespace resolution

Federation MUST preserve globally or contextually resolvable identifiers sufficient to distinguish artifacts, versions, challenges, supersessions, and custody events.

## 8. Round trip

An ECS-Federation implementation SHOULD demonstrate:

`Node A → Node B → Node A or Node C`

without loss of required identity, disclosure, challenge, or custody semantics.


---

Copyright © 2026 Arjay Asadi. Documentation licensed under CC BY-SA 4.0 unless otherwise marked.
