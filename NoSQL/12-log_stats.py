#!/usr/bin/env python3
"""
Provides some stats about Nginx logs
"""
from pymongo import MongoClient


def log():
    """
    Connect to MongoDB and print some stats about Nginx logs
    """
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs  # connect to the 'logs' database
    collection = db.nginx  # connect to the 'nginx' collection
    total_logs = collection.count_documents({})  # count all documents

    print(f'{total_logs} logs')

    methods = [
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE"
    ]
    print('Methods:')
    for method in methods:
        method_count = collection.count_documents({'method': method})
        print(f'\tmethod {method}: {method_count}')

    status_check = collection.count_documents({
        'method': "GET",
        'path': "/status"
        })  # count documents with method GET and path /status
    print(f'{status_check} status check')


if __name__ == "__main__":
    log()
