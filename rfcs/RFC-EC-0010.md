# RFC-EC-0010 — Commons Governance

**Status:** Draft  
**Target:** ECS 1.0  
**Namespace:** `urn:substratex:evidence-commons:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®


## 1. Scope

Commons governance concerns repository behavior, conformance labeling, privacy correction, challenge handling, moderation, and auditability.

It does not create authority to rewrite upstream evidence.

## 2. Roles

A Commons MAY define roles such as:

- operator;
- steward;
- reviewer;
- preservation custodian;
- privacy responder;
- conformance evaluator.

Role names are implementation-defined.

## 3. Moderation scope

A Commons MAY moderate:

- privacy violations;
- unlawful or prohibited disclosure;
- forged or altered metadata;
- false conformance representation;
- malicious payloads;
- harassment or targeted abuse;
- duplicate spam;
- policy-violating publication.

## 4. Evidence neutrality

Moderation SHOULD distinguish:

- removal or restriction of publication;
- evidence invalidation;
- scientific disagreement;
- conformance failure.

Removing an artifact from a public surface does not, by itself, prove the underlying evidence false.

## 5. Decision records

Material governance decisions SHOULD be recorded with:

- decision identity;
- policy/version;
- affected artifact;
- action;
- reason category;
- effective time;
- reviewer/steward role;
- appeal or challenge path where provided.

## 6. Conformance labels

A node MUST NOT create proprietary labels that are confusingly represented as official ECS conformance profiles.

## 7. Auditability

A Full Commons SHALL maintain sufficient governance history to reconstruct material publication, challenge, supersession, withdrawal, and conformance-label changes.


---

Copyright © 2026 Arjay Asadi. Documentation licensed under CC BY-SA 4.0 unless otherwise marked.
