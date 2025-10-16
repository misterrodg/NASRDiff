from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class MAA_RMK(FAA_Record_Base):
    eff_date: str
    maa_id: str
    tab_name: str
    ref_col_name: str
    ref_col_seq_no: str
    remark: str

    def __init__(
        self,
        eff_date: str,
        maa_id: str,
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
        self.maa_id = replace_empty_string(maa_id)
        self.tab_name = replace_empty_string(tab_name)
        self.ref_col_name = replace_empty_string(ref_col_name)
        self.ref_col_seq_no = replace_empty_string(ref_col_seq_no)
        self.remark = replace_empty_string(remark)

    def __hash__(self) -> int:
        return hash((self.maa_id, self.ref_col_seq_no))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, MAA_RMK):
            return False
        return (
            self.maa_id == other.maa_id and self.ref_col_seq_no == other.ref_col_seq_no
        )

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, MAA_RMK):
            return False
        return (self.maa_id, self.ref_col_seq_no, self.file) < (
            other.maa_id,
            other.ref_col_seq_no,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"MAA_ID={self.maa_id!r}, "
            f"TAB_NAME={self.tab_name!r}, "
            f"REF_COL_NAME={self.ref_col_name!r}, "
            f"REF_COL_SEQ_NO={self.ref_col_seq_no!r}, "
            f"REMARK={self.remark!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.maa_id}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"TAB_NAME: {self.tab_name}, "
                f"REF_COL_NAME: {self.ref_col_name}, "
                f"REF_COL_SEQ_NO: {self.ref_col_seq_no}, "
                f"REMARK: {self.remark}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("MAA_RMK")
class MAA_RMK_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(
            file_path, "Misc Activity Area Remark", use_verbose, filter_object
        )

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = MAA_RMK(
                    eff_date=row["EFF_DATE"],
                    maa_id=row["MAA_ID"],
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
