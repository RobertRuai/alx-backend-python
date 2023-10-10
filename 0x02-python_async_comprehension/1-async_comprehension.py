#!/usr/bin/env python3
"""async_comprehension module"""
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """collect 10 random numbers using async comprehension."""
    r_list = [r async for r in async_generator()]
    return r_list
