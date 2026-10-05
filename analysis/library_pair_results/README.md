# Open-source migration results by library pair

The full open-source benchmark contains **594 instances across 48 distinct directed source-to-target library pairs** (24 source libraries and 37 target libraries). A to B and B to A are different pairs.

RepoFlow's per-pair success rate ranges from **0.00% to 100.00%**. Pair sizes range from **1 to 58 instances**, so the counts below should be considered alongside the percentages. The overall result is **372/594 (62.63%)**.

Success is the recorded `overall_pass` outcome: regression, deterministic integrity, and agent audit must all pass. These are pipeline acceptance results, not a claim that every accepted migration was independently proved correct. All five configurations below use GPT-5.6 Luna High.

This table covers the full 594-case benchmark, not the separate 150-case subset. SAP per-pair outcomes are not included in this table.

| Source → target | Instances | RepoFlow | LLM-GT | MigrateLib | SWE-agent | PIG |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| aiohttp → httpx | 5 | 3/5 (60.00%) | 2/5 (40.00%) | 2/5 (40.00%) | 3/5 (60.00%) | 2/5 (40.00%) |
| attrs → cattrs | 5 | 5/5 (100.00%) | 0/5 (0.00%) | 1/5 (20.00%) | 1/5 (20.00%) | 0/5 (0.00%) |
| beautifulsoup4 → pyquery | 4 | 3/4 (75.00%) | 0/4 (0.00%) | 1/4 (25.00%) | 2/4 (50.00%) | 0/4 (0.00%) |
| chardet → cchardet | 1 | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) |
| chardet → charset-normalizer | 1 | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) |
| click → plac | 9 | 5/9 (55.56%) | 1/9 (11.11%) | 3/9 (33.33%) | 5/9 (55.56%) | 1/9 (11.11%) |
| click → typer | 9 | 5/9 (55.56%) | 2/9 (22.22%) | 3/9 (33.33%) | 6/9 (66.67%) | 0/9 (0.00%) |
| colorama → rich | 6 | 5/6 (83.33%) | 5/6 (83.33%) | 5/6 (83.33%) | 3/6 (50.00%) | 0/6 (0.00%) |
| colorama → termcolor | 6 | 5/6 (83.33%) | 4/6 (66.67%) | 4/6 (66.67%) | 3/6 (50.00%) | 2/6 (33.33%) |
| cryptography → pycryptodome | 8 | 6/8 (75.00%) | 4/8 (50.00%) | 4/8 (50.00%) | 5/8 (62.50%) | 1/8 (12.50%) |
| fastapi → sanic | 3 | 0/3 (0.00%) | 0/3 (0.00%) | 0/3 (0.00%) | 2/3 (66.67%) | 0/3 (0.00%) |
| filelock → portalocker | 1 | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) |
| flask → bottle | 2 | 2/2 (100.00%) | 2/2 (100.00%) | 2/2 (100.00%) | 2/2 (100.00%) | 1/2 (50.00%) |
| flask → cherrypy | 2 | 2/2 (100.00%) | 1/2 (50.00%) | 0/2 (0.00%) | 1/2 (50.00%) | 1/2 (50.00%) |
| flask → fastapi | 2 | 2/2 (100.00%) | 1/2 (50.00%) | 1/2 (50.00%) | 1/2 (50.00%) | 0/2 (0.00%) |
| flask → sanic | 2 | 2/2 (100.00%) | 1/2 (50.00%) | 2/2 (100.00%) | 2/2 (100.00%) | 1/2 (50.00%) |
| flask → tornado | 2 | 2/2 (100.00%) | 2/2 (100.00%) | 2/2 (100.00%) | 1/2 (50.00%) | 1/2 (50.00%) |
| httpx → aiohttp | 4 | 3/4 (75.00%) | 0/4 (0.00%) | 0/4 (0.00%) | 2/4 (50.00%) | 1/4 (25.00%) |
| httpx → requests | 4 | 3/4 (75.00%) | 3/4 (75.00%) | 2/4 (50.00%) | 1/4 (25.00%) | 3/4 (75.00%) |
| httpx → urllib3 | 4 | 3/4 (75.00%) | 1/4 (25.00%) | 1/4 (25.00%) | 2/4 (50.00%) | 2/4 (50.00%) |
| importlib-metadata → setuptools | 1 | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) | 0/1 (0.00%) | 0/1 (0.00%) |
| jinja2 → mako | 7 | 5/7 (71.43%) | 0/7 (0.00%) | 1/7 (14.29%) | 5/7 (71.43%) | 0/7 (0.00%) |
| jsonschema → cerberus | 7 | 4/7 (57.14%) | 0/7 (0.00%) | 1/7 (14.29%) | 2/7 (28.57%) | 0/7 (0.00%) |
| matplotlib → altair | 16 | 9/16 (56.25%) | 5/16 (31.25%) | 3/16 (18.75%) | 8/16 (50.00%) | 0/16 (0.00%) |
| matplotlib → plotly | 16 | 9/16 (56.25%) | 6/16 (37.50%) | 5/16 (31.25%) | 9/16 (56.25%) | 1/16 (6.25%) |
| matplotlib → seaborn | 16 | 12/16 (75.00%) | 2/16 (12.50%) | 2/16 (12.50%) | 5/16 (31.25%) | 3/16 (18.75%) |
| pygments → rich | 4 | 2/4 (50.00%) | 1/4 (25.00%) | 2/4 (50.00%) | 2/4 (50.00%) | 0/4 (0.00%) |
| python-dotenv → dynaconf | 12 | 11/12 (91.67%) | 5/12 (41.67%) | 3/12 (25.00%) | 11/12 (91.67%) | 2/12 (16.67%) |
| python-dotenv → environs | 12 | 10/12 (83.33%) | 9/12 (75.00%) | 10/12 (83.33%) | 8/12 (66.67%) | 9/12 (75.00%) |
| requests → aiohttp | 57 | 29/57 (50.88%) | 4/57 (7.02%) | 6/57 (10.53%) | 25/57 (43.86%) | 3/57 (5.26%) |
| requests → httpx | 56 | 32/56 (57.14%) | 18/56 (32.14%) | 15/56 (26.79%) | 21/56 (37.50%) | 10/56 (17.86%) |
| requests → pycurl | 58 | 28/58 (48.28%) | 17/58 (29.31%) | 14/58 (24.14%) | 23/58 (39.66%) | 2/58 (3.45%) |
| requests → requests_futures | 57 | 42/57 (73.68%) | 14/57 (24.56%) | 11/57 (19.30%) | 17/57 (29.82%) | 3/57 (5.26%) |
| requests → treq | 58 | 30/58 (51.72%) | 6/58 (10.34%) | 3/58 (5.17%) | 23/58 (39.66%) | 3/58 (5.17%) |
| requests → urllib3 | 58 | 31/58 (53.45%) | 15/58 (25.86%) | 13/58 (22.41%) | 26/58 (44.83%) | 8/58 (13.79%) |
| seaborn → altair | 4 | 2/4 (50.00%) | 0/4 (0.00%) | 1/4 (25.00%) | 2/4 (50.00%) | 0/4 (0.00%) |
| seaborn → plotly | 5 | 2/5 (40.00%) | 1/5 (20.00%) | 2/5 (40.00%) | 3/5 (60.00%) | 0/5 (0.00%) |
| sqlalchemy → sqlobject | 2 | 1/2 (50.00%) | 0/2 (0.00%) | 1/2 (50.00%) | 0/2 (0.00%) | 0/2 (0.00%) |
| sqlalchemy → tortoise-orm | 2 | 1/2 (50.00%) | 0/2 (0.00%) | 1/2 (50.00%) | 0/2 (0.00%) | 1/2 (50.00%) |
| tabulate → prettytable | 5 | 5/5 (100.00%) | 1/5 (20.00%) | 1/5 (20.00%) | 3/5 (60.00%) | 0/5 (0.00%) |
| tabulate → rich | 5 | 5/5 (100.00%) | 0/5 (0.00%) | 0/5 (0.00%) | 3/5 (60.00%) | 0/5 (0.00%) |
| toml → tomli | 6 | 5/6 (83.33%) | 3/6 (50.00%) | 3/6 (50.00%) | 5/6 (83.33%) | 1/6 (16.67%) |
| toml → tomlkit | 6 | 5/6 (83.33%) | 4/6 (66.67%) | 2/6 (33.33%) | 4/6 (66.67%) | 1/6 (16.67%) |
| tqdm → alive-progress | 13 | 10/13 (76.92%) | 10/13 (76.92%) | 10/13 (76.92%) | 9/13 (69.23%) | 4/13 (30.77%) |
| tqdm → progressbar2 | 13 | 10/13 (76.92%) | 11/13 (84.62%) | 10/13 (76.92%) | 9/13 (69.23%) | 5/13 (38.46%) |
| urllib3 → aiohttp | 6 | 4/6 (66.67%) | 1/6 (16.67%) | 1/6 (16.67%) | 2/6 (33.33%) | 1/6 (16.67%) |
| urllib3 → httpx | 6 | 4/6 (66.67%) | 1/6 (16.67%) | 1/6 (16.67%) | 3/6 (50.00%) | 1/6 (16.67%) |
| urllib3 → requests | 6 | 4/6 (66.67%) | 1/6 (16.67%) | 1/6 (16.67%) | 2/6 (33.33%) | 2/6 (33.33%) |

Totals: RepoFlow 372/594 (62.63%); LLM-GT 168/594 (28.28%); MigrateLib 160/594 (26.94%); SWE-agent 275/594 (46.30%); PIG 79/594 (13.30%).

## Data and verification

- [Machine-readable pair results](data/pair_results.csv): 240 rows, one for each of the 48 pairs and five configurations.
- [Verification and source hashes](verification.json): source paths, hashes, counts, and acceptance totals.
- [Published per-case results](../../results/migration_run_results_20260624/full_594): the underlying outcome records.

The summary was recomputed from the included per-case records. All five configurations contain exactly the same 594 unique case IDs; every accepted outcome passes all three gates; and all pair counts and accepted counts sum to the reported totals. No case, outcome, or experiment was changed.
