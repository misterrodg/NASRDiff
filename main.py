from modules.diff import Diff
from modules.navdata_handler import clear_navdata
from modules.reports_handler import clear_reports

import argparse

FORMAT_OPTIONS = ["console", "text"]


def main():
    parser = argparse.ArgumentParser(description="NASRDiff")
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="run for all files and all file content",
    )
    parser.add_argument(
        "-c", "--clear", action="store_true", help="clear files from navdata dir"
    )
    parser.add_argument(
        "-f", "--format", type=str, help="report format: console (default), text"
    )
    parser.add_argument(
        "-n", "--norun", action="store_true", help="skip report generation"
    )
    parser.add_argument(
        "-p", "--purge", action="store_true", help="purge files from reports dir"
    )
    parser.add_argument(
        "-s", "--show", action="store_true", help="show filters in console"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="include record details"
    )
    args = parser.parse_args()
    use_filters = not args.all
    should_clear = args.clear
    format = args.format
    if format is None or format not in FORMAT_OPTIONS:
        format = "console"
    should_skip_run = args.norun
    should_purge = args.purge
    should_show = args.show
    use_verbose = args.verbose

    if should_clear:
        clear_navdata()
        print("navdata cleared")
    if should_purge:
        clear_reports()
        print("reports purged")

    if not should_skip_run:
        diff = Diff(format, should_show, use_filters, use_verbose)
        diff.build_reports()


if __name__ == "__main__":
    main()
