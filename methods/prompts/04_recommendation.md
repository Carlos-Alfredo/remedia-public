# Recommendation prompts (phase 2)

**Goal of the family:** draft **at most one** change that resolves the locked phase-1 DTP under the stamped verb `a = v(f)`.

## Roles

### `recommendation_actor`

| Segment | What is inserted |
|---------|------------------|
| **DEFAULT** | Phase-2 contract: do not re-hunt DTPs; one recommendation; verb must match ACTION |
| **FOCUS** | Same clinical target framing as detection for this focus |
| **SCOPE** | Pass / module bounds |
| **COORD** | O — sequencing vs earlier acceptances |
| **PRM** | — (category calibration already applied in detection; phase 2 leans on ACTION/FLAG) |
| **ACTION** | **Y** — lock or allowlist for `v(f)`, field templates (what the draft must fill) |
| **FLAG** | O — flag addendum / binder when catalog triggers fire |
| **CONTEXT** | Generation-actor manifest blocks + phase-1 result facts (inherited pattern for later critics) |
| **OUTPUT** | Recommendation JSON schema (action fields, causal explanation, risk_level, …) |

### `recommendation_revision_actor`

Same clinical overlays; **DEFAULT** is the revision contract; **ACTION** templates are re-embedded; **CONTEXT** inherited from the shared generation bundle.

### Recommendation critics (three specialized DEFAULT variants)

Critics share inherited **CONTEXT** and optional **FLAG**. They do **not** re-open FOCUS/SCOPE/COORD/PRM/ACTION as full overlays. Return contracts are **unlabeled** (not `## SEGMENT [OUTPUT]`).

| Role | DEFAULT owns | Fails on |
|------|--------------|----------|
| `recommendation_grounding_critic` | Chart identity / invention only | Invented meds, wrong line identity, hallucinated chart facts |
| `recommendation_coverage_critic` | Stakeholder coverage for the locked DTP | Missing coverage the locked flag requires; not “clean up every sibling” |
| `recommendation_safety_critic` | Net clinical harm / safety checklist | Barrier contraindications, compounding harm, unsafe exposure |

## Structural items always implied in phase 2

Even when not separate segment headers, phase 2 prompts carry:

1. **Phase-1 result** — locked `dtp_flag` + four-field problem record (the sole DTP anchor).
2. **ACTION LOCK / ALLOWLIST** — code-stamped verb(s) for that flag (manuscript: verb map `v(f)`).
3. **Updated chart state** — after earlier acceptances (recommendation awareness), via chart pharmacotherapy / prior-rec blocks inside CONTEXT.

## Gate relationship (not a prompt sheet row)

Deterministic ActionFit / format checks sit **beside** these critics in `Gate`. They are code, not LLM roles, and are omitted from the role matrix.
