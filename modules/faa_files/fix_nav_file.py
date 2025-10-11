from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class FIX_NAV(FAA_Record_Base):
    eff_date: str
    fix_id: str
    icao_region_code: str
    state_code: str
    country_code: str
    nav_id: str
    nav_type: str
    bearing: str
    distance: str
    file: str
    action: Action
    mods: str

    def __init__(
        self,
        eff_date: str,
        fix_id: str,
        icao_region_code: str,
        state_code: str,
        country_code: str,
        nav_id: str,
        nav_type: str,
        bearing: str,
        distance: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        self.eff_date = replace_empty_string(eff_date)
        self.fix_id = replace_empty_string(fix_id)
        self.icao_region_code = replace_empty_string(icao_region_code)
        self.state_code = replace_empty_string(state_code)
        self.country_code = replace_empty_string(country_code)
        self.nav_id = replace_empty_string(nav_id)
        self.nav_type = replace_empty_string(nav_type)
        self.bearing = replace_empty_string(bearing)
        self.distance = replace_empty_string(distance)
        self.file = file
        self.action = action
        self.mods = mods

    def to_string(self, last_record: Self | None = None) -> str:
        if last_record:
            modification_string = self.get_mod_string(last_record)
            return f"{self.fix_id} :: {modification_string}"
        return (
            f"{self.fix_id} :: "
            f"EFF_DATE: {self.eff_date}, "
            f"ICAO_REGION_CODE: {self.icao_region_code}, "
            f"STATE_CODE: {self.state_code}, "
            f"COUNTRY_CODE: {self.country_code}, "
            f"NAV_ID: {self.nav_id}, "
            f"NAV_TYPE: {self.nav_type}, "
            f"BEARING: {self.bearing}, "
            f"DISTANCE: {self.distance}"
        )


@register_faa_file("FIX_NAV")
class FIX_NAV_File(FAA_File_Base):
    def __init__(
        self, file_path: str, filter_object: FilterObject | None = None
    ) -> None:
        super().__init__(file_path, "FIX NAV", filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = FIX_NAV(
                    eff_date=row["EFF_DATE"],
                    fix_id=row["FIX_ID"],
                    icao_region_code=row["ICAO_REGION_CODE"],
                    state_code=row["STATE_CODE"],
                    country_code=row["COUNTRY_CODE"],
                    nav_id=row["NAV_ID"],
                    nav_type=row["NAV_TYPE"],
                    bearing=row["BEARING"],
                    distance=row["DISTANCE"],
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
