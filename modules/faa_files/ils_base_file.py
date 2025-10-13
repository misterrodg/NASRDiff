from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class ILS_BASE(FAA_Record_Base):
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
    state_name: str
    region_code: str
    rwy_len: str
    rwy_width: str
    category: str
    owner: str
    operator: str
    apch_bear: str
    mag_var: str
    mag_var_hemis: str
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
    loc_freq: str
    bk_course_status_code: str
    file: str
    action: Action
    mods: str

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
        state_name: str,
        region_code: str,
        rwy_len: str,
        rwy_width: str,
        category: str,
        owner: str,
        operator: str,
        apch_bear: str,
        mag_var: str,
        mag_var_hemis: str,
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
        loc_freq: str,
        bk_course_status_code: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
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
        self.state_name = replace_empty_string(state_name)
        self.region_code = replace_empty_string(region_code)
        self.rwy_len = replace_empty_string(rwy_len)
        self.rwy_width = replace_empty_string(rwy_width)
        self.category = replace_empty_string(category)
        self.owner = replace_empty_string(owner)
        self.operator = replace_empty_string(operator)
        self.apch_bear = replace_empty_string(apch_bear)
        self.mag_var = replace_empty_string(mag_var)
        self.mag_var_hemis = replace_empty_string(mag_var_hemis)
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
        self.loc_freq = replace_empty_string(loc_freq)
        self.bk_course_status_code = replace_empty_string(bk_course_status_code)
        self.file = file
        self.action = action
        self.mods = mods

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
                f"STATE_NAME: {self.state_name}, "
                f"REGION_CODE: {self.region_code}, "
                f"RWY_LEN: {self.rwy_len}, "
                f"RWY_WIDTH: {self.rwy_width}, "
                f"CATEGORY: {self.category}, "
                f"OWNER: {self.owner}, "
                f"OPERATOR: {self.operator}, "
                f"APCH_BEAR: {self.apch_bear}, "
                f"MAG_VAR: {self.mag_var}, "
                f"MAG_VAR_HEMIS: {self.mag_var_hemis}, "
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
                f"LOC_FREQ: {self.loc_freq}, "
                f"BK_COURSE_STATUS_CODE: {self.bk_course_status_code}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("ILS_BASE")
class ILS_BASE_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "ILS Base", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = ILS_BASE(
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
                    state_name=row["STATE_NAME"],
                    region_code=row["REGION_CODE"],
                    rwy_len=row["RWY_LEN"],
                    rwy_width=row["RWY_WIDTH"],
                    category=row["CATEGORY"],
                    owner=row["OWNER"],
                    operator=row["OPERATOR"],
                    apch_bear=row["APCH_BEAR"],
                    mag_var=row["MAG_VAR"],
                    mag_var_hemis=row["MAG_VAR_HEMIS"],
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
                    loc_freq=row["LOC_FREQ"],
                    bk_course_status_code=row["BK_COURSE_STATUS_CODE"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_airports(
                        record.arpt_id.strip()
                    )

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
