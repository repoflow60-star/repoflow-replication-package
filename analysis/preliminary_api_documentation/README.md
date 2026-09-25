# Preliminary API-reference documentation experiment

This historical experiment compared documentation enabled and disabled in an early file-level migration-and-repair prototype, before the final RepoFlow agentic evaluation. It is supplementary evidence, not an additional ablation of the final paper's system.

## Design

Two completed runs used the same **134 open-source migration cases**, spanning **48 directed library pairs and 84 repositories**, and the same saved case configurations. Both used GPT-5.4-mini, temperature 0, an initial generation plus up to 20 repair attempts (21 cycles), and a 3,600-second whole-case timeout. The pipeline configurations differ only in their names and the three API-reference enablement switches. The runs occurred sequentially on May 3–4, 2026 (UTC).

The enabled configuration supplied source-API signatures and available docstrings, and supplied target-API references grounded in failure evidence during repair. The API-reference resolver used installed library objects; descriptions were capped at 400 characters per entry. This was local API-reference injection, not online documentation retrieval, a curated source-to-target API mapping, or a retrieval-augmented documentation system. The earlier prototype's optional pre-migration dynamic-behavior context was disabled in both arms; this switch is different from the final paper's dynamic integrity validation.

The saved prompts confirm that documentation was actually supplied: the enabled run contains 776 prompt files with source-reference sections and 509 with target-reference sections. The disabled run contains 727 prompt files, with neither section. Prompt counts differ because the runs follow different repair trajectories. Some references resolve only partially; source and target resolution counts are recorded in `verification.json`.

## Results

| Configuration | Recorded successes | Rate | Failed | No-op | Timeout |
| --- | ---: | ---: | ---: | ---: | ---: |
| API references enabled |111/134|82.84%|18|3|2|
| API references disabled |116/134|86.57%|12|3|3|

Both runs recorded success on 106 cases. Documentation alone succeeded on 5 cases; the disabled configuration alone succeeded on 10; neither succeeded on 13. Documentation therefore did not improve the aggregate recorded success in this comparison, although it helped some individual cases. This is one run per configuration and does not establish that documentation has no benefit in general.

**Metric boundary:** `recorded_success` reproduces the historical runner's `status=success`, corroborated by a saved passing post-migration assessment. The prototype used its then-current regression and test-dependent-failure-exclusion policy. These outputs have not been evaluated with the final paper's deterministic integrity checks and LLM audit. Thus these percentages must not be described as the final paper's accepted-migration accuracy or directly compared with its 375/594 result. The historical 134-case set overlaps the final 594-case benchmark on 122 cases; 12 historical cases are outside that final set. No-op cases remain in the denominator and are not successes.

This study supports a bounded statement: the tested local API-reference mechanism did not improve aggregate recorded success in this preliminary comparison. It does not test live web access, comprehensive/version-pinned manuals, explicit source-to-target mappings, or their integration into the final RepoFlow implementation.

## Data and verification

- [Run summary](data/run_summary.csv): counts for both configurations.
- [Per-case results](data/per_case_results.csv): all 268 run/case records, including no-op and unsuccessful cases.
- [Cycle assessments](data/cycle_assessments.csv): saved per-cycle assessment labels and original evidence hashes.
- [Saved run settings](data/run_settings.json): both pipeline configurations and execution settings.
- [Verification](verification.json): case-set reconciliation, paired outcomes, actual prompt evidence, and source hashes.

All totals were recomputed from the saved individual results and independently matched against passing cycle assessments. Publishing this historical analysis does not change any existing benchmark case or published outcome. Original machine paths, raw prompts, environments, and credentials are omitted.
