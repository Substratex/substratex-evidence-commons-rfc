# Evidence Commons Threat Model

ECS assumes that portability and federation create new failure modes beyond evidence formation itself.

## Threats

### Artifact substitution
A different payload is presented under an existing artifact identity.

**Required controls:** fixity metadata, identity continuity, explicit supersession.

### Provenance truncation
A receiving node drops upstream lineage or custody information.

**Required controls:** federation transfer record and preservation-history retention.

### Disclosure inflation
A metadata-only or redacted artifact is represented as independently reproducible from source.

**Required controls:** preserved disclosure posture and verification-limit statement.

### Comparability inflation
Artifacts with incompatible methods, horizons, schemas, source qualifications, coordinates, or claim definitions are aggregated as equivalent.

**Required controls:** explicit comparability assessment and aggregation contract.

### Challenge erasure
A disputed artifact is replicated without its open challenge state.

**Required controls:** challenge-state propagation and history retention.

### Withdrawal erasure
A withdrawn artifact remains presented as active after federation.

**Required controls:** withdrawal state is part of the governed history.

### Custody laundering
A receiving institution presents an artifact as locally originated or independently verified merely because it was imported.

**Required controls:** origin identity and custody-event distinction.

### Redaction laundering
A redacted artifact is transformed into an apparently complete artifact without disclosure of what was withheld.

**Required controls:** redaction history and disclosure posture are non-destructive.

### Duplicate amplification
Replicated copies are counted as independent observations.

**Required controls:** stable artifact identity, duplicate detection, copy/origin distinction.

### Aggregation overclaim
A large aggregate is treated as proof of scientific generality, causation, population validity, or safety.

**Required controls:** aggregation boundary statement and population/method disclosure.

### Malicious metadata
An artifact contains instructions or labels intended to alter Commons policy or validator behavior.

**Required controls:** evidence content and policy are separate; imported content never becomes local policy merely by being present.

### Governance capture
A Commons operator changes conformance labels or removes challenges to favor a participant.

**Required controls:** decision logs, versioned policy, non-destructive review history, auditable moderation actions.

### Privacy leakage
Publication or federation reveals information beyond the declared disclosure posture.

**Required controls:** publication-class enforcement, redaction history, consent/legal-basis metadata where applicable, node access policy.

## Non-goals

ECS does not guarantee that upstream observations are true, that cryptographic keys are trustworthy, that a method is scientifically valid, or that every participant acts lawfully. It requires those limits to remain inspectable rather than silently erased.
