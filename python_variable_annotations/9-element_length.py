#!/usr/bin/env python3
"""
This module contains a function that takes a list of sequences
and returns a list of tuples containing each sequence and its length.
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function to return a list of tuples containing each sequence
    and its length.
    Args:
        lst (Iterable[Sequence]): List of sequences to process
    Returns:
        List[Tuple[Sequence, int]]: List of tuples containing each sequence
        and its length.
    """
    return [(i, len(i)) for i in lst]
