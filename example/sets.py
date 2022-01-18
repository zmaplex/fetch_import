from abc import ABC
from typing import List


class AbstractClass(ABC):
    pass


class AbstractMetaClass(metaclass=ABC):
    pass


class ObjectClass:
    pass


class TypeClass(type):
    pass


def def_function():
    pass


var_int: int = 0
var_str: str = "hello world"
var_list: List = [1, 2, 3, 4, 5, 6]
