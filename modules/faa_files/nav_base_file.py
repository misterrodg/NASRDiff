from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class NAV_BASE(FAA_Record_Base):
    eff_date: str
    nav_id: str
    nav_type: str
    state_code: str
    city: str
    country_code: str
    nav_status: str
    name: str
    state_name: str
    region_code: str
    country_name: str
    fan_marker: str
    owner: str
    operator: str
    nas_use_flag: str
    public_use_flag: str
    ndb_class_code: str
    oper_hours: str
    high_alt_artcc_id: str
    high_artcc_name: str
    low_alt_artcc_id: str
    low_artcc_name: str
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
    survey_accuracy_code: str
    tacan_dme_status: str
    tacan_dme_lat_deg: str
    tacan_dme_lat_min: str
    tacan_dme_lat_sec: str
    tacan_dme_lat_hemis: str
    tacan_dme_lat_decimal: str
    tacan_dme_long_deg: str
    tacan_dme_long_min: str
    tacan_dme_long_sec: str
    tacan_dme_long_hemis: str
    tacan_dme_long_decimal: str
    elev: str
    mag_varn: str
    mag_varn_hemis: str
    mag_varn_year: str
    simul_voice_flag: str
    pwr_output: str
    auto_voice_id_flag: str
    mnt_cat_code: str
    voice_call: str
    chan: str
    freq: str
    mkr_ident: str
    mkr_shape: str
    mkr_brg: str
    alt_code: str
    dme_ssv: str
    low_nav_on_high_chart_flag: str
    z_mkr_flag: str
    fss_id: str
    fss_name: str
    fss_hours: str
    notam_id: str
    quad_ident: str
    pitch_flag: str
    catch_flag: str
    sua_atcaa_flag: str
    restriction_flag: str
    hiwas_flag: str

    def __init__(
        self,
        eff_date: str,
        nav_id: str,
        nav_type: str,
        state_code: str,
        city: str,
        country_code: str,
        nav_status: str,
        name: str,
        state_name: str,
        region_code: str,
        country_name: str,
        fan_marker: str,
        owner: str,
        operator: str,
        nas_use_flag: str,
        public_use_flag: str,
        ndb_class_code: str,
        oper_hours: str,
        high_alt_artcc_id: str,
        high_artcc_name: str,
        low_alt_artcc_id: str,
        low_artcc_name: str,
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
        survey_accuracy_code: str,
        tacan_dme_status: str,
        tacan_dme_lat_deg: str,
        tacan_dme_lat_min: str,
        tacan_dme_lat_sec: str,
        tacan_dme_lat_hemis: str,
        tacan_dme_lat_decimal: str,
        tacan_dme_long_deg: str,
        tacan_dme_long_min: str,
        tacan_dme_long_sec: str,
        tacan_dme_long_hemis: str,
        tacan_dme_long_decimal: str,
        elev: str,
        mag_varn: str,
        mag_varn_hemis: str,
        mag_varn_year: str,
        simul_voice_flag: str,
        pwr_output: str,
        auto_voice_id_flag: str,
        mnt_cat_code: str,
        voice_call: str,
        chan: str,
        freq: str,
        mkr_ident: str,
        mkr_shape: str,
        mkr_brg: str,
        alt_code: str,
        dme_ssv: str,
        low_nav_on_high_chart_flag: str,
        z_mkr_flag: str,
        fss_id: str,
        fss_name: str,
        fss_hours: str,
        notam_id: str,
        quad_ident: str,
        pitch_flag: str,
        catch_flag: str,
        sua_atcaa_flag: str,
        restriction_flag: str,
        hiwas_flag: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.nav_id = replace_empty_string(nav_id)
        self.nav_type = replace_empty_string(nav_type)
        self.state_code = replace_empty_string(state_code)
        self.city = replace_empty_string(city)
        self.country_code = replace_empty_string(country_code)
        self.nav_status = replace_empty_string(nav_status)
        self.name = replace_empty_string(name)
        self.state_name = replace_empty_string(state_name)
        self.region_code = replace_empty_string(region_code)
        self.country_name = replace_empty_string(country_name)
        self.fan_marker = replace_empty_string(fan_marker)
        self.owner = replace_empty_string(owner)
        self.operator = replace_empty_string(operator)
        self.nas_use_flag = replace_empty_string(nas_use_flag)
        self.public_use_flag = replace_empty_string(public_use_flag)
        self.ndb_class_code = replace_empty_string(ndb_class_code)
        self.oper_hours = replace_empty_string(oper_hours)
        self.high_alt_artcc_id = replace_empty_string(high_alt_artcc_id)
        self.high_artcc_name = replace_empty_string(high_artcc_name)
        self.low_alt_artcc_id = replace_empty_string(low_alt_artcc_id)
        self.low_artcc_name = replace_empty_string(low_artcc_name)
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
        self.survey_accuracy_code = replace_empty_string(survey_accuracy_code)
        self.tacan_dme_status = replace_empty_string(tacan_dme_status)
        self.tacan_dme_lat_deg = replace_empty_string(tacan_dme_lat_deg)
        self.tacan_dme_lat_min = replace_empty_string(tacan_dme_lat_min)
        self.tacan_dme_lat_sec = replace_empty_string(tacan_dme_lat_sec)
        self.tacan_dme_lat_hemis = replace_empty_string(tacan_dme_lat_hemis)
        self.tacan_dme_lat_decimal = replace_empty_string(tacan_dme_lat_decimal)
        self.tacan_dme_long_deg = replace_empty_string(tacan_dme_long_deg)
        self.tacan_dme_long_min = replace_empty_string(tacan_dme_long_min)
        self.tacan_dme_long_sec = replace_empty_string(tacan_dme_long_sec)
        self.tacan_dme_long_hemis = replace_empty_string(tacan_dme_long_hemis)
        self.tacan_dme_long_decimal = replace_empty_string(tacan_dme_long_decimal)
        self.elev = replace_empty_string(elev)
        self.mag_varn = replace_empty_string(mag_varn)
        self.mag_varn_hemis = replace_empty_string(mag_varn_hemis)
        self.mag_varn_year = replace_empty_string(mag_varn_year)
        self.simul_voice_flag = replace_empty_string(simul_voice_flag)
        self.pwr_output = replace_empty_string(pwr_output)
        self.auto_voice_id_flag = replace_empty_string(auto_voice_id_flag)
        self.mnt_cat_code = replace_empty_string(mnt_cat_code)
        self.voice_call = replace_empty_string(voice_call)
        self.chan = replace_empty_string(chan)
        self.freq = replace_empty_string(freq)
        self.mkr_ident = replace_empty_string(mkr_ident)
        self.mkr_shape = replace_empty_string(mkr_shape)
        self.mkr_brg = replace_empty_string(mkr_brg)
        self.alt_code = replace_empty_string(alt_code)
        self.dme_ssv = replace_empty_string(dme_ssv)
        self.low_nav_on_high_chart_flag = replace_empty_string(
            low_nav_on_high_chart_flag
        )
        self.z_mkr_flag = replace_empty_string(z_mkr_flag)
        self.fss_id = replace_empty_string(fss_id)
        self.fss_name = replace_empty_string(fss_name)
        self.fss_hours = replace_empty_string(fss_hours)
        self.notam_id = replace_empty_string(notam_id)
        self.quad_ident = replace_empty_string(quad_ident)
        self.pitch_flag = replace_empty_string(pitch_flag)
        self.catch_flag = replace_empty_string(catch_flag)
        self.sua_atcaa_flag = replace_empty_string(sua_atcaa_flag)
        self.restriction_flag = replace_empty_string(restriction_flag)
        self.hiwas_flag = replace_empty_string(hiwas_flag)

    def __hash__(self) -> int:
        return hash((self.nav_id, self.nav_type))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, NAV_BASE):
            return False
        return self.nav_id == other.nav_id and self.nav_type == other.nav_type

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, NAV_BASE):
            return False
        return (self.nav_id, self.nav_type, self.file) < (
            other.nav_id,
            other.nav_type,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"NAV_ID={self.nav_id!r}, "
            f"NAV_TYPE={self.nav_type!r}, "
            f"STATE_CODE={self.state_code!r}, "
            f"CITY={self.city!r}, "
            f"COUNTRY_CODE={self.country_code!r}, "
            f"NAV_STATUS={self.nav_status!r}, "
            f"NAME={self.name!r}, "
            f"STATE_NAME={self.state_name!r}, "
            f"REGION_CODE={self.region_code!r}, "
            f"COUNTRY_NAME={self.country_name!r}, "
            f"FAN_MARKER={self.fan_marker!r}, "
            f"OWNER={self.owner!r}, "
            f"OPERATOR={self.operator!r}, "
            f"NAS_USE_FLAG={self.nas_use_flag!r}, "
            f"PUBLIC_USE_FLAG={self.public_use_flag!r}, "
            f"NDB_CLASS_CODE={self.ndb_class_code!r}, "
            f"OPER_HOURS={self.oper_hours!r}, "
            f"HIGH_ALT_ARTCC_ID={self.high_alt_artcc_id!r}, "
            f"HIGH_ARTCC_NAME={self.high_artcc_name!r}, "
            f"LOW_ALT_ARTCC_ID={self.low_alt_artcc_id!r}, "
            f"LOW_ARTCC_NAME={self.low_artcc_name!r}, "
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
            f"SURVEY_ACCURACY_CODE={self.survey_accuracy_code!r}, "
            f"TACAN_DME_STATUS={self.tacan_dme_status!r}, "
            f"TACAN_DME_LAT_DEG={self.tacan_dme_lat_deg!r}, "
            f"TACAN_DME_LAT_MIN={self.tacan_dme_lat_min!r}, "
            f"TACAN_DME_LAT_SEC={self.tacan_dme_lat_sec!r}, "
            f"TACAN_DME_LAT_HEMIS={self.tacan_dme_lat_hemis!r}, "
            f"TACAN_DME_LAT_DECIMAL={self.tacan_dme_lat_decimal!r}, "
            f"TACAN_DME_LONG_DEG={self.tacan_dme_long_deg!r}, "
            f"TACAN_DME_LONG_MIN={self.tacan_dme_long_min!r}, "
            f"TACAN_DME_LONG_SEC={self.tacan_dme_long_sec!r}, "
            f"TACAN_DME_LONG_HEMIS={self.tacan_dme_long_hemis!r}, "
            f"TACAN_DME_LONG_DECIMAL={self.tacan_dme_long_decimal!r}, "
            f"ELEV={self.elev!r}, "
            f"MAG_VARN={self.mag_varn!r}, "
            f"MAG_VARN_HEMIS={self.mag_varn_hemis!r}, "
            f"MAG_VARN_YEAR={self.mag_varn_year!r}, "
            f"SIMUL_VOICE_FLAG={self.simul_voice_flag!r}, "
            f"PWR_OUTPUT={self.pwr_output!r}, "
            f"AUTO_VOICE_ID_FLAG={self.auto_voice_id_flag!r}, "
            f"MNT_CAT_CODE={self.mnt_cat_code!r}, "
            f"VOICE_CALL={self.voice_call!r}, "
            f"CHAN={self.chan!r}, "
            f"FREQ={self.freq!r}, "
            f"MKR_IDENT={self.mkr_ident!r}, "
            f"MKR_SHAPE={self.mkr_shape!r}, "
            f"MKR_BRG={self.mkr_brg!r}, "
            f"ALT_CODE={self.alt_code!r}, "
            f"DME_SSV={self.dme_ssv!r}, "
            f"LOW_NAV_ON_HIGH_CHART_FLAG={self.low_nav_on_high_chart_flag!r}, "
            f"Z_MKR_FLAG={self.z_mkr_flag!r}, "
            f"FSS_ID={self.fss_id!r}, "
            f"FSS_NAME={self.fss_name!r}, "
            f"FSS_HOURS={self.fss_hours!r}, "
            f"NOTAM_ID={self.notam_id!r}, "
            f"QUAD_IDENT={self.quad_ident!r}, "
            f"PITCH_FLAG={self.pitch_flag!r}, "
            f"CATCH_FLAG={self.catch_flag!r}, "
            f"SUA_ATCAA_FLAG={self.sua_atcaa_flag!r}, "
            f"RESTRICTION_FLAG={self.restriction_flag!r}, "
            f"HIWAS_FLAG={self.hiwas_flag!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.nav_id} :: {self.nav_type}"

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
                f"NAV_STATUS: {self.nav_status}, "
                f"NAME: {self.name}, "
                f"STATE_NAME: {self.state_name}, "
                f"REGION_CODE: {self.region_code}, "
                f"COUNTRY_NAME: {self.country_name}, "
                f"FAN_MARKER: {self.fan_marker}, "
                f"OWNER: {self.owner}, "
                f"OPERATOR: {self.operator}, "
                f"NAS_USE_FLAG: {self.nas_use_flag}, "
                f"PUBLIC_USE_FLAG: {self.public_use_flag}, "
                f"NDB_CLASS_CODE: {self.ndb_class_code}, "
                f"OPER_HOURS: {self.oper_hours}, "
                f"HIGH_ALT_ARTCC_ID: {self.high_alt_artcc_id}, "
                f"HIGH_ARTCC_NAME: {self.high_artcc_name}, "
                f"LOW_ALT_ARTCC_ID: {self.low_alt_artcc_id}, "
                f"LOW_ARTCC_NAME: {self.low_artcc_name}, "
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
                f"SURVEY_ACCURACY_CODE: {self.survey_accuracy_code}, "
                f"TACAN_DME_STATUS: {self.tacan_dme_status}, "
                f"TACAN_DME_LAT_DEG: {self.tacan_dme_lat_deg}, "
                f"TACAN_DME_LAT_MIN: {self.tacan_dme_lat_min}, "
                f"TACAN_DME_LAT_SEC: {self.tacan_dme_lat_sec}, "
                f"TACAN_DME_LAT_HEMIS: {self.tacan_dme_lat_hemis}, "
                f"TACAN_DME_LAT_DECIMAL: {self.tacan_dme_lat_decimal}, "
                f"TACAN_DME_LONG_DEG: {self.tacan_dme_long_deg}, "
                f"TACAN_DME_LONG_MIN: {self.tacan_dme_long_min}, "
                f"TACAN_DME_LONG_SEC: {self.tacan_dme_long_sec}, "
                f"TACAN_DME_LONG_HEMIS: {self.tacan_dme_long_hemis}, "
                f"TACAN_DME_LONG_DECIMAL: {self.tacan_dme_long_decimal}, "
                f"ELEV: {self.elev}, "
                f"MAG_VARN: {self.mag_varn}, "
                f"MAG_VARN_HEMIS: {self.mag_varn_hemis}, "
                f"MAG_VARN_YEAR: {self.mag_varn_year}, "
                f"SIMUL_VOICE_FLAG: {self.simul_voice_flag}, "
                f"PWR_OUTPUT: {self.pwr_output}, "
                f"AUTO_VOICE_ID_FLAG: {self.auto_voice_id_flag}, "
                f"MNT_CAT_CODE: {self.mnt_cat_code}, "
                f"VOICE_CALL: {self.voice_call}, "
                f"CHAN: {self.chan}, "
                f"FREQ: {self.freq}, "
                f"MKR_IDENT: {self.mkr_ident}, "
                f"MKR_SHAPE: {self.mkr_shape}, "
                f"MKR_BRG: {self.mkr_brg}, "
                f"ALT_CODE: {self.alt_code}, "
                f"DME_SSV: {self.dme_ssv}, "
                f"LOW_NAV_ON_HIGH_CHART_FLAG: {self.low_nav_on_high_chart_flag}, "
                f"Z_MKR_FLAG: {self.z_mkr_flag}, "
                f"FSS_ID: {self.fss_id}, "
                f"FSS_NAME: {self.fss_name}, "
                f"FSS_HOURS: {self.fss_hours}, "
                f"NOTAM_ID: {self.notam_id}, "
                f"QUAD_IDENT: {self.quad_ident}, "
                f"PITCH_FLAG: {self.pitch_flag}, "
                f"CATCH_FLAG: {self.catch_flag}, "
                f"SUA_ATCAA_FLAG: {self.sua_atcaa_flag}, "
                f"RESTRICTION_FLAG: {self.restriction_flag}, "
                f"HIWAS_FLAG: {self.hiwas_flag}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("NAV_BASE")
class NAV_BASE_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "Navigation Base", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = NAV_BASE(
                    eff_date=row["EFF_DATE"],
                    nav_id=row["NAV_ID"],
                    nav_type=row["NAV_TYPE"],
                    state_code=row["STATE_CODE"],
                    city=row["CITY"],
                    country_code=row["COUNTRY_CODE"],
                    nav_status=row["NAV_STATUS"],
                    name=row["NAME"],
                    state_name=row["STATE_NAME"],
                    region_code=row["REGION_CODE"],
                    country_name=row["COUNTRY_NAME"],
                    fan_marker=row["FAN_MARKER"],
                    owner=row["OWNER"],
                    operator=row["OPERATOR"],
                    nas_use_flag=row["NAS_USE_FLAG"],
                    public_use_flag=row["PUBLIC_USE_FLAG"],
                    ndb_class_code=row["NDB_CLASS_CODE"],
                    oper_hours=row["OPER_HOURS"],
                    high_alt_artcc_id=row["HIGH_ALT_ARTCC_ID"],
                    high_artcc_name=row["HIGH_ARTCC_NAME"],
                    low_alt_artcc_id=row["LOW_ALT_ARTCC_ID"],
                    low_artcc_name=row["LOW_ARTCC_NAME"],
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
                    survey_accuracy_code=row["SURVEY_ACCURACY_CODE"],
                    tacan_dme_status=row["TACAN_DME_STATUS"],
                    tacan_dme_lat_deg=row["TACAN_DME_LAT_DEG"],
                    tacan_dme_lat_min=row["TACAN_DME_LAT_MIN"],
                    tacan_dme_lat_sec=row["TACAN_DME_LAT_SEC"],
                    tacan_dme_lat_hemis=row["TACAN_DME_LAT_HEMIS"],
                    tacan_dme_lat_decimal=row["TACAN_DME_LAT_DECIMAL"],
                    tacan_dme_long_deg=row["TACAN_DME_LONG_DEG"],
                    tacan_dme_long_min=row["TACAN_DME_LONG_MIN"],
                    tacan_dme_long_sec=row["TACAN_DME_LONG_SEC"],
                    tacan_dme_long_hemis=row["TACAN_DME_LONG_HEMIS"],
                    tacan_dme_long_decimal=row["TACAN_DME_LONG_DECIMAL"],
                    elev=row["ELEV"],
                    mag_varn=row["MAG_VARN"],
                    mag_varn_hemis=row["MAG_VARN_HEMIS"],
                    mag_varn_year=row["MAG_VARN_YEAR"],
                    simul_voice_flag=row["SIMUL_VOICE_FLAG"],
                    pwr_output=row["PWR_OUTPUT"],
                    auto_voice_id_flag=row["AUTO_VOICE_ID_FLAG"],
                    mnt_cat_code=row["MNT_CAT_CODE"],
                    voice_call=row["VOICE_CALL"],
                    chan=row["CHAN"],
                    freq=row["FREQ"],
                    mkr_ident=row["MKR_IDENT"],
                    mkr_shape=row["MKR_SHAPE"],
                    mkr_brg=row["MKR_BRG"],
                    alt_code=row["ALT_CODE"],
                    dme_ssv=row["DME_SSV"],
                    low_nav_on_high_chart_flag=row["LOW_NAV_ON_HIGH_CHART_FLAG"],
                    z_mkr_flag=row["Z_MKR_FLAG"],
                    fss_id=row["FSS_ID"],
                    fss_name=row["FSS_NAME"],
                    fss_hours=row["FSS_HOURS"],
                    notam_id=row["NOTAM_ID"],
                    quad_ident=row["QUAD_IDENT"],
                    pitch_flag=row["PITCH_FLAG"],
                    catch_flag=row["CATCH_FLAG"],
                    sua_atcaa_flag=row["SUA_ATCAA_FLAG"],
                    restriction_flag=row["RESTRICTION_FLAG"],
                    hiwas_flag=row["HIWAS_FLAG"],
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
