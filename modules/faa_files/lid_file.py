from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class LID(FAA_Record_Base):
    eff_date: str
    country_code: str
    loc_id: str
    region_code: str
    state: str
    city: str
    lid_group: str
    fac_type: str
    fac_name: str
    resp_artcc_id: str
    artcc_computer_id: str
    fss_id: str

    def __init__(
        self,
        eff_date: str,
        country_code: str,
        loc_id: str,
        region_code: str,
        state: str,
        city: str,
        lid_group: str,
        fac_type: str,
        fac_name: str,
        resp_artcc_id: str,
        artcc_computer_id: str,
        fss_id: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.country_code = replace_empty_string(country_code)
        self.loc_id = replace_empty_string(loc_id)
        self.region_code = replace_empty_string(region_code)
        self.state = replace_empty_string(state)
        self.city = replace_empty_string(city)
        self.lid_group = replace_empty_string(lid_group)
        self.fac_type = replace_empty_string(fac_type)
        self.fac_name = replace_empty_string(fac_name)
        self.resp_artcc_id = replace_empty_string(resp_artcc_id)
        self.artcc_computer_id = replace_empty_string(artcc_computer_id)
        self.fss_id = replace_empty_string(fss_id)

    def __hash__(self) -> int:
        return hash((self.loc_id))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, LID):
            return False
        return self.loc_id == other.loc_id

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, LID):
            return False
        return (self.loc_id, self.file) < (other.loc_id, other.file)

    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"EFF_DATE={self.eff_date!r}, "
            f"COUNTRY_CODE={self.country_code!r}, "
            f"LOC_ID={self.loc_id!r}, "
            f"REGION_CODE={self.region_code!r}, "
            f"STATE={self.state!r}, "
            f"CITY={self.city!r}, "
            f"LID_GROUP={self.lid_group!r}, "
            f"FAC_TYPE={self.fac_type!r}, "
            f"FAC_NAME={self.fac_name!r}, "
            f"RESP_ARTCC_ID={self.resp_artcc_id!r}, "
            f"ARTCC_COMPUTER_ID={self.artcc_computer_id!r}, "
            f"FSS_ID={self.fss_id!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.loc_id}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"COUNTRY_CODE: {self.country_code}, "
                f"REGION_CODE: {self.region_code}, "
                f"STATE: {self.state}, "
                f"CITY: {self.city}, "
                f"LID_GROUP: {self.lid_group}, "
                f"FAC_TYPE: {self.fac_type}, "
                f"FAC_NAME: {self.fac_name}, "
                f"RESP_ARTCC_ID: {self.resp_artcc_id}, "
                f"ARTCC_COMPUTER_ID: {self.artcc_computer_id}, "
                f"FSS_ID: {self.fss_id}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("LID")
class LID_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(file_path, "Location Identifier", use_verbose, filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = LID(
                    eff_date=row["EFF_DATE"],
                    country_code=row["COUNTRY_CODE"],
                    loc_id=row["LOC_ID"],
                    region_code=row["REGION_CODE"],
                    state=row["STATE"],
                    city=row["CITY"],
                    lid_group=row["LID_GROUP"],
                    fac_type=row["FAC_TYPE"],
                    fac_name=row["FAC_NAME"],
                    resp_artcc_id=row["RESP_ARTCC_ID"],
                    artcc_computer_id=row["ARTCC_COMPUTER_ID"],
                    fss_id=row["FSS_ID"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_artccs(
                        record.resp_artcc_id
                    )

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
