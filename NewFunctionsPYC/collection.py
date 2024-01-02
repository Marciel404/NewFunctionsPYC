from typing import Any


class _EmptyCollection:

    def __bool__(self) -> bool:
        return False
    
    def __repr__(self) -> str:
        return "Collection.Empty"
    
    def __len__(self) -> int:
        return 0


class _NotInCollection:

    def __bool__(self) -> bool:
        return False
    
    def __repr__(self) -> str:
        return "Collection.UnknownItem"
    
    def __len__(self) -> int:
        return 0


NotInCollection = _NotInCollection()
EmptyCollection = _EmptyCollection()


class Collection():

    def __init__(self) -> None:

        self.__Array: dict = {}

    def set(self, name: str, value: Any) -> None:

        self.__Array[name] = value
    
    def get(self, name: str) -> Any:

        if self.__Array.get(name) and self.__Array.__len__() > 0: return self.__Array.get(name)
        if self.__Array.get(name) is None and self.__Array.__len__() > 0: return NotInCollection
        if self.__Array.__len__() == 0: return EmptyCollection
    
    def getIgnoreCase(self, name: str) -> Any:

        if self.__Array.__len__() == 0: return EmptyCollection

        for item in self.keys():
            if item.lower() == name.lower():
                return self.get(item)

        return self.get(name)

    def keys(self):

        Array: set = set()
        for r in self.__Array.keys():
            Array.add(r)

        return Array if Array.__len__() > 0 else EmptyCollection

    def delete(self, name: str) -> None:

        try:
            del self.__Array[name]
        except AttributeError:
            pass


class collection(Collection):
    ...
