# Repository exclusions before migration

This table documents 93 excluded migration cases across 18 repository snapshots: seven cases with an unavailable upstream commit, followed by 86 cases across 17 repositories that did not meet the archived baseline reproducibility requirement.

The requirement was at least 90% of the original tests passing in the reproduction environment. The `PASS_80` and `FAIL_80` values in the CSV are legacy status labels from the archived report; they do not change the 90% selection threshold. All numeric outcomes listed below are below 90%. These are historical screening results, not a claim that the repositories cannot run in any other environment or at a later date.

| Repository snapshot | Migration cases | Archived baseline result | Recorded reason |
| --- | ---: | --- | --- |
| `aio-libs/aiosmtpd@3615f5ef` | 1 | NO_COUNTS | Pytest collection did not produce usable counts because current dependency/tooling behavior turned a conftest import path into an import failure. |
| `alanhamlett/pip-update-requirements@e407b929` | 2 | 0/1 | The project depends on old pip internals that are no longer available in the reproduced environment, so tests fail during collection. |
| `avinassh/haxor@8c0cb6be` | 7 | NO_TESTS | The repository did not yield a usable baseline test set because pytest collection failed under the current pytest/plugin stack. |
| `codewithemad/apyrat@de1852d8` | 8 | 1/8 | The baseline tests rely on live media/API responses; the external endpoint returned an HTTP gateway failure and invalid JSON. |
| `esds-leipzig/sen2nbar@1ecded1e` | 6 | 0/5 | The baseline tests depend on current STAC/Sentinel metadata whose CRS/projection fields no longer match the test assumptions. |
| `gugarosa/learnergy@870d8a6b` | 3 | TIMEOUT | The baseline test suite did not finish within the reproduction timeout, so no stable pass count was available. |
| `haidra-org/ai-horde-styles@1221207a` | 6 | 2/3 | The tests rely on a model/style reference catalog that drifted from the expected baseline contents. |
| `irahorecka/comics@47a0b5c2` | 7 | missing_commit_upstream | The recorded upstream repository commit could not be retrieved during setup. |
| `j4asper/dmr.py@8f335fd5` | 7 | 9/13 | The tests assert values parsed from live vehicle/registry data that changed or disappeared since the original artifact. |
| `jaldekoa/bcra-wrapper@73c84046` | 6 | 0/1 | Test collection performs a live HTTPS call to the BCRA API, and certificate verification failed in the reproduction environment. |
| `jannisborn/paperscraper@fa7c5e26` | 8 | 37/47 | The tests depend on live scholarly services and current metadata whose responses changed or became inaccessible. |
| `metlife/ocspchecker@c9db90c5` | 1 | 36/41 | Certificate-chain and OCSP responder tests rely on live certificate state that changed since the artifact was created. |
| `paytmmoney/pypmclient@8f966de0` | 3 | 89/116 | The baseline fails under the current dependency/API behavior because the project calls httpx.HTTPError with an obsolete signature. |
| `saleweaver/rapid-rest-client@79aa8970` | 6 | 4/9 | The tests call live HTTP endpoints that are now blocked or changed, returning a Cloudflare challenge instead of the expected response. |
| `sindrel/nrk-pod-feeds@69b3cf40` | 6 | 11/14 | The tests rely on live NRK podcast/feed data whose seasons and episode records changed. |
| `skyme5/snapchat-dl@9b382d01` | 6 | 12/14 | Downloader tests depend on an external sample media host that timed out during reproduction. |
| `texzk/hexrec@a3553b56` | 4 | 1113/1354 | A large set of baseline assertions no longer matches current behavior, especially expected list-vs-tuple record representations. |
| `unpywall/unpywall@7909fde0` | 6 | 23/26 | The tests depend on live Unpaywall/DOI lookup and download behavior whose responses were empty or invalid in reproduction. |

The [case inventory](data/case_inventory.csv) identifies every affected migration. The [machine-readable repository table](data/excluded_repositories.csv) preserves the recorded status and reason categories without local machine paths.

See the [curation reconciliation](README.md) for the distinction between the paper-reported starting count and the downloaded artifact inventory.
