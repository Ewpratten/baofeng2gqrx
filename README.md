# Baofeng to Gqrx

A tool for converting [@nerdoug](https://github.com/nerdoug)'s Baofeng configs to Gqrx bookmark files


## Usage

```
usage: baofeng2gqrx.py [-h] [-o OUTFILE] [--simplex-overrides SIMPLEX_OVERRIDES] infile

positional arguments:
  infile                Input radio CSV file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTFILE, --outfile OUTFILE
                        Optional output file (if not set, stdout is used)
  --simplex-overrides SIMPLEX_OVERRIDES
                        Comma-seperated list of channel prefixes to specify as SIMPLEX
```