def replace_empty_string(value: str) -> str:
    if value.strip() == "":
        return "[blank]"
    return value
