#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests
import sys

def number_of_subscribers(subreddit):
    user = {"User-Agent": "fake_user_agent"}
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers=user)
    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0
