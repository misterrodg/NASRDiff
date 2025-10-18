from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class MAA_SHP(FAA_Record_Base):
    eff_date: str
    maa_id: str
    point_seq: str
    latitude: str
    longitude: str

    def __init__(
        self,
        eff_date: str,
        maa_id: str,
        point_seq: str,
        latitude: str,
        longitude: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.maa_id = replace_empty_string(maa_id)
        self.point_seq = replace_empty_string(point_seq)
        self.latitude = replace_empty_string(latitude)
        self.longitude = replace_empty_string(longitude)

    def __hash__(self) -> int:
        return hash((self.maa_id, self.point_seq))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MAA_SHP):
            return False
        return self.maa_id == other.maa_id and self.point_seq == other.point_seq

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, MAA_SHP):
            return False
        return (self.maa_id, self.point_seq, self.file) < (
            other.maa_id,
            other.point_seq,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"MAA_ID={self.maa_id!r}, "
            f"POINT_SEQ={self.point_seq!r}, "
            f"LATITUDE={self.latitude!r}, "
            f"LONGITUDE={self.longitude!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.maa_id}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"POINT_SEQ:{ self.point_seq}, "
                f"LATITUDE: {self.latitude}, "
                f"LONGITUDE:{ self.longitude}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("MAA_SHP")
class MAA_SHP_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(
            file_path, "Misc Activity Area Shape", use_verbose, filter_object
        )

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = MAA_SHP(
                    eff_date=row["EFF_DATE"],
                    maa_id=row["MAA_ID"],
                    point_seq=row["POINT_SEQ"],
                    latitude=row["LATITUDE"],
                    longitude=row["LONGITUDE"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_bounds_dms(
                        record.latitude, record.longitude
                    )

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
