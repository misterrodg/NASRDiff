from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class APT_RWY_END(FAA_Record_Base):
    eff_date: str
    site_no: str
    site_type_code: str
    state_code: str
    arpt_id: str
    city: str
    country_code: str
    rwy_id: str
    rwy_end_id: str
    true_alignment: str
    ils_type: str
    right_hand_traffic_pat_flag: str
    rwy_marking_type_code: str
    rwy_marking_cond: str
    rwy_end_lat_deg: str
    rwy_end_lat_min: str
    rwy_end_lat_sec: str
    rwy_end_lat_hemis: str
    lat_decimal: str
    rwy_end_long_deg: str
    rwy_end_long_min: str
    rwy_end_long_sec: str
    rwy_end_long_hemis: str
    long_decimal: str
    rwy_end_elev: str
    thr_crossing_hgt: str
    visual_glide_path_angle: str
    displaced_thr_lat_deg: str
    displaced_thr_lat_min: str
    displaced_thr_lat_sec: str
    displaced_thr_lat_hemis: str
    lat_displaced_thr_decimal: str
    displaced_thr_long_deg: str
    displaced_thr_long_min: str
    displaced_thr_long_sec: str
    displaced_thr_long_hemis: str
    long_displaced_thr_decimal: str
    displaced_thr_elev: str
    displaced_thr_len: str
    tdz_elev: str
    vgsi_code: str
    rwy_visual_range_equip_code: str
    rwy_vsby_value_equip_flag: str
    apch_lgt_system_code: str
    rwy_end_lgts_flag: str
    cntrln_lgts_avbl_flag: str
    tdz_lgt_avbl_flag: str
    obstn_type: str
    obstn_mrkd_code: str
    far_part_77_code: str
    obstn_clnc_slope: str
    obstn_hgt: str
    dist_from_thr: str
    cntrln_offset: str
    cntrln_dir_code: str
    rwy_grad: str
    rwy_grad_direction: str
    rwy_end_psn_source: str
    rwy_end_psn_date: str
    rwy_end_elev_source: str
    rwy_end_elev_date: str
    dspl_thr_psn_source: str
    rwy_end_dspl_thr_psn_date: str
    dspl_thr_elev_source: str
    rwy_end_dspl_thr_elev_date: str
    tdz_elev_source: str
    rwy_end_tdz_elev_date: str
    tkof_run_avbl: str
    tkof_dist_avbl: str
    aclt_stop_dist_avbl: str
    lndg_dist_avbl: str
    lahso_ald: str
    rwy_end_intersect_lahso: str
    lahso_desc: str
    lahso_lat: str
    lat_lahso_decimal: str
    lahso_long: str
    long_lahso_decimal: str
    lahso_psn_source: str
    rwy_end_lahso_psn_date: str

    def __init__(
        self,
        eff_date: str,
        site_no: str,
        site_type_code: str,
        state_code: str,
        arpt_id: str,
        city: str,
        country_code: str,
        rwy_id: str,
        rwy_end_id: str,
        true_alignment: str,
        ils_type: str,
        right_hand_traffic_pat_flag: str,
        rwy_marking_type_code: str,
        rwy_marking_cond: str,
        rwy_end_lat_deg: str,
        rwy_end_lat_min: str,
        rwy_end_lat_sec: str,
        rwy_end_lat_hemis: str,
        lat_decimal: str,
        rwy_end_long_deg: str,
        rwy_end_long_min: str,
        rwy_end_long_sec: str,
        rwy_end_long_hemis: str,
        long_decimal: str,
        rwy_end_elev: str,
        thr_crossing_hgt: str,
        visual_glide_path_angle: str,
        displaced_thr_lat_deg: str,
        displaced_thr_lat_min: str,
        displaced_thr_lat_sec: str,
        displaced_thr_lat_hemis: str,
        lat_displaced_thr_decimal: str,
        displaced_thr_long_deg: str,
        displaced_thr_long_min: str,
        displaced_thr_long_sec: str,
        displaced_thr_long_hemis: str,
        long_displaced_thr_decimal: str,
        displaced_thr_elev: str,
        displaced_thr_len: str,
        tdz_elev: str,
        vgsi_code: str,
        rwy_visual_range_equip_code: str,
        rwy_vsby_value_equip_flag: str,
        apch_lgt_system_code: str,
        rwy_end_lgts_flag: str,
        cntrln_lgts_avbl_flag: str,
        tdz_lgt_avbl_flag: str,
        obstn_type: str,
        obstn_mrkd_code: str,
        far_part_77_code: str,
        obstn_clnc_slope: str,
        obstn_hgt: str,
        dist_from_thr: str,
        cntrln_offset: str,
        cntrln_dir_code: str,
        rwy_grad: str,
        rwy_grad_direction: str,
        rwy_end_psn_source: str,
        rwy_end_psn_date: str,
        rwy_end_elev_source: str,
        rwy_end_elev_date: str,
        dspl_thr_psn_source: str,
        rwy_end_dspl_thr_psn_date: str,
        dspl_thr_elev_source: str,
        rwy_end_dspl_thr_elev_date: str,
        tdz_elev_source: str,
        rwy_end_tdz_elev_date: str,
        tkof_run_avbl: str,
        tkof_dist_avbl: str,
        aclt_stop_dist_avbl: str,
        lndg_dist_avbl: str,
        lahso_ald: str,
        rwy_end_intersect_lahso: str,
        lahso_desc: str,
        lahso_lat: str,
        lat_lahso_decimal: str,
        lahso_long: str,
        long_lahso_decimal: str,
        lahso_psn_source: str,
        rwy_end_lahso_psn_date: str,
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
        self.rwy_id = replace_empty_string(rwy_id)
        self.rwy_end_id = replace_empty_string(rwy_end_id)
        self.true_alignment = replace_empty_string(true_alignment)
        self.ils_type = replace_empty_string(ils_type)
        self.right_hand_traffic_pat_flag = replace_empty_string(
            right_hand_traffic_pat_flag
        )
        self.rwy_marking_type_code = replace_empty_string(rwy_marking_type_code)
        self.rwy_marking_cond = replace_empty_string(rwy_marking_cond)
        self.rwy_end_lat_deg = replace_empty_string(rwy_end_lat_deg)
        self.rwy_end_lat_min = replace_empty_string(rwy_end_lat_min)
        self.rwy_end_lat_sec = replace_empty_string(rwy_end_lat_sec)
        self.rwy_end_lat_hemis = replace_empty_string(rwy_end_lat_hemis)
        self.lat_decimal = replace_empty_string(lat_decimal)
        self.rwy_end_long_deg = replace_empty_string(rwy_end_long_deg)
        self.rwy_end_long_min = replace_empty_string(rwy_end_long_min)
        self.rwy_end_long_sec = replace_empty_string(rwy_end_long_sec)
        self.rwy_end_long_hemis = replace_empty_string(rwy_end_long_hemis)
        self.long_decimal = replace_empty_string(long_decimal)
        self.rwy_end_elev = replace_empty_string(rwy_end_elev)
        self.thr_crossing_hgt = replace_empty_string(thr_crossing_hgt)
        self.visual_glide_path_angle = replace_empty_string(visual_glide_path_angle)
        self.displaced_thr_lat_deg = replace_empty_string(displaced_thr_lat_deg)
        self.displaced_thr_lat_min = replace_empty_string(displaced_thr_lat_min)
        self.displaced_thr_lat_sec = replace_empty_string(displaced_thr_lat_sec)
        self.displaced_thr_lat_hemis = replace_empty_string(displaced_thr_lat_hemis)
        self.lat_displaced_thr_decimal = replace_empty_string(lat_displaced_thr_decimal)
        self.displaced_thr_long_deg = replace_empty_string(displaced_thr_long_deg)
        self.displaced_thr_long_min = replace_empty_string(displaced_thr_long_min)
        self.displaced_thr_long_sec = replace_empty_string(displaced_thr_long_sec)
        self.displaced_thr_long_hemis = replace_empty_string(displaced_thr_long_hemis)
        self.long_displaced_thr_decimal = replace_empty_string(
            long_displaced_thr_decimal
        )
        self.displaced_thr_elev = replace_empty_string(displaced_thr_elev)
        self.displaced_thr_len = replace_empty_string(displaced_thr_len)
        self.tdz_elev = replace_empty_string(tdz_elev)
        self.vgsi_code = replace_empty_string(vgsi_code)
        self.rwy_visual_range_equip_code = replace_empty_string(
            rwy_visual_range_equip_code
        )
        self.rwy_vsby_value_equip_flag = replace_empty_string(rwy_vsby_value_equip_flag)
        self.apch_lgt_system_code = replace_empty_string(apch_lgt_system_code)
        self.rwy_end_lgts_flag = replace_empty_string(rwy_end_lgts_flag)
        self.cntrln_lgts_avbl_flag = replace_empty_string(cntrln_lgts_avbl_flag)
        self.tdz_lgt_avbl_flag = replace_empty_string(tdz_lgt_avbl_flag)
        self.obstn_type = replace_empty_string(obstn_type)
        self.obstn_mrkd_code = replace_empty_string(obstn_mrkd_code)
        self.far_part_77_code = replace_empty_string(far_part_77_code)
        self.obstn_clnc_slope = replace_empty_string(obstn_clnc_slope)
        self.obstn_hgt = replace_empty_string(obstn_hgt)
        self.dist_from_thr = replace_empty_string(dist_from_thr)
        self.cntrln_offset = replace_empty_string(cntrln_offset)
        self.cntrln_dir_code = replace_empty_string(cntrln_dir_code)
        self.rwy_grad = replace_empty_string(rwy_grad)
        self.rwy_grad_direction = replace_empty_string(rwy_grad_direction)
        self.rwy_end_psn_source = replace_empty_string(rwy_end_psn_source)
        self.rwy_end_psn_date = replace_empty_string(rwy_end_psn_date)
        self.rwy_end_elev_source = replace_empty_string(rwy_end_elev_source)
        self.rwy_end_elev_date = replace_empty_string(rwy_end_elev_date)
        self.dspl_thr_psn_source = replace_empty_string(dspl_thr_psn_source)
        self.rwy_end_dspl_thr_psn_date = replace_empty_string(rwy_end_dspl_thr_psn_date)
        self.dspl_thr_elev_source = replace_empty_string(dspl_thr_elev_source)
        self.rwy_end_dspl_thr_elev_date = replace_empty_string(
            rwy_end_dspl_thr_elev_date
        )
        self.tdz_elev_source = replace_empty_string(tdz_elev_source)
        self.rwy_end_tdz_elev_date = replace_empty_string(rwy_end_tdz_elev_date)
        self.tkof_run_avbl = replace_empty_string(tkof_run_avbl)
        self.tkof_dist_avbl = replace_empty_string(tkof_dist_avbl)
        self.aclt_stop_dist_avbl = replace_empty_string(aclt_stop_dist_avbl)
        self.lndg_dist_avbl = replace_empty_string(lndg_dist_avbl)
        self.lahso_ald = replace_empty_string(lahso_ald)
        self.rwy_end_intersect_lahso = replace_empty_string(rwy_end_intersect_lahso)
        self.lahso_desc = replace_empty_string(lahso_desc)
        self.lahso_lat = replace_empty_string(lahso_lat)
        self.lat_lahso_decimal = replace_empty_string(lat_lahso_decimal)
        self.lahso_long = replace_empty_string(lahso_long)
        self.long_lahso_decimal = replace_empty_string(long_lahso_decimal)
        self.lahso_psn_source = replace_empty_string(lahso_psn_source)
        self.rwy_end_lahso_psn_date = replace_empty_string(rwy_end_lahso_psn_date)

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
            f"RWY_ID={self.rwy_id!r}, "
            f"RWY_END_ID={self.rwy_end_id!r}, "
            f"TRUE_ALIGNMENT={self.true_alignment!r}, "
            f"ILS_TYPE={self.ils_type!r}, "
            f"RIGHT_HAND_TRAFFIC_PAT_FLAG={self.right_hand_traffic_pat_flag!r}, "
            f"RWY_MARKING_TYPE_CODE={self.rwy_marking_type_code!r}, "
            f"RWY_MARKING_COND={self.rwy_marking_cond!r}, "
            f"RWY_END_LAT_DEG={self.rwy_end_lat_deg!r}, "
            f"RWY_END_LAT_MIN={self.rwy_end_lat_min!r}, "
            f"RWY_END_LAT_SEC={self.rwy_end_lat_sec!r}, "
            f"RWY_END_LAT_HEMIS={self.rwy_end_lat_hemis!r}, "
            f"LAT_DECIMAL={self.lat_decimal!r}, "
            f"RWY_END_LONG_DEG={self.rwy_end_long_deg!r}, "
            f"RWY_END_LONG_MIN={self.rwy_end_long_min!r}, "
            f"RWY_END_LONG_SEC={self.rwy_end_long_sec!r}, "
            f"RWY_END_LONG_HEMIS={self.rwy_end_long_hemis!r}, "
            f"LONG_DECIMAL={self.long_decimal!r}, "
            f"RWY_END_ELEV={self.rwy_end_elev!r}, "
            f"THR_CROSSING_HGT={self.thr_crossing_hgt!r}, "
            f"VISUAL_GLIDE_PATH_ANGLE={self.visual_glide_path_angle!r}, "
            f"DISPLACED_THR_LAT_DEG={self.displaced_thr_lat_deg!r}, "
            f"DISPLACED_THR_LAT_MIN={self.displaced_thr_lat_min!r}, "
            f"DISPLACED_THR_LAT_SEC={self.displaced_thr_lat_sec!r}, "
            f"DISPLACED_THR_LAT_HEMIS={self.displaced_thr_lat_hemis!r}, "
            f"LAT_DISPLACED_THR_DECIMAL={self.lat_displaced_thr_decimal!r}, "
            f"DISPLACED_THR_LONG_DEG={self.displaced_thr_long_deg!r}, "
            f"DISPLACED_THR_LONG_MIN={self.displaced_thr_long_min!r}, "
            f"DISPLACED_THR_LONG_SEC={self.displaced_thr_long_sec!r}, "
            f"DISPLACED_THR_LONG_HEMIS={self.displaced_thr_long_hemis!r}, "
            f"LONG_DISPLACED_THR_DECIMAL={self.long_displaced_thr_decimal!r}, "
            f"DISPLACED_THR_ELEV={self.displaced_thr_elev!r}, "
            f"DISPLACED_THR_LEN={self.displaced_thr_len!r}, "
            f"TDZ_ELEV={self.tdz_elev!r}, "
            f"VGSI_CODE={self.vgsi_code!r}, "
            f"RWY_VISUAL_RANGE_EQUIP_CODE={self.rwy_visual_range_equip_code!r}, "
            f"RWY_VSBY_VALUE_EQUIP_FLAG={self.rwy_vsby_value_equip_flag!r}, "
            f"APCH_LGT_SYSTEM_CODE={self.apch_lgt_system_code!r}, "
            f"RWY_END_LGTS_FLAG={self.rwy_end_lgts_flag!r}, "
            f"CNTRLN_LGTS_AVBL_FLAG={self.cntrln_lgts_avbl_flag!r}, "
            f"TDZ_LGT_AVBL_FLAG={self.tdz_lgt_avbl_flag!r}, "
            f"OBSTN_TYPE={self.obstn_type!r}, "
            f"OBSTN_MRKD_CODE={self.obstn_mrkd_code!r}, "
            f"FAR_PART_77_CODE={self.far_part_77_code!r}, "
            f"OBSTN_CLNC_SLOPE={self.obstn_clnc_slope!r}, "
            f"OBSTN_HGT={self.obstn_hgt!r}, "
            f"DIST_FROM_THR={self.dist_from_thr!r}, "
            f"CNTRLN_OFFSET={self.cntrln_offset!r}, "
            f"CNTRLN_DIR_CODE={self.cntrln_dir_code!r}, "
            f"RWY_GRAD={self.rwy_grad!r}, "
            f"RWY_GRAD_DIRECTION={self.rwy_grad_direction!r}, "
            f"RWY_END_PSN_SOURCE={self.rwy_end_psn_source!r}, "
            f"RWY_END_PSN_DATE={self.rwy_end_psn_date!r}, "
            f"RWY_END_ELEV_SOURCE={self.rwy_end_elev_source!r}, "
            f"RWY_END_ELEV_DATE={self.rwy_end_elev_date!r}, "
            f"DSPL_THR_PSN_SOURCE={self.dspl_thr_psn_source!r}, "
            f"RWY_END_DSPL_THR_PSN_DATE={self.rwy_end_dspl_thr_psn_date!r}, "
            f"DSPL_THR_ELEV_SOURCE={self.dspl_thr_elev_source!r}, "
            f"RWY_END_DSPL_THR_ELEV_DATE={self.rwy_end_dspl_thr_elev_date!r}, "
            f"TDZ_ELEV_SOURCE={self.tdz_elev_source!r}, "
            f"RWY_END_TDZ_ELEV_DATE={self.rwy_end_tdz_elev_date!r}, "
            f"TKOF_RUN_AVBL={self.tkof_run_avbl!r}, "
            f"TKOF_DIST_AVBL={self.tkof_dist_avbl!r}, "
            f"ACLT_STOP_DIST_AVBL={self.aclt_stop_dist_avbl!r}, "
            f"LNDG_DIST_AVBL={self.lndg_dist_avbl!r}, "
            f"LAHSO_ALD={self.lahso_ald!r}, "
            f"RWY_END_INTERSECT_LAHSO={self.rwy_end_intersect_lahso!r}, "
            f"LAHSO_DESC={self.lahso_desc!r}, "
            f"LAHSO_LAT={self.lahso_lat!r}, "
            f"LAT_LAHSO_DECIMAL={self.lat_lahso_decimal!r}, "
            f"LAHSO_LONG={self.lahso_long!r}, "
            f"LONG_LAHSO_DECIMAL={self.long_lahso_decimal!r}, "
            f"LAHSO_PSN_SOURCE={self.lahso_psn_source!r}, "
            f"RWY_END_LAHSO_PSN_DATE={self.rwy_end_lahso_psn_date!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.arpt_id} :: {self.rwy_end_id}"

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
                f"RWY_ID: {self.rwy_id}, "
                f"TRUE_ALIGNMENT: {self.true_alignment}, "
                f"ILS_TYPE: {self.ils_type}, "
                f"RIGHT_HAND_TRAFFIC_PAT_FLAG: {self.right_hand_traffic_pat_flag}, "
                f"RWY_MARKING_TYPE_CODE: {self.rwy_marking_type_code}, "
                f"RWY_MARKING_COND: {self.rwy_marking_cond}, "
                f"RWY_END_LAT_DEG: {self.rwy_end_lat_deg}, "
                f"RWY_END_LAT_MIN: {self.rwy_end_lat_min}, "
                f"RWY_END_LAT_SEC: {self.rwy_end_lat_sec}, "
                f"RWY_END_LAT_HEMIS: {self.rwy_end_lat_hemis}, "
                f"LAT_DECIMAL: {self.lat_decimal}, "
                f"RWY_END_LONG_DEG: {self.rwy_end_long_deg}, "
                f"RWY_END_LONG_MIN: {self.rwy_end_long_min}, "
                f"RWY_END_LONG_SEC: {self.rwy_end_long_sec}, "
                f"RWY_END_LONG_HEMIS: {self.rwy_end_long_hemis}, "
                f"LONG_DECIMAL: {self.long_decimal}, "
                f"RWY_END_ELEV: {self.rwy_end_elev}, "
                f"THR_CROSSING_HGT: {self.thr_crossing_hgt}, "
                f"VISUAL_GLIDE_PATH_ANGLE: {self.visual_glide_path_angle}, "
                f"DISPLACED_THR_LAT_DEG: {self.displaced_thr_lat_deg}, "
                f"DISPLACED_THR_LAT_MIN: {self.displaced_thr_lat_min}, "
                f"DISPLACED_THR_LAT_SEC: {self.displaced_thr_lat_sec}, "
                f"DISPLACED_THR_LAT_HEMIS: {self.displaced_thr_lat_hemis}, "
                f"LAT_DISPLACED_THR_DECIMAL: {self.lat_displaced_thr_decimal}, "
                f"DISPLACED_THR_LONG_DEG: {self.displaced_thr_long_deg}, "
                f"DISPLACED_THR_LONG_MIN: {self.displaced_thr_long_min}, "
                f"DISPLACED_THR_LONG_SEC: {self.displaced_thr_long_sec}, "
                f"DISPLACED_THR_LONG_HEMIS: {self.displaced_thr_long_hemis}, "
                f"LONG_DISPLACED_THR_DECIMAL: {self.long_displaced_thr_decimal}, "
                f"DISPLACED_THR_ELEV: {self.displaced_thr_elev}, "
                f"DISPLACED_THR_LEN: {self.displaced_thr_len}, "
                f"TDZ_ELEV: {self.tdz_elev}, "
                f"VGSI_CODE: {self.vgsi_code}, "
                f"RWY_VISUAL_RANGE_EQUIP_CODE: {self.rwy_visual_range_equip_code}, "
                f"RWY_VSBY_VALUE_EQUIP_FLAG: {self.rwy_vsby_value_equip_flag}, "
                f"APCH_LGT_SYSTEM_CODE: {self.apch_lgt_system_code}, "
                f"RWY_END_LGTS_FLAG: {self.rwy_end_lgts_flag}, "
                f"CNTRLN_LGTS_AVBL_FLAG: {self.cntrln_lgts_avbl_flag}, "
                f"TDZ_LGT_AVBL_FLAG: {self.tdz_lgt_avbl_flag}, "
                f"OBSTN_TYPE: {self.obstn_type}, "
                f"OBSTN_MRKD_CODE: {self.obstn_mrkd_code}, "
                f"FAR_PART_77_CODE: {self.far_part_77_code}, "
                f"OBSTN_CLNC_SLOPE: {self.obstn_clnc_slope}, "
                f"OBSTN_HGT: {self.obstn_hgt}, "
                f"DIST_FROM_THR: {self.dist_from_thr}, "
                f"CNTRLN_OFFSET: {self.cntrln_offset}, "
                f"CNTRLN_DIR_CODE: {self.cntrln_dir_code}, "
                f"RWY_GRAD: {self.rwy_grad}, "
                f"RWY_GRAD_DIRECTION: {self.rwy_grad_direction}, "
                f"RWY_END_PSN_SOURCE: {self.rwy_end_psn_source}, "
                f"RWY_END_PSN_DATE: {self.rwy_end_psn_date}, "
                f"RWY_END_ELEV_SOURCE: {self.rwy_end_elev_source}, "
                f"RWY_END_ELEV_DATE: {self.rwy_end_elev_date}, "
                f"DSPL_THR_PSN_SOURCE: {self.dspl_thr_psn_source}, "
                f"RWY_END_DSPL_THR_PSN_DATE: {self.rwy_end_dspl_thr_psn_date}, "
                f"DSPL_THR_ELEV_SOURCE: {self.dspl_thr_elev_source}, "
                f"RWY_END_DSPL_THR_ELEV_DATE: {self.rwy_end_dspl_thr_elev_date}, "
                f"TDZ_ELEV_SOURCE: {self.tdz_elev_source}, "
                f"RWY_END_TDZ_ELEV_DATE: {self.rwy_end_tdz_elev_date}, "
                f"TKOF_RUN_AVBL: {self.tkof_run_avbl}, "
                f"TKOF_DIST_AVBL: {self.tkof_dist_avbl}, "
                f"ACLT_STOP_DIST_AVBL: {self.aclt_stop_dist_avbl}, "
                f"LNDG_DIST_AVBL: {self.lndg_dist_avbl}, "
                f"LAHSO_ALD: {self.lahso_ald}, "
                f"RWY_END_INTERSECT_LAHSO: {self.rwy_end_intersect_lahso}, "
                f"LAHSO_DESC: {self.lahso_desc}, "
                f"LAHSO_LAT: {self.lahso_lat}, "
                f"LAT_LAHSO_DECIMAL: {self.lat_lahso_decimal}, "
                f"LAHSO_LONG: {self.lahso_long}, "
                f"LONG_LAHSO_DECIMAL: {self.long_lahso_decimal}, "
                f"LAHSO_PSN_SOURCE: {self.lahso_psn_source}, "
                f"RWY_END_LAHSO_PSN_DATE: {self.rwy_end_lahso_psn_date}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("APT_RWY_END")
class APT_RWY_END_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "Airport Runway End", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = APT_RWY_END(
                    eff_date=row["EFF_DATE"],
                    site_no=row["SITE_NO"],
                    site_type_code=row["SITE_TYPE_CODE"],
                    state_code=row["STATE_CODE"],
                    arpt_id=row["ARPT_ID"],
                    city=row["CITY"],
                    country_code=row["COUNTRY_CODE"],
                    rwy_id=row["RWY_ID"],
                    rwy_end_id=row["RWY_END_ID"],
                    true_alignment=row["TRUE_ALIGNMENT"],
                    ils_type=row["ILS_TYPE"],
                    right_hand_traffic_pat_flag=row["RIGHT_HAND_TRAFFIC_PAT_FLAG"],
                    rwy_marking_type_code=row["RWY_MARKING_TYPE_CODE"],
                    rwy_marking_cond=row["RWY_MARKING_COND"],
                    rwy_end_lat_deg=row["RWY_END_LAT_DEG"],
                    rwy_end_lat_min=row["RWY_END_LAT_MIN"],
                    rwy_end_lat_sec=row["RWY_END_LAT_SEC"],
                    rwy_end_lat_hemis=row["RWY_END_LAT_HEMIS"],
                    lat_decimal=row["LAT_DECIMAL"],
                    rwy_end_long_deg=row["RWY_END_LONG_DEG"],
                    rwy_end_long_min=row["RWY_END_LONG_MIN"],
                    rwy_end_long_sec=row["RWY_END_LONG_SEC"],
                    rwy_end_long_hemis=row["RWY_END_LONG_HEMIS"],
                    long_decimal=row["LONG_DECIMAL"],
                    rwy_end_elev=row["RWY_END_ELEV"],
                    thr_crossing_hgt=row["THR_CROSSING_HGT"],
                    visual_glide_path_angle=row["VISUAL_GLIDE_PATH_ANGLE"],
                    displaced_thr_lat_deg=row["DISPLACED_THR_LAT_DEG"],
                    displaced_thr_lat_min=row["DISPLACED_THR_LAT_MIN"],
                    displaced_thr_lat_sec=row["DISPLACED_THR_LAT_SEC"],
                    displaced_thr_lat_hemis=row["DISPLACED_THR_LAT_HEMIS"],
                    lat_displaced_thr_decimal=row["LAT_DISPLACED_THR_DECIMAL"],
                    displaced_thr_long_deg=row["DISPLACED_THR_LONG_DEG"],
                    displaced_thr_long_min=row["DISPLACED_THR_LONG_MIN"],
                    displaced_thr_long_sec=row["DISPLACED_THR_LONG_SEC"],
                    displaced_thr_long_hemis=row["DISPLACED_THR_LONG_HEMIS"],
                    long_displaced_thr_decimal=row["LONG_DISPLACED_THR_DECIMAL"],
                    displaced_thr_elev=row["DISPLACED_THR_ELEV"],
                    displaced_thr_len=row["DISPLACED_THR_LEN"],
                    tdz_elev=row["TDZ_ELEV"],
                    vgsi_code=row["VGSI_CODE"],
                    rwy_visual_range_equip_code=row["RWY_VISUAL_RANGE_EQUIP_CODE"],
                    rwy_vsby_value_equip_flag=row["RWY_VSBY_VALUE_EQUIP_FLAG"],
                    apch_lgt_system_code=row["APCH_LGT_SYSTEM_CODE"],
                    rwy_end_lgts_flag=row["RWY_END_LGTS_FLAG"],
                    cntrln_lgts_avbl_flag=row["CNTRLN_LGTS_AVBL_FLAG"],
                    tdz_lgt_avbl_flag=row["TDZ_LGT_AVBL_FLAG"],
                    obstn_type=row["OBSTN_TYPE"],
                    obstn_mrkd_code=row["OBSTN_MRKD_CODE"],
                    far_part_77_code=row["FAR_PART_77_CODE"],
                    obstn_clnc_slope=row["OBSTN_CLNC_SLOPE"],
                    obstn_hgt=row["OBSTN_HGT"],
                    dist_from_thr=row["DIST_FROM_THR"],
                    cntrln_offset=row["CNTRLN_OFFSET"],
                    cntrln_dir_code=row["CNTRLN_DIR_CODE"],
                    rwy_grad=row["RWY_GRAD"],
                    rwy_grad_direction=row["RWY_GRAD_DIRECTION"],
                    rwy_end_psn_source=row["RWY_END_PSN_SOURCE"],
                    rwy_end_psn_date=row["RWY_END_PSN_DATE"],
                    rwy_end_elev_source=row["RWY_END_ELEV_SOURCE"],
                    rwy_end_elev_date=row["RWY_END_ELEV_DATE"],
                    dspl_thr_psn_source=row["DSPL_THR_PSN_SOURCE"],
                    rwy_end_dspl_thr_psn_date=row["RWY_END_DSPL_THR_PSN_DATE"],
                    dspl_thr_elev_source=row["DSPL_THR_ELEV_SOURCE"],
                    rwy_end_dspl_thr_elev_date=row["RWY_END_DSPL_THR_ELEV_DATE"],
                    tdz_elev_source=row["TDZ_ELEV_SOURCE"],
                    rwy_end_tdz_elev_date=row["RWY_END_TDZ_ELEV_DATE"],
                    tkof_run_avbl=row["TKOF_RUN_AVBL"],
                    tkof_dist_avbl=row["TKOF_DIST_AVBL"],
                    aclt_stop_dist_avbl=row["ACLT_STOP_DIST_AVBL"],
                    lndg_dist_avbl=row["LNDG_DIST_AVBL"],
                    lahso_ald=row["LAHSO_ALD"],
                    rwy_end_intersect_lahso=row["RWY_END_INTERSECT_LAHSO"],
                    lahso_desc=row["LAHSO_DESC"],
                    lahso_lat=row["LAHSO_LAT"],
                    lat_lahso_decimal=row["LAT_LAHSO_DECIMAL"],
                    lahso_long=row["LAHSO_LONG"],
                    long_lahso_decimal=row["LONG_LAHSO_DECIMAL"],
                    lahso_psn_source=row["LAHSO_PSN_SOURCE"],
                    rwy_end_lahso_psn_date=row["RWY_END_LAHSO_PSN_DATE"],
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
