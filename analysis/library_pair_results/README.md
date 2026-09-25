# Open-source migration results by library pair

The full open-source benchmark contains **594 instances across 48 distinct directed source-to-target library pairs** (24 source libraries and 37 target libraries). A to B and B to A are different pairs.

RepoFlow's per-pair success rate ranges from **0.00% to 100.00%**. Pair sizes range from **1 to 58 instances**, so the counts below should be considered alongside the percentages. The overall result is **375/594 (63.13%)**.

Success is the recorded `overall_pass` outcome: regression, deterministic integrity, and agent audit must all pass. These are pipeline acceptance results, not a claim that every accepted migration was independently proved correct. All four configurations below use GPT-5.4-mini.

This table covers the full 594-case benchmark, not the separate 150-case subset. SAP per-pair outcomes are not included in this table.

| Source → target | Instances | RepoFlow | MigrateLib | LLM-GT | Codex |
| --- | ---: | ---: | ---: | ---: | ---: |
| aiohttp → httpx | 5 | 4/5 (80.00%) | 2/5 (40.00%) | 2/5 (40.00%) | 0/5 (0.00%) |
| attrs → cattrs | 5 | 4/5 (80.00%) | 0/5 (0.00%) | 0/5 (0.00%) | 0/5 (0.00%) |
| beautifulsoup4 → pyquery | 4 | 2/4 (50.00%) | 0/4 (0.00%) | 0/4 (0.00%) | 0/4 (0.00%) |
| chardet → cchardet | 1 | 0/1 (0.00%) | 0/1 (0.00%) | 0/1 (0.00%) | 0/1 (0.00%) |
| chardet → charset-normalizer | 1 | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) |
| click → plac | 9 | 4/9 (44.44%) | 1/9 (11.11%) | 4/9 (44.44%) | 0/9 (0.00%) |
| click → typer | 9 | 4/9 (44.44%) | 3/9 (33.33%) | 1/9 (11.11%) | 0/9 (0.00%) |
| colorama → rich | 6 | 5/6 (83.33%) | 3/6 (50.00%) | 4/6 (66.67%) | 4/6 (66.67%) |
| colorama → termcolor | 6 | 5/6 (83.33%) | 3/6 (50.00%) | 4/6 (66.67%) | 4/6 (66.67%) |
| cryptography → pycryptodome | 8 | 4/8 (50.00%) | 3/8 (37.50%) | 2/8 (25.00%) | 0/8 (0.00%) |
| fastapi → sanic | 3 | 0/3 (0.00%) | 0/3 (0.00%) | 0/3 (0.00%) | 0/3 (0.00%) |
| filelock → portalocker | 1 | 1/1 (100.00%) | 1/1 (100.00%) | 1/1 (100.00%) | 0/1 (0.00%) |
| flask → bottle | 2 | 2/2 (100.00%) | 2/2 (100.00%) | 2/2 (100.00%) | 1/2 (50.00%) |
| flask → cherrypy | 2 | 2/2 (100.00%) | 1/2 (50.00%) | 1/2 (50.00%) | 1/2 (50.00%) |
| flask → fastapi | 2 | 2/2 (100.00%) | 2/2 (100.00%) | 0/2 (0.00%) | 0/2 (0.00%) |
| flask → sanic | 2 | 2/2 (100.00%) | 0/2 (0.00%) | 2/2 (100.00%) | 2/2 (100.00%) |
| flask → tornado | 2 | 2/2 (100.00%) | 1/2 (50.00%) | 1/2 (50.00%) | 0/2 (0.00%) |
| httpx → aiohttp | 4 | 2/4 (50.00%) | 1/4 (25.00%) | 0/4 (0.00%) | 0/4 (0.00%) |
| httpx → requests | 4 | 3/4 (75.00%) | 2/4 (50.00%) | 1/4 (25.00%) | 1/4 (25.00%) |
| httpx → urllib3 | 4 | 2/4 (50.00%) | 1/4 (25.00%) | 1/4 (25.00%) | 2/4 (50.00%) |
| importlib-metadata → setuptools | 1 | 1/1 (100.00%) | 0/1 (0.00%) | 0/1 (0.00%) | 0/1 (0.00%) |
| jinja2 → mako | 7 | 4/7 (57.14%) | 0/7 (0.00%) | 0/7 (0.00%) | 0/7 (0.00%) |
| jsonschema → cerberus | 7 | 4/7 (57.14%) | 1/7 (14.29%) | 0/7 (0.00%) | 1/7 (14.29%) |
| matplotlib → altair | 16 | 11/16 (68.75%) | 5/16 (31.25%) | 6/16 (37.50%) | 4/16 (25.00%) |
| matplotlib → plotly | 16 | 10/16 (62.50%) | 7/16 (43.75%) | 5/16 (31.25%) | 3/16 (18.75%) |
| matplotlib → seaborn | 16 | 13/16 (81.25%) | 1/16 (6.25%) | 3/16 (18.75%) | 2/16 (12.50%) |
| pygments → rich | 4 | 2/4 (50.00%) | 0/4 (0.00%) | 1/4 (25.00%) | 0/4 (0.00%) |
| python-dotenv → dynaconf | 12 | 11/12 (91.67%) | 9/12 (75.00%) | 7/12 (58.33%) | 1/12 (8.33%) |
| python-dotenv → environs | 12 | 10/12 (83.33%) | 7/12 (58.33%) | 7/12 (58.33%) | 1/12 (8.33%) |
| requests → aiohttp | 57 | 33/57 (57.89%) | 14/57 (24.56%) | 4/57 (7.02%) | 8/57 (14.04%) |
| requests → httpx | 56 | 32/56 (57.14%) | 20/56 (35.71%) | 19/56 (33.93%) | 4/56 (7.14%) |
| requests → pycurl | 58 | 35/58 (60.34%) | 9/58 (15.52%) | 12/58 (20.69%) | 18/58 (31.03%) |
| requests → requests_futures | 57 | 40/57 (70.18%) | 13/57 (22.81%) | 17/57 (29.82%) | 0/57 (0.00%) |
| requests → treq | 58 | 31/58 (53.45%) | 7/58 (12.07%) | 7/58 (12.07%) | 5/58 (8.62%) |
| requests → urllib3 | 58 | 34/58 (58.62%) | 12/58 (20.69%) | 13/58 (22.41%) | 30/58 (51.72%) |
| seaborn → altair | 4 | 1/4 (25.00%) | 3/4 (75.00%) | 2/4 (50.00%) | 1/4 (25.00%) |
| seaborn → plotly | 5 | 2/5 (40.00%) | 3/5 (60.00%) | 3/5 (60.00%) | 2/5 (40.00%) |
| sqlalchemy → sqlobject | 2 | 1/2 (50.00%) | 1/2 (50.00%) | 1/2 (50.00%) | 1/2 (50.00%) |
| sqlalchemy → tortoise-orm | 2 | 1/2 (50.00%) | 1/2 (50.00%) | 1/2 (50.00%) | 1/2 (50.00%) |
| tabulate → prettytable | 5 | 3/5 (60.00%) | 1/5 (20.00%) | 1/5 (20.00%) | 1/5 (20.00%) |
| tabulate → rich | 5 | 4/5 (80.00%) | 0/5 (0.00%) | 0/5 (0.00%) | 2/5 (40.00%) |
| toml → tomli | 6 | 5/6 (83.33%) | 3/6 (50.00%) | 2/6 (33.33%) | 2/6 (33.33%) |
| toml → tomlkit | 6 | 5/6 (83.33%) | 3/6 (50.00%) | 3/6 (50.00%) | 0/6 (0.00%) |
| tqdm → alive-progress | 13 | 9/13 (69.23%) | 11/13 (84.62%) | 11/13 (84.62%) | 7/13 (53.85%) |
| tqdm → progressbar2 | 13 | 10/13 (76.92%) | 12/13 (92.31%) | 9/13 (69.23%) | 6/13 (46.15%) |
| urllib3 → aiohttp | 6 | 4/6 (66.67%) | 0/6 (0.00%) | 0/6 (0.00%) | 2/6 (33.33%) |
| urllib3 → httpx | 6 | 4/6 (66.67%) | 1/6 (16.67%) | 1/6 (16.67%) | 1/6 (16.67%) |
| urllib3 → requests | 6 | 4/6 (66.67%) | 2/6 (33.33%) | 1/6 (16.67%) | 1/6 (16.67%) |

Totals: RepoFlow 375/594 (63.13%); MigrateLib 173/594 (29.12%); LLM-GT 163/594 (27.44%); Codex 120/594 (20.20%).

## Data and verification

- [Machine-readable pair results](data/pair_results.csv): 192 rows, one for each of the 48 pairs and four configurations.
- [Verification and source hashes](verification.json): source paths, hashes, counts, and acceptance totals.
- [Published per-case results](../../results/migration_run_results_20260624/full_594): the underlying outcome records.

The summary was recomputed from the existing per-case records. All four configurations contain exactly the same 594 unique case IDs; all recorded overall outcomes agree with the three gates; and all pair counts and accepted counts sum to the published totals. No case, outcome, or experiment was changed.
