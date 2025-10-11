from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class AWY_BASE(FAA_Record_Base):
    eff_date: str
    regulatory: str
    awy_designation: str
    awy_location: str
    awy_id: str
    update_date: str
    remark: str
    airway_string: str
    file: str
    action: Action
    mods: str

    def __init__(
        self,
        eff_date: str,
        regulatory: str,
        awy_designation: str,
        awy_location: str,
        awy_id: str,
        update_date: str,
        remark: str,
        airway_string: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        self.eff_date = replace_empty_string(eff_date)
        self.regulatory = replace_empty_string(regulatory)
        self.awy_designation = replace_empty_string(awy_designation)
        self.awy_location = replace_empty_string(awy_location)
        self.awy_id = replace_empty_string(awy_id)
        self.update_date = replace_empty_string(update_date)
        self.remark = replace_empty_string(remark)
        self.airway_string = replace_empty_string(airway_string)
        self.file = file
        self.action = action
        self.mods = mods

    def to_string(self, last_record: Self | None = None) -> str:
        if last_record:
            modification_string = self.get_mod_string(last_record)
            return f"{self.awy_id} :: {modification_string}"
        return (
            f"{self.awy_id} :: "
            f"EFF_DATE: {self.eff_date}, "
            f"REGULATORY: {self.regulatory}, "
            f"AWY_DESIGNATION: {self.awy_designation}, "
            f"AWY_LOCATION: {self.awy_location}, "
            f"UPDATE_DATE: {self.update_date}, "
            f"REMARK: {self.remark}, "
            f"AIRWAY_STRING: {self.airway_string}"
        )


@register_faa_file("AWY_BASE")
class AWY_BASE_File(FAA_File_Base):
    def __init__(
        self, file_path: str, filter_object: FilterObject | None = None
    ) -> None:
        super().__init__(file_path, "Airway Base", filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = AWY_BASE(
                    eff_date=row["EFF_DATE"],
                    regulatory=row["REGULATORY"],
                    awy_designation=row["AWY_DESIGNATION"],
                    awy_location=row["AWY_LOCATION"],
                    awy_id=row["AWY_ID"],
                    update_date=row["UPDATE_DATE"],
                    remark=row["REMARK"],
                    airway_string=row["AIRWAY_STRING"],
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
