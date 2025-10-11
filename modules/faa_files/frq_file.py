from .faa_file_base import FAA_Record_Base, FAA_File_Base
from modules.action import Action
from modules.filters import FilterObject
from modules.record_helpers import replace_empty_string
from modules.registry import register_faa_file

from typing import Self

import csv


class FRQ(FAA_Record_Base):
    eff_date: str
    facility: str
    fac_name: str
    facility_type: str
    artcc_or_fss_id: str
    cpdlc: str
    tower_hrs: str
    serviced_facility: str
    serviced_fac_name: str
    serviced_site_type: str
    lat_decimal: str
    long_decimal: str
    serviced_city: str
    serviced_state: str
    serviced_country: str
    tower_or_comm_call: str
    primary_approach_radio_call: str
    freq: str
    sectorization: str
    freq_use: str
    remark: str
    file: str
    action: Action
    mods: str

    def __init__(
        self,
        eff_date: str,
        facility: str,
        fac_name: str,
        facility_type: str,
        artcc_or_fss_id: str,
        cpdlc: str,
        tower_hrs: str,
        serviced_facility: str,
        serviced_fac_name: str,
        serviced_site_type: str,
        lat_decimal: str,
        long_decimal: str,
        serviced_city: str,
        serviced_state: str,
        serviced_country: str,
        tower_or_comm_call: str,
        primary_approach_radio_call: str,
        freq: str,
        sectorization: str,
        freq_use: str,
        remark: str,
        file: str,
        action: Action,
        mods: str,
    ) -> None:
        self.eff_date = replace_empty_string(eff_date)
        self.facility = replace_empty_string(facility)
        self.fac_name = replace_empty_string(fac_name)
        self.facility_type = replace_empty_string(facility_type)
        self.artcc_or_fss_id = replace_empty_string(artcc_or_fss_id)
        self.cpdlc = replace_empty_string(cpdlc)
        self.tower_hrs = replace_empty_string(tower_hrs)
        self.serviced_facility = replace_empty_string(serviced_facility)
        self.serviced_fac_name = replace_empty_string(serviced_fac_name)
        self.serviced_site_type = replace_empty_string(serviced_site_type)
        self.lat_decimal = replace_empty_string(lat_decimal)
        self.long_decimal = replace_empty_string(long_decimal)
        self.serviced_city = replace_empty_string(serviced_city)
        self.serviced_state = replace_empty_string(serviced_state)
        self.serviced_country = replace_empty_string(serviced_country)
        self.tower_or_comm_call = replace_empty_string(tower_or_comm_call)
        self.primary_approach_radio_call = replace_empty_string(
            primary_approach_radio_call
        )
        self.freq = replace_empty_string(freq)
        self.sectorization = replace_empty_string(sectorization)
        self.freq_use = replace_empty_string(freq_use)
        self.remark = replace_empty_string(remark)
        self.file = file
        self.action = action
        self.mods = mods

    def to_string(self, last_record: Self | None = None) -> str:
        if last_record:
            modification_string = self.get_mod_string(last_record)
            return f"{self.facility} :: {self.freq_use} :: {modification_string}"
        return (
            f"{self.facility} :: {self.freq_use} :: "
            f"EFF_DATE: {self.eff_date}, "
            f"FAC_NAME: {self.fac_name}, "
            f"FACILITY_TYPE: {self.facility_type}, "
            f"ARTCC_OR_FSS_ID: {self.artcc_or_fss_id}, "
            f"CPDLC: {self.cpdlc}, "
            f"TOWER_HRS: {self.tower_hrs}, "
            f"SERVICED_FACILITY: {self.serviced_facility}, "
            f"SERVICED_FAC_NAME: {self.serviced_fac_name}, "
            f"SERVICED_SITE_TYPE: {self.serviced_site_type}, "
            f"LAT_DECIMAL: {self.lat_decimal}, "
            f"LONG_DECIMAL: {self.long_decimal}, "
            f"SERVICED_CITY: {self.serviced_city}, "
            f"SERVICED_STATE: {self.serviced_state}, "
            f"SERVICED_COUNTRY: {self.serviced_country}, "
            f"TOWER_OR_COMM_CALL: {self.tower_or_comm_call}, "
            f"PRIMARY_APPROACH_RADIO_CALL: {self.primary_approach_radio_call}, "
            f"FREQ: {self.freq}, "
            f"SECTORIZATION: {self.sectorization}, "
            f"REMARK: {self.remark}"
        )


@register_faa_file("FRQ")
class FRQ_File(FAA_File_Base):
    def __init__(
        self, file_path: str, filter_object: FilterObject | None = None
    ) -> None:
        super().__init__(file_path, "Frequency Change", filter_object)

        self.__load_from_csv()

    def __load_from_csv(self) -> None:
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = FRQ(
                    eff_date=row["EFF_DATE"],
                    facility=row["FACILITY"],
                    fac_name=row["FAC_NAME"],
                    facility_type=row["FACILITY_TYPE"],
                    artcc_or_fss_id=row["ARTCC_OR_FSS_ID"],
                    cpdlc=row["CPDLC"],
                    tower_hrs=row["TOWER_HRS"],
                    serviced_facility=row["SERVICED_FACILITY"],
                    serviced_fac_name=row["SERVICED_FAC_NAME"],
                    serviced_site_type=row["SERVICED_SITE_TYPE"],
                    lat_decimal=row["LAT_DECIMAL"],
                    long_decimal=row["LONG_DECIMAL"],
                    serviced_city=row["SERVICED_CITY"],
                    serviced_state=row["SERVICED_STATE"],
                    serviced_country=row["SERVICED_COUNTRY"],
                    tower_or_comm_call=row["TOWER_OR_COMM_CALL"],
                    primary_approach_radio_call=row["PRIMARY_APPROACH_RADIO_CALL"],
                    freq=row["FREQ"],
                    sectorization=row["SECTORIZATION"],
                    freq_use=row["FREQ_USE"],
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
