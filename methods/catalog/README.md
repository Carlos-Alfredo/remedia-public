# Flag → action catalog

Flag map of the RemedIA workup, as described in the manuscript Methods (passes 1–7, Table III).

- `prm`: the Cipolle pass (1 unnecessary drug therapy, 2 additional drug therapy, 3 ineffective drug, 4 dosage too low, 5 adverse drug reaction, 6 dosage too high, 7 nonadherence).
- `dtp_flag`: the cause detection may return in that pass.
- `primary_action`: the one verb the flag authorizes. Code stamps it, and the recommendation is drafted under it. A flag whose verb is `none` emits no recommendation.
- `defer_to_prm`: for a `none` flag, the later pass that reviews the same line.
