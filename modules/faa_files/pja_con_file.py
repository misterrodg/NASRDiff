from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class PJA_CON(FAA_Record_Base):
    eff_date: str
    pja_id: str
    fac_id: str
    fac_name: str
    loc_id: str
    commercial_freq: str
    commercial_chart_flag: str
    mil_freq: str
    mil_chart_flag: str
    sector: str
    contact_freq_altitude: str

    def __init__(
        self,
        eff_date: str,
        pja_id: str,
        fac_id: str,
        fac_name: str,
        loc_id: str,
        commercial_freq: str,
        commercial_chart_flag: str,
        mil_freq: str,
        mil_chart_flag: str,
        sector: str,
        contact_freq_altitude: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        super().__init__(file, action, mods)

        self.eff_date = replace_empty_string(eff_date)
        self.pja_id = replace_empty_string(pja_id)
        self.fac_id = replace_empty_string(fac_id)
        self.fac_name = replace_empty_string(fac_name)
        self.loc_id = replace_empty_string(loc_id)
        self.commercial_freq = replace_empty_string(commercial_freq)
        self.commercial_chart_flag = replace_empty_string(commercial_chart_flag)
        self.mil_freq = replace_empty_string(mil_freq)
        self.mil_chart_flag = replace_empty_string(mil_chart_flag)
        self.sector = replace_empty_string(sector)
        self.contact_freq_altitude = replace_empty_string(contact_freq_altitude)

    def __hash__(self) -> int:
        return hash((self.pja_id))

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, PJA_CON):
            return False
        return self.pja_id == other.pja_id

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, PJA_CON):
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
            f"FAC_ID={self.fac_id!r}, "
            f"FAC_NAME={self.fac_name!r}, "
            f"LOC_ID={self.loc_id!r}, "
            f"COMMERCIAL_FREQ={self.commercial_freq!r}, "
            f"COMMERCIAL_CHART_FLAG={self.commercial_chart_flag!r}, "
            f"MIL_FREQ={self.mil_freq!r}, "
            f"MIL_CHART_FLAG={self.mil_chart_flag!r}, "
            f"SECTOR={self.sector!r}, "
            f"CONTACT_FREQ_ALTITUDE={self.contact_freq_altitude!r}, "
            f"{super().__repr__()}"
            " )"
        )

    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        base_string = f"{self.pja_id} :: {self.fac_name}"

        modification_string = ""
        if last_record:
            modification_string = f" :: {self.get_mod_string(last_record)}"

        record_string = ""
        if use_verbose:
            record_string = (
                " :: [ "
                f"EFF_DATE: {self.eff_date}, "
                f"FAC_ID: {self.fac_id}, "
                f"LOC_ID: {self.loc_id}, "
                f"COMMERCIAL_FREQ: {self.commercial_freq}, "
                f"COMMERCIAL_CHART_FLAG: {self.commercial_chart_flag}, "
                f"MIL_FREQ: {self.mil_freq}, "
                f"MIL_CHART_FLAG: {self.mil_chart_flag}, "
                f"SECTOR: {self.sector}, "
                f"CONTACT_FREQ_ALTITUDE: {self.contact_freq_altitude}"
                " ]"
            )

        return f"{base_string}{modification_string}{record_string}"


@register_faa_file("PJA_CON")
class PJA_CON_File(FAA_File_Base):
    def __init__(
        self,
        file_path: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        super().__init__(
            file_path, "Parachute Jump Area Contact", use_verbose, filter_object
        )

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = PJA_CON(
                    eff_date=row["EFF_DATE"],
                    pja_id=row["PJA_ID"],
                    fac_id=row["FAC_ID"],
                    fac_name=row["FAC_NAME"],
                    loc_id=row["LOC_ID"],
                    commercial_freq=row["COMMERCIAL_FREQ"],
                    commercial_chart_flag=row["COMMERCIAL_CHART_FLAG"],
                    mil_freq=row["MIL_FREQ"],
                    mil_chart_flag=row["MIL_CHART_FLAG"],
                    sector=row["SECTOR"],
                    contact_freq_altitude=row["CONTACT_FREQ_ALTITUDE"],
                    file=row["File"],
                    action=Action(row["Action"]),
                    mods=row["Mods"],
                )

                use_filters = True if self.filter_object else False
                is_in_filters = False
                if use_filters and self.filter_object is not None:
                    is_in_filters = self.filter_object.is_in_airports(
                        record.fac_id
                    ) or self.filter_object.is_in_artccs(record.fac_id)

                if not use_filters or is_in_filters:
                    if record.action == Action.ADDED:
                        self.adds.append(record)
                    if record.action == Action.MODIFIED:
                        self.mods.append(record)
                    if record.action == Action.DELETED:
                        self.dels.append(record)
