#!/usr/bin/env python3
"""
This module is a basic use for async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a delay.
    Args:
        max_delay (int): The maximum delay defined (optional arg).
    Returns:
        randomizer (float): A random number choose between 0 and max_delay.
    """
    randomizer = random.uniform(0, max_delay)
    await asyncio.sleep(randomizer)
    return randomizer
