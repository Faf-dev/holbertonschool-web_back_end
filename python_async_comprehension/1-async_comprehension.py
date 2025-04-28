#!/usr/bin/env python3
"""
Create a coroutine called async_compregension that takes no arguments.
It will collect 10 random numbers using an async comprehension
over async_generator. Then return the 10 random numbers.
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async_generator,
    then returns the 10 random numbers.
    """
    result: List[float] = [i async for i in async_generator()]
    return result
