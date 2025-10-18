from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class ILS_MKR(FAA_Record_Base):
    eff_date: str
    site_no: str
    site_type_code: str
    state_code: str
    arpt_id: str
    city: str
    country_code: str
    rwy_end_id: str
    ils_loc_id: str
    system_type_code: str
    ils_comp_type_code: str
    component_status: str
    component_status_date: str
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
    lat_long_source_code: str
    site_elevation: str
    mkr_fac_type_code: str
    marker_id_beacon: str
    compass_locator_name: str
    freq: str
    nav_id: str
    nav_type: str
    low_powered_ndb_status: str

    def __init__(
        self,
        eff_date: str,
        site_no: str,
        site_type_code: str,
        state_code: str,
        arpt_id: str,
        city: str,
        country_code: str,
        rwy_end_id: str,
        ils_loc_id: str,
        system_type_code: str,
        ils_comp_type_code: str,
        component_status: str,
        component_status_date: str,
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
        lat_long_source_code: str,
        site_elevation: str,
        mkr_fac_type_code: str,
        marker_id_beacon: str,
        compass_locator_name: str,
        freq: str,
        nav_id: str,
        nav_type: str,
        low_powered_ndb_status: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.site_no = replace_empty_string(site_no)
        self.site_type_code = replace_empty_string(site_type_code)
        self.state_code = replace_empty_string(state_code)
        self.arpt_id = replace_empty_string(arpt_id)
        self.city = replace_empty_string(city)
        self.country_code = replace_empty_string(country_code)
        self.rwy_end_id = replace_empty_string(rwy_end_id)
        self.ils_loc_id = replace_empty_string(ils_loc_id)
        self.system_type_code = replace_empty_string(system_type_code)
        self.ils_comp_type_code = replace_empty_string(ils_comp_type_code)
        self.component_status = replace_empty_string(component_status)
        self.component_status_date = replace_empty_string(component_status_date)
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
        self.lat_long_source_code = replace_empty_string(lat_long_source_code)
        self.site_elevation = replace_empty_string(site_elevation)
        self.mkr_fac_type_code = replace_empty_string(mkr_fac_type_code)
        self.marker_id_beacon = replace_empty_string(marker_id_beacon)
        self.compass_locator_name = replace_empty_string(compass_locator_name)
        self.freq = replace_empty_string(freq)
        self.nav_id = replace_empty_string(nav_id)
        self.nav_type = replace_empty_string(nav_type)
        self.low_powered_ndb_status = replace_empty_string(low_powered_ndb_status)

    def __hash__(self) -> int:
        return hash((self.arpt_id, self.ils_loc_id))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ILS_MKR):
            return False
        return self.arpt_id == other.arpt_id and self.ils_loc_id == other.ils_loc_id

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, ILS_MKR):
            return False
        return (self.arpt_id, self.ils_loc_id, self.file) < (
            other.arpt_id,
            other.ils_loc_id,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"SITE_NO={self.site_no!r}, "
            f"SITE_TYPE_CODE={self.site_type_code!r}, "
            f"STATE_CODE={self.state_code!r}, "
            f"ARPT_ID={self.arpt_id!r}, "
            f"CITY={self.city!r}, "
            f"COUNTRY_CODE={self.country_code!r}, "
            f"RWY_END_ID={self.rwy_end_id!r}, "
            f"ILS_LOC_ID={self.ils_loc_id!r}, "
            f"SYSTEM_TYPE_CODE={self.system_type_code!r}, "
            f"ILS_COMP_TYPE_CODE={self.ils_comp_type_code!r}, "
            f"COMPONENT_STATUS={self.component_status!r}, "
            f"COMPONENT_STATUS_DATE={self.component_status_date!r}, "
            f"LAT_DEG={self.lat_deg!r}, "
            f"LAT_MIN={self.lat_min!r}, "
            f"LAT_SEC={self.lat_sec!r}, "
            f"LAT_HEMIS={self.lat_hemis!r}, "
            f"LAT_DECIMAL={self.lat_decimal!r}, "
            f"LONG_DEG={self.long_deg!r}, "
            f"LONG_MIN={self.long_min!r}, "
            f"LONG_SEC={self.long_sec!r}, "
            f"LONG_HEMIS={self.long_hemis!r}, "
            f"LONG_DECIMAL={self.long_decimal!r}, "
            f"LAT_LONG_SOURCE_CODE={self.lat_long_source_code!r}, "
            f"SITE_ELEVATION={self.site_elevation!r}, "
            f"MKR_FAC_TYPE_CODE={self.mkr_fac_type_code!r}, "
            f"MARKER_ID_BEACON={self.marker_id_beacon!r}, "
            f"COMPASS_LOCATOR_NAME={self.compass_locator_name!r}, "
            f"FREQ={self.freq!r}, "
            f"NAV_ID={self.nav_id!r}, "
            f"NAV_TYPE={self.nav_type!r}, "
            f"LOW_POWERED_NDB_STATUS={self.low_powered_ndb_status!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.arpt_id} :: {self.rwy_end_id} :: I-{self.ils_loc_id}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"SITE_NO: {self.site_no}, "
                f"SITE_TYPE_CODE: {self.site_type_code}, "
                f"STATE_CODE: {self.state_code}, "
                f"CITY: {self.city}, "
                f"COUNTRY_CODE: {self.country_code}, "
                f"SYSTEM_TYPE_CODE: {self.system_type_code}, "
                f"ILS_COMP_TYPE_CODE: {self.ils_comp_type_code}, "
                f"COMPONENT_STATUS: {self.component_status}, "
                f"COMPONENT_STATUS_DATE: {self.component_status_date}, "
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
                f"LAT_LONG_SOURCE_CODE: {self.lat_long_source_code}, "
                f"SITE_ELEVATION: {self.site_elevation}, "
                f"MKR_FAC_TYPE_CODE: {self.mkr_fac_type_code}, "
                f"MARKER_ID_BEACON: {self.marker_id_beacon}, "
                f"COMPASS_LOCATOR_NAME: {self.compass_locator_name}, "
                f"FREQ: {self.freq}, "
                f"NAV_ID: {self.nav_id}, "
                f"NAV_TYPE: {self.nav_type}, "
                f"LOW_POWERED_NDB_STATUS: {self.low_powered_ndb_status}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("ILS_MKR")
class ILS_MKR_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "ILS MKR", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = ILS_MKR(
                    eff_date=row["EFF_DATE"],
                    site_no=row["SITE_NO"],
                    site_type_code=row["SITE_TYPE_CODE"],
                    state_code=row["STATE_CODE"],
                    arpt_id=row["ARPT_ID"],
                    city=row["CITY"],
                    country_code=row["COUNTRY_CODE"],
                    rwy_end_id=row["RWY_END_ID"],
                    ils_loc_id=row["ILS_LOC_ID"],
                    system_type_code=row["SYSTEM_TYPE_CODE"],
                    ils_comp_type_code=row["ILS_COMP_TYPE_CODE"],
                    component_status=row["COMPONENT_STATUS"],
                    component_status_date=row["COMPONENT_STATUS_DATE"],
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
                    lat_long_source_code=row["LAT_LONG_SOURCE_CODE"],
                    site_elevation=row["SITE_ELEVATION"],
                    mkr_fac_type_code=row["MKR_FAC_TYPE_CODE"],
                    marker_id_beacon=row["MARKER_ID_BEACON"],
                    compass_locator_name=row["COMPASS_LOCATOR_NAME"],
                    freq=row["FREQ"],
                    nav_id=row["NAV_ID"],
                    nav_type=row["NAV_TYPE"],
                    low_powered_ndb_status=row["LOW_POWERED_NDB_STATUS"],
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
