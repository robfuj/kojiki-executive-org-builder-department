# S9 + S7 Schema — Executive Org Builder

This line records every decision with the **shared canonical schemas** (mirrored
from `00-kojiki-ontology`). Do not redefine fields locally.

## Decision Object — `schema/decision-object.json`
| `decision_id` |
| `decision_name` |
| `owning_function` |
| `decision_owner_role` |
| `trigger_condition` |
| `current_state` |
| `required_inputs` |
| `evidence_threshold` |
| `available_options` |
| `decision_criteria` |
| `constraints` |
| `risk_level` |
| `delegation_level` |
| `escalation_conditions` |
| `expected_outcome` |
| `verification_method` |
| `actual_outcome` |
| `learning_extracted` |
| `rule_version` |
| `last_reviewed` |

## Learning Ledger — `schema/learning-ledger.json`
| `case` |
| `decision` |
| `assumption` |
| `action` |
| `expected_result` |
| `actual_result` |
| `variance` |
| `cause` |
| `learning` |
| `rule_update` |

## This line's mapping
- `operating_tree` stages → Decision Object `current_state` / `trigger_condition`
- `decision_states` → Decision Object `current_state` lifecycle
- Every case → a Learning Ledger entry + a `rule_version` update

## Validation
`python3 tools/validate.py data/<name>.json` checks both schemas + orientation-ready fields.
