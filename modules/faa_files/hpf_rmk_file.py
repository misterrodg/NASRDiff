from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class HPF_RMK(FAA_Record_Base):
    eff_date: str
    hp_name: str
    hp_no: str
    state_code: str
    country_code: str
    tab_name: str
    ref_col_name: str
    ref_col_seq_no: str
    remark: str

    def __init__(
        self,
        eff_date: str,
        hp_name: str,
        hp_no: str,
        state_code: str,
        country_code: str,
        tab_name: str,
        ref_col_name: str,
        ref_col_seq_no: str,
        remark: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.hp_name = replace_empty_string(hp_name)
        self.hp_no = replace_empty_string(hp_no)
        self.state_code = replace_empty_string(state_code)
        self.country_code = replace_empty_string(country_code)
        self.tab_name = replace_empty_string(tab_name)
        self.ref_col_name = replace_empty_string(ref_col_name)
        self.ref_col_seq_no = replace_empty_string(ref_col_seq_no)
        self.remark = replace_empty_string(remark)

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.hp_name} :: {self.hp_no} :: {self.remark}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"STATE_CODE: {self.state_code}, "
                f"COUNTRY_CODE: {self.country_code}, "
                f"TAB_NAME: {self.tab_name}, "
                f"REF_COL_NAME: {self.ref_col_name}, "
                f"REF_COL_SEQ_NO: {self.ref_col_seq_no}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("HPF_RMK")
class HPF_RMK_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(
            file_path, "Holding Pattern Remark", use_verbose, filter_object
        )

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = HPF_RMK(
                    eff_date=row["EFF_DATE"],
                    hp_name=row["HP_NAME"],
                    hp_no=row["HP_NO"],
                    state_code=row["STATE_CODE"],
                    country_code=row["COUNTRY_CODE"],
                    tab_name=row["TAB_NAME"],
                    ref_col_name=row["REF_COL_NAME"],
                    ref_col_seq_no=row["REF_COL_SEQ_NO"],
                    remark=row["REMARK"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    # This file does not have filterable fields.
                    pass

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
