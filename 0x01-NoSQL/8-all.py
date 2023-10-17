#!/usr/bin/env python3

"""Write a Python function that lists all documents in a collection:

    Prototype: def list_all(mongo_collection):
    Return an empty list if no document in the collection
    mongo_collection will be the pymongo collection object
"""


def list_all(mongo_collection):
    """List all documents in a collection"""
    return [i for i in mongo_collection.find()]
