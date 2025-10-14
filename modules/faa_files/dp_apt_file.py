from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class DP_APT(FAA_Record_Base):
    eff_date: str
    dp_name: str
    artcc: str
    dp_computer_code: str
    body_name: str
    body_seq: str
    arpt_id: str
    rwy_end_id: str
    file: str
    action: Action
    mods: str

    def __init__(
        self,
        eff_date: str,
        dp_name: str,
        artcc: str,
        dp_computer_code: str,
        body_name: str,
        body_seq: str,
        arpt_id: str,
        rwy_end_id: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        self.eff_date = replace_empty_string(eff_date)
        self.dp_name = replace_empty_string(dp_name)
        self.artcc = replace_empty_string(artcc)
        self.dp_computer_code = replace_empty_string(dp_computer_code)
        self.body_name = replace_empty_string(body_name)
        self.body_seq = replace_empty_string(body_seq)
        self.arpt_id = replace_empty_string(arpt_id)
        self.rwy_end_id = replace_empty_string(rwy_end_id)
        self.file = file
        self.action = action
        self.mods = mods

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.arpt_id} :: {self.dp_computer_code} :: {self.body_name}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"DP_NAME: {self.dp_name}"
                f"ARTCC: {self.artcc}, "
                f"BODY_SEQ: {self.body_seq}, "
                f"RWY_END_ID: {self.rwy_end_id}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("DP_APT")
class DP_APT_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(
            file_path, "Departure Procedure Airport", use_verbose, filter_object
        )

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = DP_APT(
                    eff_date=row["EFF_DATE"],
                    dp_name=row["DP_NAME"],
                    artcc=row["ARTCC"],
                    dp_computer_code=row["DP_COMPUTER_CODE"],
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
