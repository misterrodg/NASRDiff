from modules.filters import FilterObject

from abc import ABC, abstractmethod
from typing import Self


class FAA_Record_Base(ABC):
    def get_mod_string(self, last_record: Self) -> str:
        modifications = []
        modification_list = self.mods.split(" ")
        for mod in modification_list:
            mod_lower = mod.lower()
            last = getattr(last_record, mod_lower)
            this = getattr(self, mod_lower)
            mod_string = f"{mod} Change: "
            mod_string += f"{last} -> "
            mod_string += f"{this}"
            modifications.append(mod_string)
        return " // ".join(modifications)

    @abstractmethod
    def to_string(self, last_record: Self | None = None) -> str:
        pass


class FAA_File_Base:
    file_path: str
    report_name: str
    adds: list[FAA_Record_Base]
    mods: list[FAA_Record_Base]
    dels: list[FAA_Record_Base]
    filter_object: FilterObject | None

    def __init__(
        self,
        file_path: str,
        report_name: str,
        filter_object: FilterObject | None = None,
    ) -> None:
        self.file_path = file_path
        self.report_name = report_name
        self.adds = []
        self.mods = []
        self.dels = []
        self.filter_object = filter_object

    def get_text_report(self) -> str:
        result = f"{self.report_name}:\n"
        if len(self.adds) == 0 and len(self.mods) == 0 and len(self.dels) == 0:
            result += "  No changes\n"
            return result

        if len(self.adds) > 0:
            result += "  Additions:\n"
            for r in self.adds:
                result += f"    {r.to_string()}\n"

        if len(self.mods) > 0:
            result += "  Modifications:\n"
            last_record = None
            for r in self.mods:
                if r.file == "1":
                    last_record = r
                else:
                    result += f"    {r.to_string(last_record)}\n"
                    last_record = None

        if len(self.dels) > 0:
            result += "  Deletions:\n"
            for r in self.dels:
                result += f"    {r.to_string()}\n"

        return result
