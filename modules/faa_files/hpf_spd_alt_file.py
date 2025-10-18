from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class HPF_SPD_ALT(FAA_Record_Base):
    eff_date: str
    hp_name: str
    hp_no: str
    state_code: str
    country_code: str
    speed_range: str
    altitude: str

    def __init__(
        self,
        eff_date: str,
        hp_name: str,
        hp_no: str,
        state_code: str,
        country_code: str,
        speed_range: str,
        altitude: str,
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
        self.speed_range = replace_empty_string(speed_range)
        self.altitude = replace_empty_string(altitude)

    def __hash__(self) -> int:
        return hash((self.hp_name, self.hp_no))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HPF_SPD_ALT):
            return False
        return self.hp_name == other.hp_name and self.hp_no == other.hp_no

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, HPF_SPD_ALT):
            return False
        return (self.hp_name, self.hp_no, self.file) < (
            other.hp_name,
            other.hp_no,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"HP_NAME={self.hp_name!r}, "
            f"HP_NO={self.hp_no!r}, "
            f"STATE_CODE={self.state_code!r}, "
            f"COUNTRY_CODE={self.country_code!r}, "
            f"SPEED_RANGE={self.speed_range!r}, "
            f"ALTITUDE={self.altitude!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = (
            f"{self.hp_name} :: {self.hp_no} :: {self.speed_range} // {self.altitude}"
        )

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"STATE_CODE: {self.state_code}, "
                f"COUNTRY_CODE: {self.country_code}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("HPF_SPD_ALT")
class HPF_SPD_ALT_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(
            file_path, "Holding Pattern Remark", use_verbose, filter_object, False
        )

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = HPF_SPD_ALT(
                    eff_date=row["EFF_DATE"],
                    hp_name=row["HP_NAME"],
                    hp_no=row["HP_NO"],
                    state_code=row["STATE_CODE"],
                    country_code=row["COUNTRY_CODE"],
                    speed_range=row["SPEED_RANGE"],
                    altitude=row["ALTITUDE"],
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
