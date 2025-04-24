#!/usr/bin/env python3
"""
This module return an asyncio.Task class
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create a task with asyncio.create_task then return the class.
    Args:
        max_delay (int): Maximum delay.
    Return:
        a asyncio.Task class.
    """
    return asyncio.create_task(wait_random(max_delay))
