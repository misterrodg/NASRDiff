# NASRDiff

A diff report generator for the [FAA NASR](https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/).
NASRDiff parses the files in the "28 Day Cycle CSV Change Report Files" product, 
generating a report for any additions, modifications, and deletions.

By adding a `filters.json` in the project root, the parser will filter the 
reports for the specified files, airports or heliports within those files, 
and/or a bounding box for items that are not specified by airport/heliport ID. 
An `example_filters.json` is present in the project root as a template.

## Requirements

- Python 3.11+

## Use

- Copy the `example_filters.json` as `filters.json`.
- Edit the `filters.json` to include the files, airports, and bounds of your choice.
- Run with `python3 main.py [args]`

### Arguments

| Short | Long | Action |
| - | - | - |
| `-a` | `--all` | Run for all files and all file content (ignores the `filters.json`). |
| `-c` | `--clear` | Clear files from navdata dir. |
| `-f` | `--format` | Sets the report format with options `console` (default) or `text`. |
| `-n` | `--norun` | Skip report generation. |
| `-p` | `--purge` | Purge files from reports dir. |
| `-s` | `--show` | Show filters in console. |
