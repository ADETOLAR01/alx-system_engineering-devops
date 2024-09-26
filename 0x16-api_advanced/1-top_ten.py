#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import sys
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'this_is_a_fake_subreddit'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(None)
        return
        
    data = response.json()
    posts = data["data"]["children"]
    
    for post in posts:
        print(post["data"]["title"])
