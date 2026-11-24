# Prompt sheet — how to read this folder

Companion to the RemedIA manuscript and evaluation archive. This is a **structural map** of LLM prompts: agent family → role → which labeled segments are inserted → which clinical blocks fill `CONTEXT`. It does **not** dump full prompt bodies (those remain in private source / optional large run trees).

## Display order (read top-down)

| File | What it answers |
|------|-----------------|
| [`00_architecture.md`](00_architecture.md) | How a prompt is assembled; the nine `## SEGMENT […]` layers |
| [`01_role_matrix.md`](01_role_matrix.md) | One matrix: every role × which segments appear |
| [`02_chart_construction.md`](02_chart_construction.md) | Extract Collect/Check + linking (outside the PRM segment system) |
| [`03_detection.md`](03_detection.md) | Phase-1 detection actor / critic / revision |
| [`04_recommendation.md`](04_recommendation.md) | Phase-2 recommendation actor / revision / three critics |
| [`05_context_blocks.md`](05_context_blocks.md) | Structural items that fill `CONTEXT` (manifest block IDs) |
| [`06_special_and_retired.md`](06_special_and_retired.md) | Dose proposal, DTP validity, retired assessment roles |

## Categorization rationale

1. **Family first** (chart → detection → recommendation → special), matching pipeline order in the manuscript.
2. **Role second** (actor / revision / critic), matching who owns `DEFAULT`.
3. **Segments third** (process overlays vs evidence vs return schema), so a reader sees *what kind of text* is injected before *which clinical facts*.
4. **`CONTEXT` blocks last**, because they vary by PRM and stance while the segment skeleton stays fixed.

## Legend used everywhere

| Mark | Meaning |
|------|---------|
| **Y** | Typically present when that role is assembled |
| **O** | Optional / trigger-gated (empty → segment omitted) |
| **—** | Not used by that role’s builder |
| **U** | Present as unlabeled prose (not wrapped in `## SEGMENT […]`) |

## Source of truth (private repo)

| Concern | Path in `med-agents` |
|---------|----------------------|
| Segment names, roles, DEFAULT bodies | `Pharmacotherapy_agentic_v4/app/vf/prm/prm_prompt_segments.py` |
| CONTEXT manifests | `…/prm/filtering/prompt_manifests.py` |
| CONTEXT composer | `…/prm/prm_prompt_compose.py` |
| Chart extract / link | `…/vf/extract/`, `…/vf/link/chart_links.py` |

Internal audit notes (more verbose): `Pharmacotherapy_agentic_v4/docs/PRM_PROMPT_STANCE_INVENTORY.md`.
