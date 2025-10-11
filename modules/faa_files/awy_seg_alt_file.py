from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class AWY_SEG_ALT(FAA_Record_Base):
    eff_date: str
    regulatory: str
    awy_location: str
    awy_id: str
    point_seq: str
    from_point: str
    from_pt_type: str
    nav_name: str
    nav_city: str
    artcc: str
    icao_region_code: str
    state_code: str
    country_code: str
    to_point: str
    mag_course: str
    opp_mag_course: str
    mag_course_dist: str
    chgovr_pt: str
    chgovr_pt_name: str
    chgovr_pt_dist: str
    awy_seg_gap_flag: str
    signal_gap_flag: str
    dogleg: str
    next_mea_pt: str
    min_enroute_alt: str
    min_enroute_alt_dir: str
    min_enroute_alt_opposite: str
    min_enroute_alt_opposite_dir: str
    gps_min_enroute_alt: str
    gps_min_enroute_alt_dir: str
    gps_min_enroute_alt_opposite: str
    gps_mea_opposite_dir: str
    dd_iru_mea: str
    dd_iru_mea_dir: str
    dd_i_mea_opposite: str
    dd_i_mea_opposite_dir: str
    min_obstn_clnc_alt: str
    min_cross_alt: str
    min_cross_alt_dir: str
    min_cross_alt_nav_pt: str
    min_cross_alt_opposite: str
    min_cross_alt_opposite_dir: str
    min_recep_alt: str
    max_auth_alt: str
    mea_gap: str
    reqd_nav_performance: str
    remark: str
    file: str
    action: Action
    mods: str

    def __init__(
        self,
        eff_date: str,
        regulatory: str,
        awy_location: str,
        awy_id: str,
        point_seq: str,
        from_point: str,
        from_pt_type: str,
        nav_name: str,
        nav_city: str,
        artcc: str,
        icao_region_code: str,
        state_code: str,
        country_code: str,
        to_point: str,
        mag_course: str,
        opp_mag_course: str,
        mag_course_dist: str,
        chgovr_pt: str,
        chgovr_pt_name: str,
        chgovr_pt_dist: str,
        awy_seg_gap_flag: str,
        signal_gap_flag: str,
        dogleg: str,
        next_mea_pt: str,
        min_enroute_alt: str,
        min_enroute_alt_dir: str,
        min_enroute_alt_opposite: str,
        min_enroute_alt_opposite_dir: str,
        gps_min_enroute_alt: str,
        gps_min_enroute_alt_dir: str,
        gps_min_enroute_alt_opposite: str,
        gps_mea_opposite_dir: str,
        dd_iru_mea: str,
        dd_iru_mea_dir: str,
        dd_i_mea_opposite: str,
        dd_i_mea_opposite_dir: str,
        min_obstn_clnc_alt: str,
        min_cross_alt: str,
        min_cross_alt_dir: str,
        min_cross_alt_nav_pt: str,
        min_cross_alt_opposite: str,
        min_cross_alt_opposite_dir: str,
        min_recep_alt: str,
        max_auth_alt: str,
        mea_gap: str,
        reqd_nav_performance: str,
        remark: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        self.eff_date = replace_empty_string(eff_date)
        self.regulatory = replace_empty_string(regulatory)
        self.awy_location = replace_empty_string(awy_location)
        self.awy_id = replace_empty_string(awy_id)
        self.point_seq = replace_empty_string(point_seq)
        self.from_point = replace_empty_string(from_point)
        self.from_pt_type = replace_empty_string(from_pt_type)
        self.nav_name = replace_empty_string(nav_name)
        self.nav_city = replace_empty_string(nav_city)
        self.artcc = replace_empty_string(artcc)
        self.icao_region_code = replace_empty_string(icao_region_code)
        self.state_code = replace_empty_string(state_code)
        self.country_code = replace_empty_string(country_code)
        self.to_point = replace_empty_string(to_point)
        self.mag_course = replace_empty_string(mag_course)
        self.opp_mag_course = replace_empty_string(opp_mag_course)
        self.mag_course_dist = replace_empty_string(mag_course_dist)
        self.chgovr_pt = replace_empty_string(chgovr_pt)
        self.chgovr_pt_name = replace_empty_string(chgovr_pt_name)
        self.chgovr_pt_dist = replace_empty_string(chgovr_pt_dist)
        self.awy_seg_gap_flag = replace_empty_string(awy_seg_gap_flag)
        self.signal_gap_flag = replace_empty_string(signal_gap_flag)
        self.dogleg = replace_empty_string(dogleg)
        self.next_mea_pt = replace_empty_string(next_mea_pt)
        self.min_enroute_alt = replace_empty_string(min_enroute_alt)
        self.min_enroute_alt_dir = replace_empty_string(min_enroute_alt_dir)
        self.min_enroute_alt_opposite = replace_empty_string(min_enroute_alt_opposite)
        self.min_enroute_alt_opposite_dir = replace_empty_string(
            min_enroute_alt_opposite_dir
        )
        self.gps_min_enroute_alt = replace_empty_string(gps_min_enroute_alt)
        self.gps_min_enroute_alt_dir = replace_empty_string(gps_min_enroute_alt_dir)
        self.gps_min_enroute_alt_opposite = replace_empty_string(
            gps_min_enroute_alt_opposite
        )
        self.gps_mea_opposite_dir = replace_empty_string(gps_mea_opposite_dir)
        self.dd_iru_mea = replace_empty_string(dd_iru_mea)
        self.dd_iru_mea_dir = replace_empty_string(dd_iru_mea_dir)
        self.dd_i_mea_opposite = replace_empty_string(dd_i_mea_opposite)
        self.dd_i_mea_opposite_dir = replace_empty_string(dd_i_mea_opposite_dir)
        self.min_obstn_clnc_alt = replace_empty_string(min_obstn_clnc_alt)
        self.min_cross_alt = replace_empty_string(min_cross_alt)
        self.min_cross_alt_dir = replace_empty_string(min_cross_alt_dir)
        self.min_cross_alt_nav_pt = replace_empty_string(min_cross_alt_nav_pt)
        self.min_cross_alt_opposite = replace_empty_string(min_cross_alt_opposite)
        self.min_cross_alt_opposite_dir = replace_empty_string(
            min_cross_alt_opposite_dir
        )
        self.min_recep_alt = replace_empty_string(min_recep_alt)
        self.max_auth_alt = replace_empty_string(max_auth_alt)
        self.mea_gap = replace_empty_string(mea_gap)
        self.reqd_nav_performance = replace_empty_string(reqd_nav_performance)
        self.remark = replace_empty_string(remark)
        self.file = file
        self.action = action
        self.mods = mods

    def to_string(self, last_record: Self | None = None) -> str:
        if last_record:
            modification_string = self.get_mod_string(last_record)
            return f"{self.awy_id} :: {self.point_seq} :: {modification_string}"
        return (
            f"{self.awy_id} :: {self.point_seq} :: "
            f"EFF_DATE: {self.eff_date}, "
            f"REGULATORY: {self.regulatory}, "
            f"AWY_LOCATION: {self.awy_location}, "
            f"FROM_POINT: {self.from_point}, "
            f"FROM_PT_TYPE: {self.from_pt_type}, "
            f"NAV_NAME: {self.nav_name}, "
            f"NAV_CITY: {self.nav_city}, "
            f"ARTCC: {self.artcc}, "
            f"ICAO_REGION_CODE: {self.icao_region_code}, "
            f"STATE_CODE: {self.state_code}, "
            f"COUNTRY_CODE: {self.country_code}, "
            f"TO_POINT: {self.to_point}, "
            f"MAG_COURSE: {self.mag_course}, "
            f"OPP_MAG_COURSE: {self.opp_mag_course}, "
            f"MAG_COURSE_DIST: {self.mag_course_dist}, "
            f"CHGOVR_PT: {self.chgovr_pt}, "
            f"CHGOVR_PT_NAME: {self.chgovr_pt_name}, "
            f"CHGOVR_PT_DIST: {self.chgovr_pt_dist}, "
            f"AWY_SEG_GAP_FLAG: {self.awy_seg_gap_flag}, "
            f"SIGNAL_GAP_FLAG: {self.signal_gap_flag}, "
            f"DOGLEG: {self.dogleg}, "
            f"NEXT_MEA_PT: {self.next_mea_pt}, "
            f"MIN_ENROUTE_ALT: {self.min_enroute_alt}, "
            f"MIN_ENROUTE_ALT_DIR: {self.min_enroute_alt_dir}, "
            f"MIN_ENROUTE_ALT_OPPOSITE: {self.min_enroute_alt_opposite}, "
            f"MIN_ENROUTE_ALT_OPPOSITE_DIR: {self.min_enroute_alt_opposite_dir}, "
            f"GPS_MIN_ENROUTE_ALT: {self.gps_min_enroute_alt}, "
            f"GPS_MIN_ENROUTE_ALT_DIR: {self.gps_min_enroute_alt_dir}, "
            f"GPS_MIN_ENROUTE_ALT_OPPOSITE: {self.gps_min_enroute_alt_opposite}, "
            f"GPS_MEA_OPPOSITE_DIR: {self.gps_mea_opposite_dir}, "
            f"DD_IRU_MEA: {self.dd_iru_mea}, "
            f"DD_IRU_MEA_DIR: {self.dd_iru_mea_dir}, "
            f"DD_I_MEA_OPPOSITE: {self.dd_i_mea_opposite}, "
            f"DD_I_MEA_OPPOSITE_DIR: {self.dd_i_mea_opposite_dir}, "
            f"MIN_OBSTN_CLNC_ALT: {self.min_obstn_clnc_alt}, "
            f"MIN_CROSS_ALT: {self.min_cross_alt}, "
            f"MIN_CROSS_ALT_DIR: {self.min_cross_alt_dir}, "
            f"MIN_CROSS_ALT_NAV_PT: {self.min_cross_alt_nav_pt}, "
            f"MIN_CROSS_ALT_OPPOSITE: {self.min_cross_alt_opposite}, "
            f"MIN_CROSS_ALT_OPPOSITE_DIR: {self.min_cross_alt_opposite_dir}, "
            f"MIN_RECEP_ALT: {self.min_recep_alt}, "
            f"MAX_AUTH_ALT: {self.max_auth_alt}, "
            f"MEA_GAP: {self.mea_gap}, "
            f"REQD_NAV_PERFORMANCE: {self.reqd_nav_performance}, "
            f"REMARK: {self.remark}"
        )


@register_faa_file("AWY_SEG_ALT")
class AWY_SEG_ALT_File(FAA_File_Base):
    def __init__(
        self, file_path: str, filter_object: FilterObject | None = None
    ) -> None:
        super().__init__(file_path, "Airway Segment Altitude", filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = AWY_SEG_ALT(
                    eff_date=row["EFF_DATE"],
                    regulatory=row["REGULATORY"],
                    awy_location=row["AWY_LOCATION"],
                    awy_id=row["AWY_ID"],
                    point_seq=row["POINT_SEQ"],
                    from_point=row["FROM_POINT"],
                    from_pt_type=row["FROM_PT_TYPE"],
                    nav_name=row["NAV_NAME"],
                    nav_city=row["NAV_CITY"],
                    artcc=row["ARTCC"],
                    icao_region_code=row["ICAO_REGION_CODE"],
                    state_code=row["STATE_CODE"],
                    country_code=row["COUNTRY_CODE"],
                    to_point=row["TO_POINT"],
                    mag_course=row["MAG_COURSE"],
                    opp_mag_course=row["OPP_MAG_COURSE"],
                    mag_course_dist=row["MAG_COURSE_DIST"],
                    chgovr_pt=row["CHGOVR_PT"],
                    chgovr_pt_name=row["CHGOVR_PT_NAME"],
                    chgovr_pt_dist=row["CHGOVR_PT_DIST"],
                    awy_seg_gap_flag=row["AWY_SEG_GAP_FLAG"],
                    signal_gap_flag=row["SIGNAL_GAP_FLAG"],
                    dogleg=row["DOGLEG"],
                    next_mea_pt=row["NEXT_MEA_PT"],
                    min_enroute_alt=row["MIN_ENROUTE_ALT"],
                    min_enroute_alt_dir=row["MIN_ENROUTE_ALT_DIR"],
                    min_enroute_alt_opposite=row["MIN_ENROUTE_ALT_OPPOSITE"],
                    min_enroute_alt_opposite_dir=row["MIN_ENROUTE_ALT_OPPOSITE_DIR"],
                    gps_min_enroute_alt=row["GPS_MIN_ENROUTE_ALT"],
                    gps_min_enroute_alt_dir=row["GPS_MIN_ENROUTE_ALT_DIR"],
                    gps_min_enroute_alt_opposite=row["GPS_MIN_ENROUTE_ALT_OPPOSITE"],
                    gps_mea_opposite_dir=row["GPS_MEA_OPPOSITE_DIR"],
                    dd_iru_mea=row["DD_IRU_MEA"],
                    dd_iru_mea_dir=row["DD_IRU_MEA_DIR"],
                    dd_i_mea_opposite=row["DD_I_MEA_OPPOSITE"],
                    dd_i_mea_opposite_dir=row["DD_I_MEA_OPPOSITE_DIR"],
                    min_obstn_clnc_alt=row["MIN_OBSTN_CLNC_ALT"],
                    min_cross_alt=row["MIN_CROSS_ALT"],
                    min_cross_alt_dir=row["MIN_CROSS_ALT_DIR"],
                    min_cross_alt_nav_pt=row["MIN_CROSS_ALT_NAV_PT"],
                    min_cross_alt_opposite=row["MIN_CROSS_ALT_OPPOSITE"],
                    min_cross_alt_opposite_dir=row["MIN_CROSS_ALT_OPPOSITE_DIR"],
                    min_recep_alt=row["MIN_RECEP_ALT"],
                    max_auth_alt=row["MAX_AUTH_ALT"],
                    mea_gap=row["MEA_GAP"],
                    reqd_nav_performance=row["REQD_NAV_PERFORMANCE"],
                    remark=row["REMARK"],
                    file=row["File"],
                    action=row["Action"],
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_airways(
                        record.awy_id.strip()
                    )

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
