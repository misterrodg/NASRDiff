from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class ATC_BASE(FAA_Record_Base):
    eff_date: str
    site_no: str
    site_type_code: str
    facility_type: str
    state_code: str
    facility_id: str
    city: str
    country_code: str
    icao_id: str
    facility_name: str
    region_code: str
    twr_operator_code: str
    twr_call: str
    twr_hrs: str
    primary_apch_radio_call: str
    apch_p_provider: str
    apch_p_prov_type_cd: str
    secondary_apch_radio_call: str
    apch_s_provider: str
    apch_s_prov_type_cd: str
    primary_dep_radio_call: str
    dep_p_provider: str
    dep_p_prov_type_cd: str
    secondary_dep_radio_call: str
    dep_s_provider: str
    dep_s_prov_type_cd: str
    ctl_fac_apch_dep_calls: str
    apch_dep_oper_code: str
    ctl_prvding_hrs: str
    secondary_ctl_prvding_hrs: str

    def __init__(
        self,
        eff_date: str,
        site_no: str,
        site_type_code: str,
        facility_type: str,
        state_code: str,
        facility_id: str,
        city: str,
        country_code: str,
        icao_id: str,
        facility_name: str,
        region_code: str,
        twr_operator_code: str,
        twr_call: str,
        twr_hrs: str,
        primary_apch_radio_call: str,
        apch_p_provider: str,
        apch_p_prov_type_cd: str,
        secondary_apch_radio_call: str,
        apch_s_provider: str,
        apch_s_prov_type_cd: str,
        primary_dep_radio_call: str,
        dep_p_provider: str,
        dep_p_prov_type_cd: str,
        secondary_dep_radio_call: str,
        dep_s_provider: str,
        dep_s_prov_type_cd: str,
        ctl_fac_apch_dep_calls: str,
        apch_dep_oper_code: str,
        ctl_prvding_hrs: str,
        secondary_ctl_prvding_hrs: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.site_no = replace_empty_string(site_no)
        self.site_type_code = replace_empty_string(site_type_code)
        self.facility_type = replace_empty_string(facility_type)
        self.state_code = replace_empty_string(state_code)
        self.facility_id = replace_empty_string(facility_id)
        self.city = replace_empty_string(city)
        self.country_code = replace_empty_string(country_code)
        self.icao_id = replace_empty_string(icao_id)
        self.facility_name = replace_empty_string(facility_name)
        self.region_code = replace_empty_string(region_code)
        self.twr_operator_code = replace_empty_string(twr_operator_code)
        self.twr_call = replace_empty_string(twr_call)
        self.twr_hrs = replace_empty_string(twr_hrs)
        self.primary_apch_radio_call = replace_empty_string(primary_apch_radio_call)
        self.apch_p_provider = replace_empty_string(apch_p_provider)
        self.apch_p_prov_type_cd = replace_empty_string(apch_p_prov_type_cd)
        self.secondary_apch_radio_call = replace_empty_string(secondary_apch_radio_call)
        self.apch_s_provider = replace_empty_string(apch_s_provider)
        self.apch_s_prov_type_cd = replace_empty_string(apch_s_prov_type_cd)
        self.primary_dep_radio_call = replace_empty_string(primary_dep_radio_call)
        self.dep_p_provider = replace_empty_string(dep_p_provider)
        self.dep_p_prov_type_cd = replace_empty_string(dep_p_prov_type_cd)
        self.secondary_dep_radio_call = replace_empty_string(secondary_dep_radio_call)
        self.dep_s_provider = replace_empty_string(dep_s_provider)
        self.dep_s_prov_type_cd = replace_empty_string(dep_s_prov_type_cd)
        self.ctl_fac_apch_dep_calls = replace_empty_string(ctl_fac_apch_dep_calls)
        self.apch_dep_oper_code = replace_empty_string(apch_dep_oper_code)
        self.ctl_prvding_hrs = replace_empty_string(ctl_prvding_hrs)
        self.secondary_ctl_prvding_hrs = replace_empty_string(secondary_ctl_prvding_hrs)

    def __hash__(self) -> int:
        return hash((self.facility_id, self.facility_type))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, ATC_BASE):
            return False
        return (
            self.facility_id == other.facility_id
            and self.facility_type == other.facility_type
        )

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, ATC_BASE):
            return False
        return (self.facility_id, self.facility_type, self.file) < (
            other.facility_id,
            other.facility_type,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"SITE_NO={self.site_no!r}, "
            f"SITE_TYPE_CODE={self.site_type_code!r}, "
            f"FACILITY_TYPE={self.facility_type!r}, "
            f"STATE_CODE={self.state_code!r}, "
            f"FACILITY_ID={self.facility_id!r}, "
            f"CITY={self.city!r}, "
            f"COUNTRY_CODE={self.country_code!r}, "
            f"ICAO_ID={self.icao_id!r}, "
            f"FACILITY_NAME={self.facility_name!r}, "
            f"REGION_CODE={self.region_code!r}, "
            f"TWR_OPERATOR_CODE={self.twr_operator_code!r}, "
            f"TWR_CALL={self.twr_call!r}, "
            f"TWR_HRS={self.twr_hrs!r}, "
            f"PRIMARY_APCH_RADIO_CALL={self.primary_apch_radio_call!r}, "
            f"APCH_P_PROVIDER={self.apch_p_provider!r}, "
            f"APCH_P_PROV_TYPE_CD={self.apch_p_prov_type_cd!r}, "
            f"SECONDARY_APCH_RADIO_CALL={self.secondary_apch_radio_call!r}, "
            f"APCH_S_PROVIDER={self.apch_s_provider!r}, "
            f"APCH_S_PROV_TYPE_CD={self.apch_s_prov_type_cd!r}, "
            f"PRIMARY_DEP_RADIO_CALL={self.primary_dep_radio_call!r}, "
            f"DEP_P_PROVIDER={self.dep_p_provider!r}, "
            f"DEP_P_PROV_TYPE_CD={self.dep_p_prov_type_cd!r}, "
            f"SECONDARY_DEP_RADIO_CALL={self.secondary_dep_radio_call!r}, "
            f"DEP_S_PROVIDER={self.dep_s_provider!r}, "
            f"DEP_S_PROV_TYPE_CD={self.dep_s_prov_type_cd!r}, "
            f"CTL_FAC_APCH_DEP_CALLS={self.ctl_fac_apch_dep_calls!r}, "
            f"APCH_DEP_OPER_CODE={self.apch_dep_oper_code!r}, "
            f"CTL_PRVDING_HRS={self.ctl_prvding_hrs!r}, "
            f"SECONDARY_CTL_PRVDING_HRS={self.secondary_ctl_prvding_hrs!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.facility_id} :: {self.facility_type}"

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
                f"ICAO_ID: {self.icao_id}, "
                f"FACILITY_NAME: {self.facility_name}, "
                f"REGION_CODE: {self.region_code}, "
                f"TWR_OPERATOR_CODE: {self.twr_operator_code}, "
                f"TWR_CALL: {self.twr_call}, "
                f"TWR_HRS: {self.twr_hrs}, "
                f"PRIMARY_APCH_RADIO_CALL: {self.primary_apch_radio_call}, "
                f"APCH_P_PROVIDER: {self.apch_p_provider}, "
                f"APCH_P_PROV_TYPE_CD: {self.apch_p_prov_type_cd}, "
                f"SECONDARY_APCH_RADIO_CALL: {self.secondary_apch_radio_call}, "
                f"APCH_S_PROVIDER: {self.apch_s_provider}, "
                f"APCH_S_PROV_TYPE_CD: {self.apch_s_prov_type_cd}, "
                f"PRIMARY_DEP_RADIO_CALL: {self.primary_dep_radio_call}, "
                f"DEP_P_PROVIDER: {self.dep_p_provider}, "
                f"DEP_P_PROV_TYPE_CD: {self.dep_p_prov_type_cd}, "
                f"SECONDARY_DEP_RADIO_CALL: {self.secondary_dep_radio_call}, "
                f"DEP_S_PROVIDER: {self.dep_s_provider}, "
                f"DEP_S_PROV_TYPE_CD: {self.dep_s_prov_type_cd}, "
                f"CTL_FAC_APCH_DEP_CALLS: {self.ctl_fac_apch_dep_calls}, "
                f"APCH_DEP_OPER_CODE: {self.apch_dep_oper_code}, "
                f"CTL_PRVDING_HRS: {self.ctl_prvding_hrs}, "
                f"SECONDARY_CTL_PRVDING_HRS: {self.secondary_ctl_prvding_hrs}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("ATC_BASE")
class ATC_BASE_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "ATC Base", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = ATC_BASE(
                    eff_date=row["EFF_DATE"],
                    site_no=row["SITE_NO"],
                    site_type_code=row["SITE_TYPE_CODE"],
                    facility_type=row["FACILITY_TYPE"],
                    state_code=row["STATE_CODE"],
                    facility_id=row["FACILITY_ID"],
                    city=row["CITY"],
                    country_code=row["COUNTRY_CODE"],
                    icao_id=row["ICAO_ID"],
                    facility_name=row["FACILITY_NAME"],
                    region_code=row["REGION_CODE"],
                    twr_operator_code=row["TWR_OPERATOR_CODE"],
                    twr_call=row["TWR_CALL"],
                    twr_hrs=row["TWR_HRS"],
                    primary_apch_radio_call=row["PRIMARY_APCH_RADIO_CALL"],
                    apch_p_provider=row["APCH_P_PROVIDER"],
                    apch_p_prov_type_cd=row["APCH_P_PROV_TYPE_CD"],
                    secondary_apch_radio_call=row["SECONDARY_APCH_RADIO_CALL"],
                    apch_s_provider=row["APCH_S_PROVIDER"],
                    apch_s_prov_type_cd=row["APCH_S_PROV_TYPE_CD"],
                    primary_dep_radio_call=row["PRIMARY_DEP_RADIO_CALL"],
                    dep_p_provider=row["DEP_P_PROVIDER"],
                    dep_p_prov_type_cd=row["DEP_P_PROV_TYPE_CD"],
                    secondary_dep_radio_call=row["SECONDARY_DEP_RADIO_CALL"],
                    dep_s_provider=row["DEP_S_PROVIDER"],
                    dep_s_prov_type_cd=row["DEP_S_PROV_TYPE_CD"],
                    ctl_fac_apch_dep_calls=row["CTL_FAC_APCH_DEP_CALLS"],
                    apch_dep_oper_code=row["APCH_DEP_OPER_CODE"],
                    ctl_prvding_hrs=row["CTL_PRVDING_HRS"],
                    secondary_ctl_prvding_hrs=row["SECONDARY_CTL_PRVDING_HRS"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_airports(
                        record.facility_id
                    )

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
