#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list that takes a list mxd_lst of
integers and floats and returns their sum as a float.
"""
from typing import Union


def sum_mixed_list(mxd_lst: Union[float | int]) -> float:
    """
    Function to sum a list of integers and floats
    Args:
        mxd_lst (Union[float | int]): List of integers and floats to sum
    Returns:
        float: Sum of the list
    """
    return sum(mxd_lst)
