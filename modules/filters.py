import json
import os


FILTER_DIR = "./"
FILTER_FILE = "filters.json"


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

    def is_in_airports(self, airport_id: str) -> bool:
        if len(self.airports) == 0:
            return False
        if airport_id in self.airports:
            return True
        return False

    def is_in_airways(self, airway_id: str) -> bool:
        if len(self.airways) == 0:
            return False
        if airway_id in self.airways:
            return True
        return False

    def is_in_bounds(self, lat: str, lon: str) -> bool:
        lat_float = 0.0
        lon_float = 0.0
        try:
            lat_float = float(lat)
        except ValueError:
            return False
        try:
            lon_float = float(lon)
        except ValueError:
            return False
        if (
            self.n_lat == 0.0
            and self.s_lat == 0.0
            and self.w_lon == 0.0
            and self.e_lon == 0.0
        ):
            return False
        if (
            self.n_lat >= lat_float
            and self.s_lat <= lat_float
            and self.w_lon <= lon_float
            and self.e_lon >= lon_float
        ):
            return True
        return False


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
