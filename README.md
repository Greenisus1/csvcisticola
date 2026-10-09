# Csvcisticola

Read-only CSV column frequency spectrum with source values hidden. Python 3.9+, no dependencies. Published in a private GitHub repository. Download its ZIP while signed into the owner account, extract it and open a terminal inside the source folder. Not verified as store-installed.

```text
python3 csvcisticola.py
python3 csvcisticola.py sample.csv --column 2
python3 csvcisticola.py sample.csv --no-header
python3 -m unittest -v
bash app-store.sh install
bash app-store.sh run
```

Regular UTF-8 (optional BOM) file <=1 MiB. Comma CSV via strict Python reader, quoted multiline cells accepted, standard-library field-size cap applies. First record skipped as header by default (even if empty); --no-header includes it. Column position 1..1000, default 1, no name inference. Maximum 1000 columns/data record. Blank records counted and missing chosen column; absent cells distinct from present empty string. Ragged records reported via missing count, not rejected. UTF-8 BOM stripped.

JSON reports data records, present/missing/empty cells, distinct values, and anonymous spectrum: frequency 3 with distinct_values_with_frequency 2 means two hidden values each appeared three times. NOT a ranked category-value report. Exact cell equality, no trim/casefold/type conversion. No values/header names emitted, no file writes/export/network. Counts/spectrum still can reveal sensitive distributions. Invalid CSV/UTF-8/cap returns 2 with generic errors, no source echo. No argument prompts, 0 exits.

16 tests cover spectrum, redaction, header/column/missing/empty/blank, quotes/multiline/BOM and equality definitions. Linux tested; Pi/non-Linux untested. Marker/version1.0.0 published.

The current public-only Pi App Store cannot discover private repositories; authenticated store support is not verified.

Fullscreen update: Store interactive launch uses terminal-sized board cells or wrapped full-terminal utility input/results with PgUp/PgDn scrolling. Original core rules and direct CLI commands remain unchanged. Ctrl+C cancels utility entry, result Enter returns; no new dependency downloads. Linux PTY resize/restoration checked; physical Pi untested.
