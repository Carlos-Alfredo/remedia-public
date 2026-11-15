# RemedIA — public evaluation artifacts

Companion archive for the IEEE Open Journal of Engineering in Medicine and Biology Technology manuscript on RemedIA.

**Repository:** [github.com/Carlos-Alfredo/remedia-public](https://github.com/Carlos-Alfredo/remedia-public)

**Compared arms:** RemedIA (staged Cipolle pipeline, locked 14 Oct 2026 run) vs Ong-inspired per-medication single-prompt baseline. Chase arm D was not specialist-graded and is not included.

---

## What supports each manuscript pointer

| Manuscript claim | Path |
|------------------|------|
| Full flag → action mappings | [`methods/catalog/flag_action_catalog.csv`](methods/catalog/flag_action_catalog.csv) |
| Worked example `scot_09_17` | [`examples/scot_09_17/`](examples/scot_09_17/) |
| Runtime / cost sample (5×3 notes) | [`pipeline_cost/complexity_sample/`](pipeline_cost/complexity_sample/) |
| Baseline wall time / USD (26 notes) | [`pipeline_cost/sota_arms_time_and_cost.json`](pipeline_cost/sota_arms_time_and_cost.json) |
| Linking + PRM analysis dominate calls | [`pipeline_cost/complexity_sample/call_phase_totals.csv`](pipeline_cost/complexity_sample/call_phase_totals.csv) |
| Verb locks + FP / per-case rates | [`methods/catalog/`](methods/catalog/) · [`evaluation/tables/per_case_rates.csv`](evaluation/tables/per_case_rates.csv) · [`evaluation/tables/false_positives_*.csv`](evaluation/tables/) |
| Specialist workbooks | [`specialist_workbooks/`](specialist_workbooks/) |
| Row-level grades | [`evaluation/derived/`](evaluation/derived/) |
| Manuscript figures (PDF) | [`figures/`](figures/) |

---

## Layout

| Path | Role |
|------|------|
| `specialist_workbooks/` | Specialist-returned Excel (RemedIA + baseline) |
| `evaluation/derived/` | One row per recommendation + gaps |
| `evaluation/tables/` | Aggregates used to build Results tables |
| `evaluation/charts_data/` | Key CSVs for plots / table reconstruction |
| `evaluation/*.md` | Analysis notes (PT) |
| `vignettes/clinical_notes/` | `scot_09_01`–`scot_09_26` inputs |
| `model_outputs/` | Pre-grade pipeline sheets |
| `methods/catalog/` | Flag → primary/allowed verb catalog |
| `methods/manuscript_appendix/` | Full row LaTeX listing |
| `pipeline_cost/` | Arm totals + complexity sample |
| `examples/scot_09_17/` | Worked-example chart + PRM payloads |
| `figures/` | Manuscript PDFs |
| `optional_large_runs/` | What was left out (full LLM JSONL trees) |

Root: this file, `REPRODUCIBILITY.md`.

**Not published:** private `med-agents` source, full multi-MB per-run `llm_io.jsonl` trees, Chase arm D, ground-truth SOTA coding side study.

---

## Citation

Cite `https://github.com/Carlos-Alfredo/remedia-public` with the **release tag or commit** named in the manuscript.
