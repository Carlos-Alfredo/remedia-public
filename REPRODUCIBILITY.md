# Reproducibility pin

Locked evaluation values cited in the manuscript.

| Item | Value |
|------|--------|
| Staged run date | 14 October 2026 |
| Staged sheets | `model_outputs/remedia_20261014/` |
| Baseline arm | Ong-inspired per-medication prompt (`model_outputs/baseline_ong_inspired_per_medication/`) |
| Specialist workbooks | `specialist_workbooks/specialist_grades_*.xlsx` |
| Cases | `scot_09_01`–`scot_09_26` |
| Complexity sample | `pipeline_cost/complexity_sample/` (5 runs × `scot_09_17` / `scot_09_04` / `scot_09_08`) |
| Baseline suite totals | `pipeline_cost/baseline_time_and_cost.json` (1356.489 s; USD 0.136503) |
| Flag catalog | `methods/catalog/flag_action_catalog.csv` (44 flags) |

## Numeric checks against the manuscript

| Claim | Archive check |
|-------|----------------|
| Staged acceptability 201/305 (65.9%) | `evaluation/tables/overall.csv` |
| Baseline acceptability 260/306 (85.0%) | same |
| Replacement 75 vs 5; discontinue 65 vs 110; keep 92 vs 113 | `evaluation/tables/volume_by_type.csv` |
| 45 of 68 staged FPs in replace+dose | `false_positives_by_action.csv` (27+9+9); non-keep RemedIA FP rows = 68 |
| Cost means ~901 / 1728 / 3462 s; ~209 / 383 / 716 calls; ~0.31 / 0.73 / 1.21 USD | `complexity_sample/table_means.csv` |
| Linking + PRM dominate calls | `call_phase_totals.csv` (linking ≈59%, prm_analysis ≈24%) |
| `scot_09_17` replacements then lithium 800→600 mg | `examples/scot_09_17/specialist_rows_remedia.csv` |
