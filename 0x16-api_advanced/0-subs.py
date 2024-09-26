#!/usr/bin/python3
"""
Module for requesting the Reddit API
"""
import requests
URL = 'https://www.reddit.com'


def number_of_subscribers(subreddit):
    """Queries and returns the number of subscribers of a given subreddit"""
    try:
        endpoint = '/r/{}/about.json'.format(subreddit)
        headers = {"User-Agent": "Custom Agent"}
        res = requests.get(URL + endpoint,
                           headers=headers,
                           allow_redirects=False)
        if res.status_code == 200:
            return res.json().get('data', {}).get('subscribers', 0)
        else:
            return 0
    except Exception:
        return 0
