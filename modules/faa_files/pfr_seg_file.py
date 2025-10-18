from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class PFR_SEG(FAA_Record_Base):
    eff_date: str
    origin_id: str
    dstn_id: str
    pfr_type_code: str
    route_no: str
    segment_seq: str
    seg_value: str
    seg_type: str
    state_code: str
    country_code: str
    icao_region_code: str
    nav_type: str
    next_seg: str

    def __init__(
        self,
        eff_date: str,
        origin_id: str,
        dstn_id: str,
        pfr_type_code: str,
        route_no: str,
        segment_seq: str,
        seg_value: str,
        seg_type: str,
        state_code: str,
        country_code: str,
        icao_region_code: str,
        nav_type: str,
        next_seg: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.origin_id = replace_empty_string(origin_id)
        self.dstn_id = replace_empty_string(dstn_id)
        self.pfr_type_code = replace_empty_string(pfr_type_code)
        self.route_no = replace_empty_string(route_no)
        self.segment_seq = replace_empty_string(segment_seq)
        self.seg_value = replace_empty_string(seg_value)
        self.seg_type = replace_empty_string(seg_type)
        self.state_code = replace_empty_string(state_code)
        self.country_code = replace_empty_string(country_code)
        self.icao_region_code = replace_empty_string(icao_region_code)
        self.nav_type = replace_empty_string(nav_type)
        self.next_seg = replace_empty_string(next_seg)

    def __hash__(self) -> int:
        return hash((self.origin_id, self.dstn_id, self.route_no, self.seg_value))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PFR_SEG):
            return False
        return (
            self.origin_id == other.origin_id
            and self.dstn_id == other.dstn_id
            and self.route_no == other.route_no
            and self.seg_value == other.seg_value
        )

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, PFR_SEG):
            return False
        return (
            self.origin_id,
            self.dstn_id,
            self.route_no,
            self.seg_value,
            self.file,
        ) < (
            other.origin_id,
            other.dstn_id,
            other.route_no,
            other.seg_value,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"ORIGIN_ID={self.origin_id!r}, "
            f"DSTN_ID={self.dstn_id!r}, "
            f"PFR_TYPE_CODE={self.pfr_type_code!r}, "
            f"ROUTE_NO={self.route_no!r}, "
            f"SEGMENT_SEQ={self.segment_seq!r}, "
            f"SEG_VALUE={self.seg_value!r}, "
            f"SEG_TYPE={self.seg_type!r}, "
            f"STATE_CODE={self.state_code!r}, "
            f"COUNTRY_CODE={self.country_code!r}, "
            f"ICAO_REGION_CODE={self.icao_region_code!r}, "
            f"NAV_TYPE={self.nav_type!r}, "
            f"NEXT_SEG={self.next_seg!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.origin_id} :: {self.dstn_id} :: {self.route_no}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date!r}, "
                f"PFR_TYPE_CODE: {self.pfr_type_code!r}, "
                f"SEGMENT_SEQ: {self.segment_seq!r}, "
                f"SEG_VALUE: {self.seg_value!r}, "
                f"SEG_TYPE: {self.seg_type!r}, "
                f"STATE_CODE: {self.state_code!r}, "
                f"COUNTRY_CODE: {self.country_code!r}, "
                f"ICAO_REGION_CODE: {self.icao_region_code!r}, "
                f"NAV_TYPE: {self.nav_type!r}, "
                f"NEXT_SEG: {self.next_seg!r}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("PFR_SEG")
class PFR_SEG_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(
            file_path, "Preferred Route Segment", use_verbose, filter_object
        )

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = PFR_SEG(
                    eff_date=row["EFF_DATE"],
                    origin_id=row["ORIGIN_ID"],
                    dstn_id=row["DSTN_ID"],
                    pfr_type_code=row["PFR_TYPE_CODE"],
                    route_no=row["ROUTE_NO"],
                    segment_seq=row["SEGMENT_SEQ"],
                    seg_value=row["SEG_VALUE"],
                    seg_type=row["SEG_TYPE"],
                    state_code=row["STATE_CODE"],
                    country_code=row["COUNTRY_CODE"],
                    icao_region_code=row["ICAO_REGION_CODE"],
                    nav_type=row["NAV_TYPE"],
                    next_seg=row["NEXT_SEG"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_airports(
                        record.origin_id
                    ) or self.filter_object.is_in_airports(record.dstn_id)

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
