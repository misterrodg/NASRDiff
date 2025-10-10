# NASRDiff

A diff report generator for the [FAA NASR](https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/).
NASRDiff parses the files in the `28 Day Cycle CSV Change Report Files` product, 
generating a report for any additions, modifications, and deletions.

By adding a `filters.json` in the project root, the parser will filter the 
reports for the specified files, airports or heliports within those files, 
and/or a bounding box for items that are not specified by airport/heliport ID. 
An `example_filters.json` is present in the project root as a template.

## Requirements

- Python 3.11+

## Use

To find the NASR Change Report, go to the [FAA NASR](https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/) page, 
select the `Current` or `Preview` page, search for `28 Day Cycle CSV Change Report Files`, 
and download the ZIP file. Since the `Current` and `Preview` pages have dates in 
the URL, it cannot be linked directly.

- Unzip the `28 Day Cycle CSV Change Report Files` and copy the `.csv` files into 
the `navdata` directory.
- Copy the `example_filters.json` as `filters.json`.
- Edit the `filters.json` to include the files, airports, and bounds of your choice 
(see [Filters](#filters), below).
- Run with `python3 main.py [args]` (see [Arguments](#arguments), below).

By default, a summary will be printed to the console. If a format is specified 
as an argument, the resulting reports will be in the `reports` directory.

### Arguments

| Short | Long | Action |
| - | - | - |
| `-a` | `--all` | Run for all files and all file content (ignores the `filters.json`). |
| `-c` | `--clear` | Clear files from navdata dir. |
| `-f` | `--format` | Sets the report format with options `console` (default) or `text`. |
| `-n` | `--norun` | Skip report generation. |
| `-p` | `--purge` | Purge files from reports dir. |
| `-s` | `--show` | Show filters in console. |

### Filters

| Field | Description |
| - | - |
| `files` | An array of strings representing the initial part of a change report filename (everything up to `_CHG_RPT.csv`). Set this to select the files that contain data that you are interested in. |
| `bounds` | An object with the next four fields. |
| `n_lat` | The northernmost latitude boundary in decimal form. |
| `s_lat` | The southernmost latitude boundary in decimal form. |
| `w_lon` | The westernmost longitude boundary in decimal form. |
| `e_lon` | The easternmost longitude boundary in decimal form. |
| `airports` | An array of strings representing the FAA code* of the airports (and heliports) that you are interested in. |

\* The FAA Code is a three-letter identifier, commonly mistaken for an IATA 
code since they are usually the same. Generally, it is the ICAO code without the 
initial `K`. There are some oddities that exist, such as Manassas, VA, which 
uses `ICAO: KHEF`, `FAA: HEF`, and `IATA: MNZ`. If you are unsure, download the 
full NASR product, open the `APT_BASE.csv` file, and search for the facility by 
name. Use the value from the `ARPT_ID` in the `airports` array.

#### Example

The example provided in `example_filters.json` sets filters for:

- `files`: `"APT_BASE"`, `"FIX_BASE"` and `"NAV_BASE"`. This selects only these 
three files. The rest are ignored.
- `bounds`: `"n_lat": 40.1`, `"s_lat": 32.9`, `"w_lon": -80.8`, and `"e_lon": -72.5`. 
This selects anything defined by a lat/lon position in the area that is shown 
in the image below.
- `airports`: `"ADW"`, `"BWI"`, `"DCA"`, and `"IAD"`. This selects only these 
airports. The rest are ignored.

![Example Boundaries](./docs/images/example.png)
