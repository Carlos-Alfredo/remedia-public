# RemedIA — public evaluation artifacts

Companion archive for the IEEE Open Journal of Engineering in Medicine and Biology Technology manuscript on RemedIA.

**Repository:** [github.com/Carlos-Alfredo/remedia-public](https://github.com/Carlos-Alfredo/remedia-public)

**Compared arms in this archive:** RemedIA (staged Cipolle pipeline, locked 14 Oct 2026 run) vs an Ong-inspired per-medication single-prompt baseline. Chase arm D was not specialist-graded for the paper and is **not** included.

**Not published here:** private RemedIA source (`med-agents`), full multi-MB per-run `llm_io.jsonl` trees, Chase arm D, and the ground-truth SOTA coding side study.

---

## Manuscript → file index

Every `\cite{remediapublic}` / Data Availability pointer in the manuscript maps here:

| Manuscript claim | Path |
|------------------|------|
| Full flag → action mappings | [`methods/catalog/flag_action_catalog.csv`](methods/catalog/flag_action_catalog.csv) ([JSON](methods/catalog/flag_action_catalog.json)) |
| Worked example `scot_09_17` (pass 5 replacements → pass 6 lithium dose cut) | [`examples/scot_09_17/`](examples/scot_09_17/) |
| Runtime / cost sample (5 runs × 3 notes) | [`pipeline_cost/complexity_sample/`](pipeline_cost/complexity_sample/) — means in [`table_means.csv`](pipeline_cost/complexity_sample/table_means.csv) |
| Baseline wall time / USD (26 notes: 1356 s, ≈USD 0.14) | [`pipeline_cost/baseline_time_and_cost.json`](pipeline_cost/baseline_time_and_cost.json) |
| Linking + PRM analysis dominate calls | [`pipeline_cost/complexity_sample/call_phase_totals.csv`](pipeline_cost/complexity_sample/call_phase_totals.csv) |
| Verb locks; 45/68 staged FPs in replace+dose; per-case rates | [`methods/catalog/`](methods/catalog/) · [`evaluation/tables/false_positives_by_action.csv`](evaluation/tables/false_positives_by_action.csv) · [`evaluation/tables/false_positives_changed_rows.csv`](evaluation/tables/false_positives_changed_rows.csv) · [`evaluation/tables/per_case_rates.csv`](evaluation/tables/per_case_rates.csv) · [`evaluation/tables/remedia_false_positives_by_flag.csv`](evaluation/tables/remedia_false_positives_by_flag.csv) |
| Specialist workbooks (graded Excel) | [`specialist_workbooks/specialist_grades_remedia.xlsx`](specialist_workbooks/specialist_grades_remedia.xlsx) · [`specialist_workbooks/specialist_grades_baseline.xlsx`](specialist_workbooks/specialist_grades_baseline.xlsx) |
| Row-level grades used for Results tables | [`evaluation/derived/`](evaluation/derived/) · [`evaluation/tables/`](evaluation/tables/) |
| Teaching vignettes (`scot_09_01`–`26`) | [`vignettes/clinical_notes/`](vignettes/clinical_notes/) |
| Manuscript figure PDFs | [`figures/`](figures/) |

Supporting (not separately cited, but used to rebuild tables):

| Path | Role |
|------|------|
| `evaluation/charts_data/` | Convenience copy of key CSVs from `evaluation/tables/` (same numbers; tables/ is canonical) |
| `evaluation/specialist_analysis_pt.md` | Portuguese narrative of the specialist scoring (source for many aggregates) |
| `evaluation/case_report_pt.md` | Portuguese per-case comparison notes |
| `model_outputs/remedia_20261014/` | Pre-grade RemedIA sheets for the locked run |
| `model_outputs/baseline_ong_inspired_per_medication/` | Pre-grade baseline sheet |
| `methods/manuscript_appendix/appendix_sheets.tex` | Full-row LaTeX listing (optional supplement) |
| `pipeline_cost/complexity_sample/cost_ledger.json` · `cost_calls.jsonl` | Call-level USD reconstruction |
| `optional_large_runs/README.md` | What was deliberately omitted |

---

## Layout

```
specialist_workbooks/     Graded Excel returned by the specialist
evaluation/derived/       One CSV row per recommendation (+ gaps)
evaluation/tables/        Aggregates backing Results
evaluation/charts_data/   Plot-ready subset of tables/
vignettes/clinical_notes/ Input notes scot_09_01–26
model_outputs/            Pre-grade pipeline sheets
methods/catalog/          Flag → primary verb catalog (49 flags)
methods/manuscript_appendix/  Optional full-row TeX
pipeline_cost/            Baseline totals + complexity sample
examples/scot_09_17/      Worked-example chart + PRM payloads
figures/                  Manuscript PDFs
optional_large_runs/      Notes on omitted large trees
```

---

## Citation

Cite `https://github.com/Carlos-Alfredo/remedia-public` with the release tag or commit named in the manuscript bibliography (`remediapublic`).
