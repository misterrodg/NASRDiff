from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class COM(FAA_Record_Base):
    eff_date: str
    comm_loc_id: str
    comm_type: str
    nav_id: str
    nav_type: str
    city: str
    state_code: str
    region_code: str
    country_code: str
    comm_outlet_name: str
    lat_deg: str
    lat_min: str
    lat_sec: str
    lat_hemis: str
    lat_decimal: str
    long_deg: str
    long_min: str
    long_sec: str
    long_hemis: str
    long_decimal: str
    facility_id: str
    facility_name: str
    alt_fss_id: str
    alt_fss_name: str
    opr_hrs: str
    comm_status_code: str
    comm_status_date: str
    remark: str
    file: str
    action: Action
    mods: str

    def __init__(
        self,
        eff_date: str,
        comm_loc_id: str,
        comm_type: str,
        nav_id: str,
        nav_type: str,
        city: str,
        state_code: str,
        region_code: str,
        country_code: str,
        comm_outlet_name: str,
        lat_deg: str,
        lat_min: str,
        lat_sec: str,
        lat_hemis: str,
        lat_decimal: str,
        long_deg: str,
        long_min: str,
        long_sec: str,
        long_hemis: str,
        long_decimal: str,
        facility_id: str,
        facility_name: str,
        alt_fss_id: str,
        alt_fss_name: str,
        opr_hrs: str,
        comm_status_code: str,
        comm_status_date: str,
        remark: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        self.eff_date = replace_empty_string(eff_date)
        self.comm_loc_id = replace_empty_string(comm_loc_id)
        self.comm_type = replace_empty_string(comm_type)
        self.nav_id = replace_empty_string(nav_id)
        self.nav_type = replace_empty_string(nav_type)
        self.city = replace_empty_string(city)
        self.state_code = replace_empty_string(state_code)
        self.region_code = replace_empty_string(region_code)
        self.country_code = replace_empty_string(country_code)
        self.comm_outlet_name = replace_empty_string(comm_outlet_name)
        self.lat_deg = replace_empty_string(lat_deg)
        self.lat_min = replace_empty_string(lat_min)
        self.lat_sec = replace_empty_string(lat_sec)
        self.lat_hemis = replace_empty_string(lat_hemis)
        self.lat_decimal = replace_empty_string(lat_decimal)
        self.long_deg = replace_empty_string(long_deg)
        self.long_min = replace_empty_string(long_min)
        self.long_sec = replace_empty_string(long_sec)
        self.long_hemis = replace_empty_string(long_hemis)
        self.long_decimal = replace_empty_string(long_decimal)
        self.facility_id = replace_empty_string(facility_id)
        self.facility_name = replace_empty_string(facility_name)
        self.alt_fss_id = replace_empty_string(alt_fss_id)
        self.alt_fss_name = replace_empty_string(alt_fss_name)
        self.opr_hrs = replace_empty_string(opr_hrs)
        self.comm_status_code = replace_empty_string(comm_status_code)
        self.comm_status_date = replace_empty_string(comm_status_date)
        self.remark = replace_empty_string(remark)
        self.file = file
        self.action = action
        self.mods = mods

    def to_string(self, last_record: Self | None = None) -> str:
        if last_record:
            modification_string = self.get_mod_string(last_record)
            return f"{self.facility_id} :: {modification_string}"
        return (
            f"{self.facility_id} :: "
            f"EFF_DATE: {self.eff_date}, "
            f"COMM_LOC_ID: {self.comm_loc_id}, "
            f"COMM_TYPE: {self.comm_type}, "
            f"NAV_ID: {self.nav_id}, "
            f"NAV_TYPE: {self.nav_type}, "
            f"CITY: {self.city}, "
            f"STATE_CODE: {self.state_code}, "
            f"REGION_CODE: {self.region_code}, "
            f"COUNTRY_CODE: {self.country_code}, "
            f"COMM_OUTLET_NAME: {self.comm_outlet_name}, "
            f"LAT_DEG: {self.lat_deg}, "
            f"LAT_MIN: {self.lat_min}, "
            f"LAT_SEC: {self.lat_sec}, "
            f"LAT_HEMIS: {self.lat_hemis}, "
            f"LAT_DECIMAL: {self.lat_decimal}, "
            f"LONG_DEG: {self.long_deg}, "
            f"LONG_MIN: {self.long_min}, "
            f"LONG_SEC: {self.long_sec}, "
            f"LONG_HEMIS: {self.long_hemis}, "
            f"LONG_DECIMAL: {self.long_decimal}, "
            f"FACILITY_NAME: {self.facility_name}, "
            f"ALT_FSS_ID: {self.alt_fss_id}, "
            f"ALT_FSS_NAME: {self.alt_fss_name}, "
            f"OPR_HRS: {self.opr_hrs}, "
            f"COMM_STATUS_CODE: {self.comm_status_code}, "
            f"COMM_STATUS_DATE: {self.comm_status_date}, "
            f"REMARK: {self.remark}"
        )


@register_faa_file("COM")
class COM_File(FAA_File_Base):
    def __init__(
        self, file_path: str, filter_object: FilterObject | None = None
    ) -> None:
        super().__init__(file_path, "Communication", filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = COM(
                    eff_date=row["EFF_DATE"],
                    comm_loc_id=row["COMM_LOC_ID"],
                    comm_type=row["COMM_TYPE"],
                    nav_id=row["NAV_ID"],
                    nav_type=row["NAV_TYPE"],
                    city=row["CITY"],
                    state_code=row["STATE_CODE"],
                    region_code=row["REGION_CODE"],
                    country_code=row["COUNTRY_CODE"],
                    comm_outlet_name=row["COMM_OUTLET_NAME"],
                    lat_deg=row["LAT_DEG"],
                    lat_min=row["LAT_MIN"],
                    lat_sec=row["LAT_SEC"],
                    lat_hemis=row["LAT_HEMIS"],
                    lat_decimal=row["LAT_DECIMAL"],
                    long_deg=row["LONG_DEG"],
                    long_min=row["LONG_MIN"],
                    long_sec=row["LONG_SEC"],
                    long_hemis=row["LONG_HEMIS"],
                    long_decimal=row["LONG_DECIMAL"],
                    facility_id=row["FACILITY_ID"],
                    facility_name=row["FACILITY_NAME"],
                    alt_fss_id=row["ALT_FSS_ID"],
                    alt_fss_name=row["ALT_FSS_NAME"],
                    opr_hrs=row["OPR_HRS"],
                    comm_status_code=row["COMM_STATUS_CODE"],
                    comm_status_date=row["COMM_STATUS_DATE"],
                    remark=row["REMARK"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_bounds(
                        record.lat_decimal, record.long_decimal
                    )

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
