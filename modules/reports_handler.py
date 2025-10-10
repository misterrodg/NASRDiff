import os

REPORTS_DIR = "./reports/"


def __get_file_list() -> list[str]:
    result: list[str] = []
    for item in os.listdir(REPORTS_DIR):
        full_path = os.path.join(REPORTS_DIR, item)
        if os.path.isfile(full_path) and not item.startswith("."):
            result.append(full_path)
    return result


def clear_reports() -> None:
    file_list = __get_file_list()
    for f in file_list:
        os.remove(f)
