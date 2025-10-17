from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class ARB_SEG(FAA_Record_Base):
    eff_date: str
    rec_id: str
    location_id: str
    location_name: str
    altitude: str
    type: str
    point_seq: str
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
    bndry_pt_descrip: str
    nas_descrip_flag: str

    def __init__(
        self,
        eff_date: str,
        rec_id: str,
        location_id: str,
        location_name: str,
        altitude: str,
        type: str,
        point_seq: str,
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
        bndry_pt_descrip: str,
        nas_descrip_flag: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.rec_id = replace_empty_string(rec_id)
        self.location_id = replace_empty_string(location_id)
        self.location_name = replace_empty_string(location_name)
        self.altitude = replace_empty_string(altitude)
        self.type = replace_empty_string(type)
        self.point_seq = replace_empty_string(point_seq)
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
        self.bndry_pt_descrip = replace_empty_string(bndry_pt_descrip)
        self.nas_descrip_flag = replace_empty_string(nas_descrip_flag)

    def __hash__(self) -> int:
        return hash((self.location_id, self.point_seq))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, ARB_SEG):
            return False
        return (
            self.location_id == other.location_id and self.point_seq == other.point_seq
        )

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, ARB_SEG):
            return False
        return (self.location_id, self.point_seq, self.file) < (
            other.location_id,
            other.point_seq,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"REC_ID={self.rec_id!r}, "
            f"LOCATION_ID={self.location_id!r}, "
            f"LOCATION_NAME={self.location_name!r}, "
            f"ALTITUDE={self.altitude!r}, "
            f"TYPE={self.type!r}, "
            f"POINT_SEQ={self.point_seq!r}, "
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
            f"BNDRY_PT_DESCRIP={self.bndry_pt_descrip!r}, "
            f"NAS_DESCRIP_FLAG={self.nas_descrip_flag!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.location_id} :: {self.point_seq}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"REC_ID: {self.rec_id}, "
                f"LOCATION_NAME: {self.location_name}, "
                f"ALTITUDE: {self.altitude}, "
                f"TYPE: {self.type}, "
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
                f"BNDRY_PT_DESCRIP: {self.bndry_pt_descrip}, "
                f"NAS_DESCRIP_FLAG: {self.nas_descrip_flag}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("ARB_SEG")
class ARB_SEG_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(
            file_path, "ARTCC Boundary Segment", use_verbose, filter_object
        )

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = ARB_SEG(
                    eff_date=row["EFF_DATE"],
                    rec_id=row["REC_ID"],
                    location_id=row["LOCATION_ID"],
                    location_name=row["LOCATION_NAME"],
                    altitude=row["ALTITUDE"],
                    type=row["TYPE"],
                    point_seq=row["POINT_SEQ"],
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
                    bndry_pt_descrip=row["BNDRY_PT_DESCRIP"],
                    nas_descrip_flag=row["NAS_DESCRIP_FLAG"],
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
