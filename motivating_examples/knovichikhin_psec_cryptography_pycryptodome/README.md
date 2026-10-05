# psec: `cryptography` to `pycryptodome`

Case ID:

`knovichikhin@psec__7c71610b__cryptography__pycryptodome`

This is a motivating example for an iterative API migration where the final Agentic-RepoFlow candidate succeeds and the comparison outputs do not.

## Why This Is A Clean Example

- The migration is a direct replacement of `cryptography` primitives with PyCryptodome primitives.
- The final migration does not keep a source-library compatibility alias.
- The baseline test suite has `473 / 473` passing tests.
- Agentic-RepoFlow reaches `473 / 473` passing tests in cycle 3.
- Intermediate cycles expose real semantic migration issues, mostly around DES/TDES behavior.
- The no-context ablation reaches cycle 5 but still has `60` pass-to-fail regressions.
- Codex and migratelib both attempt the migration but fail the regression criteria.

## Directory Layout

- `viewer/`
  - Static HTML viewer for comparing original, Agentic-RepoFlow cycles, Codex, and migratelib outputs.
  - Open `viewer/index.html` directly or serve it with `python3 -m http.server`.
- `build_viewer.py`
  - Script used to build the viewer from the local experiment artifacts.
  - The generated viewer is already included.
- `evidence/original/`
  - Original pre-migration source files used in the viewer.
- `evidence/agentic_repoflow/`
  - Agentic-RepoFlow result, final diff, per-cycle diffs, test summaries, regression summaries, and integrity-check outputs.
- `evidence/no_context_ablation/`
  - Matching no-context ablation output, including cycle 1-5 diffs, final generated files, test summaries, regression summaries, and integrity-check outputs.
- `evidence/codex/`
  - Codex output diff, result/acceptance files, test summaries, final message, and changed production files.
- `evidence/migratelib/`
  - migratelib report/log/test report and generated production files.

## Key Outcome

| Output | Tests | Status |
| --- | ---: | --- |
| Original baseline | 473 / 473 | pass |
| Agentic-RepoFlow Cycle 1 | 409 / 473 | fail |
| Agentic-RepoFlow Cycle 2 | 470 / 473 | fail |
| Agentic-RepoFlow Cycle 3 (Final) | 473 / 473 | pass |
| No-context ablation Cycle 5 (Final) | 413 / 473 | fail |
| Codex | 0 / 16 runnable cases | fail |
| migratelib | 409 / 473 | fail |

## View Locally

```bash
cd viewer
python3 -m http.server 8776 --bind 0.0.0.0
```

Then open:

`http://<machine-address>:8776/`
