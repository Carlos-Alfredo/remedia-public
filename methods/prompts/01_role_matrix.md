# Role × segment matrix

Roles are grouped by pipeline family. Marks: **Y** typical, **O** optional/trigger-gated, **—** unused, **U** unlabeled prose (not a `## SEGMENT` wrapper).

## Chart construction (outside PRM `ROLE_*` set)

See [`02_chart_construction.md`](02_chart_construction.md). Extract uses a light DEFAULT/FOCUS/OUTPUT/CONTEXT labeling; link prompts are free-form call-site templates.

## Detection (phase 1)

| Role | DEFAULT | FOCUS | SCOPE | COORD | PRM | ACTION | FLAG | CONTEXT | OUTPUT |
|------|:-------:|:-----:|:-----:|:-----:|:---:|:------:|:----:|:-------:|:------:|
| `detection_actor` | Y | Y | Y | O | O | — | — | Y | Y |
| `detection_revision_actor` | Y | Y | Y | O | O | — | — | Y† | Y |
| `detection_critic` | Y | Y | Y | O | O | — | O | Y† | Y |

† Prefer inherited first-actor CONTEXT.

Detection never receives **ACTION** (no treatment verb in phase 1).

## Recommendation (phase 2)

| Role | DEFAULT | FOCUS | SCOPE | COORD | PRM | ACTION | FLAG | CONTEXT | OUTPUT |
|------|:-------:|:-----:|:-----:|:-----:|:---:|:------:|:----:|:-------:|:------:|
| `recommendation_actor` | Y | Y | Y | O | — | Y | O | Y | Y |
| `recommendation_revision_actor` | Y | Y | Y | O | — | Y | O | Y† | Y |
| `recommendation_grounding_critic` | Y | — | — | — | — | — | O | Y† | U‡ |
| `recommendation_coverage_critic` | Y | — | — | — | — | — | O | Y† | U‡ |
| `recommendation_safety_critic` | Y | — | — | — | — | — | O | Y† | U‡ |

‡ Critic return contract is unlabeled (`build_critic_contract_prompt`), not `## SEGMENT [OUTPUT]`.

## Special

| Role | DEFAULT | FOCUS | SCOPE | COORD | PRM | ACTION | FLAG | CONTEXT | OUTPUT |
|------|:-------:|:-----:|:-----:|:-----:|:---:|:------:|:----:|:-------:|:------:|
| `dose_proposal_actor` | Y | Y | — | — | — | Y | — | U | Y |
| `dtp_validity_critic` | Y | — | — | — | — | — | — | U | Y |

## Retired assessment roles (DEFAULT bodies exist; not called live)

| Family | Roles | Typical segments when builders were live |
|--------|-------|------------------------------------------|
| Focus test / symptom / risk assessment | `*_assessment_actor`, `*_revision_actor`, `*_critic` | DEFAULT + FOCUS + thin PRM + unlabeled evidence + OUTPUT |
| Global patient risk assessment | `global_risk_assessment_*` | DEFAULT only in registry; no live assembler |

Details: [`06_special_and_retired.md`](06_special_and_retired.md).

## Role → job (one line)

| Role | Job |
|------|-----|
| `detection_actor` | Decide whether a DTP in this pass applies; pick cause flag; no treatment verb |
| `detection_revision_actor` | Rewrite detection after critic rejection |
| `detection_critic` | Fact/logic check on detection JSON only |
| `recommendation_actor` | Draft one action under the stamped verb for the locked flag |
| `recommendation_revision_actor` | Rewrite draft after critic rejection |
| `recommendation_grounding_critic` | Chart identity / invention only |
| `recommendation_coverage_critic` | Stakeholder coverage for the locked DTP only |
| `recommendation_safety_critic` | Net clinical harm / safety checklist |
| `dose_proposal_actor` | Chart-completion dose/frequency fill (no phase-1 DTP) |
| `dtp_validity_critic` | Mid-wave re-check that an earlier DTP still holds on the updated chart |
