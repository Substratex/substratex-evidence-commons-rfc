# ECS ↔ OpenLineage Mapping

Informative mapping.

OpenLineage run/job/dataset facets may carry operational lineage relevant to ECS artifacts. ECS can preserve OpenLineage identifiers as provenance references.

ECS does not require OpenLineage and does not reinterpret job/run lineage as evidentiary authority.

Potential mapping:

- origin job/run → artifact origin/provenance
- dataset identifiers → source/evidence references
- custom facets → ECS extension objects

Comparability, challenge, disclosure, and Commons governance remain ECS concerns.
