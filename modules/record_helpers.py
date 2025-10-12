EMPTY_VALUE = "[blank]"


def replace_empty_string(value: str) -> str:
    if value.strip() == "":
        return EMPTY_VALUE
    return value
