# Codex GPT-5.4-mini plain prompt

Plain-prompt Codex migration run on the 594-case filtered dataset. Restricted to the seed-42 150-case subset.

- Scope: seed42_150
- Cases: 150
- Regression pass: 100/150
- Deterministic pass: 27/150
- Agent audit pass: 25/150
- Overall pass: 25/150 (16.67%)

Each result row contains only the case id, the three gate values, and the overall pass value. Per-file unified diffs are stored under `diffs/<case_id>/`.
