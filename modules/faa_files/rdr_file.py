from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class RDR(FAA_Record_Base):
    eff_date: str
    facility_id: str
    facility_type: str
    state_code: str
    country_code: str
    radar_type: str
    radar_no: str
    radar_hrs: str
    remark: str

    def __init__(
        self,
        eff_date: str,
        facility_id: str,
        facility_type: str,
        state_code: str,
        country_code: str,
        radar_type: str,
        radar_no: str,
        radar_hrs: str,
        remark: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.facility_id = replace_empty_string(facility_id)
        self.facility_type = replace_empty_string(facility_type)
        self.state_code = replace_empty_string(state_code)
        self.country_code = replace_empty_string(country_code)
        self.radar_type = replace_empty_string(radar_type)
        self.radar_no = replace_empty_string(radar_no)
        self.radar_hrs = replace_empty_string(radar_hrs)
        self.remark = replace_empty_string(remark)

    def __hash__(self) -> int:
        return hash((self.facility_id, self.radar_no))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, RDR):
            return False
        return self.facility_id == other.facility_id and self.radar_no == other.radar_no

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, RDR):
            return False
        return (self.facility_id, self.radar_no, self.file) < (
            other.facility_id,
            other.radar_no,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"FACILITY_ID={self.facility_id!r}, "
            f"FACILITY_TYPE={self.facility_type!r}, "
            f"STATE_CODE={self.state_code!r}, "
            f"COUNTRY_CODE={self.country_code!r}, "
            f"RADAR_TYPE={self.radar_type!r}, "
            f"RADAR_NO={self.radar_no!r}, "
            f"RADAR_HRS={self.radar_hrs!r}, "
            f"REMARK={self.remark!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.facility_id} :: {self.radar_type}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"FACILITY_TYPE: {self.facility_type}, "
                f"STATE_CODE: {self.state_code}, "
                f"COUNTRY_CODE: {self.country_code}, "
                f"RADAR_NO: {self.radar_no}, "
                f"RADAR_HRS: {self.radar_hrs}, "
                f"REMARK: {self.remark}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("RDR")
class RDR_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "Radar", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = RDR(
                    eff_date=row["EFF_DATE"],
                    facility_id=row["FACILITY_ID"],
                    facility_type=row["FACILITY_TYPE"],
                    state_code=row["STATE_CODE"],
                    country_code=row["COUNTRY_CODE"],
                    radar_type=row["RADAR_TYPE"],
                    radar_no=row["RADAR_NO"],
                    radar_hrs=row["RADAR_HRS"],
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
