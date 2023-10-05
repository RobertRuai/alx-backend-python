#!/usr/bin/env python3
"""string and int/float to tuple module"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """string and int/float to tuple"""
    return (k, v * v)
