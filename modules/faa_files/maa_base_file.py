from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class MAA_BASE(FAA_Record_Base):
    eff_date: str
    maa_id: str
    maa_type_name: str
    nav_id: str
    nav_type: str
    nav_radial: str
    nav_distance: str
    state_code: str
    city: str
    latitude: str
    longitude: str
    arpt_ids: str
    nearest_arpt: str
    nearest_arpt_dist: str
    nearest_arpt_dir: str
    maa_name: str
    max_alt: str
    min_alt: str
    maa_radius: str
    description: str
    maa_use: str
    check_notams: str
    time_of_use: str
    user_group_name: str

    def __init__(
        self,
        eff_date: str,
        maa_id: str,
        maa_type_name: str,
        nav_id: str,
        nav_type: str,
        nav_radial: str,
        nav_distance: str,
        state_code: str,
        city: str,
        latitude: str,
        longitude: str,
        arpt_ids: str,
        nearest_arpt: str,
        nearest_arpt_dist: str,
        nearest_arpt_dir: str,
        maa_name: str,
        max_alt: str,
        min_alt: str,
        maa_radius: str,
        description: str,
        maa_use: str,
        check_notams: str,
        time_of_use: str,
        user_group_name: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.maa_id = replace_empty_string(maa_id)
        self.maa_type_name = replace_empty_string(maa_type_name)
        self.nav_id = replace_empty_string(nav_id)
        self.nav_type = replace_empty_string(nav_type)
        self.nav_radial = replace_empty_string(nav_radial)
        self.nav_distance = replace_empty_string(nav_distance)
        self.state_code = replace_empty_string(state_code)
        self.city = replace_empty_string(city)
        self.latitude = replace_empty_string(latitude)
        self.longitude = replace_empty_string(longitude)
        self.arpt_ids = replace_empty_string(arpt_ids)
        self.nearest_arpt = replace_empty_string(nearest_arpt)
        self.nearest_arpt_dist = replace_empty_string(nearest_arpt_dist)
        self.nearest_arpt_dir = replace_empty_string(nearest_arpt_dir)
        self.maa_name = replace_empty_string(maa_name)
        self.max_alt = replace_empty_string(max_alt)
        self.min_alt = replace_empty_string(min_alt)
        self.maa_radius = replace_empty_string(maa_radius)
        self.description = replace_empty_string(description)
        self.maa_use = replace_empty_string(maa_use)
        self.check_notams = replace_empty_string(check_notams)
        self.time_of_use = replace_empty_string(time_of_use)
        self.user_group_name = replace_empty_string(user_group_name)

    def __hash__(self) -> int:
        return hash((self.maa_id))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, MAA_BASE):
            return False
        return self.maa_id == other.maa_id

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, MAA_BASE):
            return False
        return (self.maa_id) < (other.maa_id)

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"MAA_ID={self.maa_id!r}, "
            f"MAA_TYPE_NAME={self.maa_type_name!r}, "
            f"NAV_ID={self.nav_id!r}, "
            f"NAV_TYPE={self.nav_type!r}, "
            f"NAV_RADIAL={self.nav_radial!r}, "
            f"NAV_DISTANCE={self.nav_distance!r}, "
            f"STATE_CODE={self.state_code!r}, "
            f"CITY={self.city!r}, "
            f"LATITUDE={self.latitude!r}, "
            f"LONGITUDE={self.longitude!r}, "
            f"ARPT_IDS={self.arpt_ids!r}, "
            f"NEAREST_ARPT={self.nearest_arpt!r}, "
            f"NEAREST_ARPT_DIST={self.nearest_arpt_dist!r}, "
            f"NEAREST_ARPT_DIR={self.nearest_arpt_dir!r}, "
            f"MAA_NAME={self.maa_name!r}, "
            f"MAX_ALT={self.max_alt!r}, "
            f"MIN_ALT={self.min_alt!r}, "
            f"MAA_RADIUS={self.maa_radius!r}, "
            f"DESCRIPTION={self.description!r}, "
            f"MAA_USE={self.maa_use!r}, "
            f"CHECK_NOTAMS={self.check_notams!r}, "
            f"TIME_OF_USE={self.time_of_use!r}, "
            f"USER_GROUP_NAME={self.user_group_name!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.maa_id}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"MAA_TYPE_NAME: {self.maa_type_name}, "
                f"NAV_ID: {self.nav_id}, "
                f"NAV_TYPE: {self.nav_type}, "
                f"NAV_RADIAL: {self.nav_radial}, "
                f"NAV_DISTANCE: {self.nav_distance}, "
                f"STATE_CODE: {self.state_code}, "
                f"CITY: {self.city}, "
                f"LATITUDE: {self.latitude}, "
                f"LONGITUDE: {self.longitude}, "
                f"ARPT_IDS: {self.arpt_ids}, "
                f"NEAREST_ARPT: {self.nearest_arpt}, "
                f"NEAREST_ARPT_DIST: {self.nearest_arpt_dist}, "
                f"NEAREST_ARPT_DIR: {self.nearest_arpt_dir}, "
                f"MAA_NAME: {self.maa_name}, "
                f"MAX_ALT: {self.max_alt}, "
                f"MIN_ALT: {self.min_alt}, "
                f"MAA_RADIUS: {self.maa_radius}, "
                f"DESCRIPTION: {self.description}, "
                f"MAA_USE: {self.maa_use}, "
                f"CHECK_NOTAMS: {self.check_notams}, "
                f"TIME_OF_USE: {self.time_of_use}, "
                f"USER_GROUP_NAME: {self.user_group_name}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("MAA_BASE")
class MAA_BASE_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(
            file_path, "Misc Activity Area Base", use_verbose, filter_object
        )

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = MAA_BASE(
                    eff_date=row["EFF_DATE"],
                    maa_id=row["MAA_ID"],
                    maa_type_name=row["MAA_TYPE_NAME"],
                    nav_id=row["NAV_ID"],
                    nav_type=row["NAV_TYPE"],
                    nav_radial=row["NAV_RADIAL"],
                    nav_distance=row["NAV_DISTANCE"],
                    state_code=row["STATE_CODE"],
                    city=row["CITY"],
                    latitude=row["LATITUDE"],
                    longitude=row["LONGITUDE"],
                    arpt_ids=row["ARPT_IDS"],
                    nearest_arpt=row["NEAREST_ARPT"],
                    nearest_arpt_dist=row["NEAREST_ARPT_DIST"],
                    nearest_arpt_dir=row["NEAREST_ARPT_DIR"],
                    maa_name=row["MAA_NAME"],
                    max_alt=row["MAX_ALT"],
                    min_alt=row["MIN_ALT"],
                    maa_radius=row["MAA_RADIUS"],
                    description=row["DESCRIPTION"],
                    maa_use=row["MAA_USE"],
                    check_notams=row["CHECK_NOTAMS"],
                    time_of_use=row["TIME_OF_USE"],
                    user_group_name=row["USER_GROUP_NAME"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_airports_many(
                        record.arpt_ids
                    )

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
