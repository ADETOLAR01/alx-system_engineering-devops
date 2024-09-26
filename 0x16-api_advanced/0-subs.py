#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Returns 0 if the subreddit is invalid or doesn't exist.
    """
    if not isinstance(subreddit, str):
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)

        # Check if subreddit is valid (status code 200 indicates success)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)

        # Invalid subreddit (status code 404 or redirect)
        return 0

    except requests.exceptions.RequestException as e:
        # In case of request failure or network issue, return 0
        return 0
