import os
from typing import Callable
from modules.apt_att_file import APT_ATT_File
from modules.apt_base_file import APT_BASE_File
from modules.apt_con_file import APT_CON_File
from modules.apt_rmk_file import APT_RMK_File
from modules.apt_rwy_file import APT_RWY_File
from modules.apt_rwy_end_file import APT_RWY_END_File
from modules.atc_atis_file import ATC_ATIS_File
from modules.faa_file_base import FAA_File_Base
from modules.filters import Filters
from modules.navdata_handler import get_csv_files
from modules.reports_handler import REPORTS_DIR

FILE_SUFFIX = "CHG_RPT.csv"

FILE_TYPES = {
    "APT_ATT": APT_ATT_File,
    "APT_BASE": APT_BASE_File,
    "APT_CON": APT_CON_File,
    "APT_RMK": APT_RMK_File,
    "APT_RWY": APT_RWY_File,
    "APT_RWY_END": APT_RWY_END_File,
    "ATC_ATIS": ATC_ATIS_File,
}

OUTPUT_NAMES = {
    "APT_ATT": "APT_ATT.txt",
    "APT_BASE": "APT_BASE.txt",
    "APT_CON": "APT_CON.txt",
    "APT_RMK": "APT_RMK.txt",
    "APT_RWY": "APT_RWY.txt",
    "APT_RWY_END": "APT_RWY_END.txt",
    "ATC_ATIS": "ATC_ATIS.txt",
}


class Diff:
    format: str
    filters: Filters | None
    file_paths: list[str]
    files_map: dict[str, FAA_File_Base]

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
        allowed = set(FILE_TYPES.keys())

        if use_filters:
            self.filters = Filters(should_show)
            airports = self.filters.airports or None
            if self.filters.files:
                allowed = set(self.filters.files)

        for fp in self.file_paths:
            for key, rpt in FILE_TYPES.items():
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
        def writer(key: str, faa_file: FAA_File_Base):
            file_name = OUTPUT_NAMES.get(key, f"{key}.txt")
            full_path = os.path.join(REPORTS_DIR, file_name)
            with open(full_path, "w") as f:
                f.writelines(faa_file.get_text_report())

        self.__handle_operation(writer)
