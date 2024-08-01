#!/usr/bin/env python3
"""
Retrieves a value from a dict using a given key.
"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Safely retrieves a value from a dictionary using a specified key.
    If the key is not present in the dictionary, returns a default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
