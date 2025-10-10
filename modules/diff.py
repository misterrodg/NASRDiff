import os
from modules.apt_att_file import APT_ATT_File
from modules.apt_base_file import APT_BASE_File
from modules.apt_con_file import APT_CON_File
from modules.apt_rmk_file import APT_RMK_File
from modules.filters import Filters
from modules.navdata_handler import get_csv_files
from modules.reports_handler import REPORTS_DIR

FILE_SUFFIX = "CHG_RPT.csv"


class Diff:
    format: str
    filters: Filters | None
    file_paths: list[str]
    apt_att: APT_ATT_File | None
    apt_base: APT_BASE_File | None
    apt_con: APT_CON_File | None
    apt_rmk: APT_RMK_File | None

    def __init__(self, format: str, should_show: bool, use_filters: bool) -> None:
        self.format = format
        self.filters = None
        self.file_paths = get_csv_files()
        self.apt_att = None
        self.apt_base = None
        self.apt_con = None
        self.apt_rmk = None

        if use_filters:
            self.__process_filtered_file_list(should_show)
        else:
            self.__process_file_list()

    def build_reports(self) -> None:
        if self.format == "console":
            self.__get_text_report()
        if self.format == "text":
            self.__to_text_report()

    def __process_filtered_file_list(self, should_show: bool) -> None:
        self.filters = Filters(should_show)

        for fp in self.file_paths:
            if len(self.filters.files) > 0:
                if (
                    fp.endswith(f"APT_ATT_{FILE_SUFFIX}")
                    and "APT_ATT" in self.filters.files
                ):
                    airports = (
                        self.filters.airports
                        if len(self.filters.airports) > 0
                        else None
                    )
                    self.apt_att = APT_ATT_File(fp, airports)
                if (
                    fp.endswith(f"APT_BASE_{FILE_SUFFIX}")
                    and "APT_BASE" in self.filters.files
                ):
                    airports = (
                        self.filters.airports
                        if len(self.filters.airports) > 0
                        else None
                    )
                    self.apt_base = APT_BASE_File(fp, airports)
                if (
                    fp.endswith(f"APT_CON_{FILE_SUFFIX}")
                    and "APT_CON" in self.filters.files
                ):
                    airports = (
                        self.filters.airports
                        if len(self.filters.airports) > 0
                        else None
                    )
                    self.apt_con = APT_CON_File(fp, airports)
                if (
                    fp.endswith(f"APT_RMK_{FILE_SUFFIX}")
                    and "APT_RMK" in self.filters.files
                ):
                    airports = (
                        self.filters.airports
                        if len(self.filters.airports) > 0
                        else None
                    )
                    self.apt_rmk = APT_RMK_File(fp, airports)

    def __process_file_list(self) -> None:
        for fp in self.file_paths:
            if fp.endswith(f"APT_ATT_{FILE_SUFFIX}"):
                self.apt_att = APT_ATT_File(fp)
            if fp.endswith(f"APT_BASE_{FILE_SUFFIX}"):
                self.apt_base = APT_BASE_File(fp)
            if fp.endswith(f"APT_CON_{FILE_SUFFIX}"):
                self.apt_con = APT_CON_File(fp)
            if fp.endswith(f"APT_RMK_{FILE_SUFFIX}"):
                self.apt_rmk = APT_RMK_File(fp)

    def __get_text_report(self) -> None:
        if self.apt_att is not None:
            print(self.apt_att.get_text_report())
        if self.apt_base is not None:
            print(self.apt_base.get_text_report())
        if self.apt_con is not None:
            print(self.apt_con.get_text_report())
        if self.apt_rmk is not None:
            print(self.apt_rmk.get_text_report())

    def __to_text_report(self) -> None:
        if self.apt_att is not None:
            full_path = os.path.join(REPORTS_DIR, "APT_ATT.txt")
            with open(full_path, "w") as f:
                f.writelines(self.apt_att.get_text_report())
        if self.apt_base is not None:
            full_path = os.path.join(REPORTS_DIR, "APT_BASE.txt")
            with open(full_path, "w") as f:
                f.writelines(self.apt_base.get_text_report())
        if self.apt_con is not None:
            full_path = os.path.join(REPORTS_DIR, "APT_CON.txt")
            with open(full_path, "w") as f:
                f.writelines(self.apt_con.get_text_report())
        if self.apt_rmk is not None:
            full_path = os.path.join(REPORTS_DIR, "APT_RMK.txt")
            with open(full_path, "w") as f:
                f.writelines(self.apt_rmk.get_text_report())
