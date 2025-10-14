from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string, EMPTY_VALUE
from modules.registry import register_faa_file

from typing import Self

import csv


class DP_RTE(FAA_Record_Base):
    eff_date: str
    dp_name: str
    artcc: str
    dp_computer_code: str
    route_portion_type: str
    route_name: str
    body_seq: str
    transition_computer_code: str
    point_seq: str
    point: str
    icao_region_code: str
    point_type: str
    next_point: str
    arpt_rwy_assoc: str

    def __init__(
        self,
        eff_date: str,
        dp_name: str,
        artcc: str,
        dp_computer_code: str,
        route_portion_type: str,
        route_name: str,
        body_seq: str,
        transition_computer_code: str,
        point_seq: str,
        point: str,
        icao_region_code: str,
        point_type: str,
        next_point: str,
        arpt_rwy_assoc: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.dp_name = replace_empty_string(dp_name)
        self.artcc = replace_empty_string(artcc)
        self.dp_computer_code = replace_empty_string(dp_computer_code)
        self.route_portion_type = replace_empty_string(route_portion_type)
        self.route_name = replace_empty_string(route_name)
        self.body_seq = replace_empty_string(body_seq)
        self.transition_computer_code = replace_empty_string(transition_computer_code)
        self.point_seq = replace_empty_string(point_seq)
        self.point = replace_empty_string(point)
        self.icao_region_code = replace_empty_string(icao_region_code)
        self.point_type = replace_empty_string(point_type)
        self.next_point = replace_empty_string(next_point)
        self.arpt_rwy_assoc = replace_empty_string(arpt_rwy_assoc)

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"DP_NAME={self.dp_name!r}, "
            f"ARTCC={self.artcc!r}, "
            f"DP_COMPUTER_CODE={self.dp_computer_code!r}, "
            f"ROUTE_PORTION_TYPE={self.route_portion_type!r}, "
            f"ROUTE_NAME={self.route_name!r}, "
            f"BODY_SEQ={self.body_seq!r}, "
            f"TRANSITION_COMPUTER_CODE={self.transition_computer_code!r}, "
            f"POINT_SEQ={self.point_seq!r}, "
            f"POINT={self.point!r}, "
            f"ICAO_REGION_CODE={self.icao_region_code!r}, "
            f"POINT_TYPE={self.point_type!r}, "
            f"NEXT_POINT={self.next_point!r}, "
            f"ARPT_RWY_ASSOC={self.arpt_rwy_assoc!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        comp_code = self.transition_computer_code
        if comp_code == EMPTY_VALUE:
            comp_code = self.dp_computer_code
        base_string = f"{self.artcc} :: {comp_code} :: {self.point} :: {self.point_seq}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"DP_NAME: {self.dp_name}, "
                f"DP_COMPUTER_CODE: {self.dp_computer_code}, "
                f"ROUTE_PORTION_TYPE: {self.route_portion_type}, "
                f"ROUTE_NAME: {self.route_name}, "
                f"BODY_SEQ: {self.body_seq}, "
                f"ICAO_REGION_CODE: {self.icao_region_code}, "
                f"POINT_TYPE: {self.point_type}, "
                f"NEXT_POINT: {self.next_point}, "
                f"ARPT_RWY_ASSOC: {self.arpt_rwy_assoc}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("DP_RTE")
class DP_RTE_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(
            file_path, "Departure Procedure Route", use_verbose, filter_object
        )

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = DP_RTE(
                    eff_date=row["EFF_DATE"],
                    dp_name=row["DP_NAME"],
                    artcc=row["ARTCC"],
                    dp_computer_code=row["DP_COMPUTER_CODE"],
                    route_portion_type=row["ROUTE_PORTION_TYPE"],
                    route_name=row["ROUTE_NAME"],
                    body_seq=row["BODY_SEQ"],
                    transition_computer_code=row["TRANSITION_COMPUTER_CODE"],
                    point_seq=row["POINT_SEQ"],
                    point=row["POINT"],
                    icao_region_code=row["ICAO_REGION_CODE"],
                    point_type=row["POINT_TYPE"],
                    next_point=row["NEXT_POINT"],
                    arpt_rwy_assoc=row["ARPT_RWY_ASSOC"],
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
