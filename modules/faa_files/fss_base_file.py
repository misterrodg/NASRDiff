from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class FSS_BASE(FAA_Record_Base):
    eff_date: str
    fss_id: str
    name: str
    update_date: str
    fss_fac_type: str
    voice_call: str
    city: str
    state_code: str
    country_code: str
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
    opr_hours: str
    fac_status: str
    alternate_fss: str
    wea_radar_flag: str
    phone_no: str
    toll_free_no: str
    file: str
    action: Action
    mods: str

    def __init__(
        self,
        eff_date: str,
        fss_id: str,
        name: str,
        update_date: str,
        fss_fac_type: str,
        voice_call: str,
        city: str,
        state_code: str,
        country_code: str,
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
        opr_hours: str,
        fac_status: str,
        alternate_fss: str,
        wea_radar_flag: str,
        phone_no: str,
        toll_free_no: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        self.eff_date = replace_empty_string(eff_date)
        self.fss_id = replace_empty_string(fss_id)
        self.name = replace_empty_string(name)
        self.update_date = replace_empty_string(update_date)
        self.fss_fac_type = replace_empty_string(fss_fac_type)
        self.voice_call = replace_empty_string(voice_call)
        self.city = replace_empty_string(city)
        self.state_code = replace_empty_string(state_code)
        self.country_code = replace_empty_string(country_code)
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
        self.opr_hours = replace_empty_string(opr_hours)
        self.fac_status = replace_empty_string(fac_status)
        self.alternate_fss = replace_empty_string(alternate_fss)
        self.wea_radar_flag = replace_empty_string(wea_radar_flag)
        self.phone_no = replace_empty_string(phone_no)
        self.toll_free_no = replace_empty_string(toll_free_no)
        self.file = file
        self.action = action
        self.mods = mods

    def to_string(self, last_record: Self | None = None) -> str:
        if last_record:
            modification_string = self.get_mod_string(last_record)
            return f"{self.fss_id} :: {modification_string}"
        return (
            f"{self.fss_id} :: "
            f"EFF_DATE: {self.eff_date}, "
            f"NAME: {self.name}, "
            f"UPDATE_DATE: {self.update_date}, "
            f"FSS_FAC_TYPE: {self.fss_fac_type}, "
            f"VOICE_CALL: {self.voice_call}, "
            f"CITY: {self.city}, "
            f"STATE_CODE: {self.state_code}, "
            f"COUNTRY_CODE: {self.country_code}, "
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
            f"OPR_HOURS: {self.opr_hours}, "
            f"FAC_STATUS: {self.fac_status}, "
            f"ALTERNATE_FSS: {self.alternate_fss}, "
            f"WEA_RADAR_FLAG: {self.wea_radar_flag}, "
            f"PHONE_NO: {self.phone_no}, "
            f"TOLL_FREE_NO: {self.toll_free_no}"
        )


@register_faa_file("FSS_BASE")
class FSS_BASE_File(FAA_File_Base):
    def __init__(
        self, file_path: str, filter_object: FilterObject | None = None
    ) -> None:
        super().__init__(file_path, "FSS Base", filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = FSS_BASE(
                    eff_date=row["EFF_DATE"],
                    fss_id=row["FSS_ID"],
                    name=row["NAME"],
                    update_date=row["UPDATE_DATE"],
                    fss_fac_type=row["FSS_FAC_TYPE"],
                    voice_call=row["VOICE_CALL"],
                    city=row["CITY"],
                    state_code=row["STATE_CODE"],
                    country_code=row["COUNTRY_CODE"],
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
                    opr_hours=row["OPR_HOURS"],
                    fac_status=row["FAC_STATUS"],
                    alternate_fss=row["ALTERNATE_FSS"],
                    wea_radar_flag=row["WEA_RADAR_FLAG"],
                    phone_no=row["PHONE_NO"],
                    toll_free_no=row["TOLL_FREE_NO"],
                    file=row["File"],
                    action=row["Action"],
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
