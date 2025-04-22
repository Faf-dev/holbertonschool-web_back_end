#!/usr/bin/env python3
"""
Module to sum a list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function to sum a list of floats
    Args:
        input_list (List[float]): List of floats to sum
    Returns:
        float: Sum of the list
    """
    return sum(input_list)
