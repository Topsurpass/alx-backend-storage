#!/usr/bin/env python3
"""Create a Cache class. In the __init__ method,
store an instance of the Redis client as a private
variable named _redis (using redis.Redis()) and flush
the instance using flushdb.

Create a store method that takes a data argument and
returns a string. The method should generate a random key
(e.g. using uuid), store the input data in Redis using
the random key and return the key.

Type-annotate store correctly. Remember that data
can be a str, bytes, int or float.
"""
from typing import Union, Optional, Callable
import redis
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """A decorated function that count how many times methods
    of the Cache class are called."""

    """conserve the original arg method’s name, docstring e.t.c"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """This function performs before the normal function.
        it increments the count for that key every time the method
        is called and returns the value returned by the original
        method"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)


class Cache:
    """Cache data in redis database
        Attributes:
            store: Accepts the value to be stored in the database
            and return the key.
    """
    def __init__(self):
        """Initialize the instance of the class Cache once created"""
        self._redis = redis.Redis()
        """Flush all keys in the database"""
        self._redis.flushdb
    
    """Now, pass the store method to the count_calls decorator functn"""
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate random key, stored input data in Redis"""
        dBaseKey = str(uuid4())
        self._redis.set(dBaseKey, data)
        return dBaseKey
    
    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """A function to convert the returned data from db back to
        the desired format."""
        dbRtrVal = self._redis.get(key)

        """if key exist, use function else return raw output"""
        if fn:
            return fn(dbRtrVal)
        return dbRtrVal

    def get_str(self, key: str) -> str:
        """Automatically parametrize Cache.get with correct conversion
        function"""
        val = self._redis.get(key)
        return val.decode("utf-8")
    
    def get_int(self, key:str) -> str:
        """Automatically parametrize Cache.get with correct conversion
        function"""
        val = self._redis.get(key)
        try:
            val = int(val.decode("utf-8"))
        except Exception:
            val = 0

        return val
