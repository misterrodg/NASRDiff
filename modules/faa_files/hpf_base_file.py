from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class HPF_BASE(FAA_Record_Base):
    eff_date: str
    hp_name: str
    hp_no: str
    state_code: str
    country_code: str
    fix_id: str
    icao_region_code: str
    nav_id: str
    nav_type: str
    hold_direction: str
    hold_deg_or_crs: str
    azimuth: str
    course_inbound_deg: str
    turn_direction: str
    leg_length_dist: str
    file: str
    action: Action
    mods: str

    def __init__(
        self,
        eff_date: str,
        hp_name: str,
        hp_no: str,
        state_code: str,
        country_code: str,
        fix_id: str,
        icao_region_code: str,
        nav_id: str,
        nav_type: str,
        hold_direction: str,
        hold_deg_or_crs: str,
        azimuth: str,
        course_inbound_deg: str,
        turn_direction: str,
        leg_length_dist: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        self.eff_date = replace_empty_string(eff_date)
        self.hp_name = replace_empty_string(hp_name)
        self.hp_no = replace_empty_string(hp_no)
        self.state_code = replace_empty_string(state_code)
        self.country_code = replace_empty_string(country_code)
        self.fix_id = replace_empty_string(fix_id)
        self.icao_region_code = replace_empty_string(icao_region_code)
        self.nav_id = replace_empty_string(nav_id)
        self.nav_type = replace_empty_string(nav_type)
        self.hold_direction = replace_empty_string(hold_direction)
        self.hold_deg_or_crs = replace_empty_string(hold_deg_or_crs)
        self.azimuth = replace_empty_string(azimuth)
        self.course_inbound_deg = replace_empty_string(course_inbound_deg)
        self.turn_direction = replace_empty_string(turn_direction)
        self.leg_length_dist = replace_empty_string(leg_length_dist)
        self.file = file
        self.action = action
        self.mods = mods

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.hp_name} :: {self.hp_no}"

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
                f"FIX_ID: {self.fix_id}, "
                f"ICAO_REGION_CODE: {self.icao_region_code}, "
                f"NAV_ID: {self.nav_id}, "
                f"NAV_TYPE: {self.nav_type}, "
                f"HOLD_DIRECTION: {self.hold_direction}, "
                f"HOLD_DEG_OR_CRS: {self.hold_deg_or_crs}, "
                f"AZIMUTH: {self.azimuth}, "
                f"COURSE_INBOUND_DEG: {self.course_inbound_deg}, "
                f"TURN_DIRECTION: {self.turn_direction}, "
                f"LEG_LENGTH_DIST: {self.leg_length_dist}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("HPF_BASE")
class HPF_BASE_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "Holding Pattern Base", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = HPF_BASE(
                    eff_date=row["EFF_DATE"],
                    hp_name=row["HP_NAME"],
                    hp_no=row["HP_NO"],
                    state_code=row["STATE_CODE"],
                    country_code=row["COUNTRY_CODE"],
                    fix_id=row["FIX_ID"],
                    icao_region_code=row["ICAO_REGION_CODE"],
                    nav_id=row["NAV_ID"],
                    nav_type=row["NAV_TYPE"],
                    hold_direction=row["HOLD_DIRECTION"],
                    hold_deg_or_crs=row["HOLD_DEG_OR_CRS"],
                    azimuth=row["AZIMUTH"],
                    course_inbound_deg=row["COURSE_INBOUND_DEG"],
                    turn_direction=row["TURN_DIRECTION"],
                    leg_length_dist=row["LEG_LENGTH_DIST"],
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
