# Omitted large artifacts

Deliberately **not** published in this companion archive:

- Full per-run `llm_io.jsonl` trees for the complexity sample (~50 MB of prompts/responses)
- Private RemedIA pipeline source (`med-agents`)
- Chase comparator arm (not specialist-graded for the paper)
- Ground-truth SOTA coding side study

Call counts and USD for the published cost table are reconstructible from
`pipeline_cost/complexity_sample/cost_calls.jsonl`, `cost_ledger.json`, and each run’s `04_summary.json` without prompt/response bodies.
