# RepoFlow Full Clean Success Human Audit Set

This component contains the human-audit sheet and local viewer for all 375 Agentic-RepoFlow full-run cases that passed both repository regression testing and deterministic anti-cheat validation.

## Source

- Run: `agentic_repoflow_opencode_gpt54mini_606`
- Results file: `results/migration_run_results_20260624/full_594/agentic_repoflow_opencode_gpt54mini_606/results.jsonl`
- Selection rule: `regression_pass == true` and `deterministic_pass == true`
- Regression+deterministic selected pool: `379`
- Retained human-review cases: `375`
- LLM audit pass: `375`
- LLM audit reject: `1`
- LLM audit unavailable no-edit/no-op entries: `3`

## Files

- `repoflow_clean_success_375_human_audit.csv`: blank human-review CSV template for the retained cases.
- `metadata.json`: compact provenance and column description.
- `viewer/`: local HTML viewer for the same cases.

## Viewer

The viewer shows the RepoFlow clean-success cases with:

- sequential case index;
- technique label;
- LLM audit reasoning when available;
- side-by-side diff with dark mode and lightweight Python syntax coloring;
- deterministic evidence.

Run it locally with:

```bash
cd human_audit/repoflow_clean_success_375/viewer
python3 serve.py --host 0.0.0.0 --port 8765
```

Then open:

`http://<machine-address>:8765/index.html`

## Columns

1. `index`: sequential case index, `001` through `375`.
2. `name`: benchmark case name / case id.
3. `approach`: technique that produced the clean success.
4. `human audit result (Reviewer 1)`: intentionally blank for Reviewer 1's manual review result.
5. `human audit notes (Reviewer 1)`: intentionally blank for Reviewer 1's manual review notes.
6. `human audit result (Reviewer 2)`: intentionally blank for Reviewer 2's manual review result.
7. `human audit notes (Reviewer 2)`: intentionally blank for Reviewer 2's manual review notes.


## Dropped from Human Review

Four entries from the broader regression+deterministic clean-success pool are excluded from this human-review package because they did not pass the LLM audit gate: one `target_api_not_used` reject and three `not_audited_no_editable_source_api_usage` entries. The dropped case IDs are recorded in `metadata.json`.
