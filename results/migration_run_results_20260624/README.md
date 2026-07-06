# Migration Run Results

This module contains simplified migration run outputs for the full 594-case comparison set and the 150-case ablation subset.

For each run, `results.jsonl` contains one record per case with:

- `case_id`
- `regression_pass`
- `deterministic_pass`
- `agent_audit_pass`
- `overall_pass`

A skipped or unperformed gate is encoded as JSON `null`; failed performed gates are `false`.

Per-file unified diffs are stored separately under `diffs/<case_id>/` inside each run directory. The diff file path and the diff headers use repository-relative paths.

## Accuracy Summary

| Scope | Run | Regression | Deterministic | Agent audit | Overall |
|---|---|---:|---:|---:|---:|
| `full_594` | `full_594/agentic_repoflow_opencode_gpt54mini_606`<br>Agentic-RepoFlow full iterative | 379/594 (63.80%) | 379/594 (63.80%) | 375/594 (63.13%) | 375/594 (63.13%) |
| `full_594` | `full_594/agentic_repoflow_initial_candidate_opencode_gpt54mini_606`<br>Agentic-RepoFlow first cycle only | 239/594 (40.24%) | 239/594 (40.24%) | 239/594 (40.24%) | 239/594 (40.24%) |
| `full_594` | `full_594/llm_gt_pymigbench_gpt54mini`<br>LLM-GT / PyMigBench GPT-5.4-mini | 194/594 (32.66%) | 179/594 (30.13%) | 163/594 (27.44%) | 163/594 (27.44%) |
| `full_594` | `full_594/migratelib_gpt54mini`<br>migratelib GPT-5.4-mini | 215/594 (36.20%) | 183/594 (30.81%) | 173/594 (29.12%) | 173/594 (29.12%) |
| `full_594` | `full_594/codex_gpt54mini_plain_prompt`<br>Codex GPT-5.4-mini plain prompt | 436/594 (73.40%) | 128/594 (21.55%) | 120/594 (20.20%) | 120/594 (20.20%) |
| `seed42_150` | `seed42_150/agentic_repoflow_opencode_gpt54mini_606`<br>Agentic-RepoFlow full iterative | 94/150 (62.67%) | 94/150 (62.67%) | 93/150 (62.00%) | 93/150 (62.00%) |
| `seed42_150` | `seed42_150/agentic_repoflow_initial_candidate_opencode_gpt54mini_606`<br>Agentic-RepoFlow first cycle only | 63/150 (42.00%) | 63/150 (42.00%) | 63/150 (42.00%) | 63/150 (42.00%) |
| `seed42_150` | `seed42_150/llm_gt_pymigbench_gpt54mini`<br>LLM-GT / PyMigBench GPT-5.4-mini | 57/150 (38.00%) | 53/150 (35.33%) | 48/150 (32.00%) | 48/150 (32.00%) |
| `seed42_150` | `seed42_150/migratelib_gpt54mini`<br>migratelib GPT-5.4-mini | 57/150 (38.00%) | 47/150 (31.33%) | 45/150 (30.00%) | 45/150 (30.00%) |
| `seed42_150` | `seed42_150/codex_gpt54mini_plain_prompt`<br>Codex GPT-5.4-mini plain prompt | 100/150 (66.67%) | 27/150 (18.00%) | 25/150 (16.67%) | 25/150 (16.67%) |
| `seed42_150` | `seed42_150/no_migration_context_system_opencode_gpt54mini_20260622`<br>Agentic-RepoFlow no migration context system | 74/150 (49.33%) | 74/150 (49.33%) | 73/150 (48.67%) | 73/150 (48.67%) |
| `seed42_150` | `seed42_150/no_anti_cheat_guardrails_opencode_gpt54mini_20260623`<br>Agentic-RepoFlow no anti-cheat guardrails | 110/150 (73.33%) | 90/150 (60.00%) | 89/150 (59.33%) | 89/150 (59.33%) |
| `seed42_150` | `seed42_150/agentic_repoflow_variation1_same_machine_opencode_gpt54mini_20260623`<br>Agentic-RepoFlow full technique variation 1 | 101/150 (67.33%) | 101/150 (67.33%) | 97/150 (64.67%) | 97/150 (64.67%) |
| `seed42_150` | `seed42_150/agentic_repoflow_variation2_free_machine_opencode_gpt54mini_20260623`<br>Agentic-RepoFlow full technique variation 2 | 96/150 (64.00%) | 96/150 (64.00%) | 95/150 (63.33%) | 95/150 (63.33%) |
| `seed42_150` | `seed42_150/agentic_repoflow_gpt54_seed42_150_20260623`<br>Agentic-RepoFlow GPT-5.4 | 102/150 (68.00%) | 102/150 (68.00%) | 101/150 (67.33%) | 101/150 (67.33%) |
| `seed42_150` | `seed42_150/agentic_repoflow_claude46_sonnet_seed42_150_20260623`<br>Agentic-RepoFlow Claude 4.6 Sonnet | 93/150 (62.00%) | 93/150 (62.00%) | 91/150 (60.67%) | 91/150 (60.67%) |
| `seed42_150` | `seed42_150/agentic_repoflow_max10_true_continuation_opencode_gpt54mini_20260624`<br>Agentic-RepoFlow full iterative max-10 true continuation | 100/150 (66.67%) | 100/150 (66.67%) | 97/150 (64.67%) | 97/150 (64.67%) |

## Run Directories

- `full_594/agentic_repoflow_opencode_gpt54mini_606`: Agentic-RepoFlow full iterative, 375/594 overall pass (63.13%)
- `full_594/agentic_repoflow_initial_candidate_opencode_gpt54mini_606`: Agentic-RepoFlow first cycle only, 239/594 overall pass (40.24%)
- `full_594/llm_gt_pymigbench_gpt54mini`: LLM-GT / PyMigBench GPT-5.4-mini, 163/594 overall pass (27.44%)
- `full_594/migratelib_gpt54mini`: migratelib GPT-5.4-mini, 173/594 overall pass (29.12%)
- `full_594/codex_gpt54mini_plain_prompt`: Codex GPT-5.4-mini plain prompt, 120/594 overall pass (20.20%)
- `seed42_150/agentic_repoflow_opencode_gpt54mini_606`: Agentic-RepoFlow full iterative, 93/150 overall pass (62.00%)
- `seed42_150/agentic_repoflow_initial_candidate_opencode_gpt54mini_606`: Agentic-RepoFlow first cycle only, 63/150 overall pass (42.00%)
- `seed42_150/llm_gt_pymigbench_gpt54mini`: LLM-GT / PyMigBench GPT-5.4-mini, 48/150 overall pass (32.00%)
- `seed42_150/migratelib_gpt54mini`: migratelib GPT-5.4-mini, 45/150 overall pass (30.00%)
- `seed42_150/codex_gpt54mini_plain_prompt`: Codex GPT-5.4-mini plain prompt, 25/150 overall pass (16.67%)
- `seed42_150/no_migration_context_system_opencode_gpt54mini_20260622`: Agentic-RepoFlow no migration context system, 73/150 overall pass (48.67%)
- `seed42_150/no_anti_cheat_guardrails_opencode_gpt54mini_20260623`: Agentic-RepoFlow no anti-cheat guardrails, 89/150 overall pass (59.33%)
- `seed42_150/agentic_repoflow_variation1_same_machine_opencode_gpt54mini_20260623`: Agentic-RepoFlow full technique variation 1, 97/150 overall pass (64.67%)
- `seed42_150/agentic_repoflow_variation2_free_machine_opencode_gpt54mini_20260623`: Agentic-RepoFlow full technique variation 2, 95/150 overall pass (63.33%)
- `seed42_150/agentic_repoflow_gpt54_seed42_150_20260623`: Agentic-RepoFlow GPT-5.4, 101/150 overall pass (67.33%)
- `seed42_150/agentic_repoflow_claude46_sonnet_seed42_150_20260623`: Agentic-RepoFlow Claude 4.6 Sonnet, 91/150 overall pass (60.67%)
- `seed42_150/agentic_repoflow_max10_true_continuation_opencode_gpt54mini_20260624`: Agentic-RepoFlow full iterative max-10 true continuation, 97/150 overall pass (64.67%)
