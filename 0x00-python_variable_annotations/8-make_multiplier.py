#!/usr/bin/env python3
"""Writes a type-annotated funct make_multiplier that takes
a float multiplier as args and returns a funct that
multiplies a float by multiplier.
"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def float_multiply(x: float) -> float:
        return multiplier * x

    return float_multiply

