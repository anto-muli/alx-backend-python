#!/usr/bin/env python3
"""Writes a type-annotated funct to_kv that takes a str k
and an int OR float v as args and returns a tuple.The 1st
element of the tuple is the string k. The 2nd element is the
square of the int/float v and should be annotated as a float.
"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns a tuple of the string & square of v as float"""
    return (k, float(v * v))

