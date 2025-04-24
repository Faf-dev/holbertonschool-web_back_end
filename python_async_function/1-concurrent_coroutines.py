#!/usr/bin/env python3
"""
This module execute wait_random n times with the specified max_delay
then return the delay in order
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a list of all the delays (float values)
    Args:
        n (int): Number of loops.
        max_delay (int): Maximum delay.
        i (int): Iterable.
        tasks (List): List of call.
    Returns:
        results: List of float containing all the delays.
    """
    tasks: List = []
    results: List[float] = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    for completed_task in asyncio.as_completed(tasks):
        results.append(await completed_task)
    return results
