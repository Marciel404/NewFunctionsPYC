from typing import Any
from discord.ext.commands import CommandError


class Raise(CommandError):

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message)


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

        """Add a item in collection

        :param name: str
        :param value: Any
        :return:
        """

        self.__Array[name] = value
    
    def get(self, name: str) -> Any:

        """Return a item in collection

        Args:
        ------
            name (str): name of item
        Returns:
            Any: Return any item in collection
        """

        if self.__Array.get(name) and self.__Array.__len__() > 0: return self.__Array.get(name)
        if self.__Array.get(name) is None and self.__Array.__len__() > 0: return NotInCollection
        if self.__Array.__len__() == 0: return EmptyCollection
    
    def getIgnoreCase(self, name: str) -> Any:

        """Return a item in collection ignorating Case

        Not recommended if you have items with the same name with different case

        :param name: str

        Returns:
            Any: Return any item in collection
        """

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

    def delete(self, name: str):

        """ Delete a item in Collection

        Raises:
            NotInCollection: _description_
        """

        try:
            del self.__Array[name]
        except KeyError:
            raise Raise(NotInCollection.__str__())
    
    def purge(self):

        """ Delete all itens in collection

        Raises:
            NotInCollection: _description_
        """

        try:
            for i in self.keys():
                self.delete(i)
        except TypeError:
            raise Raise(EmptyCollection.__str__())


class collection(Collection):
    ...
