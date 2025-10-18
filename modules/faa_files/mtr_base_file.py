from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class MTR_BASE(FAA_Record_Base):
    eff_date: str
    route_type_code: str
    route_id: str
    artcc: str
    fss: str
    time_of_use: str

    def __init__(
        self,
        eff_date: str,
        route_type_code: str,
        route_id: str,
        artcc: str,
        fss: str,
        time_of_use: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.route_type_code = replace_empty_string(route_type_code)
        self.route_id = replace_empty_string(route_id)
        self.artcc = replace_empty_string(artcc)
        self.fss = replace_empty_string(fss)
        self.time_of_use = replace_empty_string(time_of_use)

    def __hash__(self) -> int:
        return hash((self.route_type_code, self.route_id))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MTR_BASE):
            return False
        return (
            self.route_type_code == other.route_type_code
            and self.route_id == other.route_id
        )

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, MTR_BASE):
            return False
        return (self.route_type_code, self.route_id, self.file) < (
            other.route_type_code,
            other.route_id,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"ROUTE_TYPE_CODE={self.route_type_code!r}, "
            f"ROUTE_ID={self.route_id!r}, "
            f"ARTCC={self.artcc!r}, "
            f"FSS={self.fss!r}, "
            f"TIME_OF_USE={self.time_of_use!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.route_type_code}{self.route_id}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"ARTCC: {self.artcc}, "
                f"FSS: {self.fss}, "
                f"TIME_OF_USE: {self.time_of_use}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("MTR_BASE")
class MTR_BASE_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "MTR Base", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = MTR_BASE(
                    eff_date=row["EFF_DATE"],
                    route_type_code=row["ROUTE_TYPE_CODE"],
                    route_id=row["ROUTE_ID"],
                    artcc=row["ARTCC"],
                    fss=row["FSS"],
                    time_of_use=row["TIME_OF_USE"],
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
