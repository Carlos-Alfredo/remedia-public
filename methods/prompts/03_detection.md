# Detection prompts (phase 1)

**Goal of the family:** identify a drug-therapy problem (DTP) and cause flag for the current focus. **No treatment verb.**

## Roles

### `detection_actor`

| Segment | What is inserted |
|---------|------------------|
| **DEFAULT** | Phase-1 detection contract: cause only; ignore catalog-stamped verbs if they appear |
| **FOCUS** | Target framing for this focus (HP / prevention / symptomatic / medication line) |
| **SCOPE** | Pass bounds and research-field pointers for this Minnesota cause class |
| **COORD** | O — same-wave / prior-acceptance sequencing when history triggers fire (common on med-scoped multi-indication prompts) |
| **PRM** | O — category calibration (scope-exit, etc.); omitted when empty |
| **ACTION** | — |
| **FLAG** | — |
| **CONTEXT** | Chart + enrichment blocks from the detection-actor manifest (see [`05_context_blocks.md`](05_context_blocks.md)) |
| **OUTPUT** | Detection JSON schema (flag, causes, four-field explanation, evidence) |

### `detection_revision_actor`

Same overlays as the first actor; **DEFAULT** swaps to the revision contract. **CONTEXT** is inherited from the first actor attempt.

### `detection_critic`

| Segment | What is inserted |
|---------|------------------|
| **DEFAULT** | Phase-1 critic contract: evaluate identification only |
| **FOCUS** / **SCOPE** / **COORD** / **PRM** | Same overlay pattern as actor (COORD/PRM optional) |
| **FLAG** | O — cause-fit nuance when the locked `dtp_flag` has critic text |
| **ACTION** | — |
| **CONTEXT** | Inherited first-actor CONTEXT when available; else a lean critic composition |
| **OUTPUT** | Critic JSON: `fact_error` / `logic_error` (+ explanations) |

Canonical instruction order for the critic block:

`DEFAULT → FOCUS → SCOPE → COORD → PRM → FLAG → OUTPUT`

(`CONTEXT` is supplied around that instruction block.)

## Pass-dependent content (same skeleton)

Pass number changes FOCUS/SCOPE/PRM/CONTEXT **bodies**, not which segment slots exist. Examples:

| Pass focus (manuscript Table “Prompt additions by pass”) | Typical CONTEXT emphasis |
|----------------------------------------------------------|--------------------------|
| 1 — medication line | Linked problems, sibling lines, history; combination / stewardship hints when relevant |
| 2 — diagnosis or prevention gap | Regimen coverage, prior adds, care facts |
| 3 — line (effectiveness) | Indications, sibling lines, med enrichment |
| 4 / 6 — dose | Current dose, renal/hepatic limits, dose labs |
| 5 — adverse reaction | Adverse-effect profile, sibling agents |
| 7 — adherence | Adherence barriers, timing, siblings |

## Hard exclusions

- No **ACTION** segment (verb lock belongs to phase 2).
- Critic must not invent treatment recommendations.
