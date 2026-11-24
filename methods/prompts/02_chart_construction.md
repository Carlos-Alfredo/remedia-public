# Chart construction prompts

These calls build the linked chart **before** the Pharmacotherapy Workup. They are **not** PRM `ROLE_*` agents and do not use the full nine-segment stack.

Pipeline order: **extract buckets → link relations → (optional enrich) → PRM workup**.

## Extract — Collect / Check per bucket

Each structured bucket runs a Collect–Check loop (up to a fixed round cap). The note text is the primary injected artifact.

| Call site (pattern) | Role | Structural items inserted |
|---------------------|------|---------------------------|
| `vf.extract.list.patient` | Patient demographics | Full note → age/sex fields |
| `…diagnosis.collect` / `.check` | Diagnosis list | Note + current accepted diagnosis list |
| `…history.collect` / `.check` | History list | Note + current accepted history list |
| `…course.collect` / `.check` | Course / issues list | Note + current accepted issues |
| `…prevention.collect` / `.check` (+ `.review`) | Prevention list | Note + current accepted preventions |
| `…exam.collect` / `.check` | Exams / labs / vitals | Note + current accepted exams |
| `…care_facts.collect` / `.check` | Care facts | Note + current accepted care facts |
| `…mar.collect` / `.check` | Medication lines (MAR) | Note + current accepted medication lines |

**Buckets** (canonical set): diagnoses, history, course, prevention, exams, care_facts, medications.

**Labeling:** light `DEFAULT` / `FOCUS` / `OUTPUT` / `CONTEXT` via `plain_segment` where used; the clinical payload is typically `CHART:\n{note}` (or CONTEXT wrapping the note). Check rounds also see the **current accepted list** for that bucket so the model confirms or edits against prior Collect output.

## Linking — list + handshake

| Call site | Role | Structural items inserted |
|-----------|------|---------------------------|
| `link.list` | Propose typed relations from a focus item to candidates | Focus item (kind, name, detail) + target list (`id: name detail`) + relation guide |
| `link.handshake` | Confirm or reject a proposed inverse label | Proposed relation/inverse + reason + focus and target chart lines |

Used for initial chart edges and for re-inferring links when an accepted recommendation adds a product.

## What is *not* in this sheet

Enrichment topic/association/indication/ATC/combination-candidate actor–critics produce research JSON for later `CONTEXT` blocks. They are listed only as **sources** of CONTEXT content in [`05_context_blocks.md`](05_context_blocks.md), not as PRM workup roles.
