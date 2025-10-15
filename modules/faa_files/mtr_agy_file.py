from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class MTR_AGY(FAA_Record_Base):
    eff_date: str
    route_type_code: str
    route_id: str
    artcc: str
    agency_type: str
    agency_name: str
    station: str
    address: str
    city: str
    state_code: str
    zip_code: str
    commercial_no: str
    dsn_no: str
    hours: str

    def __init__(
        self,
        eff_date: str,
        route_type_code: str,
        route_id: str,
        artcc: str,
        agency_type: str,
        agency_name: str,
        station: str,
        address: str,
        city: str,
        state_code: str,
        zip_code: str,
        commercial_no: str,
        dsn_no: str,
        hours: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.route_type_code = replace_empty_string(route_type_code)
        self.route_id = replace_empty_string(route_id)
        self.artcc = replace_empty_string(artcc)
        self.agency_type = replace_empty_string(agency_type)
        self.agency_name = replace_empty_string(agency_name)
        self.station = replace_empty_string(station)
        self.address = replace_empty_string(address)
        self.city = replace_empty_string(city)
        self.state_code = replace_empty_string(state_code)
        self.zip_code = replace_empty_string(zip_code)
        self.commercial_no = replace_empty_string(commercial_no)
        self.dsn_no = replace_empty_string(dsn_no)
        self.hours = replace_empty_string(hours)

    def __hash__(self) -> int:
        return hash((self.route_id))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, MTR_AGY):
            return False
        return self.route_id == other.route_id

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, MTR_AGY):
            return False
        return (self.route_id) < (other.route_id)

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"ROUTE_TYPE_CODE={self.route_type_code!r}, "
            f"ROUTE_ID={self.route_id!r}, "
            f"ARTCC={self.artcc!r}, "
            f"AGENCY_TYPE={self.agency_type!r}, "
            f"AGENCY_NAME={self.agency_name!r}, "
            f"STATION={self.station!r}, "
            f"ADDRESS={self.address!r}, "
            f"CITY={self.city!r}, "
            f"STATE_CODE={self.state_code!r}, "
            f"ZIP_CODE={self.zip_code!r}, "
            f"COMMERCIAL_NO={self.commercial_no!r}, "
            f"DSN_NO={self.dsn_no!r}, "
            f"HOURS={self.hours!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.route_id}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"ROUTE_TYPE_CODE: {self.route_type_code}, "
                f"ARTCC: {self.artcc}, "
                f"AGENCY_TYPE: {self.agency_type}, "
                f"AGENCY_NAME: {self.agency_name}, "
                f"STATION: {self.station}, "
                f"ADDRESS: {self.address}, "
                f"CITY: {self.city}, "
                f"STATE_CODE: {self.state_code}, "
                f"ZIP_CODE: {self.zip_code}, "
                f"COMMERCIAL_NO: {self.commercial_no}, "
                f"DSN_NO: {self.dsn_no}, "
                f"HOURS: {self.hours}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("MTR_AGY")
class MTR_AGY_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "MTR Agency", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = MTR_AGY(
                    eff_date=row["EFF_DATE"],
                    route_type_code=row["ROUTE_TYPE_CODE"],
                    route_id=row["ROUTE_ID"],
                    artcc=row["ARTCC"],
                    agency_type=row["AGENCY_TYPE"],
                    agency_name=row["AGENCY_NAME"],
                    station=row["STATION"],
                    address=row["ADDRESS"],
                    city=row["CITY"],
                    state_code=row["STATE_CODE"],
                    zip_code=row["ZIP_CODE"],
                    commercial_no=row["COMMERCIAL_NO"],
                    dsn_no=row["DSN_NO"],
                    hours=row["HOURS"],
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
