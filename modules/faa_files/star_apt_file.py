from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv
import re


class STAR_APT(FAA_Record_Base):
    eff_date: str
    star_name: str
    artcc: str
    star_computer_code: str
    body_name: str
    body_seq: str
    arpt_id: str
    rwy_end_id: str

    def __init__(
        self,
        eff_date: str,
        star_computer_code: str,
        artcc: str,
        body_name: str,
        body_seq: str,
        arpt_id: str,
        rwy_end_id: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.artcc = replace_empty_string(artcc)
        self.star_computer_code = replace_empty_string(star_computer_code)
        self.body_name = replace_empty_string(body_name)
        self.body_seq = replace_empty_string(body_seq)
        self.arpt_id = replace_empty_string(arpt_id)
        self.rwy_end_id = replace_empty_string(rwy_end_id)

        pattern = r"[A-Z]{3,5}\.([A-Z]{3,5})\d"
        match = re.search(pattern, self.star_computer_code)
        self.star_name = match.group(1)

    def __hash__(self) -> int:
        return hash((self.star_name, self.artcc, self.arpt_id, self.rwy_end_id))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, STAR_APT):
            return False
        return (
            self.star_name == other.star_name
            and self.artcc == other.artcc
            and self.arpt_id == other.arpt_id
            and self.rwy_end_id == other.rwy_end_id
        )

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, STAR_APT):
            return False
        return (
            self.star_name,
            self.artcc,
            self.arpt_id,
            self.rwy_end_id,
            self.file,
        ) < (
            other.star_name,
            other.artcc,
            other.arpt_id,
            other.rwy_end_id,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"STAR_COMPUTER_CODE={self.star_computer_code!r}, "
            f"ARTCC={self.artcc!r}, "
            f"BODY_NAME={self.body_name!r}, "
            f"BODY_SEQ={self.body_seq!r}, "
            f"ARPT_ID={self.arpt_id!r}, "
            f"RWY_END_ID={self.rwy_end_id!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.arpt_id} :: {self.star_computer_code} :: {self.body_name}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"ARTCC: {self.artcc}, "
                f"BODY_SEQ: {self.body_seq}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("STAR_APT")
class STAR_APT_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(
            file_path, "Arrival Procedure Airport", use_verbose, filter_object
        )

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = STAR_APT(
                    eff_date=row["EFF_DATE"],
                    star_computer_code=row["STAR_COMPUTER_CODE"],
                    artcc=row["ARTCC"],
                    body_name=row["BODY_NAME"],
                    body_seq=row["BODY_SEQ"],
                    arpt_id=row["ARPT_ID"],
                    rwy_end_id=row["RWY_END_ID"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_airports(record.arpt_id)

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
