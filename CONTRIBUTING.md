# Contributing — adding a decision record

1. Copy `data/example.json` to `data/<short-name>.json`.
2. Fill the `decision_object` and `learning_ledger` blocks.
3. Keep values as short factual strings; confidence in `decision_object` notes.
4. Validate: `python3 tools/validate.py data/<short-name>.json`
5. Commit. Never mutate history; append new episodes. A `rule_version` bump is required
 whenever `learning_ledger.rule_update` changes reusable logic.
