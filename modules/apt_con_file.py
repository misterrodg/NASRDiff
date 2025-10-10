from modules.action import Action
from modules.record_helpers import replace_empty_string

from typing import Self

import csv


class APT_CON:
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
        self.file = file
        self.action = action
        self.mods = mods

    def to_string(self, last_record: Self | None = None) -> str:
        if last_record:
            modifications = []
            modification_list = self.mods.split(" ")
            for mod in modification_list:
                mod_lower = mod.lower()
                last = getattr(last_record, mod_lower)
                this = getattr(self, mod_lower)
                mod_string = f"{mod} Change: "
                mod_string += f"{last} -> "
                mod_string += f"{this}"
                modifications.append(mod_string)
            modification_string = " // ".join(modifications)
            return f"{self.arpt_id} :: {modification_string}"
        return (
            f"{self.arpt_id} :: "
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
        )


class APT_CON_File:
    file_path: str
    adds: list[APT_CON]
    mods: list[APT_CON]
    dels: list[APT_CON]
    filter_airports: list[str]

    def __init__(
        self, file_path: str, filter_airports: list[str] | None = None
    ) -> None:
        self.file_path = file_path
        self.adds = []
        self.mods = []
        self.dels = []
        self.filter_airports = filter_airports if filter_airports else []

        self.__load_from_csv()

    def get_text_report(self) -> str:
        result = ""
        result = "Airport Continuation:\n"

        if len(self.adds) > 0:
            result += "  Additions:\n"
            for r in self.adds:
                result += f"    {r.to_string()}\n"

        if len(self.mods) > 0:
            result += "  Modifications:\n"
            last_record = None
            for r in self.mods:
                if r.file == "1":
                    last_record = r
                else:
                    result += f"    {r.to_string(last_record)}\n"
                    last_record = None

        if len(self.dels) > 0:
            result += "  Deletions:\n"
            for r in self.dels:
                result += f"    {r.to_string()}\n"

        return result

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

                use_filters = True if self.filter_airports else False
                is_in_filters = False
                if use_filters and record.arpt_id.strip() in self.filter_airports:
                    is_in_filters = True

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
