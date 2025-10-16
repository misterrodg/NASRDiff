from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class WXL_SVC(FAA_Record_Base):
    eff_date: str
    wea_id: str
    city: str
    state_code: str
    country_code: str
    wea_svc_type_code: str
    wea_affect_area: str

    def __init__(
        self,
        eff_date: str,
        wea_id: str,
        city: str,
        state_code: str,
        country_code: str,
        wea_svc_type_code: str,
        wea_affect_area: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.wea_id = replace_empty_string(wea_id)
        self.city = replace_empty_string(city)
        self.state_code = replace_empty_string(state_code)
        self.country_code = replace_empty_string(country_code)
        self.wea_svc_type_code = replace_empty_string(wea_svc_type_code)
        self.wea_affect_area = replace_empty_string(wea_affect_area)

    def __hash__(self) -> int:
        return hash((self.wea_id, self.wea_svc_type_code))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, WXL_SVC):
            return False
        return (
            self.wea_id == other.wea_id
            and self.wea_svc_type_code == other.wea_svc_type_code
        )

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, WXL_SVC):
            return False
        return (self.wea_id, self.wea_svc_type_code, self.file) < (
            other.wea_id,
            other.wea_svc_type_code,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"WEA_ID={self.wea_id!r}, "
            f"CITY={self.city!r}, "
            f"STATE_CODE={self.state_code!r}, "
            f"COUNTRY_CODE={self.country_code!r}, "
            f"WEA_SVC_TYPE_CODE={self.wea_svc_type_code!r}, "
            f"WEA_AFFECT_AREA={self.wea_affect_area!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.wea_id} :: {self.wea_svc_type_code}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"CITY: {self.city}, "
                f"STATE_CODE: {self.state_code}, "
                f"COUNTRY_CODE: {self.country_code}, "
                f"WEA_AFFECT_AREA: {self.wea_affect_area}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("WXL_SVC")
class WXL_SVC_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(
            file_path, "Weather Service", use_verbose, filter_object, False
        )

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = WXL_SVC(
                    eff_date=row["EFF_DATE"],
                    wea_id=row["WEA_ID"],
                    city=row["CITY"],
                    state_code=row["STATE_CODE"],
                    country_code=row["COUNTRY_CODE"],
                    wea_svc_type_code=row["WEA_SVC_TYPE_CODE"],
                    wea_affect_area=row["WEA_AFFECT_AREA"],
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
