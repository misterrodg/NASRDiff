from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class APT_BASE(FAA_Record_Base):
    eff_date: str
    site_no: str
    site_type_code: str
    state_code: str
    arpt_id: str
    city: str
    country_code: str
    region_code: str
    ado_code: str
    state_name: str
    county_name: str
    county_assoc_state: str
    arpt_name: str
    ownership_type_code: str
    facility_use_code: str
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
    survey_method_code: str
    elev: str
    elev_method_code: str
    mag_varn: str
    mag_hemis: str
    mag_varn_year: str
    tpa: str
    chart_name: str
    dist_city_to_airport: str
    direction_code: str
    acreage: str
    resp_artcc_id: str
    computer_id: str
    artcc_name: str
    fss_on_arpt_flag: str
    fss_id: str
    fss_name: str
    phone_no: str
    toll_free_no: str
    alt_fss_id: str
    alt_fss_name: str
    alt_toll_free_no: str
    notam_id: str
    notam_flag: str
    activation_date: str
    arpt_status: str
    far_139_type_code: str
    far_139_carrier_ser_code: str
    arff_cert_type_date: str
    nasp_code: str
    asp_anlys_dtrm_code: str
    cust_flag: str
    lndg_rights_flag: str
    joint_use_flag: str
    mil_lndg_flag: str
    inspect_method_code: str
    inspector_code: str
    last_inspection: str
    last_info_response: str
    fuel_types: str
    airframe_repair_ser_code: str
    pwr_plant_repair_ser: str
    bottled_oxy_type: str
    bulk_oxy_type: str
    lgt_sked: str
    bcn_lgt_sked: str
    twr_type_code: str
    seg_circle_mkr_flag: str
    bcn_lens_color: str
    lndg_fee_flag: str
    medical_use_flag: str
    arpt_psn_source: str
    position_src_date: str
    arpt_elev_source: str
    elevation_src_date: str
    contr_fuel_avbl: str
    trns_strg_buoy_flag: str
    trns_strg_hgr_flag: str
    trns_strg_tie_flag: str
    other_services: str
    wind_indcr_flag: str
    icao_id: str
    min_op_network: str
    user_fee_flag: str
    cta: str

    def __init__(
        self,
        eff_date: str,
        site_no: str,
        site_type_code: str,
        state_code: str,
        arpt_id: str,
        city: str,
        country_code: str,
        region_code: str,
        ado_code: str,
        state_name: str,
        county_name: str,
        county_assoc_state: str,
        arpt_name: str,
        ownership_type_code: str,
        facility_use_code: str,
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
        survey_method_code: str,
        elev: str,
        elev_method_code: str,
        mag_varn: str,
        mag_hemis: str,
        mag_varn_year: str,
        tpa: str,
        chart_name: str,
        dist_city_to_airport: str,
        direction_code: str,
        acreage: str,
        resp_artcc_id: str,
        computer_id: str,
        artcc_name: str,
        fss_on_arpt_flag: str,
        fss_id: str,
        fss_name: str,
        phone_no: str,
        toll_free_no: str,
        alt_fss_id: str,
        alt_fss_name: str,
        alt_toll_free_no: str,
        notam_id: str,
        notam_flag: str,
        activation_date: str,
        arpt_status: str,
        far_139_type_code: str,
        far_139_carrier_ser_code: str,
        arff_cert_type_date: str,
        nasp_code: str,
        asp_anlys_dtrm_code: str,
        cust_flag: str,
        lndg_rights_flag: str,
        joint_use_flag: str,
        mil_lndg_flag: str,
        inspect_method_code: str,
        inspector_code: str,
        last_inspection: str,
        last_info_response: str,
        fuel_types: str,
        airframe_repair_ser_code: str,
        pwr_plant_repair_ser: str,
        bottled_oxy_type: str,
        bulk_oxy_type: str,
        lgt_sked: str,
        bcn_lgt_sked: str,
        twr_type_code: str,
        seg_circle_mkr_flag: str,
        bcn_lens_color: str,
        lndg_fee_flag: str,
        medical_use_flag: str,
        arpt_psn_source: str,
        position_src_date: str,
        arpt_elev_source: str,
        elevation_src_date: str,
        contr_fuel_avbl: str,
        trns_strg_buoy_flag: str,
        trns_strg_hgr_flag: str,
        trns_strg_tie_flag: str,
        other_services: str,
        wind_indcr_flag: str,
        icao_id: str,
        min_op_network: str,
        user_fee_flag: str,
        cta: str,
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
        self.region_code = replace_empty_string(region_code)
        self.ado_code = replace_empty_string(ado_code)
        self.state_name = replace_empty_string(state_name)
        self.county_name = replace_empty_string(county_name)
        self.county_assoc_state = replace_empty_string(county_assoc_state)
        self.arpt_name = replace_empty_string(arpt_name)
        self.ownership_type_code = replace_empty_string(ownership_type_code)
        self.facility_use_code = replace_empty_string(facility_use_code)
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
        self.survey_method_code = replace_empty_string(survey_method_code)
        self.elev = replace_empty_string(elev)
        self.elev_method_code = replace_empty_string(elev_method_code)
        self.mag_varn = replace_empty_string(mag_varn)
        self.mag_hemis = replace_empty_string(mag_hemis)
        self.mag_varn_year = replace_empty_string(mag_varn_year)
        self.tpa = replace_empty_string(tpa)
        self.chart_name = replace_empty_string(chart_name)
        self.dist_city_to_airport = replace_empty_string(dist_city_to_airport)
        self.direction_code = replace_empty_string(direction_code)
        self.acreage = replace_empty_string(acreage)
        self.resp_artcc_id = replace_empty_string(resp_artcc_id)
        self.computer_id = replace_empty_string(computer_id)
        self.artcc_name = replace_empty_string(artcc_name)
        self.fss_on_arpt_flag = replace_empty_string(fss_on_arpt_flag)
        self.fss_id = replace_empty_string(fss_id)
        self.fss_name = replace_empty_string(fss_name)
        self.phone_no = replace_empty_string(phone_no)
        self.toll_free_no = replace_empty_string(toll_free_no)
        self.alt_fss_id = replace_empty_string(alt_fss_id)
        self.alt_fss_name = replace_empty_string(alt_fss_name)
        self.alt_toll_free_no = replace_empty_string(alt_toll_free_no)
        self.notam_id = replace_empty_string(notam_id)
        self.notam_flag = replace_empty_string(notam_flag)
        self.activation_date = replace_empty_string(activation_date)
        self.arpt_status = replace_empty_string(arpt_status)
        self.far_139_type_code = replace_empty_string(far_139_type_code)
        self.far_139_carrier_ser_code = replace_empty_string(far_139_carrier_ser_code)
        self.arff_cert_type_date = replace_empty_string(arff_cert_type_date)
        self.nasp_code = replace_empty_string(nasp_code)
        self.asp_anlys_dtrm_code = replace_empty_string(asp_anlys_dtrm_code)
        self.cust_flag = replace_empty_string(cust_flag)
        self.lndg_rights_flag = replace_empty_string(lndg_rights_flag)
        self.joint_use_flag = replace_empty_string(joint_use_flag)
        self.mil_lndg_flag = replace_empty_string(mil_lndg_flag)
        self.inspect_method_code = replace_empty_string(inspect_method_code)
        self.inspector_code = replace_empty_string(inspector_code)
        self.last_inspection = replace_empty_string(last_inspection)
        self.last_info_response = replace_empty_string(last_info_response)
        self.fuel_types = replace_empty_string(fuel_types)
        self.airframe_repair_ser_code = replace_empty_string(airframe_repair_ser_code)
        self.pwr_plant_repair_ser = replace_empty_string(pwr_plant_repair_ser)
        self.bottled_oxy_type = replace_empty_string(bottled_oxy_type)
        self.bulk_oxy_type = replace_empty_string(bulk_oxy_type)
        self.lgt_sked = replace_empty_string(lgt_sked)
        self.bcn_lgt_sked = replace_empty_string(bcn_lgt_sked)
        self.twr_type_code = replace_empty_string(twr_type_code)
        self.seg_circle_mkr_flag = replace_empty_string(seg_circle_mkr_flag)
        self.bcn_lens_color = replace_empty_string(bcn_lens_color)
        self.lndg_fee_flag = replace_empty_string(lndg_fee_flag)
        self.medical_use_flag = replace_empty_string(medical_use_flag)
        self.arpt_psn_source = replace_empty_string(arpt_psn_source)
        self.position_src_date = replace_empty_string(position_src_date)
        self.arpt_elev_source = replace_empty_string(arpt_elev_source)
        self.elevation_src_date = replace_empty_string(elevation_src_date)
        self.contr_fuel_avbl = replace_empty_string(contr_fuel_avbl)
        self.trns_strg_buoy_flag = replace_empty_string(trns_strg_buoy_flag)
        self.trns_strg_hgr_flag = replace_empty_string(trns_strg_hgr_flag)
        self.trns_strg_tie_flag = replace_empty_string(trns_strg_tie_flag)
        self.other_services = replace_empty_string(other_services)
        self.wind_indcr_flag = replace_empty_string(wind_indcr_flag)
        self.icao_id = replace_empty_string(icao_id)
        self.min_op_network = replace_empty_string(min_op_network)
        self.user_fee_flag = replace_empty_string(user_fee_flag)
        self.cta = replace_empty_string(cta)

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.arpt_id}"

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
                f"REGION_CODE: {self.region_code}, "
                f"ADO_CODE: {self.ado_code}, "
                f"STATE_NAME: {self.state_name}, "
                f"COUNTY_NAME: {self.county_name}, "
                f"COUNTY_ASSOC_STATE: {self.county_assoc_state}, "
                f"ARPT_NAME: {self.arpt_name}, "
                f"OWNERSHIP_TYPE_CODE: {self.ownership_type_code}, "
                f"FACILITY_USE_CODE: {self.facility_use_code}, "
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
                f"SURVEY_METHOD_CODE: {self.survey_method_code}, "
                f"ELEV: {self.elev}, "
                f"ELEV_METHOD_CODE: {self.elev_method_code}, "
                f"MAG_VARN: {self.mag_varn}, "
                f"MAG_HEMIS: {self.mag_hemis}, "
                f"MAG_VARN_YEAR: {self.mag_varn_year}, "
                f"TPA: {self.tpa}, "
                f"CHART_NAME: {self.chart_name}, "
                f"DIST_CITY_TO_AIRPORT: {self.dist_city_to_airport}, "
                f"DIRECTION_CODE: {self.direction_code}, "
                f"ACREAGE: {self.acreage}, "
                f"RESP_ARTCC_ID: {self.resp_artcc_id}, "
                f"COMPUTER_ID: {self.computer_id}, "
                f"ARTCC_NAME: {self.artcc_name}, "
                f"FSS_ON_ARPT_FLAG: {self.fss_on_arpt_flag}, "
                f"FSS_ID: {self.fss_id}, "
                f"FSS_NAME: {self.fss_name}, "
                f"PHONE_NO: {self.phone_no}, "
                f"TOLL_FREE_NO: {self.toll_free_no}, "
                f"ALT_FSS_ID: {self.alt_fss_id}, "
                f"ALT_FSS_NAME: {self.alt_fss_name}, "
                f"ALT_TOLL_FREE_NO: {self.alt_toll_free_no}, "
                f"NOTAM_ID: {self.notam_id}, "
                f"NOTAM_FLAG: {self.notam_flag}, "
                f"ACTIVATION_DATE: {self.activation_date}, "
                f"ARPT_STATUS: {self.arpt_status}, "
                f"FAR_139_TYPE_CODE: {self.far_139_type_code}, "
                f"FAR_139_CARRIER_SER_CODE: {self.far_139_carrier_ser_code}, "
                f"ARFF_CERT_TYPE_DATE: {self.arff_cert_type_date}, "
                f"NASP_CODE: {self.nasp_code}, "
                f"ASP_ANLYS_DTRM_CODE: {self.asp_anlys_dtrm_code}, "
                f"CUST_FLAG: {self.cust_flag}, "
                f"LNDG_RIGHTS_FLAG: {self.lndg_rights_flag}, "
                f"JOINT_USE_FLAG: {self.joint_use_flag}, "
                f"MIL_LNDG_FLAG: {self.mil_lndg_flag}, "
                f"INSPECT_METHOD_CODE: {self.inspect_method_code}, "
                f"INSPECTOR_CODE: {self.inspector_code}, "
                f"LAST_INSPECTION: {self.last_inspection}, "
                f"LAST_INFO_RESPONSE: {self.last_info_response}, "
                f"FUEL_TYPES: {self.fuel_types}, "
                f"AIRFRAME_REPAIR_SER_CODE: {self.airframe_repair_ser_code}, "
                f"PWR_PLANT_REPAIR_SER: {self.pwr_plant_repair_ser}, "
                f"BOTTLED_OXY_TYPE: {self.bottled_oxy_type}, "
                f"BULK_OXY_TYPE: {self.bulk_oxy_type}, "
                f"LGT_SKED: {self.lgt_sked}, "
                f"BCN_LGT_SKED: {self.bcn_lgt_sked}, "
                f"TWR_TYPE_CODE: {self.twr_type_code}, "
                f"SEG_CIRCLE_MKR_FLAG: {self.seg_circle_mkr_flag}, "
                f"BCN_LENS_COLOR: {self.bcn_lens_color}, "
                f"LNDG_FEE_FLAG: {self.lndg_fee_flag}, "
                f"MEDICAL_USE_FLAG: {self.medical_use_flag}, "
                f"ARPT_PSN_SOURCE: {self.arpt_psn_source}, "
                f"POSITION_SRC_DATE: {self.position_src_date}, "
                f"ARPT_ELEV_SOURCE: {self.arpt_elev_source}, "
                f"ELEVATION_SRC_DATE: {self.elevation_src_date}, "
                f"CONTR_FUEL_AVBL: {self.contr_fuel_avbl}, "
                f"TRNS_STRG_BUOY_FLAG: {self.trns_strg_buoy_flag}, "
                f"TRNS_STRG_HGR_FLAG: {self.trns_strg_hgr_flag}, "
                f"TRNS_STRG_TIE_FLAG: {self.trns_strg_tie_flag}, "
                f"OTHER_SERVICES: {self.other_services}, "
                f"WIND_INDCR_FLAG: {self.wind_indcr_flag}, "
                f"ICAO_ID: {self.icao_id}, "
                f"MIN_OP_NETWORK: {self.min_op_network}, "
                f"USER_FEE_FLAG: {self.user_fee_flag}, "
                f"CTA: {self.cta}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("APT_BASE")
class APT_BASE_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "Airport Base", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = APT_BASE(
                    eff_date=row["EFF_DATE"],
                    site_no=row["SITE_NO"],
                    site_type_code=row["SITE_TYPE_CODE"],
                    state_code=row["STATE_CODE"],
                    arpt_id=row["ARPT_ID"],
                    city=row["CITY"],
                    country_code=row["COUNTRY_CODE"],
                    region_code=row["REGION_CODE"],
                    ado_code=row["ADO_CODE"],
                    state_name=row["STATE_NAME"],
                    county_name=row["COUNTY_NAME"],
                    county_assoc_state=row["COUNTY_ASSOC_STATE"],
                    arpt_name=row["ARPT_NAME"],
                    ownership_type_code=row["OWNERSHIP_TYPE_CODE"],
                    facility_use_code=row["FACILITY_USE_CODE"],
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
                    survey_method_code=row["SURVEY_METHOD_CODE"],
                    elev=row["ELEV"],
                    elev_method_code=row["ELEV_METHOD_CODE"],
                    mag_varn=row["MAG_VARN"],
                    mag_hemis=row["MAG_HEMIS"],
                    mag_varn_year=row["MAG_VARN_YEAR"],
                    tpa=row["TPA"],
                    chart_name=row["CHART_NAME"],
                    dist_city_to_airport=row["DIST_CITY_TO_AIRPORT"],
                    direction_code=row["DIRECTION_CODE"],
                    acreage=row["ACREAGE"],
                    resp_artcc_id=row["RESP_ARTCC_ID"],
                    computer_id=row["COMPUTER_ID"],
                    artcc_name=row["ARTCC_NAME"],
                    fss_on_arpt_flag=row["FSS_ON_ARPT_FLAG"],
                    fss_id=row["FSS_ID"],
                    fss_name=row["FSS_NAME"],
                    phone_no=row["PHONE_NO"],
                    toll_free_no=row["TOLL_FREE_NO"],
                    alt_fss_id=row["ALT_FSS_ID"],
                    alt_fss_name=row["ALT_FSS_NAME"],
                    alt_toll_free_no=row["ALT_TOLL_FREE_NO"],
                    notam_id=row["NOTAM_ID"],
                    notam_flag=row["NOTAM_FLAG"],
                    activation_date=row["ACTIVATION_DATE"],
                    arpt_status=row["ARPT_STATUS"],
                    far_139_type_code=row["FAR_139_TYPE_CODE"],
                    far_139_carrier_ser_code=row["FAR_139_CARRIER_SER_CODE"],
                    arff_cert_type_date=row["ARFF_CERT_TYPE_DATE"],
                    nasp_code=row["NASP_CODE"],
                    asp_anlys_dtrm_code=row["ASP_ANLYS_DTRM_CODE"],
                    cust_flag=row["CUST_FLAG"],
                    lndg_rights_flag=row["LNDG_RIGHTS_FLAG"],
                    joint_use_flag=row["JOINT_USE_FLAG"],
                    mil_lndg_flag=row["MIL_LNDG_FLAG"],
                    inspect_method_code=row["INSPECT_METHOD_CODE"],
                    inspector_code=row["INSPECTOR_CODE"],
                    last_inspection=row["LAST_INSPECTION"],
                    last_info_response=row["LAST_INFO_RESPONSE"],
                    fuel_types=row["FUEL_TYPES"],
                    airframe_repair_ser_code=row["AIRFRAME_REPAIR_SER_CODE"],
                    pwr_plant_repair_ser=row["PWR_PLANT_REPAIR_SER"],
                    bottled_oxy_type=row["BOTTLED_OXY_TYPE"],
                    bulk_oxy_type=row["BULK_OXY_TYPE"],
                    lgt_sked=row["LGT_SKED"],
                    bcn_lgt_sked=row["BCN_LGT_SKED"],
                    twr_type_code=row["TWR_TYPE_CODE"],
                    seg_circle_mkr_flag=row["SEG_CIRCLE_MKR_FLAG"],
                    bcn_lens_color=row["BCN_LENS_COLOR"],
                    lndg_fee_flag=row["LNDG_FEE_FLAG"],
                    medical_use_flag=row["MEDICAL_USE_FLAG"],
                    arpt_psn_source=row["ARPT_PSN_SOURCE"],
                    position_src_date=row["POSITION_SRC_DATE"],
                    arpt_elev_source=row["ARPT_ELEV_SOURCE"],
                    elevation_src_date=row["ELEVATION_SRC_DATE"],
                    contr_fuel_avbl=row["CONTR_FUEL_AVBL"],
                    trns_strg_buoy_flag=row["TRNS_STRG_BUOY_FLAG"],
                    trns_strg_hgr_flag=row["TRNS_STRG_HGR_FLAG"],
                    trns_strg_tie_flag=row["TRNS_STRG_TIE_FLAG"],
                    other_services=row["OTHER_SERVICES"],
                    wind_indcr_flag=row["WIND_INDCR_FLAG"],
                    icao_id=row["ICAO_ID"],
                    min_op_network=row["MIN_OP_NETWORK"],
                    user_fee_flag=row["USER_FEE_FLAG"],
                    cta=row["CTA"],
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
