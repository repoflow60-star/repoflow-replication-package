# Benchmark curation

The Open-Source Benchmark contains **594 migration instances across 151 repositories**. The exclusion reasons and counts below match Table 2 of the paper.

| Reason for exclusion | Excluded tasks |
| --- | ---: |
| Repository commit unavailable | 7 |
| Baseline tests could not run or meet the pass threshold | 86 |
| Source-library API calls originating in test code | 24 |
| No source-library API usage in editable code | 12 |

Exclusions apply to migration tasks. Source-library API calls originating in test code would require changing tests; the evaluation keeps the original tests unchanged.

## Case records

- [Case inventory](data/case_inventory.csv): migration tasks and their dispositions.
- [Filtering counts](data/filtering_counts.csv): case counts at each filtering stage.
- [Repository exclusion report](excluded_repositories.md) and [CSV](data/excluded_repositories.csv): unavailable commits and baseline-test failures.
- [Test-code API exclusions](data/test_selection_exclusions.csv): the 24 affected tasks.
- [No editable source-API usage](data/dependency_only_exclusions.csv): the 12 affected tasks.
- [Source manifest](source_manifest.json) and [verification](verification.json): source checksums and case-inventory checks.
