#!/usr/bin/env python3
"""This module contains example of how cache functionality
in web browsers works"""

import redis
from typing import Callable
from functools import wraps
import requests

"""Establish connection to the database using default details"""
redis = redis.Redis()


def wrap_requests(fn: Callable) -> Callable:
    """A decorated function definition for the cache"""

    @wraps(fn)
    def wrapper(url):
        """A wrapper function for the get_page function"""

        """Create key and automatically set & increase it's value by 1"""
        redis.incr(f"count:{url}")

        """Get cached key, if found, decode and return its value as str,
        else set the key and its value as get_page() return value with 10 secs
        expiration time"""

        cached_response = redis.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        newVal = fn(url)
        redis.setex(f"cached:{url}", 10, newVal)
        return newVal

    return wrapper


@wrap_requests
def get_page(url: str) -> str:
    """A function that get the body of a particular url"""
    response = requests.get(url)
    return response.text
