#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    try:
        r = requests.get(
            'http://www.reddit.com/r/{}/about.json'.format(subreddit),
            headers={'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'}
        )
        r.raise_for_status()
        subs = r.json().get("data", {}).get("subscribers", 0)
        return subs
    except requests.RequestException:
        return 0


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    print("Number of subscribers:", number_of_subscribers(subreddit))
