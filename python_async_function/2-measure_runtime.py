#!/usr/bin/env python3
"""
This module measure the total execution time of wait_n
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Call wait_n async func to measure the exec time (float values)
    Args:
        n (int): Number of loops.
        max_delay (int): Maximum delay.
        start (float): Start the measure
        end (float): End the measure
    Returns:
        elapsed (float): Time elapsed between start and end
    """
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.perf_counter()
    elapsed: float = end - start
    return elapsed
