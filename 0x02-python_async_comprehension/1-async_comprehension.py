#!/usr/bin/env python3
"""Import async_generator from the task 0 and then write a coroutine
called async_comprehension that takes no args.

The coroutine will collect 10 random numbers using
over async_generator, then return the 10 random numbers.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return the 10 random numbers"""
    results = [i async for i in async_generator()]
    return results
