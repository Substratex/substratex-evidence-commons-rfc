# Evidence Commons RFC Process

The Evidence Commons Standard develops through public Request for Comment documents.

## Statuses

`Draft → Review → Candidate → Accepted → Superseded | Withdrawn`

- **Draft**: active design work; incompatible changes are permitted.
- **Review**: normative surface is substantially complete and public review is requested.
- **Candidate**: implementation and interoperability evidence is required; incompatible changes require explicit justification.
- **Accepted**: normative text is stable for the identified major/minor standard version.
- **Superseded**: replaced by a later RFC or standard version while retained for lineage.
- **Withdrawn**: no longer proposed for adoption.

## Acceptance threshold

An RFC SHOULD NOT become Accepted solely because its schema validates.

For standards-track acceptance, maintainers should seek:

1. normative completeness;
2. canonical pass/fail fixtures;
3. at least one reference implementation;
4. at least one independent implementation or interoperable external system for major interchange RFCs;
5. threat-model review;
6. privacy review where disclosure is implicated;
7. migration guidance;
8. demonstrated round-trip preservation where relevant.

## Change control

Every normative change MUST identify:

- affected RFCs;
- affected schemas or vocabularies;
- backward-compatibility impact;
- conformance impact;
- migration requirements;
- privacy/security implications;
- whether artifact identity or comparability can change.

A text-only editorial change MUST NOT silently alter machine-readable semantics.
