#!/usr/bin/env python3
"""Writes a type-annotated functs sum_mixed_list which takes a list
mxd_lst of ints and floats and returns their sum as a float.
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of the list as a float"""
    return float(sum(mxd_lst))