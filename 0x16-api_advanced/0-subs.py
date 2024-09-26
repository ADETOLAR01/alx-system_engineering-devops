#!/usr/bin/python3
"""
This module provides a function to query the Reddit API
for the number of subscribers of a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditAPI/0.1'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return 0
    
    data = response.json()
    return data['data']['subscribers']
