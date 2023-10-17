#!/usr/bin/env python3

"""Write a Python function that inserts a new document in a collection
based on kwargs:

    Prototype: def insert_school(mongo_collection, **kwargs):
    mongo_collection will be the pymongo collection object
    Returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    newDoc = mongo_collection.insert_one(kwargs)
    return newDoc.inserted_id
