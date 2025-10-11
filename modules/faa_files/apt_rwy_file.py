from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class APT_RWY(FAA_Record_Base):
    eff_date: str
    site_no: str
    site_type_code: str
    state_code: str
    arpt_id: str
    city: str
    country_code: str
    rwy_id: str
    rwy_len: str
    rwy_width: str
    surface_type_code: str
    cond: str
    treatment_code: str
    pcn: str
    pavement_type_code: str
    subgrade_strength_code: str
    tire_pres_code: str
    dtrm_method_code: str
    rwy_lgt_code: str
    rwy_len_source: str
    length_source_date: str
    gross_wt_sw: str
    gross_wt_dw: str
    gross_wt_dtw: str
    gross_wt_ddtw: str
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
        rwy_id: str,
        rwy_len: str,
        rwy_width: str,
        surface_type_code: str,
        cond: str,
        treatment_code: str,
        pcn: str,
        pavement_type_code: str,
        subgrade_strength_code: str,
        tire_pres_code: str,
        dtrm_method_code: str,
        rwy_lgt_code: str,
        rwy_len_source: str,
        length_source_date: str,
        gross_wt_sw: str,
        gross_wt_dw: str,
        gross_wt_dtw: str,
        gross_wt_ddtw: str,
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
        self.rwy_id = replace_empty_string(rwy_id)
        self.rwy_len = replace_empty_string(rwy_len)
        self.rwy_width = replace_empty_string(rwy_width)
        self.surface_type_code = replace_empty_string(surface_type_code)
        self.cond = replace_empty_string(cond)
        self.treatment_code = replace_empty_string(treatment_code)
        self.pcn = replace_empty_string(pcn)
        self.pavement_type_code = replace_empty_string(pavement_type_code)
        self.subgrade_strength_code = replace_empty_string(subgrade_strength_code)
        self.tire_pres_code = replace_empty_string(tire_pres_code)
        self.dtrm_method_code = replace_empty_string(dtrm_method_code)
        self.rwy_lgt_code = replace_empty_string(rwy_lgt_code)
        self.rwy_len_source = replace_empty_string(rwy_len_source)
        self.length_source_date = replace_empty_string(length_source_date)
        self.gross_wt_sw = replace_empty_string(gross_wt_sw)
        self.gross_wt_dw = replace_empty_string(gross_wt_dw)
        self.gross_wt_dtw = replace_empty_string(gross_wt_dtw)
        self.gross_wt_ddtw = replace_empty_string(gross_wt_ddtw)
        self.file = file
        self.action = action
        self.mods = mods

    def to_string(self, last_record: Self | None = None) -> str:
        if last_record:
            modification_string = self.get_mod_string(last_record)
            return f"{self.arpt_id} :: {modification_string}"
        return (
            f"{self.arpt_id} :: "
            f"EFF_DATE: {self.eff_date}, "
            f"SITE_NO: {self.site_no}, "
            f"SITE_TYPE_CODE: {self.site_type_code}, "
            f"STATE_CODE: {self.state_code}, "
            f"CITY: {self.city}, "
            f"COUNTRY_CODE: {self.country_code}, "
            f"RWY_ID: {self.rwy_id}, "
            f"RWY_LEN: {self.rwy_len}, "
            f"RWY_WIDTH: {self.rwy_width}, "
            f"SURFACE_TYPE_CODE: {self.surface_type_code}, "
            f"COND: {self.cond}, "
            f"TREATMENT_CODE: {self.treatment_code}, "
            f"PCN: {self.pcn}, "
            f"PAVEMENT_TYPE_CODE: {self.pavement_type_code}, "
            f"SUBGRADE_STRENGTH_CODE: {self.subgrade_strength_code}, "
            f"TIRE_PRES_CODE: {self.tire_pres_code}, "
            f"DTRM_METHOD_CODE: {self.dtrm_method_code}, "
            f"RWY_LGT_CODE: {self.rwy_lgt_code}, "
            f"RWY_LEN_SOURCE: {self.rwy_len_source}, "
            f"LENGTH_SOURCE_DATE: {self.length_source_date}, "
            f"GROSS_WT_SW: {self.gross_wt_sw}, "
            f"GROSS_WT_DW: {self.gross_wt_dw}, "
            f"GROSS_WT_DTW: {self.gross_wt_dtw}, "
            f"GROSS_WT_DDTW: {self.gross_wt_ddtw}"
        )


@register_faa_file("APT_RWY")
class APT_RWY_File(FAA_File_Base):
    def __init__(
        self, file_path: str, filter_object: FilterObject | None = None
    ) -> None:
        super().__init__(file_path, "Airport Runway", filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = APT_RWY(
                    eff_date=row["EFF_DATE"],
                    site_no=row["SITE_NO"],
                    site_type_code=row["SITE_TYPE_CODE"],
                    state_code=row["STATE_CODE"],
                    arpt_id=row["ARPT_ID"],
                    city=row["CITY"],
                    country_code=row["COUNTRY_CODE"],
                    rwy_id=row["RWY_ID"],
                    rwy_len=row["RWY_LEN"],
                    rwy_width=row["RWY_WIDTH"],
                    surface_type_code=row["SURFACE_TYPE_CODE"],
                    cond=row["COND"],
                    treatment_code=row["TREATMENT_CODE"],
                    pcn=row["PCN"],
                    pavement_type_code=row["PAVEMENT_TYPE_CODE"],
                    subgrade_strength_code=row["SUBGRADE_STRENGTH_CODE"],
                    tire_pres_code=row["TIRE_PRES_CODE"],
                    dtrm_method_code=row["DTRM_METHOD_CODE"],
                    rwy_lgt_code=row["RWY_LGT_CODE"],
                    rwy_len_source=row["RWY_LEN_SOURCE"],
                    length_source_date=row["LENGTH_SOURCE_DATE"],
                    gross_wt_sw=row["GROSS_WT_SW"],
                    gross_wt_dw=row["GROSS_WT_DW"],
                    gross_wt_dtw=row["GROSS_WT_DTW"],
                    gross_wt_ddtw=row["GROSS_WT_DDTW"],
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
