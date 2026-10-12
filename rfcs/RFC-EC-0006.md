# RFC-EC-0006 — Challenge, Review, Supersession, and Withdrawal

**Status:** Draft  
**Target:** ECS 1.0  
**Namespace:** `urn:substratex:evidence-commons:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®


## 1. Challenge

A Challenge SHALL identify:

- challenged object;
- challenge category;
- reason;
- challenger identity or protected pseudonymous identifier where permitted;
- creation time;
- status;
- supporting references or counterevidence where supplied.

## 2. Counterevidence

Counterevidence SHALL retain its own identity, source relationship, and disclosure posture.

Counterevidence MUST NOT overwrite the object it challenges.

## 3. Review

A Review SHALL record:

- reviewed objects;
- process or policy;
- findings;
- outcome;
- reviewer role;
- resulting status changes;
- unresolved questions.

## 4. Supersession

Supersession creates a relationship:

`new_object supersedes old_object for declared scope`

The superseded object SHALL remain historically identifiable.

## 5. Withdrawal

Withdrawal SHALL be represented as a state transition or record, not deletion from the historical model.

## 6. Federation

Open challenge, dispute, supersession, and withdrawal state MUST be carried during standards-conformant federation where that state is available to the transferring node.

A receiving node MUST NOT silently reset a disputed artifact to uncontested.


---

Copyright © 2026 Arjay Asadi. Documentation licensed under CC BY-SA 4.0 unless otherwise marked.
