#!/usr/bin/env python3
"""
Create a corountine called measure_runtime that will execute
async_comprehension 4 times in parallel using asyncio.gather.
Measure the total runtime and return it.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Measure the total runtime of 4 async_comprehension calls.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    return time.time() - start_time
