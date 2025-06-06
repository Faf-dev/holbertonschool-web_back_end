#!/usr/bin/env python3
"""
Write a type-annotated function to_kv that takes a string k
and an int OR float v as arguments
and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function to convert a string and an int or float to a tuple
    Args:
        k (str): The string to convert
        v (Union[int, float]): The int or float to convert
    Returns:
        Tuple[str, float]: The tuple containing the string
        and the square of the int or float
    """
    return (k, v ** 2)
