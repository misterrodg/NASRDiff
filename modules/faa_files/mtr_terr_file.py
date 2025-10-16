from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class MTR_TERR(FAA_Record_Base):
    eff_date: str
    route_type_code: str
    route_id: str
    artcc: str
    terrain_seq_no: str
    terrain_text: str

    def __init__(
        self,
        eff_date: str,
        route_type_code: str,
        route_id: str,
        artcc: str,
        terrain_seq_no: str,
        terrain_text: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.route_type_code = replace_empty_string(route_type_code)
        self.route_id = replace_empty_string(route_id)
        self.artcc = replace_empty_string(artcc)
        self.terrain_seq_no = replace_empty_string(terrain_seq_no)
        self.terrain_text = replace_empty_string(terrain_text)

    def __hash__(self) -> int:
        return hash((self.route_type_code, self.route_id, self.terrain_seq_no))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, MTR_TERR):
            return False
        return (
            self.route_type_code == other.route_type_code
            and self.route_id == other.route_id
            and self.terrain_seq_no == other.terrain_seq_no
        )

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, MTR_TERR):
            return False
        return (self.route_type_code, self.route_id, self.terrain_seq_no, self.file) < (
            other.route_type_code,
            other.route_id,
            other.terrain_seq_no,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"ROUTE_TYPE_CODE={self.route_type_code!r}, "
            f"ROUTE_ID={self.route_id!r}, "
            f"ARTCC={self.artcc!r}, "
            f"TERRAIN_SEQ_NO={self.terrain_seq_no!r}, "
            f"TERRAIN_TEXT={self.terrain_text!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.route_type_code}{self.route_id} :: {self.terrain_seq_no}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"ARTCC: {self.artcc}, "
                f"TERRAIN_TEXT: {self.terrain_text}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("MTR_TERR")
class MTR_TERR_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "MTR Terrain", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = MTR_TERR(
                    eff_date=row["EFF_DATE"],
                    route_type_code=row["ROUTE_TYPE_CODE"],
                    route_id=row["ROUTE_ID"],
                    artcc=row["ARTCC"],
                    terrain_seq_no=row["TERRAIN_SEQ_NO"],
                    terrain_text=row["TERRAIN_TEXT"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_artccs_many(record.artcc)

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
