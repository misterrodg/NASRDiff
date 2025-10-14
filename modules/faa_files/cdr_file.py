from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class CDR(FAA_Record_Base):
    rcode: str
    orig: str
    dest: str
    depfix: str
    route_string: str
    dcntr: str
    acntr: str
    tcntrs: str
    coordreq: str
    play: str
    naveqp: str
    length: str

    def __init__(
        self,
        rcode: str,
        orig: str,
        dest: str,
        depfix: str,
        route_string: str,
        dcntr: str,
        acntr: str,
        tcntrs: str,
        coordreq: str,
        play: str,
        naveqp: str,
        length: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.rcode = replace_empty_string(rcode)
        self.orig = replace_empty_string(orig)
        self.dest = replace_empty_string(dest)
        self.depfix = replace_empty_string(depfix)
        self.route_string = replace_empty_string(route_string)
        self.dcntr = replace_empty_string(dcntr)
        self.acntr = replace_empty_string(acntr)
        self.tcntrs = replace_empty_string(tcntrs)
        self.coordreq = replace_empty_string(coordreq)
        self.play = replace_empty_string(play)
        self.naveqp = replace_empty_string(naveqp)
        self.length = replace_empty_string(length)

        self.mods = self.mods.replace("Route String", "Route_String")

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"RCODE={self.rcode!r}, "
            f"ORIG={self.orig!r}, "
            f"DEST={self.dest!r}, "
            f"DEPFIX={self.depfix!r}, "
            f"ROUTE STRING={self.route_string!r}, "
            f"DCNTR={self.dcntr!r}, "
            f"ACNTR={self.acntr!r}, "
            f"TCNTRS={self.tcntrs!r}, "
            f"COORDREQ={self.coordreq!r}, "
            f"PLAY={self.play!r}, "
            f"NAVEQP={self.naveqp!r}, "
            f"LENGTH={self.length!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.orig}-{self.dest} :: {self.rcode} :: {self.depfix}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"ORIG: {self.orig}, "
                f"DEST: {self.dest}, "
                f"DEPFIX: {self.depfix}, "
                f"ROUTE STRING: {self.route_string}, "
                f"DCNTR: {self.dcntr}, "
                f"ACNTR: {self.acntr}, "
                f"TCNTRS: {self.tcntrs}, "
                f"COORDREQ: {self.coordreq}, "
                f"PLAY: {self.play}, "
                f"NAVEQP: {self.naveqp}, "
                f"LENGTH: {self.length}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("CDR")
class CDR_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "Coded Departure Route", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = CDR(
                    rcode=row["RCode"],
                    orig=row["Orig"],
                    dest=row["Dest"],
                    depfix=row["DepFix"],
                    route_string=row["Route String"],
                    dcntr=row["DCNTR"],
                    acntr=row["ACNTR"],
                    tcntrs=row["TCNTRs"],
                    coordreq=row["CoordReq"],
                    play=row["Play"],
                    naveqp=row["NavEqp"],
                    length=row["Length"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_airports(record.orig)

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
