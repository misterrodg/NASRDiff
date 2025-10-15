from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class DP_BASE(FAA_Record_Base):
    eff_date: str
    dp_name: str
    amendment_no: str
    artcc: str
    dp_amend_eff_date: str
    rnav_flag: str
    dp_computer_code: str
    graphical_dp_type: str
    served_arpt: str

    def __init__(
        self,
        eff_date: str,
        dp_name: str,
        amendment_no: str,
        artcc: str,
        dp_amend_eff_date: str,
        rnav_flag: str,
        dp_computer_code: str,
        graphical_dp_type: str,
        served_arpt: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.dp_name = replace_empty_string(dp_name)
        self.amendment_no = replace_empty_string(amendment_no)
        self.artcc = replace_empty_string(artcc)
        self.dp_amend_eff_date = replace_empty_string(dp_amend_eff_date)
        self.rnav_flag = replace_empty_string(rnav_flag)
        self.dp_computer_code = replace_empty_string(dp_computer_code)
        self.graphical_dp_type = replace_empty_string(graphical_dp_type)
        self.served_arpt = replace_empty_string(served_arpt)

    def __hash__(self) -> int:
        return hash((self.served_arpt, self.dp_name))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, DP_BASE):
            return False
        return self.served_arpt == other.served_arpt and self.dp_name == other.dp_name

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, DP_BASE):
            return False
        return (self.served_arpt, self.dp_name, self.file) < (
            other.served_arpt,
            other.dp_name,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"DP_NAME={self.dp_name!r}, "
            f"AMENDMENT_NO={self.amendment_no!r}, "
            f"ARTCC={self.artcc!r}, "
            f"DP_AMEND_EFF_DATE={self.dp_amend_eff_date!r}, "
            f"RNAV_FLAG={self.rnav_flag!r}, "
            f"DP_COMPUTER_CODE={self.dp_computer_code!r}, "
            f"GRAPHICAL_DP_TYPE={self.graphical_dp_type!r}, "
            f"SERVED_ARPT={self.served_arpt!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.served_arpt} :: {self.dp_name} {self.amendment_no}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"ARTCC: {self.artcc}, "
                f"DP_AMEND_EFF_DATE: {self.dp_amend_eff_date}, "
                f"RNAV_FLAG: {self.rnav_flag}, "
                f"DP_COMPUTER_CODE: {self.dp_computer_code}, "
                f"GRAPHICAL_DP_TYPE: {self.graphical_dp_type}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("DP_BASE")
class DP_BASE_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(
            file_path, "Departure Procedure Base", use_verbose, filter_object
        )

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = DP_BASE(
                    eff_date=row["EFF_DATE"],
                    dp_name=row["DP_NAME"],
                    amendment_no=row["AMENDMENT_NO"],
                    artcc=row["ARTCC"],
                    dp_amend_eff_date=row["DP_AMEND_EFF_DATE"],
                    rnav_flag=row["RNAV_FLAG"],
                    dp_computer_code=row["DP_COMPUTER_CODE"],
                    graphical_dp_type=row["GRAPHICAL_DP_TYPE"],
                    served_arpt=row["SERVED_ARPT"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_airports(
                        record.served_arpt
                    )

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
