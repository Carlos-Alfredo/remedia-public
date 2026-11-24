# CONTEXT structural blocks

`## SEGMENT [CONTEXT]` holds clinical and enrichment evidence only. Block membership is stance-aware (detection actor vs detection critic vs generation actor vs critic inheritance).

Block IDs below are the composer’s canonical names. Headers are the human-visible leads inside the prompt.

## Block catalog

| Block ID | Typical header / lead-in | Why it exists |
|----------|--------------------------|---------------|
| `chart_pharmacotherapy` | Live chart blob (patient info, diagnoses, preventions, issues, exams, current/added/removed meds, …) | Authoritative MAR + compact accepted recs; refreshed after each acceptance |
| `chart_care_facts` | `STATED CLINICAL CONTEXT:` | Airway / devices / bleed / organ-function barriers |
| `patient_info` | `PATIENT INFORMATION:` | Age, weight, demographics, global risks |
| `patient_symptoms_names` | `PATIENT SYMPTOMS (chart-wide, names only):` | Lightweight symptom index |
| `patient_summary` | `PATIENT SUMMARY (names only):` | Compact name list when full chart absent |
| `target_line` | Target medication section | Single authoritative order row under review |
| `indications` | `DOCUMENTED INDICATIONS…` | Multi-indication coherence |
| `focus_med_enriched_target` / `med_enriched` | `ENRICHED RESEARCH…` / focus-med enrichment | Monograph slice for the target line |
| `focus_meds_siblings_names` | Focus / HP-associated sibling agents | Sibling agents on the same problem |
| `associated_test_enriched` | `ASSOCIATED TEST RESULT ENRICHED RESEARCH:` | Labs supporting the DTP decision |
| `associated_symptom_enriched` | `ASSOCIATED SYMPTOM ENRICHED RESEARCH:` | Symptom response / failure |
| `associated_regimen_meds` | `ASSOCIATED REGIMEN MEDICATION ENRICHED RESEARCH:` | Sibling pharmacology |
| `associated_comorbidities` | `ASSOCIATED COMORBIDITY ENRICHED RESEARCH:` | Comorbidity constraints |
| `enriched_disease` | `ENRICHED DISEASE DATA` | Health-problem / indication disease slice |
| `guidelines` | `CLINICAL GUIDELINE` | Rendered guideline (generation-oriented) |
| `test_assessment` / `symptom_assessment` / `risk_assessment` | `FOCUS … ASSESSMENT:` | Compressed focus evidence (when produced) |
| `all_other_meds` | `ALL OTHER PATIENT MEDICATIONS (names only):` | Fallback names when chart block absent |
| `regimen_names` | `FULL CURRENT REGIMEN` | Fallback when chart pharmacotherapy missing |
| `prior_recommendations` | `RECOMMENDATION HISTORY (accepted this run):` | Earlier acceptances this wave |
| `combination_candidates` | `REGIMEN COMBINATION CANDIDATES…` | FDC / consolidate hints |
| `prm1_combine_advisory` | `PRM 1 COMBINE ADVISORY…` | Exact-match combine advisory for pass 1 |
| `baseline_high_risk_ddi` | `HIGH-RISK BASELINE DDI…` | Major/contraindicated pairs for relevant meds |
| `prm2_regimen_coverage` | `REGIMEN COVERAGE FOR THIS HEALTH PROBLEM…` | Deterministic coverage monitor for pass 2 |
| `phase2_resolution` | `PHASE 2 RESOLUTION` | Generation-oriented resolution guidance (alongside ACTION) |
| `stewardship_hint` | Stewardship / consolidation hint | Prefer `combination_candidates` when both exist |
| `intra_wave` | *(retired as a parallel channel)* | Folded into live chart pharmacotherapy |

## Stance × block intensity (summary)

| Stance | CONTEXT character |
|--------|-------------------|
| **Detection actor** | Full clinical chart + pass-relevant enrichment; **no** generation-only resolution/guideline requirement |
| **Detection critic** | Lean fact-check slices; omit heavy research JSON blobs |
| **Recommendation actor** | Full generation set, including guidelines / phase-2 resolution material + phase-1 result |
| **Recommendation critic / revision** | **Inherit** first-actor CONTEXT; add slim fact snapshot (candidate, target row, flag overlays) — do not re-dump full enrichment |

## Dedup rules (why some blocks disappear)

- When `chart_pharmacotherapy` is present, omit `regimen_names` and `all_other_meds`.
- When target med enrichment is present, omit sibling name-only focus blocks that would duplicate it.
- When enriched symptoms are present, omit names-only symptom lists.
- Baseline combination / DDI chunks append only if their headers are not already in CONTEXT.

## Where enrichment comes from

Upstream enrichment actor–critics (topic, association, indication, ATC, combination candidates) are **not** PRM roles. Their outputs become the `*_enriched` / `combination_candidates` / DDI blocks above.
