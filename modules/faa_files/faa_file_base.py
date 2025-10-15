from modules.action import Action
from modules.filters import FilterObject

from abc import abstractmethod
from copy import deepcopy
from typing import Self


class FAA_Record_Base:
    file: str
    action: Action
    mods: str

    def __init__(self, file: str, action: Action, mods: str) -> None:
        self.file = file
        self.action = action
        self.mods = mods

    def __repr__(self):
        return f"FILE={self.file!r}, ACTION={self.action!r}, MODS={self.mods!r}"

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
    def to_string(self, use_verbose: bool, last_record: Self | None = None) -> str:
        pass


class FAA_File_Base:
    file_path: str
    report_name: str
    adds: list[FAA_Record_Base]
    mods: list[FAA_Record_Base]
    del_adds: list[tuple[FAA_Record_Base, FAA_Record_Base]]
    dels: list[FAA_Record_Base]
    ignore: list
    filter_object: FilterObject | None

    def __init__(
        self,
        file_path: str,
        report_name: str,
        use_verbose: bool,
        filter_object: FilterObject | None = None,
    ) -> None:
        self.file_path = file_path
        self.report_name = report_name
        self.use_verbose = use_verbose
        self.adds = []
        self.mods = []
        self.del_adds = []
        self.dels = []
        self.ignore = ["file", "action", "mods"]
        self.filter_object = filter_object

    def get_text_report(self) -> str:
        self.__get_delete_add()

        result = f"{self.report_name}:\n"
        if (
            len(self.adds) == 0
            and len(self.mods) == 0
            and len(self.del_adds) == 0
            and len(self.dels) == 0
        ):
            result += "  No changes\n"
            return result

        if len(self.adds) > 0:
            result += "  Additions:\n"
            for r in self.adds:
                result += f"    {r.to_string(self.use_verbose)}\n"

        if len(self.mods) > 0:
            result += "  Modifications:\n"
            last_record = None
            for r in self.mods:
                if r.file == "1":
                    last_record = r
                else:
                    result += f"    {r.to_string(self.use_verbose, last_record)}\n"
                    last_record = None

        if len(self.del_adds) > 0:
            result += "  Deleted then Added:\n"
            for r in self.del_adds:
                last, this = r
                result += f"    {this.to_string(self.use_verbose, last)}\n"

        if len(self.dels) > 0:
            result += "  Deletions:\n"
            for r in self.dels:
                result += f"    {r.to_string(self.use_verbose)}\n"

        return result

    def __get_changed_fields(
        self, rec_1: FAA_Record_Base, rec_2: FAA_Record_Base
    ) -> str:
        d1, d2 = vars(rec_1), vars(rec_2)
        result_list = [
            k.upper() for k in d1 if k not in self.ignore and d1.get(k) != d2.get(k)
        ]
        return " ".join(result_list)

    def __get_delete_add(self) -> None:
        set_adds = set(self.adds)

        matched_pairs = []
        new_dels = []
        new_adds = set_adds.copy()

        for item_del in self.dels:
            if item_del in set_adds:
                item_add = next(ia for ia in self.adds if ia == item_del)

                mods = self.__get_changed_fields(item_del, item_add)
                item_del.mods = mods
                item_add.mods = mods

                matched_pairs.append((deepcopy(item_del), deepcopy(item_add)))
                new_adds.discard(item_add)
            else:
                new_dels.append(item_del)

        self.del_adds = matched_pairs
        self.dels = new_dels
        self.adds = list(new_adds)
