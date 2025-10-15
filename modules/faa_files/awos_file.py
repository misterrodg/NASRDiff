from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class AWOS(FAA_Record_Base):
    eff_date: str
    asos_awos_id: str
    asos_awos_type: str
    state_code: str
    city: str
    country_code: str
    commissioned_date: str
    navaid_flag: str
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
    elev: str
    survey_method_code: str
    phone_no: str
    second_phone_no: str
    site_no: str
    site_type_code: str
    remark: str

    def __init__(
        self,
        eff_date: str,
        asos_awos_id: str,
        asos_awos_type: str,
        state_code: str,
        city: str,
        country_code: str,
        commissioned_date: str,
        navaid_flag: str,
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
        elev: str,
        survey_method_code: str,
        phone_no: str,
        second_phone_no: str,
        site_no: str,
        site_type_code: str,
        remark: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.asos_awos_id = replace_empty_string(asos_awos_id)
        self.asos_awos_type = replace_empty_string(asos_awos_type)
        self.state_code = replace_empty_string(state_code)
        self.city = replace_empty_string(city)
        self.country_code = replace_empty_string(country_code)
        self.commissioned_date = replace_empty_string(commissioned_date)
        self.navaid_flag = replace_empty_string(navaid_flag)
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
        self.elev = replace_empty_string(elev)
        self.survey_method_code = replace_empty_string(survey_method_code)
        self.phone_no = replace_empty_string(phone_no)
        self.second_phone_no = replace_empty_string(second_phone_no)
        self.site_no = replace_empty_string(site_no)
        self.site_type_code = replace_empty_string(site_type_code)
        self.remark = replace_empty_string(remark)

    def __hash__(self) -> int:
        return hash((self.asos_awos_id))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, AWOS):
            return False
        return self.asos_awos_id == other.asos_awos_id

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, AWOS):
            return False
        return (self.asos_awos_id, self.file) < (other.asos_awos_id, other.file)

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"ASOS_AWOS_ID={self.asos_awos_id!r}, "
            f"ASOS_AWOS_TYPE={self.asos_awos_type!r}, "
            f"STATE_CODE={self.state_code!r}, "
            f"CITY={self.city!r}, "
            f"COUNTRY_CODE={self.country_code!r}, "
            f"COMMISSIONED_DATE={self.commissioned_date!r}, "
            f"NAVAID_FLAG={self.navaid_flag!r}, "
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
            f"ELEV={self.elev!r}, "
            f"SURVEY_METHOD_CODE={self.survey_method_code!r}, "
            f"PHONE_NO={self.phone_no!r}, "
            f"SECOND_PHONE_NO={self.second_phone_no!r}, "
            f"SITE_NO={self.site_no!r}, "
            f"SITE_TYPE_CODE={self.site_type_code!r}, "
            f"REMARK={self.remark!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.asos_awos_id} :: {self.asos_awos_type}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"STATE_CODE: {self.state_code}, "
                f"CITY: {self.city}, "
                f"COUNTRY_CODE: {self.country_code}, "
                f"COMMISSIONED_DATE: {self.commissioned_date}, "
                f"NAVAID_FLAG: {self.navaid_flag}, "
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
                f"ELEV: {self.elev}, "
                f"SURVEY_METHOD_CODE: {self.survey_method_code}, "
                f"PHONE_NO: {self.phone_no}, "
                f"SECOND_PHONE_NO: {self.second_phone_no}, "
                f"SITE_NO: {self.site_no}, "
                f"SITE_TYPE_CODE: {self.site_type_code}, "
                f"REMARK   : {self.remark}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("AWOS")
class AWOS_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "AWOS", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = AWOS(
                    eff_date=row["EFF_DATE"],
                    asos_awos_id=row["ASOS_AWOS_ID"],
                    asos_awos_type=row["ASOS_AWOS_TYPE"],
                    state_code=row["STATE_CODE"],
                    city=row["CITY"],
                    country_code=row["COUNTRY_CODE"],
                    commissioned_date=row["COMMISSIONED_DATE"],
                    navaid_flag=row["NAVAID_FLAG"],
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
                    elev=row["ELEV"],
                    survey_method_code=row["SURVEY_METHOD_CODE"],
                    phone_no=row["PHONE_NO"],
                    second_phone_no=row["SECOND_PHONE_NO"],
                    site_no=row["SITE_NO"],
                    site_type_code=row["SITE_TYPE_CODE"],
                    remark=row["REMARK"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_airports(
                        record.asos_awos_id
                    )

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
