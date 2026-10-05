## Running premig
creating venv at <local-artifact-root>/migratelib_full_eval/cases/knovichikhin@psec__7c71610b/repo/.venv
installing dependencies
### running tests
- test finished with status 0, cov finished with status 0
## Running llmmig
## starting llmmig round
- migrating 3 files
### migrating psec/aes.py
### migrating psec/des.py
### migrating psec/mac.py
### running tests
- test finished with status 1, cov finished with status 0
### test diff with round premig
- `psec/cvv.py::psec.cvv.generate_cvv: passed != failed`
- `psec/tr31.py::psec.tr31.KeyBlock.unwrap: passed != failed`
- `psec/tr31.py::psec.tr31.unwrap: passed != failed`
- `tests/test_cvv.py::test_generate_cvv: passed != failed`
- `tests/test_mac.py::test_generate_retail_mac[1-4-3DDE5C55]: passed != failed`
- `tests/test_mac.py::test_generate_retail_mac[1-8-3DDE5C5511661CBF]: passed != failed`
- `tests/test_mac.py::test_generate_retail_mac[1-None-3DDE5C5511661CBF]: passed != failed`
- `tests/test_mac.py::test_generate_retail_mac[2-4-E1694103]: passed != failed`
- `tests/test_mac.py::test_generate_retail_mac[2-8-E16941032C3BC7D4]: passed != failed`
- `tests/test_mac.py::test_generate_retail_mac[2-None-E16941032C3BC7D4]: passed != failed`
- `tests/test_mac.py::test_generate_retail_mac[3-4-BA90F750]: passed != failed`
- `tests/test_mac.py::test_generate_retail_mac[3-8-BA90F750EF43F668]: passed != failed`
- `tests/test_mac.py::test_generate_retail_mac[3-None-BA90F750EF43F668]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[A-D-16--8-72]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[A-D-16-0-72]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[A-D-16-16-72]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[A-D-16-24-88]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[A-D-16-8-72]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[A-D-16-None-88]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[A-D-24-24-88]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[A-D-24-None-88]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[A-D-8-0-56]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[A-D-8-24-88]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[A-D-8-8-56]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[A-D-8-None-88]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[B-T-16--8-80]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[B-T-16-0-80]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[B-T-16-16-80]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[B-T-16-24-96]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[B-T-16-8-80]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[B-T-16-None-96]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[B-T-24-24-96]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[B-T-24-None-96]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[B-T-8-0-64]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[B-T-8-24-96]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[B-T-8-8-64]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[B-T-8-None-96]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[C-T-16--8-72]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[C-T-16-0-72]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[C-T-16-16-72]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[C-T-16-24-88]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[C-T-16-8-72]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[C-T-16-None-88]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[C-T-24-24-88]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[C-T-24-None-88]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[C-T-8-0-56]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[C-T-8-24-88]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[C-T-8-8-56]: passed != failed`
- `tests/test_tr31.py::test_kb_masking_key_length[C-T-8-None-88]: passed != failed`
- `tests/test_tr31.py::test_kb_sanity[A-AAAAAAAABBBBBBBBCCCCCCCC]: passed != failed`
- `tests/test_tr31.py::test_kb_sanity[A-AAAAAAAA]: passed != failed`
- `tests/test_tr31.py::test_kb_sanity[B-AAAAAAAABBBBBBBBCCCCCCCC]: passed != failed`
- `tests/test_tr31.py::test_kb_sanity[C-AAAAAAAABBBBBBBBCCCCCCCC]: passed != failed`
- `tests/test_tr31.py::test_kb_sanity[C-AAAAAAAA]: passed != failed`
- `tests/test_tr31.py::test_kb_unwrap_exceptions[16-A0056M3TC00E0000BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB9AA5BBA6-Key block MAC doesn't match generated MAC.]: passed != failed`
- `tests/test_tr31.py::test_kb_unwrap_exceptions[16-A0056M3TC00E0000C6F4C83842160CBA48D98A1218862857124FAF46-Decrypted key is invalid.]: passed != failed`
- `tests/test_tr31.py::test_kb_unwrap_exceptions[16-A0056M3TC00E0000EF14FD71CFCDCE0630AD5C1CDE0041DCF95CF1D0-Decrypted key is malformed.]: passed != failed`
- `tests/test_tr31.py::test_kb_unwrap_exceptions[16-B0064M3TC00E00000398DC96A5DDB0EF61E26F8935173BD478DF9484050A672A-Decrypted key is malformed.]: passed != failed`
- `tests/test_tr31.py::test_kb_unwrap_exceptions[16-B0064M3TC00E0000BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBFFFFFFFF9AA5BBA6-Key block MAC doesn't match generated MAC.]: passed != failed`
- `tests/test_tr31.py::test_kb_unwrap_exceptions[16-B0064M3TC00E0000F74E0A3502C5CEE07342D5DE9E72135E4A81944F80691F0F-Decrypted key is invalid.]: passed != failed`
- `tests/test_tr31.py::test_kb_unwrap_exceptions[16-C0056M3TC00E000001235EC22408B6CE866746FF992B8707FD7A26D2-Decrypted key is malformed.]: passed != failed`
- `tests/test_tr31.py::test_kb_unwrap_exceptions[16-C0056M3TC00E0000BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB9AA5BBA6-Key block MAC doesn't match generated MAC.]: passed != failed`
- `tests/test_tr31.py::test_kb_unwrap_exceptions[16-C0056M3TC00E0000F71573EB7441BB50A5C4511893AFB37B5B95A4AD-Decrypted key is invalid.]: passed != failed`
- `tests/test_tr31.py::test_wrap_unwrap_functions: passed != failed`
- llmmig finished
## Running merge_skipped
- merge_skipped finished
## Running async_transform
## Running inferred async transform
### Finding async transforms
- Found 0 functions to mark async including 0 tests
- Found 0 calls to await
- async_transform finished
