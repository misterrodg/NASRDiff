from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class ATC_RMK(FAA_Record_Base):
    eff_date: str
    site_no: str
    site_type_code: str
    facility_type: str
    state_code: str
    facility_id: str
    city: str
    country_code: str
    legacy_element_number: str
    tab_name: str
    ref_col_name: str
    remark_no: str
    remark: str
    file: str
    action: str
    mods: str

    def __init__(
        self,
        eff_date: str,
        site_no: str,
        site_type_code: str,
        facility_type: str,
        state_code: str,
        facility_id: str,
        city: str,
        country_code: str,
        legacy_element_number: str,
        tab_name: str,
        ref_col_name: str,
        remark_no: str,
        remark: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        self.eff_date = replace_empty_string(eff_date)
        self.site_no = replace_empty_string(site_no)
        self.site_type_code = replace_empty_string(site_type_code)
        self.facility_type = replace_empty_string(facility_type)
        self.state_code = replace_empty_string(state_code)
        self.facility_id = replace_empty_string(facility_id)
        self.city = replace_empty_string(city)
        self.country_code = replace_empty_string(country_code)
        self.legacy_element_number = replace_empty_string(legacy_element_number)
        self.tab_name = replace_empty_string(tab_name)
        self.ref_col_name = replace_empty_string(ref_col_name)
        self.remark_no = replace_empty_string(remark_no)
        self.remark = replace_empty_string(remark)
        self.file = file
        self.action = action
        self.mods = mods

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.facility_id} :: {self.remark_no} :: {self.remark}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"SITE_NO: {self.site_no}, "
                f"SITE_TYPE_CODE: {self.site_type_code}, "
                f"FACILITY_TYPE: {self.facility_type}, "
                f"STATE_CODE: {self.state_code}, "
                f"CITY: {self.city}, "
                f"COUNTRY_CODE: {self.country_code}, "
                f"LEGACY_ELEMENT_NUMBER: {self.legacy_element_number}, "
                f"TAB_NAME: {self.tab_name}, "
                f"REF_COL_NAME: {self.ref_col_name}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("ATC_RMK")
class ATC_RMK_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "ATC Remark", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = ATC_RMK(
                    eff_date=row["EFF_DATE"],
                    site_no=row["SITE_NO"],
                    site_type_code=row["SITE_TYPE_CODE"],
                    facility_type=row["FACILITY_TYPE"],
                    state_code=row["STATE_CODE"],
                    facility_id=row["FACILITY_ID"],
                    city=row["CITY"],
                    country_code=row["COUNTRY_CODE"],
                    legacy_element_number=row["LEGACY_ELEMENT_NUMBER"],
                    tab_name=row["TAB_NAME"],
                    ref_col_name=row["REF_COL_NAME"],
                    remark_no=row["REMARK_NO"],
                    remark=row["REMARK"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_airports(
                        record.facility_id
                    )

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
