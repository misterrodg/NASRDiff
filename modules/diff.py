import os
from typing import Callable
from modules.filters import Filters
from modules.navdata_handler import get_csv_files
from modules.registry import FILE_REGISTRY
from modules.reports_handler import REPORTS_DIR

import modules.faa_files as faa

FILE_SUFFIX = "CHG_RPT.csv"


class Diff:
    format: str
    filters: Filters | None
    file_paths: list[str]
    files_map: dict[str, faa.FAA_File_Base]

    def __init__(self, format: str, should_show: bool, use_filters: bool) -> None:
        self.format = format
        self.filters = None
        self.file_paths = get_csv_files()
        self.files_map = {}

        self.__process_file_list(should_show, use_filters)

    def build_reports(self) -> None:
        if self.format == "console":
            self.__get_text_report()
        if self.format == "text":
            self.__to_text_report()

    def __process_file_list(self, should_show: bool, use_filters: bool) -> None:
        airports = None
        allowed = set(FILE_REGISTRY.keys())

        if use_filters:
            self.filters = Filters(should_show)
            airports = self.filters.airports or None
            if self.filters.files:
                allowed = set(self.filters.files)

        for fp in self.file_paths:
            for key, rpt in FILE_REGISTRY.items():
                if key in allowed and fp.endswith(f"{key}_{FILE_SUFFIX}"):
                    if airports is not None:
                        self.files_map[key] = rpt(fp, airports)
                    else:
                        self.files_map[key] = rpt(fp)
                    break

    def __handle_operation(self, operation: Callable) -> None:
        for key, faa_file in self.files_map.items():
            if faa_file is not None:
                operation(key, faa_file)

    def __get_text_report(self) -> None:
        self.__handle_operation(lambda _, op: print(op.get_text_report()))

    def __to_text_report(self) -> None:
        def writer(key: str, faa_file: faa.FAA_File_Base):
            file_name = FILE_REGISTRY.get(key, f"{key}.txt")
            full_path = os.path.join(REPORTS_DIR, file_name)
            with open(full_path, "w") as f:
                f.writelines(faa_file.get_text_report())

        self.__handle_operation(writer)
