#!/usr/bin/env python3
"""
Change all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
       mongo_collection (pymongo collection) will be the pymongo collection
       to update
       name (string) will be the school name to update
       topics (list of strings) will be the list of topics
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )


if __name__ == "__main__":
    update_topics()
