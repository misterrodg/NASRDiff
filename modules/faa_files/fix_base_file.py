from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class FIX_BASE(FAA_Record_Base):
    eff_date: str
    fix_id: str
    icao_region_code: str
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
    fix_id_old: str
    charting_remark: str
    fix_use_code: str
    artcc_id_high: str
    artcc_id_low: str
    pitch_flag: str
    catch_flag: str
    sua_atcaa_flag: str
    min_recep_alt: str
    compulsory: str
    charts: str

    def __init__(
        self,
        eff_date: str,
        fix_id: str,
        icao_region_code: str,
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
        fix_id_old: str,
        charting_remark: str,
        fix_use_code: str,
        artcc_id_high: str,
        artcc_id_low: str,
        pitch_flag: str,
        catch_flag: str,
        sua_atcaa_flag: str,
        min_recep_alt: str,
        compulsory: str,
        charts: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.fix_id = replace_empty_string(fix_id)
        self.icao_region_code = replace_empty_string(icao_region_code)
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
        self.fix_id_old = replace_empty_string(fix_id_old)
        self.charting_remark = replace_empty_string(charting_remark)
        self.fix_use_code = replace_empty_string(fix_use_code)
        self.artcc_id_high = replace_empty_string(artcc_id_high)
        self.artcc_id_low = replace_empty_string(artcc_id_low)
        self.pitch_flag = replace_empty_string(pitch_flag)
        self.catch_flag = replace_empty_string(catch_flag)
        self.sua_atcaa_flag = replace_empty_string(sua_atcaa_flag)
        self.min_recep_alt = replace_empty_string(min_recep_alt)
        self.compulsory = replace_empty_string(compulsory)
        self.charts = replace_empty_string(charts)

    def __hash__(self) -> int:
        return hash((self.fix_id, self.charts))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, FIX_BASE):
            return False
        return self.fix_id == other.fix_id and self.charts == other.charts

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, FIX_BASE):
            return False
        return (self.fix_id, self.charts, self.file) < (
            other.fix_id,
            other.charts,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"FIX_ID={self.fix_id!r}, "
            f"ICAO_REGION_CODE={self.icao_region_code!r}, "
            f"STATE_CODE={self.state_code!r}, "
            f"COUNTRY_CODE={self.country_code!r}, "
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
            f"FIX_ID_OLD={self.fix_id_old!r}, "
            f"CHARTING_REMARK={self.charting_remark!r}, "
            f"FIX_USE_CODE={self.fix_use_code!r}, "
            f"ARTCC_ID_HIGH={self.artcc_id_high!r}, "
            f"ARTCC_ID_LOW={self.artcc_id_low!r}, "
            f"PITCH_FLAG={self.pitch_flag!r}, "
            f"CATCH_FLAG={self.catch_flag!r}, "
            f"SUA_ATCAA_FLAG={self.sua_atcaa_flag!r}, "
            f"MIN_RECEP_ALT={self.min_recep_alt!r}, "
            f"COMPULSORY={self.compulsory!r}, "
            f"CHARTS={self.charts!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.fix_id} :: {self.charts}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"ICAO_REGION_CODE: {self.icao_region_code}, "
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
                f"FIX_ID_OLD: {self.fix_id_old}, "
                f"CHARTING_REMARK: {self.charting_remark}, "
                f"FIX_USE_CODE: {self.fix_use_code}, "
                f"ARTCC_ID_HIGH: {self.artcc_id_high}, "
                f"ARTCC_ID_LOW: {self.artcc_id_low}, "
                f"PITCH_FLAG: {self.pitch_flag}, "
                f"CATCH_FLAG: {self.catch_flag}, "
                f"SUA_ATCAA_FLAG: {self.sua_atcaa_flag}, "
                f"MIN_RECEP_ALT: {self.min_recep_alt}, "
                f"COMPULSORY: {self.compulsory}, "
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("FIX_BASE")
class FIX_BASE_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "Fix Base", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = FIX_BASE(
                    eff_date=row["EFF_DATE"],
                    fix_id=row["FIX_ID"],
                    icao_region_code=row["ICAO_REGION_CODE"],
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
                    fix_id_old=row["FIX_ID_OLD"],
                    charting_remark=row["CHARTING_REMARK"],
                    fix_use_code=row["FIX_USE_CODE"],
                    artcc_id_high=row["ARTCC_ID_HIGH"],
                    artcc_id_low=row["ARTCC_ID_LOW"],
                    pitch_flag=row["PITCH_FLAG"],
                    catch_flag=row["CATCH_FLAG"],
                    sua_atcaa_flag=row["SUA_ATCAA_FLAG"],
                    min_recep_alt=row["MIN_RECEP_ALT"],
                    compulsory=row["COMPULSORY"],
                    charts=row["CHARTS"],
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
