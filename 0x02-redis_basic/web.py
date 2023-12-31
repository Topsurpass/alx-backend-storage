#!/usr/bin/env python3
"""This module contains example of how cache functionality
in web browsers works"""

import redis
from typing import Callable
from functools import wraps
import requests

"""Establish connection to the database using default details"""
redisdb = redis.Redis()


def wrap_get_page(fxn: Callable) -> Callable:
    """A decorated function definition for the cache"""

    @wraps(fxn)
    def wrapper(url):
        """A wrapper function for the get_page function"""

        """Track how many times a particular URL was accessed in the
        key count:{url} by creating key and automatically setting &
        increasing it's value by 1 per access"""
        redisdb.incr(f"count:{url}")

        """Get cached data, if found, decode and return it as str,
        else set cached key and fix its value as get_page() return
        value with 10 secs expiration time"""
        cached_response = redisdb.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        newVal = fxn(url)
        redisdb.set(f"cached:{url}", newVal, ex=10)
        return newVal

    return wrapper


@wrap_get_page
def get_page(url: str) -> str:
    """A function that get the body of a particular url"""
    req = requests.get(url)
    return req.text
