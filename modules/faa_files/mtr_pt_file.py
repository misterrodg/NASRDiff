from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class MTR_PT(FAA_Record_Base):
    eff_date: str
    route_type_code: str
    route_id: str
    artcc: str
    route_pt_seq: str
    route_pt_id: str
    next_route_pt_id: str
    segment_text: str
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
    nav_id: str
    navaid_bearing: str
    navaid_dist: str

    def __init__(
        self,
        eff_date: str,
        route_type_code: str,
        route_id: str,
        artcc: str,
        route_pt_seq: str,
        route_pt_id: str,
        next_route_pt_id: str,
        segment_text: str,
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
        nav_id: str,
        navaid_bearing: str,
        navaid_dist: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.route_type_code = replace_empty_string(route_type_code)
        self.route_id = replace_empty_string(route_id)
        self.artcc = replace_empty_string(artcc)
        self.route_pt_seq = replace_empty_string(route_pt_seq)
        self.route_pt_id = replace_empty_string(route_pt_id)
        self.next_route_pt_id = replace_empty_string(next_route_pt_id)
        self.segment_text = replace_empty_string(segment_text)
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
        self.nav_id = replace_empty_string(nav_id)
        self.navaid_bearing = replace_empty_string(navaid_bearing)
        self.navaid_dist = replace_empty_string(navaid_dist)

    def __hash__(self) -> int:
        return hash((self.route_id, self.route_pt_seq))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, MTR_PT):
            return False
        return (
            self.route_id == other.route_id and self.route_pt_seq == other.route_pt_seq
        )

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, MTR_PT):
            return False
        return (self.route_id, self.route_pt_seq, self.file) < (
            other.route_id,
            other.route_pt_seq,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"ROUTE_TYPE_CODE={self.route_type_code!r}, "
            f"ROUTE_ID={self.route_id!r}, "
            f"ARTCC={self.artcc!r}, "
            f"ROUTE_PT_SEQ={self.route_pt_seq!r}, "
            f"ROUTE_PT_ID={self.route_pt_id!r}, "
            f"NEXT_ROUTE_PT_ID={self.next_route_pt_id!r}, "
            f"SEGMENT_TEXT={self.segment_text!r}, "
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
            f"NAV_ID={self.nav_id!r}, "
            f"NAVAID_BEARING={self.navaid_bearing!r}, "
            f"NAVAID_DIST={self.navaid_dist!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.route_id} :: {self.route_pt_seq}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"ROUTE_TYPE_CODE: {self.route_type_code}, "
                f"ARTCC: {self.artcc}, "
                f"ROUTE_PT_ID: {self.route_pt_id}, "
                f"NEXT_ROUTE_PT_ID: {self.next_route_pt_id}, "
                f"SEGMENT_TEXT: {self.segment_text}, "
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
                f"NAV_ID: {self.nav_id}, "
                f"NAVAID_BEARING: {self.navaid_bearing}, "
                f"NAVAID_DIST: {self.navaid_dist}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("MTR_PT")
class MTR_PT_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "MTR Route Point", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = MTR_PT(
                    eff_date=row["EFF_DATE"],
                    route_type_code=row["ROUTE_TYPE_CODE"],
                    route_id=row["ROUTE_ID"],
                    artcc=row["ARTCC"],
                    route_pt_seq=row["ROUTE_PT_SEQ"],
                    route_pt_id=row["ROUTE_PT_ID"],
                    next_route_pt_id=row["NEXT_ROUTE_PT_ID"],
                    segment_text=row["SEGMENT_TEXT"],
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
                    nav_id=row["NAV_ID"],
                    navaid_bearing=row["NAVAID_BEARING"],
                    navaid_dist=row["NAVAID_DIST"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_artccs(record.artcc)

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
