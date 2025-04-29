#!/usr/bin/env python3
"""
lists all documents in a collection
return an empty list if no document in the collection
"""

def list_all(mongo_collection):
    """lists all documents in a collection
       return an empty list if no document in the collection
    """
    return list(mongo_collection.find())
