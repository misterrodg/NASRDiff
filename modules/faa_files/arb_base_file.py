from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class ARB_BASE(FAA_Record_Base):
    eff_date: str
    location_id: str
    location_name: str
    computer_id: str
    icao_id: str
    location_type: str
    city: str
    state: str
    country_code: str
    lat_deg: str
    lat_min: str
    lat_sec: str
    lat_hemis: str
    lat_decimal: str
    long_deg: str
    long_min: str
    long_sec: str
    long_hemis: str
    long_decimal: str
    cross_ref: str

    def __init__(
        self,
        eff_date: str,
        location_id: str,
        location_name: str,
        computer_id: str,
        icao_id: str,
        location_type: str,
        city: str,
        state: str,
        country_code: str,
        lat_deg: str,
        lat_min: str,
        lat_sec: str,
        lat_hemis: str,
        lat_decimal: str,
        long_deg: str,
        long_min: str,
        long_sec: str,
        long_hemis: str,
        long_decimal: str,
        cross_ref: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.location_id = replace_empty_string(location_id)
        self.location_name = replace_empty_string(location_name)
        self.computer_id = replace_empty_string(computer_id)
        self.icao_id = replace_empty_string(icao_id)
        self.location_type = replace_empty_string(location_type)
        self.city = replace_empty_string(city)
        self.state = replace_empty_string(state)
        self.country_code = replace_empty_string(country_code)
        self.lat_deg = replace_empty_string(lat_deg)
        self.lat_min = replace_empty_string(lat_min)
        self.lat_sec = replace_empty_string(lat_sec)
        self.lat_hemis = replace_empty_string(lat_hemis)
        self.lat_decimal = replace_empty_string(lat_decimal)
        self.long_deg = replace_empty_string(long_deg)
        self.long_min = replace_empty_string(long_min)
        self.long_sec = replace_empty_string(long_sec)
        self.long_hemis = replace_empty_string(long_hemis)
        self.long_decimal = replace_empty_string(long_decimal)
        self.cross_ref = replace_empty_string(cross_ref)

    def __hash__(self) -> int:
        return hash((self.location_id))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, ARB_BASE):
            return False
        return self.location_id == other.location_id

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, ARB_BASE):
            return False
        return (self.location_id, self.file) < (
            other.location_id,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"LOCATION_ID={self.location_id!r}, "
            f"LOCATION_NAME={self.location_name!r}, "
            f"COMPUTER_ID={self.computer_id!r}, "
            f"ICAO_ID={self.icao_id!r}, "
            f"LOCATION_TYPE={self.location_type!r}, "
            f"CITY={self.city!r}, "
            f"STATE={self.state!r}, "
            f"COUNTRY_CODE={self.country_code!r}, "
            f"LAT_DEG={self.lat_deg!r}, "
            f"LAT_MIN={self.lat_min!r}, "
            f"LAT_SEC={self.lat_sec!r}, "
            f"LAT_HEMIS={self.lat_hemis!r}, "
            f"LAT_DECIMAL={self.lat_decimal!r}, "
            f"LONG_DEG={self.long_deg!r}, "
            f"LONG_MIN={self.long_min!r}, "
            f"LONG_SEC={self.long_sec!r}, "
            f"LONG_HEMIS={self.long_hemis!r}, "
            f"LONG_DECIMAL={self.long_decimal!r}, "
            f"CROSS_REF={self.cross_ref!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.location_id}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"LOCATION_NAME: {self.location_name}, "
                f"COMPUTER_ID: {self.computer_id}, "
                f"ICAO_ID: {self.icao_id}, "
                f"LOCATION_TYPE: {self.location_type}, "
                f"CITY: {self.city}, "
                f"STATE: {self.state}, "
                f"COUNTRY_CODE: {self.country_code}, "
                f"LAT_DEG: {self.lat_deg}, "
                f"LAT_MIN: {self.lat_min}, "
                f"LAT_SEC: {self.lat_sec}, "
                f"LAT_HEMIS: {self.lat_hemis}, "
                f"LAT_DECIMAL: {self.lat_decimal}, "
                f"LONG_DEG: {self.long_deg}, "
                f"LONG_MIN: {self.long_min}, "
                f"LONG_SEC: {self.long_sec}, "
                f"LONG_HEMIS: {self.long_hemis}, "
                f"LONG_DECIMAL: {self.long_decimal}, "
                f"CROSS_REF: {self.cross_ref}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("ARB_BASE")
class ARB_BASE_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "ARTCC Boundary Base", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = ARB_BASE(
                    eff_date=row["EFF_DATE"],
                    location_id=row["LOCATION_ID"],
                    location_name=row["LOCATION_NAME"],
                    computer_id=row["COMPUTER_ID"],
                    icao_id=row["ICAO_ID"],
                    location_type=row["LOCATION_TYPE"],
                    city=row["CITY"],
                    state=row["STATE"],
                    country_code=row["COUNTRY_CODE"],
                    lat_deg=row["LAT_DEG"],
                    lat_min=row["LAT_MIN"],
                    lat_sec=row["LAT_SEC"],
                    lat_hemis=row["LAT_HEMIS"],
                    lat_decimal=row["LAT_DECIMAL"],
                    long_deg=row["LONG_DEG"],
                    long_min=row["LONG_MIN"],
                    long_sec=row["LONG_SEC"],
                    long_hemis=row["LONG_HEMIS"],
                    long_decimal=row["LONG_DECIMAL"],
                    cross_ref=row["CROSS_REF"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_artccs(record.location_id)

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
