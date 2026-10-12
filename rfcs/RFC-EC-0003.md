# RFC-EC-0003 — Disclosure and Privacy

**Status:** Draft  
**Target:** ECS 1.0  
**Namespace:** `urn:substratex:evidence-commons:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®


## 1. Disclosure postures

Every Commons Artifact intended for publication, exchange, comparison, or preservation SHALL declare one posture:

- `complete_source`
- `redacted_source`
- `derived_evidence_only`
- `metadata_only`
- `withheld_restricted`

## 2. Meaning

### complete_source
The declared source package required for the artifact's reproduction posture is included or resolvable for the authorized audience.

### redacted_source
Source is present in modified form and redactions are declared.

### derived_evidence_only
Derived evidence is available but the source required for full independent recomputation is not provided.

### metadata_only
Identity, provenance, method, integrity, and disclosure metadata may be inspectable without the substantive evidence payload.

### withheld_restricted
Evidence exists but access is restricted or withheld under a declared policy.

## 3. Non-inflation

A node MUST NOT represent a more restrictive disclosure posture as a less restrictive one.

Redaction MUST NOT be interpreted as evidence absence or evidence contradiction.

## 4. Verification limits

Every non-complete posture SHALL state which verification or reproduction operations are no longer possible or are conditional.

## 5. Privacy and lawful disclosure

ECS does not itself determine the legal basis for disclosure. Implementations SHALL provide fields for consent/legal-basis declarations where required by organizational or jurisdictional policy.

## 6. Data minimization

Public-facing Commons SHOULD minimize unnecessary personal or sensitive content and SHOULD permit publication of derived or metadata-only evidence where the stated purpose does not require source disclosure.


---

Copyright © 2026 Arjay Asadi. Documentation licensed under CC BY-SA 4.0 unless otherwise marked.
