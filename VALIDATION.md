# Validation and Conformance

Validation occurs at several layers.

1. **Schema validation** — an object has the required machine-readable shape.
2. **Semantic validation** — declared values obey cross-field ECS rules.
3. **Profile conformance** — the implementation satisfies the requirements of an ECS profile.
4. **Round-trip validation** — export, transfer, import, and re-export preserve required identity and history.
5. **Interoperability validation** — independently developed systems exchange artifacts with equivalent ECS semantics.

Schema-valid does not imply standards-conformant.

The reference validator in `scripts/validate.py` validates repository examples and canonical fixtures. It is test software, not a certification authority.
