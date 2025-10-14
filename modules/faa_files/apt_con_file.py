from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class APT_CON(FAA_Record_Base):
    eff_date: str
    site_no: str
    site_type_code: str
    state_code: str
    arpt_id: str
    city: str
    country_code: str
    title: str
    name: str
    address1: str
    address2: str
    title_city: str
    state: str
    zip_code: str
    zip_plus_four: str
    phone_no: str

    def __init__(
        self,
        eff_date: str,
        site_no: str,
        site_type_code: str,
        state_code: str,
        arpt_id: str,
        city: str,
        country_code: str,
        title: str,
        name: str,
        address1: str,
        address2: str,
        title_city: str,
        state: str,
        zip_code: str,
        zip_plus_four: str,
        phone_no: str,
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
        self.title = replace_empty_string(title)
        self.name = replace_empty_string(name)
        self.address1 = replace_empty_string(address1)
        self.address2 = replace_empty_string(address2)
        self.title_city = replace_empty_string(title_city)
        self.state = replace_empty_string(state)
        self.zip_code = replace_empty_string(zip_code)
        self.zip_plus_four = replace_empty_string(zip_plus_four)
        self.phone_no = replace_empty_string(phone_no)

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
                f"TITLE: {self.title}, "
                f"NAME: {self.name}, "
                f"ADDRESS1: {self.address1}, "
                f"ADDRESS2: {self.address2}, "
                f"TITLE_CITY: {self.title_city}, "
                f"STATE: {self.state}, "
                f"ZIP_CODE: {self.zip_code}, "
                f"ZIP_PLUS_FOUR: {self.zip_plus_four}, "
                f"PHONE_NO: {self.phone_no}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("APT_CON")
class APT_CON_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "Airport Continuation", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = APT_CON(
                    eff_date=row["EFF_DATE"],
                    site_no=row["SITE_NO"],
                    site_type_code=row["SITE_TYPE_CODE"],
                    state_code=row["STATE_CODE"],
                    arpt_id=row["ARPT_ID"],
                    city=row["CITY"],
                    country_code=row["COUNTRY_CODE"],
                    title=row["TITLE"],
                    name=row["NAME"],
                    address1=row["ADDRESS1"],
                    address2=row["ADDRESS2"],
                    title_city=row["TITLE_CITY"],
                    state=row["STATE"],
                    zip_code=row["ZIP_CODE"],
                    zip_plus_four=row["ZIP_PLUS_FOUR"],
                    phone_no=row["PHONE_NO"],
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
