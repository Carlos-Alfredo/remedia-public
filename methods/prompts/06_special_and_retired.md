# Special and retired prompt roles

## Live special roles

### `dose_proposal_actor` (chart completion / dose fill)

| Segment | Present? | Notes |
|---------|----------|-------|
| DEFAULT | Y | Single-phase dose proposal; no phase-1 DTP hunt |
| FOCUS | Y | Line under completion |
| ACTION | Y | Set-dosage field mechanics |
| CONTEXT | U | Chart sections composed without necessarily wrapping `## SEGMENT [CONTEXT]` |
| OUTPUT | Y | Via generation OUTPUT stitch |
| SCOPE / COORD / PRM / FLAG | — | |

Used when the workup needs dose/frequency fill rather than a new cause-locked DTP.

### `dtp_validity_critic` (mid-wave re-check)

| Segment | Present? | Notes |
|---------|----------|-------|
| DEFAULT | Y | Re-check one already-detected DTP against the updated regimen |
| OUTPUT | Y | Validity decision schema |
| FOCUS / SCOPE / COORD / PRM / ACTION / FLAG | — | |
| CONTEXT | U | Frozen DTP + “updated clinical context” as unlabeled prose |

## Retired assessment roles

DEFAULT bodies remain in the segment registry for:

- `test_assessment_{actor,revision_actor,critic}`
- `symptom_assessment_{actor,revision_actor,critic}`
- `risk_assessment_{actor,revision_actor,critic}`
- `global_risk_assessment_{actor,revision_actor,critic}`

**Runtime:** focus-evidence and global-risk assessment pipelines are marked retired (builders may exist; the live Scottish evaluation path does not call these models). When builders were active, typical assembly was:

`DEFAULT + FOCUS + thin PRM (“feeds pass N…”) + unlabeled evidence + OUTPUT`

Compressed assessment text, when present from earlier runs or alternate paths, can still appear inside CONTEXT as `FOCUS … ASSESSMENT:` blocks (see [`05_context_blocks.md`](05_context_blocks.md)).

## Other non-role stances (manifest only)

These appear in CONTEXT manifests / gates but are not PRM `ROLE_*` defaults:

| Stance ID | Use |
|-----------|-----|
| `interaction_pair` | Drug–drug interaction gate |
| `multi_indication_classifier` | Multi-indication acceptability |
| `stewardship_adjunct` | Legacy stewardship; live path prefers enrichment combination candidates |

## Manuscript alignment

Manuscript Table “Prompt additions by pass” describes **pass-level CONTEXT emphasis** (linked problems, regimen coverage, dose limits, ADR profile, adherence barriers). That table is the reader-facing summary; this folder is the role/segment map behind it.
