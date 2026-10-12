# RFC-EC-0013 — JSON Interchange Profile

**Status:** Draft  
**Target:** ECS 1.0  
**Namespace:** `urn:substratex:evidence-commons:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®


## 1. Encoding

ECS 1.0 normative interchange schemas use JSON compatible with **JSON Schema 2020-12**.

Implementations MAY use other encodings if they preserve equivalent semantics.

## 2. Identifier representation

Identifiers SHALL be non-empty strings and SHOULD be globally unique or scoped by a declared namespace.

## 3. Time representation

Timestamps SHOULD use RFC 3339 / ISO 8601-compatible strings.

## 4. Unknown fields

Schemas may permit extension fields in explicitly designated extension objects. Implementations MUST NOT interpret unknown extension fields as normative ECS authority.

## 5. Canonicalization

ECS does not mandate a universal JSON canonicalization algorithm in 1.0. If an integrity digest depends on canonicalization, the algorithm and digest scope MUST be declared.

## 6. Schemas

Normative schemas are published in `/schemas`.

Schema validation verifies structure only. Cross-object and policy invariants require semantic validation and profile tests.


---

Copyright © 2026 Arjay Asadi. Documentation licensed under CC BY-SA 4.0 unless otherwise marked.
