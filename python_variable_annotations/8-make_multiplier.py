#!/usr/bin/env python3
"""
This module contains a function that takes a float multiplier
and returns a function that multiplies a float by the multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.
    Args:
        multiplier (float): The multiplier to use.
        Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of the float and the multiplier.
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
