# RepoFlow Sanitized Open-Source Data Package

This directory is a sanitized open-source-only subset of the RepoFlow paper data package. It keeps the artifacts needed to inspect the open-source benchmark results, dataset analytics, motivating example, and human-audit support package while excluding private/proprietary data and local machine metadata.

## Included

- `motivating_examples/`
  Compact motivating example evidence and static viewer payload.
- `human_audit/repoflow_clean_success_375/`
  Human-audit CSV, metadata, viewer payloads, and the viewer server script for the 375 LLM-audit-passing clean successes. This is the only retained executable helper code.
- `results/migration_run_results_20260624/`
  Compact open-source migration outputs for the full 594-case dataset and the seed-42 150-case subset. Each run contains `results.jsonl`, `description.md`, and repository-relative diff files.
- `analysis/dataset_characteristics/outputs/`
  Generated dataset-characteristics output for the open-source benchmark.
- `analysis/migration_characteristics/outputs/`
  Generated migration-output characteristics.
- `analysis/cost_analysis/outputs/`
  Generated seed-42 150-case cost summaries and figure.
- `analysis/figures/outputs/`
  Generated figure data and rendered SVG/PNG figures for the open-source comparisons.

## Excluded

This copy intentionally excludes proprietary/private data, Git metadata, processing/rebuild code except the human-audit viewer server, raw local run roots, overlays, venvs, caches, and local machine paths.

## Human Audit Viewer

```bash
cd human_audit/repoflow_clean_success_375/viewer
python3 serve.py --host 0.0.0.0 --port 8765
```

Then open `http://<machine-address>:8765/index.html`.

## Integrity

- `MANIFEST.json` records package scope, exclusions, and run-level counts.
- `SHA256SUMS.txt` records checksums for files in this sanitized copy.
