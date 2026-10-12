# ECS ↔ W3C PROV Mapping

Informative mapping.

Potential correspondences:

- ECS Artifact / evidence package → `prov:Entity`
- Commons Node / Custodian / Originator → `prov:Agent`
- Admission, migration, transfer, preservation, review → `prov:Activity`
- custody/provenance edges → PROV derivation and attribution relations

ECS adds Commons-specific semantics not supplied by provenance alone, including disclosure posture, comparability, challenge state, publication class, aggregation contracts, and federation custody semantics.

A PROV graph does not by itself establish ECS comparability or conformance.
