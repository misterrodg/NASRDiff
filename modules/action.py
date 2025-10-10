from enum import StrEnum


class Action(StrEnum):
    ADDED = "Added"
    MODIFIED = "Modified"
    DELETED = "Deleted"
    UNKNOWN = "Unknown"
