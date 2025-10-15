from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class CLS_ARSP(FAA_Record_Base):
    eff_date: str
    site_no: str
    site_type_code: str
    state_code: str
    arpt_id: str
    city: str
    country_code: str
    class_b_airspace: str
    class_c_airspace: str
    class_d_airspace: str
    class_e_airspace: str
    airspace_hrs: str
    remark: str

    def __init__(
        self,
        eff_date: str,
        site_no: str,
        site_type_code: str,
        state_code: str,
        arpt_id: str,
        city: str,
        country_code: str,
        class_b_airspace: str,
        class_c_airspace: str,
        class_d_airspace: str,
        class_e_airspace: str,
        airspace_hrs: str,
        remark: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.site_no = replace_empty_string(site_no)
        self.site_type_code = replace_empty_string(site_type_code)
        self.state_code = replace_empty_string(state_code)
        self.arpt_id = replace_empty_string(arpt_id)
        self.city = replace_empty_string(city)
        self.country_code = replace_empty_string(country_code)
        self.class_b_airspace = replace_empty_string(class_b_airspace)
        self.class_c_airspace = replace_empty_string(class_c_airspace)
        self.class_d_airspace = replace_empty_string(class_d_airspace)
        self.class_e_airspace = replace_empty_string(class_e_airspace)
        self.airspace_hrs = replace_empty_string(airspace_hrs)
        self.remark = replace_empty_string(remark)

    def __hash__(self) -> int:
        return hash((self.arpt_id))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, CLS_ARSP):
            return False
        return self.arpt_id == other.arpt_id

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, CLS_ARSP):
            return False
        return (self.arpt_id, self.file) < (other.arpt_id, other.file)

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"SITE_NO={self.site_no!r}, "
            f"SITE_TYPE_CODE={self.site_type_code!r}, "
            f"STATE_CODE={self.state_code!r}, "
            f"ARPT_ID={self.arpt_id!r}, "
            f"CITY={self.city!r}, "
            f"COUNTRY_CODE={self.country_code!r}, "
            f"CLASS_B_AIRSPACE={self.class_b_airspace!r}, "
            f"CLASS_C_AIRSPACE={self.class_c_airspace!r}, "
            f"CLASS_D_AIRSPACE={self.class_d_airspace!r}, "
            f"CLASS_E_AIRSPACE={self.class_e_airspace!r}, "
            f"AIRSPACE_HRS={self.airspace_hrs!r}, "
            f"REMARK={self.remark!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.arpt_id}"

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
                f"STATE_CODE: {self.state_code}, "
                f"CITY: {self.city}, "
                f"COUNTRY_CODE: {self.country_code}, "
                f"CLASS_B_AIRSPACE: {self.class_b_airspace}, "
                f"CLASS_C_AIRSPACE: {self.class_c_airspace}, "
                f"CLASS_D_AIRSPACE: {self.class_d_airspace}, "
                f"CLASS_E_AIRSPACE: {self.class_e_airspace}, "
                f"AIRSPACE_HRS: {self.airspace_hrs}, "
                f"REMARK: {self.remark}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("CLS_ARSP")
class CLS_ARSP_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "Class Airspace", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = CLS_ARSP(
                    eff_date=row["EFF_DATE"],
                    site_no=row["SITE_NO"],
                    site_type_code=row["SITE_TYPE_CODE"],
                    state_code=row["STATE_CODE"],
                    arpt_id=row["ARPT_ID"],
                    city=row["CITY"],
                    country_code=row["COUNTRY_CODE"],
                    class_b_airspace=row["CLASS_B_AIRSPACE"],
                    class_c_airspace=row["CLASS_C_AIRSPACE"],
                    class_d_airspace=row["CLASS_D_AIRSPACE"],
                    class_e_airspace=row["CLASS_E_AIRSPACE"],
                    airspace_hrs=row["AIRSPACE_HRS"],
                    remark=row["REMARK"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_airports(record.arpt_id)

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
