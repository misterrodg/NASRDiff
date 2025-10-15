import json
import os
import re


FILTER_DIR = "./"
FILTER_FILE = "filters.json"

BAD_CONVERSION = 360.0


class FilterObject:
    artccs: list[str]
    airports: list[str]
    airways: list[str]
    n_lat: float
    s_lat: float
    w_lon: float
    e_lon: float

    def __init__(self) -> None:
        self.artccs = []
        self.airports = []
        self.airways = []
        self.n_lat = 0.0
        self.s_lat = 0.0
        self.w_lon = 0.0
        self.e_lon = 0.0

    def is_in_artccs(self, artcc_id: str) -> bool:
        if len(self.artccs) == 0:
            return False
        if artcc_id in self.artccs:
            return True
        return False

    def is_in_artccs_many(self, artcc_ids: str) -> bool:
        if len(self.artccs) == 0:
            return False
        list_ids = artcc_ids.split()
        for id in list_ids:
            if id in self.artccs:
                return True
        return False

    def is_in_airports(self, airport_id: str) -> bool:
        if len(self.airports) == 0:
            return False
        if airport_id in self.airports:
            return True
        return False

    def is_in_airports_many(self, airport_ids: str) -> bool:
        if len(self.airports) == 0:
            return False
        list_ids = airport_ids.split()
        for id in list_ids:
            if id in self.airports:
                return True
        return False

    def is_in_airways(self, airway_id: str) -> bool:
        if len(self.airways) == 0:
            return False
        if airway_id in self.airways:
            return True
        return False

    def __convert_float(self, value: str) -> float:
        try:
            return float(value)
        except:
            return BAD_CONVERSION

    def __is_in_bounds(self, lat: float, lon: float) -> bool:
        if (
            self.n_lat == 0.0
            and self.s_lat == 0.0
            and self.w_lon == 0.0
            and self.e_lon == 0.0
        ):
            return False
        if (
            self.n_lat >= lat
            and self.s_lat <= lat
            and self.w_lon <= lon
            and self.e_lon >= lon
        ):
            return True
        return False

    def is_in_bounds(self, lat: str, lon: str) -> bool:
        lat_float = self.__convert_float(lat)
        if lat_float == BAD_CONVERSION:
            return False

        lon_float = self.__convert_float(lon)
        if lon_float == BAD_CONVERSION:
            return False

        return self.__is_in_bounds(lat_float, lon_float)

    def __convert_dms(self, value: str) -> float:
        pattern = r"^(\d{2,3})-(\d{2})-(\d{2}\.\d{4})([NSEW])$"
        m = re.match(pattern, value)
        if not m.groups():
            return BAD_CONVERSION

        dec, mins, secs, hemi = m.groups()

        dec_float = self.__convert_float(dec)
        if dec_float == BAD_CONVERSION:
            return BAD_CONVERSION

        mins_float = self.__convert_float(mins)
        if mins_float == BAD_CONVERSION:
            return BAD_CONVERSION

        secs_float = self.__convert_float(secs)
        if secs_float == BAD_CONVERSION:
            return BAD_CONVERSION

        if hemi not in ["N", "E", "S", "W"]:
            return BAD_CONVERSION

        mins_in_dec = 60
        secs_in_min = 60
        result = (
            dec_float
            + (mins_float / mins_in_dec)
            + (secs_float / mins_in_dec / secs_in_min)
        )
        if hemi in ["S", "W"]:
            result = -result

        return result

    def is_in_bounds_dms(self, lat: str, lon: str) -> bool:
        lat_float = self.__convert_dms(lat)
        if lat_float == BAD_CONVERSION:
            return False

        lon_float = self.__convert_dms(lon)
        if lon_float == BAD_CONVERSION:
            return False

        return self.__is_in_bounds(lat_float, lon_float)


class Filters:
    files: list[str]
    filter_object: FilterObject
    filter_found: bool

    def __init__(self, should_show: bool) -> None:
        self.files = []
        self.filter_object = FilterObject()
        self.filter_found = False

        self.__load_json()

        if should_show:
            print("Filtering on:")
            if self.files:
                print(f"  Files: {", ".join(self.files)}")
            if self.filter_object.artccs:
                print(f"  ARTCCs: {", ".join(self.filter_object.artccs)}")
            if self.filter_object.airports:
                print(f"  Airports: {", ".join(self.filter_object.airports)}")
            if self.filter_object.airways:
                print(f"  Airways: {", ".join(self.filter_object.airways)}")
            if (
                self.filter_object.n_lat != 0.0
                and self.filter_object.s_lat != 0.0
                and self.filter_object.w_lon != 0.0
                and self.filter_object.e_lon != 0.0
            ):
                print(
                    f"  Bounds: Lat {self.filter_object.s_lat} to {self.filter_object.n_lat} and Lon {self.filter_object.w_lon} to {self.filter_object.e_lon}"
                )

    def __load_json(self) -> None:
        full_path = os.path.join(FILTER_DIR, FILTER_FILE)
        if os.path.exists(full_path):
            with open(full_path, "r") as f:
                data = json.load(f)

                self.files = data.get("files", [])
                self.filter_object.artccs = data.get("artccs", [])
                self.filter_object.airports = data.get("airports", [])
                self.filter_object.airways = data.get("airways", [])

                bounds = data.get("bounds", {})
                self.filter_object.n_lat = bounds.get("n_lat", 0.0)
                self.filter_object.s_lat = bounds.get("s_lat", 0.0)
                self.filter_object.w_lon = bounds.get("w_lon", 0.0)
                self.filter_object.e_lon = bounds.get("e_lon", 0.0)

                self.filter_found = True
        else:
            print("Filters file not found.\n")
