#!/usr/bin/env python3
"""Given params and the return values, add type
annotations to the funct

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""


import typing


T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any, default:
                     typing.Union[T, None] = None) -> \
        typing.Union[typing.Any, T]:
    """annotations of the function"""
    if key in dct:
        return dct[key]
    else:
        return default
