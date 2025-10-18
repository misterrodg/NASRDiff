from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class NAV_CKPT(FAA_Record_Base):
    eff_date: str
    nav_id: str
    nav_type: str
    state_code: str
    city: str
    country_code: str
    altitude: str
    brg: str
    air_gnd_code: str
    chk_desc: str
    arpt_id: str
    state_chk_code: str

    def __init__(
        self,
        eff_date: str,
        nav_id: str,
        nav_type: str,
        state_code: str,
        city: str,
        country_code: str,
        altitude: str,
        brg: str,
        air_gnd_code: str,
        chk_desc: str,
        arpt_id: str,
        state_chk_code: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.nav_id = replace_empty_string(nav_id)
        self.nav_type = replace_empty_string(nav_type)
        self.state_code = replace_empty_string(state_code)
        self.city = replace_empty_string(city)
        self.country_code = replace_empty_string(country_code)
        self.altitude = replace_empty_string(altitude)
        self.brg = replace_empty_string(brg)
        self.air_gnd_code = replace_empty_string(air_gnd_code)
        self.chk_desc = replace_empty_string(chk_desc)
        self.arpt_id = replace_empty_string(arpt_id)
        self.state_chk_code = replace_empty_string(state_chk_code)

    def __hash__(self) -> int:
        return hash((self.nav_id, self.nav_type))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, NAV_CKPT):
            return False
        return self.nav_id == other.nav_id and self.nav_type == other.nav_type

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, NAV_CKPT):
            return False
        return (self.nav_id, self.nav_type, self.file) < (
            other.nav_id,
            other.nav_type,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"NAV_ID={self.nav_id!r}, "
            f"NAV_TYPE={self.nav_type!r}, "
            f"STATE_CODE={self.state_code!r}, "
            f"CITY={self.city!r}, "
            f"COUNTRY_CODE={self.country_code!r}, "
            f"ALTITUDE={self.altitude!r}, "
            f"BRG={self.brg!r}, "
            f"AIR_GND_CODE={self.air_gnd_code!r}, "
            f"CHK_DESC={self.chk_desc!r}, "
            f"ARPT_ID={self.arpt_id!r}, "
            f"STATE_CHK_CODE={self.state_chk_code!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.nav_id} :: {self.nav_type}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"STATE_CODE: {self.state_code}, "
                f"CITY: {self.city}, "
                f"COUNTRY_CODE: {self.country_code}, "
                f"ALTITUDE: {self.altitude}, "
                f"BRG: {self.brg}, "
                f"AIR_GND_CODE: {self.air_gnd_code}, "
                f"CHK_DESC: {self.chk_desc}, "
                f"ARPT_ID: {self.arpt_id}, "
                f"STATE_CHK_CODE: {self.state_chk_code}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("NAV_CKPT")
class NAV_CKPT_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "Navigation Checkpoint", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = NAV_CKPT(
                    eff_date=row["EFF_DATE"],
                    nav_id=row["NAV_ID"],
                    nav_type=row["NAV_TYPE"],
                    state_code=row["STATE_CODE"],
                    city=row["CITY"],
                    country_code=row["COUNTRY_CODE"],
                    altitude=row["ALTITUDE"],
                    brg=row["BRG"],
                    air_gnd_code=row["AIR_GND_CODE"],
                    chk_desc=row["CHK_DESC"],
                    arpt_id=row["ARPT_ID"],
                    state_chk_code=row["STATE_CHK_CODE"],
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
