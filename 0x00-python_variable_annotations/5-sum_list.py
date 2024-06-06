#!/usr/bin/env python3
"""Writes a type-annotated funct sum_list which takes a list
input_list of floats as args and returns their sum as a float.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''returns their sum as a float
    '''
    return float(sum(input_list))