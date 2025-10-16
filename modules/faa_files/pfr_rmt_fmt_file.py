from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class PFR_RMT_FMT(FAA_Record_Base):
    orig: str
    route_string: str
    dest: str
    hours1: str
    type: str
    area: str
    altitude: str
    aircraft: str
    direction: str
    seq: str
    dcntr: str
    acntr: str

    def __init__(
        self,
        orig: str,
        route_string: str,
        dest: str,
        hours1: str,
        type: str,
        area: str,
        altitude: str,
        aircraft: str,
        direction: str,
        seq: str,
        dcntr: str,
        acntr: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.orig = replace_empty_string(orig)
        self.route_string = replace_empty_string(route_string)
        self.dest = replace_empty_string(dest)
        self.hours1 = replace_empty_string(hours1)
        self.type = replace_empty_string(type)
        self.area = replace_empty_string(area)
        self.altitude = replace_empty_string(altitude)
        self.aircraft = replace_empty_string(aircraft)
        self.direction = replace_empty_string(direction)
        self.seq = replace_empty_string(seq)
        self.dcntr = replace_empty_string(dcntr)
        self.acntr = replace_empty_string(acntr)

        self.mods = self.mods.replace("Route String", "Route_String")

    def __hash__(self) -> int:
        return hash((self.orig, self.dest, self.seq))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, PFR_RMT_FMT):
            return False
        return (
            self.orig == other.orig
            and self.dest == other.dest
            and self.seq == other.seq
        )

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, PFR_RMT_FMT):
            return False
        return (self.orig, self.dest, self.seq, self.file) < (
            other.orig,
            other.dest,
            other.seq,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"ORIG={self.orig!r}, "
            f"ROUTE_STRING={self.route_string!r}, "
            f"DEST={self.dest!r}, "
            f"HOURS1={self.hours1!r}, "
            f"TYPE={self.type!r}, "
            f"AREA={self.area!r}, "
            f"ALTITUDE={self.altitude!r}, "
            f"AIRCRAFT={self.aircraft!r}, "
            f"DIRECTION={self.direction!r}, "
            f"SEQ={self.seq!r}, "
            f"DCNTR={self.dcntr!r}, "
            f"ACNTR={self.acntr!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.orig} :: {self.dest} :: {self.seq}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"ORIG: {self.orig}, "
                f"ROUTE_STRING: {self.route_string}, "
                f"DEST: {self.dest}, "
                f"HOURS1: {self.hours1}, "
                f"TYPE: {self.type}, "
                f"AREA: {self.area}, "
                f"ALTITUDE: {self.altitude}, "
                f"AIRCRAFT: {self.aircraft}, "
                f"DIRECTION: {self.direction}, "
                f"SEQ: {self.seq}, "
                f"DCNTR: {self.dcntr}, "
                f"ACNTR: {self.acntr}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("PFR_RMT_FMT")
class PFR_RMT_FMT_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(
            file_path, "Preferred Route RMT FMT", use_verbose, filter_object
        )

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = PFR_RMT_FMT(
                    orig=row["Orig"],
                    route_string=row["Route String"],
                    dest=row["Dest"],
                    hours1=row["Hours1"],
                    type=row["Type"],
                    area=row["Area"],
                    altitude=row["Altitude"],
                    aircraft=row["Aircraft"],
                    direction=row["Direction"],
                    seq=row["Seq"],
                    dcntr=row["DCNTR"],
                    acntr=row["ACNTR"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_airports(
                        record.orig
                    ) or self.filter_object.is_in_airports(record.dest)

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
