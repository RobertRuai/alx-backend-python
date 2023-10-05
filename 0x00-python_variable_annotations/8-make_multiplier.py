#!/usr/bin/env python3
"""multiplier module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns function that x float by multiplier"""
    def mult(n: float):
        return n * multiplier
    return mult
