from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class PFR_BASE(FAA_Record_Base):
    eff_date: str
    origin_id: str
    origin_city: str
    origin_state_code: str
    origin_country_code: str
    dstn_id: str
    dstn_city: str
    dstn_state_code: str
    dstn_country_code: str
    pfr_type_code: str
    route_no: str
    special_area_descrip: str
    alt_descrip: str
    aircraft: str
    hours: str
    route_dir_descrip: str
    designator: str
    nar_type: str
    inland_fac_fix: str
    coastal_fix: str
    destination: str
    route_string: str

    def __init__(
        self,
        eff_date: str,
        origin_id: str,
        origin_city: str,
        origin_state_code: str,
        origin_country_code: str,
        dstn_id: str,
        dstn_city: str,
        dstn_state_code: str,
        dstn_country_code: str,
        pfr_type_code: str,
        route_no: str,
        special_area_descrip: str,
        alt_descrip: str,
        aircraft: str,
        hours: str,
        route_dir_descrip: str,
        designator: str,
        nar_type: str,
        inland_fac_fix: str,
        coastal_fix: str,
        destination: str,
        route_string: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.origin_id = replace_empty_string(origin_id)
        self.origin_city = replace_empty_string(origin_city)
        self.origin_state_code = replace_empty_string(origin_state_code)
        self.origin_country_code = replace_empty_string(origin_country_code)
        self.dstn_id = replace_empty_string(dstn_id)
        self.dstn_city = replace_empty_string(dstn_city)
        self.dstn_state_code = replace_empty_string(dstn_state_code)
        self.dstn_country_code = replace_empty_string(dstn_country_code)
        self.pfr_type_code = replace_empty_string(pfr_type_code)
        self.route_no = replace_empty_string(route_no)
        self.special_area_descrip = replace_empty_string(special_area_descrip)
        self.alt_descrip = replace_empty_string(alt_descrip)
        self.aircraft = replace_empty_string(aircraft)
        self.hours = replace_empty_string(hours)
        self.route_dir_descrip = replace_empty_string(route_dir_descrip)
        self.designator = replace_empty_string(designator)
        self.nar_type = replace_empty_string(nar_type)
        self.inland_fac_fix = replace_empty_string(inland_fac_fix)
        self.coastal_fix = replace_empty_string(coastal_fix)
        self.destination = replace_empty_string(destination)
        self.route_string = replace_empty_string(route_string)

    def __hash__(self) -> int:
        return hash((self.origin_id, self.dstn_id, self.route_no))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PFR_BASE):
            return False
        return (
            self.origin_id == other.origin_id
            and self.dstn_id == other.dstn_id
            and self.route_no == other.route_no
        )

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, PFR_BASE):
            return False
        return (self.origin_id, self.dstn_id, self.route_no, self.file) < (
            other.origin_id,
            other.dstn_id,
            other.route_no,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"ORIGIN_ID={self.origin_id!r}, "
            f"ORIGIN_CITY={self.origin_city!r}, "
            f"ORIGIN_STATE_CODE={self.origin_state_code!r}, "
            f"ORIGIN_COUNTRY_CODE={self.origin_country_code!r}, "
            f"DSTN_ID={self.dstn_id!r}, "
            f"DSTN_CITY={self.dstn_city!r}, "
            f"DSTN_STATE_CODE={self.dstn_state_code!r}, "
            f"DSTN_COUNTRY_CODE={self.dstn_country_code!r}, "
            f"PFR_TYPE_CODE={self.pfr_type_code!r}, "
            f"ROUTE_NO={self.route_no!r}, "
            f"SPECIAL_AREA_DESCRIP={self.special_area_descrip!r}, "
            f"ALT_DESCRIP={self.alt_descrip!r}, "
            f"AIRCRAFT={self.aircraft!r}, "
            f"HOURS={self.hours!r}, "
            f"ROUTE_DIR_DESCRIP={self.route_dir_descrip!r}, "
            f"DESIGNATOR={self.designator!r}, "
            f"NAR_TYPE={self.nar_type!r}, "
            f"INLAND_FAC_FIX={self.inland_fac_fix!r}, "
            f"COASTAL_FIX={self.coastal_fix!r}, "
            f"DESTINATION={self.destination!r}, "
            f"ROUTE_STRING={self.route_string!r}, "
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
                f"EFF_DATE: {self.eff_date}, "
                f"ORIGIN_CITY: {self.origin_city}, "
                f"ORIGIN_STATE_CODE: {self.origin_state_code}, "
                f"ORIGIN_COUNTRY_CODE: {self.origin_country_code}, "
                f"DSTN_CITY: {self.dstn_city}, "
                f"DSTN_STATE_CODE: {self.dstn_state_code}, "
                f"DSTN_COUNTRY_CODE: {self.dstn_country_code}, "
                f"PFR_TYPE_CODE: {self.pfr_type_code}, "
                f"SPECIAL_AREA_DESCRIP: {self.special_area_descrip}, "
                f"ALT_DESCRIP: {self.alt_descrip}, "
                f"AIRCRAFT: {self.aircraft}, "
                f"HOURS: {self.hours}, "
                f"ROUTE_DIR_DESCRIP: {self.route_dir_descrip}, "
                f"DESIGNATOR: {self.designator}, "
                f"NAR_TYPE: {self.nar_type}, "
                f"INLAND_FAC_FIX: {self.inland_fac_fix}, "
                f"COASTAL_FIX: {self.coastal_fix}, "
                f"DESTINATION: {self.destination}, "
                f"ROUTE_STRING: {self.route_string}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("PFR_BASE")
class PFR_BASE_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "Preferred Route Base", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = PFR_BASE(
                    eff_date=row["EFF_DATE"],
                    origin_id=row["ORIGIN_ID"],
                    origin_city=row["ORIGIN_CITY"],
                    origin_state_code=row["ORIGIN_STATE_CODE"],
                    origin_country_code=row["ORIGIN_COUNTRY_CODE"],
                    dstn_id=row["DSTN_ID"],
                    dstn_city=row["DSTN_CITY"],
                    dstn_state_code=row["DSTN_STATE_CODE"],
                    dstn_country_code=row["DSTN_COUNTRY_CODE"],
                    pfr_type_code=row["PFR_TYPE_CODE"],
                    route_no=row["ROUTE_NO"],
                    special_area_descrip=row["SPECIAL_AREA_DESCRIP"],
                    alt_descrip=row["ALT_DESCRIP"],
                    aircraft=row["AIRCRAFT"],
                    hours=row["HOURS"],
                    route_dir_descrip=row["ROUTE_DIR_DESCRIP"],
                    designator=row["DESIGNATOR"],
                    nar_type=row["NAR_TYPE"],
                    inland_fac_fix=row["INLAND_FAC_FIX"],
                    coastal_fix=row["COASTAL_FIX"],
                    destination=row["DESTINATION"],
                    route_string=row["ROUTE_STRING"],
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
