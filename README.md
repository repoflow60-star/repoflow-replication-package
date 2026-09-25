# RepoFlow Open-Source Replication Package

This repository is the sanitized open-source replication package for the RepoFlow paper. It contains the artifacts needed to inspect the open-source benchmark results, dataset analytics, motivating example, and human-audit support package.

The package is intended for public release. It excludes private/proprietary benchmark data, raw execution workspaces, virtual environments, overlay filesystems, local machine paths, Git history from the source artifact tree, credentials, and processing/rebuild code except for the small local human-audit viewer.

## Repository Layout

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

## Benchmark Curation

The [curation report](analysis/dataset_curation/README.md) provides the complete case inventory, exclusion reasons, and corrected count reconciliation. It explains the difference between the upstream paper's reported starting count and the available artifact, while confirming that the published 594-case evaluation set is unchanged.

## Data Scope

Included benchmark artifacts are limited to open-source repository cases. The package intentionally excludes proprietary/private data, local raw-run roots, overlays, venvs, caches, and local machine metadata.

Repository-relative diffs may contain variable names, comments, or paths that originally appeared in public open-source repositories. These are retained as benchmark evidence. Local execution paths and credential provenance strings from our environment are not retained.

## Human Audit Viewer

```bash
cd human_audit/repoflow_clean_success_375/viewer
python3 serve.py --host 0.0.0.0 --port 8765
```

Then open `http://<machine-address>:8765/index.html`.

## Integrity

- `MANIFEST.json` records package scope, exclusions, and run-level counts.
- `SHA256SUMS.txt` records checksums for files in this sanitized copy.

To verify checksums:

```bash
sha256sum -c SHA256SUMS.txt
```

## Results by library pair

The [library-pair breakdown](analysis/library_pair_results/README.md) reports instance counts and success rates for all 48 directed pairs in the full 594-case open-source benchmark, for RepoFlow and all three baselines. CSV data and source-hash verification are included.
