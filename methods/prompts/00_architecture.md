# Prompt architecture

Every PRM workup model call is one template whose labeled parts appear in a fixed order. Empty parts are omitted. The manuscript names these as Default, Focus, Scope, Coordination, PRM (DTP-fields calibration), Action, Flag, Context, and Output.

In the live assembler each part is emitted as:

```text
## SEGMENT [<NAME>]
<body>
```

`DEFAULT` is chosen by **agent role** (what this call is allowed to do). All other segments are **overlays** that must not restate another layer’s domain.

## The nine segments

| Segment | Owns | Must not restate |
|---------|------|------------------|
| **DEFAULT** | Process contract for this role: phase boundary, what the call may propose, baseline valid outcome | FOCUS criteria, SCOPE bounds, COORD history, PRM calibrations, FLAG nuance |
| **FOCUS** | Clinical target framing: health problem / prevention domain / symptom(s) / medication line | Action verbs, preferred `none` outcome, PRM calibrations, FLAG nuance |
| **SCOPE** | Module/wave bounds: unit under review, research-field pointers, category out-of-bounds | FOCUS prioritization, COORD history, cause menus, verbs |
| **COORD** | Cross-pass / same-wave sequencing: do not undo earlier modules or duplicate claimed pathways | FOCUS, SCOPE, PRM menus, verbs |
| **PRM** | Category calibration only (e.g. scope-exit on passes 1–2, dose intensity vs risk on pass 6, adherence bar on pass 7) | FOCUS criteria, ACTION mechanics, OUTPUT schema |
| **ACTION** | Locked verb and field mechanics (`v(f)` stamp / allowlist / templates) | FOCUS, SCOPE, COORD, PRM, OUTPUT schema |
| **FLAG** | Cause-fit accept/reject nuance for the locked `dtp_flag` only | Preferred `none` outcome, PRM module calibrations, ACTION field mechanics |
| **CONTEXT** | Clinical and enrichment evidence (chart, assessments, research, DDI, prior acceptances, phase-1 result) | Process contracts, ACTION locks, OUTPUT schemas |
| **OUTPUT** | Return contract: JSON schema, field constraints, examples | DEFAULT process, FOCUS, SCOPE, COORD, PRM, ACTION |

## Assembly rules that affect reading

1. **First actor builds `CONTEXT` once** for an attempt. Critics and revision actors **inherit** that exact `## SEGMENT [CONTEXT]` string and only add role-specific deltas.
2. **Empty overlay → omitted.** A missing COORD or FLAG segment is normal, not an error.
3. **Chart construction** (extract Collect/Check, linking) uses a lighter labeling pattern and is documented separately — it is not the nine-segment PRM stack.
4. **Pass number** (Minnesota cause class 1–7) changes FOCUS / SCOPE / PRM / ACTION / CONTEXT *content*, not the segment *skeleton*.

## Mental model

```text
┌─────────────────────────────────────────────────────────┐
│ DEFAULT          role-owned process contract            │
├─────────────────────────────────────────────────────────┤
│ FOCUS · SCOPE · COORD · PRM     clinical/module overlays│
├─────────────────────────────────────────────────────────┤
│ ACTION · FLAG                   verb lock / cause-fit   │
├─────────────────────────────────────────────────────────┤
│ CONTEXT                      evidence (inherited later) │
├─────────────────────────────────────────────────────────┤
│ OUTPUT                       return schema              │
└─────────────────────────────────────────────────────────┘
```
