#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB:

    Database: logs
    Collection: nginx
    Display (same as the example):
    first line: x logs where x is the number of documents in this collection
    second line: Methods:
    5 lines with the number of documents with the
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
    (see example below - warning: it’s a tabulation before each line)
    one line with the number of documents with:
    method=GET
    path=/status
    You can use this dump as data sample: dump.zip
"""
from pymongo import MongoClient


def nginx_request_logs(nginx_collection):
    """Function that provides some stats about Nginx logs stored in MongoDB"""
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        """Get total number of documents (logs) in the collection
        specified using each methods"""
        httpMethodCount = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, httpMethodCount))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_request_logs(client.logs.nginx)
