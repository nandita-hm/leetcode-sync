import requests
import os

def fetch_recent_problems(limit=5):
    # For now, use a static JSON placeholder or mock data
    # You can replace this with LeetCode GraphQL query later
    return [
        {"title": "Two Sum", "difficulty": "Easy", "language": "Python3",
         "status": "Accepted", "code": "class Solution: ..."},
        {"title": "Add Two Numbers", "difficulty": "Medium", "language": "Python3",
         "status": "Accepted", "code": "class Solution: ..."},
    ][:limit]
