#!/usr/bin/python3
""" this module returns the number of subscribers """
from requests import sys

def number_of_subscribers(subreddit):
    """
    returns the numberof subscribers of a subreddit
    """
    base = 'https://www.reddit.com/'
    user_agent = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(base + subreddit + '/about', headers=user_agent,
                     allow_redirects=False)
    if (r.status_code == 404):
        return 0
    else:
        data = r.json()
        return data['data']['subscribers']
