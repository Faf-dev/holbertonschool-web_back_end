#!/usr/bin/env python3
"""
Return the largest integer less than or equal to n.
"""


def floor(n: float) -> int:
    """
    Return the largest integer less than or equal to n.
    """
    if n >= 0:
        return int(n)
    else:
        return int(n) - 1
