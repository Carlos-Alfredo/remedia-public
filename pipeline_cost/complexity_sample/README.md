# Complexity cost sample (manuscript runtime/cost table)

Five staged replicates on `scot_09_17` (low), `scot_09_04` (medium), `scot_09_08` (high).

| File | Role |
|------|------|
| `table_means.csv` | Wall / recs / calls / USD mean±SD (matches manuscript Table) |
| `per_run_summary.csv` | One row per replicate |
| `call_phase_totals.csv` | Linking + PRM analysis dominate calls |
| `call_site_totals.csv` | Finer call-site roll-up |
| `cost_ledger.json` · `cost_calls.jsonl` | USD reconstruction (thoughts billed as output) |
| `run_configuration.json` | Model / thinking settings |
| `scot_09_*/run_*/04_summary.json` | Per-replicate pipeline summaries |

Full per-run prompt/response JSONL files are omitted (tens of MB).
