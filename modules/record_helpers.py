EMPTY_VALUE = "[blank]"


def replace_empty_string(value: str) -> str:
    value = value.strip()
    if value == "":
        return EMPTY_VALUE
    return value
