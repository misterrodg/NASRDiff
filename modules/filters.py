import json
import os


FILTER_DIR = "./"
FILTER_FILE = "filters.json"


class Filters:
    files: list[str]
    airports: list[str]
    n_lat: float
    s_lat: float
    w_lon: float
    e_lon: float

    def __init__(self, should_show: bool) -> None:
        self.files = []
        self.airports = []
        self.n_lat = 0.0
        self.s_lat = 0.0
        self.w_lon = 0.0
        self.e_lon = 0.0

        self.__load_json()

        if should_show:
            print("Filtering on:")
            if self.files:
                print(f"  Files: {", ".join(self.files)}")
            if self.airports:
                print(f"  Airports: {", ".join(self.airports)}")
            if (
                self.n_lat != 0.0
                and self.s_lat != 0.0
                and self.w_lon != 0.0
                and self.e_lon != 0.0
            ):
                print(
                    f"  Bounds: Lat {self.s_lat} to {self.n_lat} and Lon {self.w_lon} to {self.e_lon}"
                )

    def __load_json(self) -> None:
        full_path = os.path.join(FILTER_DIR, FILTER_FILE)
        if os.path.exists(full_path):
            with open(full_path, "r") as f:
                data = json.load(f)

                self.files = data.get("files", [])
                self.airports = data.get("airports", [])

                bounds = data.get("bounds", {})
                self.n_lat = bounds.get("n_lat", 0.0)
                self.s_lat = bounds.get("s_lat", 0.0)
                self.w_lon = bounds.get("w_lon", 0.0)
                self.e_lon = bounds.get("e_lon", 0.0)
        else:
            print("Filters file not found.")
