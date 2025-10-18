from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class ATC_SVC(FAA_Record_Base):
    eff_date: str
    site_no: str
    site_type_code: str
    facility_type: str
    state_code: str
    facility_id: str
    city: str
    country_code: str
    ctl_svc: str

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
        ctl_svc: str,
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
        self.ctl_svc = replace_empty_string(ctl_svc)

    def __hash__(self) -> int:
        return hash((self.facility_id, self.facility_type, self.ctl_svc))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ATC_SVC):
            return False
        return (
            self.facility_id == other.facility_id
            and self.facility_type == other.facility_type
            and self.ctl_svc == other.ctl_svc
        )

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, ATC_SVC):
            return False
        return (self.facility_id, self.facility_type, self.ctl_svc, self.file) < (
            other.facility_id,
            other.facility_type,
            other.ctl_svc,
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
            f"CTL_SVC={self.ctl_svc!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.facility_id} :: {self.facility_type} :: {self.ctl_svc}"

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
                f"COUNTRY_CODE: {self.country_code}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("ATC_SVC")
class ATC_SVC_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "ATC Service", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = ATC_SVC(
                    eff_date=row["EFF_DATE"],
                    site_no=row["SITE_NO"],
                    site_type_code=row["SITE_TYPE_CODE"],
                    facility_type=row["FACILITY_TYPE"],
                    state_code=row["STATE_CODE"],
                    facility_id=row["FACILITY_ID"],
                    city=row["CITY"],
                    country_code=row["COUNTRY_CODE"],
                    ctl_svc=row["CTL_SVC"],
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
