from datetime import date
from typing import List
from collection import Collection


class BinDay:
    def __init__(self, collection_date: date, bin_types: List[str]):
        self.__collection_date = collection_date
        self.__bin_types = bin_types

    def get_collection_date(self):
        return self.__collection_date

    def get_bin_types(self):
        return self.__bin_types

    @classmethod
    def get_all_from_collection(cls, collections: List[Collection]) -> List['BinDay']:
        bin_types_by_date = {}
        for collection in collections:
            if collection.get_date() not in bin_types_by_date:
                bin_types_by_date[collection.get_date()] = [collection.get_bin_type()]
            else:
                bin_types_by_date[collection.get_date()].append(collection.get_bin_type())
        return [cls(bin_date, bin_types) for bin_date, bin_types in bin_types_by_date.items()]
