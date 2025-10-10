from modules.action import Action
from modules.faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.record_helpers import replace_empty_string

from typing import Self

import csv


class APT_ATT(FAA_Record_Base):
    eff_date: str
    site_no: str
    site_type_code: str
    state_code: str
    arpt_id: str
    city: str
    country_code: str
    sked_seq_no: str
    month: str
    day: str
    hour: str
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
        sked_seq_no: str,
        month: str,
        day: str,
        hour: str,
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
        self.sked_seq_no = replace_empty_string(sked_seq_no)
        self.month = replace_empty_string(month)
        self.day = replace_empty_string(day)
        self.hour = replace_empty_string(hour)
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
            return f"{self.arpt_id} :: {self.sked_seq_no} :: {modification_string}"
        return (
            f"{self.arpt_id} :: {self.sked_seq_no} :: "
            f"EFF_DATE: {self.eff_date}, "
            f"SITE_NO: {self.site_no}, "
            f"SITE_TYPE_CODE: {self.site_type_code}, "
            f"STATE_CODE: {self.state_code}, "
            f"CITY: {self.city}, "
            f"COUNTRY_CODE: {self.country_code}, "
            f"MONTH: {self.month}, "
            f"DAY: {self.day}, "
            f"HOUR: {self.hour}"
        )


class APT_ATT_File(FAA_File_Base):
    def __init__(
        self, file_path: str, filter_airports: list[str] | None = None
    ) -> None:
        super().__init__(file_path, "Airport Attendance", filter_airports)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = APT_ATT(
                    eff_date=row["EFF_DATE"],
                    site_no=row["SITE_NO"],
                    site_type_code=row["SITE_TYPE_CODE"],
                    state_code=row["STATE_CODE"],
                    arpt_id=row["ARPT_ID"],
                    city=row["CITY"],
                    country_code=row["COUNTRY_CODE"],
                    sked_seq_no=row["SKED_SEQ_NO"],
                    month=row["MONTH"],
                    day=row["DAY"],
                    hour=row["HOUR"],
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
