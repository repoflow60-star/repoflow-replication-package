# Agentic-RepoFlow no anti-cheat guardrails

Seed-42 150-case ablation with anti-cheat guardrails disabled during generation; outputs were later evaluated with integrity validation and GPT-5.5/high agentic audit.

- Scope: seed42_150
- Cases: 150
- Regression pass: 110/150
- Deterministic pass: 90/150
- Agent audit pass: 89/150
- Overall pass: 89/150 (59.33%)

Each result row contains only the case id, the three gate values, and the overall pass value. Per-file unified diffs are stored under `diffs/<case_id>/`.
