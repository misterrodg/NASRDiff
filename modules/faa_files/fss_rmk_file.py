from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class FSS_RMK(FAA_Record_Base):
    eff_date: str
    fss_id: str
    name: str
    city: str
    state_code: str
    country_code: str
    ref_col_name: str
    ref_col_seq_no: str
    remark: str

    def __init__(
        self,
        eff_date: str,
        fss_id: str,
        name: str,
        city: str,
        state_code: str,
        country_code: str,
        ref_col_name: str,
        ref_col_seq_no: str,
        remark: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.fss_id = replace_empty_string(fss_id)
        self.name = replace_empty_string(name)
        self.city = replace_empty_string(city)
        self.state_code = replace_empty_string(state_code)
        self.country_code = replace_empty_string(country_code)
        self.ref_col_name = replace_empty_string(ref_col_name)
        self.ref_col_seq_no = replace_empty_string(ref_col_seq_no)
        self.remark = replace_empty_string(remark)

    def __hash__(self) -> int:
        return hash((self.fss_id, self.ref_col_seq_no))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, FSS_RMK):
            return False
        return (
            self.fss_id == other.fss_id and self.ref_col_seq_no == other.ref_col_seq_no
        )

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, FSS_RMK):
            return False
        return (self.fss_id, self.ref_col_seq_no, self.file) < (
            other.fss_id,
            other.ref_col_seq_no,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"FSS_ID={self.fss_id!r}, "
            f"NAME={self.name!r}, "
            f"CITY={self.city!r}, "
            f"STATE_CODE={self.state_code!r}, "
            f"COUNTRY_CODE={self.country_code!r}, "
            f"REF_COL_NAME={self.ref_col_name!r}, "
            f"REF_COL_SEQ_NO={self.ref_col_seq_no!r}, "
            f"REMARK={self.remark!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.fss_id} :: {self.ref_col_seq_no}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"NAME: {self.name}, "
                f"CITY: {self.city}, "
                f"STATE_CODE: {self.state_code}, "
                f"COUNTRY_CODE: {self.country_code}, "
                f"REF_COL_NAME: {self.ref_col_name}, "
                f"REMARK: {self.remark}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("FSS_RMK")
class FSS_RMK_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "FSS Remark", use_verbose, filter_object, False)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = FSS_RMK(
                    eff_date=row["EFF_DATE"],
                    fss_id=row["FSS_ID"],
                    name=row["NAME"],
                    city=row["CITY"],
                    state_code=row["STATE_CODE"],
                    country_code=row["COUNTRY_CODE"],
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
