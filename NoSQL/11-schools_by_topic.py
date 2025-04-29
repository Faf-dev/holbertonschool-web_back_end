#!/usr/bin/env python3
"""
Returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    mongo_collection (pymongo collection) will be the pymongo collection
    topic (string) will be topic searched
    Returns the list of school having a specific topic
    """
    return list(mongo_collection.find({"topics": topic}))


if __name__ == "__main__":
    schools_by_topic()
