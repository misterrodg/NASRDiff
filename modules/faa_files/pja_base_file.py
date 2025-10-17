from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class PJA_BASE(FAA_Record_Base):
    eff_date: str
    pja_id: str
    nav_id: str
    nav_type: str
    radial: str
    distance: str
    navaid_name: str
    state_code: str
    city: str
    latitude: str
    lat_decimal: str
    longitude: str
    long_decimal: str
    arpt_id: str
    site_no: str
    site_type_code: str
    drop_zone_name: str
    max_altitude: str
    max_altitude_type_code: str
    pja_radius: str
    chart_request_flag: str
    publish_criteria: str
    description: str
    time_of_use: str
    fss_id: str
    fss_name: str
    pja_use: str
    volume: str
    pja_user: str
    remark: str

    def __init__(
        self,
        eff_date: str,
        pja_id: str,
        nav_id: str,
        nav_type: str,
        radial: str,
        distance: str,
        navaid_name: str,
        state_code: str,
        city: str,
        latitude: str,
        lat_decimal: str,
        longitude: str,
        long_decimal: str,
        arpt_id: str,
        site_no: str,
        site_type_code: str,
        drop_zone_name: str,
        max_altitude: str,
        max_altitude_type_code: str,
        pja_radius: str,
        chart_request_flag: str,
        publish_criteria: str,
        description: str,
        time_of_use: str,
        fss_id: str,
        fss_name: str,
        pja_use: str,
        volume: str,
        pja_user: str,
        remark: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.pja_id = replace_empty_string(pja_id)
        self.nav_id = replace_empty_string(nav_id)
        self.nav_type = replace_empty_string(nav_type)
        self.radial = replace_empty_string(radial)
        self.distance = replace_empty_string(distance)
        self.navaid_name = replace_empty_string(navaid_name)
        self.state_code = replace_empty_string(state_code)
        self.city = replace_empty_string(city)
        self.latitude = replace_empty_string(latitude)
        self.lat_decimal = replace_empty_string(lat_decimal)
        self.longitude = replace_empty_string(longitude)
        self.long_decimal = replace_empty_string(long_decimal)
        self.arpt_id = replace_empty_string(arpt_id)
        self.site_no = replace_empty_string(site_no)
        self.site_type_code = replace_empty_string(site_type_code)
        self.drop_zone_name = replace_empty_string(drop_zone_name)
        self.max_altitude = replace_empty_string(max_altitude)
        self.max_altitude_type_code = replace_empty_string(max_altitude_type_code)
        self.pja_radius = replace_empty_string(pja_radius)
        self.chart_request_flag = replace_empty_string(chart_request_flag)
        self.publish_criteria = replace_empty_string(publish_criteria)
        self.description = replace_empty_string(description)
        self.time_of_use = replace_empty_string(time_of_use)
        self.fss_id = replace_empty_string(fss_id)
        self.fss_name = replace_empty_string(fss_name)
        self.pja_use = replace_empty_string(pja_use)
        self.volume = replace_empty_string(volume)
        self.pja_user = replace_empty_string(pja_user)
        self.remark = replace_empty_string(remark)

    def __hash__(self) -> int:
        return hash((self.pja_id))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, PJA_BASE):
            return False
        return self.pja_id == other.pja_id

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, PJA_BASE):
            return False
        return (self.pja_id, self.file) < (
            other.pja_id,
            other.file,
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"PJA_ID={self.pja_id!r}, "
            f"NAV_ID={self.nav_id!r}, "
            f"NAV_TYPE={self.nav_type!r}, "
            f"RADIAL={self.radial!r}, "
            f"DISTANCE={self.distance!r}, "
            f"NAVAID_NAME={self.navaid_name!r}, "
            f"STATE_CODE={self.state_code!r}, "
            f"CITY={self.city!r}, "
            f"LATITUDE={self.latitude!r}, "
            f"LAT_DECIMAL={self.lat_decimal!r}, "
            f"LONGITUDE={self.longitude!r}, "
            f"LONG_DECIMAL={self.long_decimal!r}, "
            f"ARPT_ID={self.arpt_id!r}, "
            f"SITE_NO={self.site_no!r}, "
            f"SITE_TYPE_CODE={self.site_type_code!r}, "
            f"DROP_ZONE_NAME={self.drop_zone_name!r}, "
            f"MAX_ALTITUDE={self.max_altitude!r}, "
            f"MAX_ALTITUDE_TYPE_CODE={self.max_altitude_type_code!r}, "
            f"PJA_RADIUS={self.pja_radius!r}, "
            f"CHART_REQUEST_FLAG={self.chart_request_flag!r}, "
            f"PUBLISH_CRITERIA={self.publish_criteria!r}, "
            f"DESCRIPTION={self.description!r}, "
            f"TIME_OF_USE={self.time_of_use!r}, "
            f"FSS_ID={self.fss_id!r}, "
            f"FSS_NAME={self.fss_name!r}, "
            f"PJA_USE={self.pja_use!r}, "
            f"VOLUME={self.volume!r}, "
            f"PJA_USER={self.pja_user!r}, "
            f"REMARK={self.remark!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.pja_id} :: {self.drop_zone_name}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"NAV_ID: {self.nav_id}, "
                f"NAV_TYPE: {self.nav_type}, "
                f"RADIAL: {self.radial}, "
                f"DISTANCE: {self.distance}, "
                f"NAVAID_NAME: {self.navaid_name}, "
                f"STATE_CODE: {self.state_code}, "
                f"CITY: {self.city}, "
                f"LATITUDE: {self.latitude}, "
                f"LAT_DECIMAL: {self.lat_decimal}, "
                f"LONGITUDE: {self.longitude}, "
                f"LONG_DECIMAL: {self.long_decimal}, "
                f"ARPT_ID: {self.arpt_id}, "
                f"SITE_NO: {self.site_no}, "
                f"SITE_TYPE_CODE: {self.site_type_code}, "
                f"MAX_ALTITUDE: {self.max_altitude}, "
                f"MAX_ALTITUDE_TYPE_CODE: {self.max_altitude_type_code}, "
                f"PJA_RADIUS: {self.pja_radius}, "
                f"CHART_REQUEST_FLAG: {self.chart_request_flag}, "
                f"PUBLISH_CRITERIA: {self.publish_criteria}, "
                f"DESCRIPTION: {self.description}, "
                f"TIME_OF_USE: {self.time_of_use}, "
                f"FSS_ID: {self.fss_id}, "
                f"FSS_NAME: {self.fss_name}, "
                f"PJA_USE: {self.pja_use}, "
                f"VOLUME: {self.volume}, "
                f"PJA_USER: {self.pja_user}, "
                f"REMARK: {self.remark}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("PJA_BASE")
class PJA_BASE_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(
            file_path, "Parachute Jump Area Base", use_verbose, filter_object
        )

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = PJA_BASE(
                    eff_date=row["EFF_DATE"],
                    pja_id=row["PJA_ID"],
                    nav_id=row["NAV_ID"],
                    nav_type=row["NAV_TYPE"],
                    radial=row["RADIAL"],
                    distance=row["DISTANCE"],
                    navaid_name=row["NAVAID_NAME"],
                    state_code=row["STATE_CODE"],
                    city=row["CITY"],
                    latitude=row["LATITUDE"],
                    lat_decimal=row["LAT_DECIMAL"],
                    longitude=row["LONGITUDE"],
                    long_decimal=row["LONG_DECIMAL"],
                    arpt_id=row["ARPT_ID"],
                    site_no=row["SITE_NO"],
                    site_type_code=row["SITE_TYPE_CODE"],
                    drop_zone_name=row["DROP_ZONE_NAME"],
                    max_altitude=row["MAX_ALTITUDE"],
                    max_altitude_type_code=row["MAX_ALTITUDE_TYPE_CODE"],
                    pja_radius=row["PJA_RADIUS"],
                    chart_request_flag=row["CHART_REQUEST_FLAG"],
                    publish_criteria=row["PUBLISH_CRITERIA"],
                    description=row["DESCRIPTION"],
                    time_of_use=row["TIME_OF_USE"],
                    fss_id=row["FSS_ID"],
                    fss_name=row["FSS_NAME"],
                    pja_use=row["PJA_USE"],
                    volume=row["VOLUME"],
                    pja_user=row["PJA_USER"],
                    remark=row["REMARK"],
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
