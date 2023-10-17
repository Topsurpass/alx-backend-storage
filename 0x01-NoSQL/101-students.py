#!/usr/bin/env python3
"""Write a Python function that returns all students sorted by average score:

    Prototype: def top_students(mongo_collection):
    mongo_collection will be the pymongo collection object
    The top must be ordered
    The average score must be part of each item returns with key = averageScore
"""


def top_students(mongo_collection):
    """Write a Python function that returns all students sorted by
    average score"""

    allStudents = [doc for doc in mongo_collection.find()]
    for student in allStudents:
        totalScore = sum(topic.get("score") for topic in student.get("topics"))
        averageScore = totalScore / len(student.get("topics"))
        student["averageScore"] = averageScore

    """Sort the students by average score in descending order"""
    sortedStudents = sorted(allStudents, key=lambda x: x["averageScore"], reverse=True)

    return sortedStudents
