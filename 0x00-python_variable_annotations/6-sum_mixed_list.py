#!/usr/bin/env python3
"""mixed list module"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ takes a list mxd_lst of integers and floats
    and returns their sum as float. """
    return sum(mxd_lst)
