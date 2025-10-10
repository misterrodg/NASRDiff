import os

NAVDATA_DIR = "./navdata/"
NAVDATA_FILE_TYPE = ".csv"


def __get_file_list() -> list[str]:
    result: list[str] = []
    for item in os.listdir(NAVDATA_DIR):
        full_path = os.path.join(NAVDATA_DIR, item)
        if os.path.isfile(full_path) and item.endswith(NAVDATA_FILE_TYPE):
            result.append(full_path)
    result.sort()
    return result


def get_csv_files() -> list[str]:
    return __get_file_list()


def clear_navdata() -> None:
    file_list = __get_file_list()
    for f in file_list:
        os.remove(f)
