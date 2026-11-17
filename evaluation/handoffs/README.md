# Chart handoffs

Staged recommendations that use an earlier acceptance in the same note. This is the count behind the "Chart the next cause reads" subsection of the manuscript Results.

A **handoff** is a changed staged row, after the first acceptance in its note, whose recommendation uses an earlier acceptance as a chart fact:

- **(a)** it names a product an earlier row added or switched to, and that product is not on the note's starting medication list; or
- **(b)** it names a product an earlier row stopped or switched away from, and the text states that the change was made.

| File | Role |
|------|------|
| `count_handoffs.py` | Proposes candidates from `../derived/rows_remedia.csv` by string match; writes the summary from the decisions |
| `handoff_candidates.csv` | One row per candidate: case, order, kind, product, the earlier acceptance, and the sentence that names it |
| `handoff_decisions.csv` | Reading of each candidate: kept yes/no, with a one-line reason |
| `handoff_summary.csv` | Counts from the kept candidates |

Run `python count_handoffs.py` from this folder. The script stops if a candidate has no decision.

The count shows that a later recommendation used an earlier acceptance, which reaches the later call through both the updated chart and the list of accepted changes; it does not separate the two. It does not show that the recommendation would differ without that update, and the specialist grade in `rec_evaluation` is descriptive only.
