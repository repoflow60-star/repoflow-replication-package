# Benchmark curation and count reconciliation

This document provides the exclusion reasons and a complete case-level accounting of the open-source benchmark. The published evaluation still contains **594 migration instances across 151 repositories**. No evaluated case, result, or success/failure label is changed by this documentation update.

## Verified count flow

| Stage | Repository snapshots | Migration cases | Cases removed at this stage |
| --- | ---: | ---: | ---: |
| Downloaded MigrateLib artifact | 176 | 723 | — |
| Repository commits available for reproduction | 175 | 716 | 7 |
| Baseline reproducibility requirement met | 158 | 630 | 86 |
| Applicable-test/test-selection filter applied | 154 | 606 | 24 |
| Dependency-only cases removed: published comparison set | 151 | 594 | 12 |

**723 − 7 − 86 − 24 − 12 = 594.**

Every downloaded case appears exactly once in [case_inventory.csv](data/case_inventory.csv), with its disposition and reason. The five groups are disjoint and cover all 723 cases. The retained case IDs match the published `full_594` results exactly.

## Why the earlier summary said 87

The [MigrateLib paper, Section 5.1](https://arxiv.org/html/2510.08810v3#S5.SS1), reports 717 cases across 175 repositories. Both publicly released artifact versions instead contain 723 distinct migration reports across 176 repositories; both inventories match the archived input used for this evaluation. Their checksums and download links are recorded in [source_manifest.json](source_manifest.json).

The earlier curation summary, introduced on June 3, 2026, combined the paper-reported 717 starting cases with the observed 630 reproducible cases and recorded 87 exclusions as fixed summary values. It also described that starting point as being after removal of the unavailable `irahorecka/comics` repository. The case inventory does not support that description: this repository has seven cases, so removing it from the downloaded artifact leaves 716 cases, followed by 86 baseline exclusions.

The value 87 therefore reflects mixed starting counts, rather than a case-level list of 87 baseline exclusions. The accounting above corrects that inconsistency. It does not infer which six artifact cases differ from the upstream paper's reported 717-case evaluation; the released archive does not include the upstream `mig_db/included` selection metadata used by its analysis scripts to define that evaluation set. All 723 available artifact cases are accounted for here without inventing a missing case or changing the retained dataset.

## Exclusion reasons

1. **Unavailable repository commit: seven cases.** The setup log records `irahorecka/comics@47a0b5c2` as `missing_commit_upstream`. These cases could not enter reproduction.
2. **Baseline reproducibility: 86 cases across 17 repositories.** The archived filter required at least 90% of the original tests to pass before migration. The recorded failures concern dependency/API or stale test expectations, environment/tooling or test collection, external services or live data, and a baseline execution timeout. The [repository exclusion report](excluded_repositories.md) lists each repository, its case count, test outcome when available, and recorded reason. These are failures encountered during historical reproduction, not failures of a generated migration.
3. **Applicable-test/test-selection filtering: 24 cases.** The [archived case list](data/test_selection_exclusions.csv) records which cases were removed and labels them `test_selection_applicability`. It does not provide a more detailed per-case explanation or establish that every case required test-code migration. No stronger reason is assigned here.
4. **Dependency-only instances: 12 cases.** The [case list and evidence](data/dependency_only_exclusions.csv) identify cases where the source library appears only in dependency/configuration metadata and has no editable production-code API usage to migrate.

The submitted paper groups the last 36 exclusions as cases requiring test migration. The archived records distinguish 24 test-selection exclusions from 12 dependency-only exclusions; that wording requires correction. The exclusions and final 594-case evaluation set are unchanged.

## Files and verification

- [data/case_inventory.csv](data/case_inventory.csv): all 723 available upstream cases and their dispositions.
- [data/filtering_counts.csv](data/filtering_counts.csv): independently counted stages.
- [excluded_repositories.md](excluded_repositories.md) and [data/excluded_repositories.csv](data/excluded_repositories.csv): repository-level reasons and affected case counts.
- [data/test_selection_exclusions.csv](data/test_selection_exclusions.csv) and [data/dependency_only_exclusions.csv](data/dependency_only_exclusions.csv): archived later-stage exclusions.
- [source_manifest.json](source_manifest.json): source versions, checksums, and evidence provenance.
- [verification.json](verification.json): inventory, partition, and published-result checks.

Verification reads archive entries and recorded case lists; it does not rerun migration experiments. Local machine paths and private repository data are not included.
