#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""


import requests

def recurse(subreddit, hot_list=[], after=None):
    # Base case: invalid subreddit or no more pages
    if after is "":
        return None
    
    # Set the base URL and the headers for the API request
    base_url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "python:redquery:v1.0 (by /u/redquery)"}

    # Append the after parameter if given
    if after is not None:
        url = base_url + subreddit + "/hot.json?after=" + after
    else:
        url = base_url + subreddit + "/hot.json"

    # Make the request and get the JSON response
    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()

    # Check if the response is valid
    if response.status_code == 200:
        # Get the list of posts and the next page token
        posts = data["data"]["children"]
        after = data["data"]["after"]

        # Loop through the posts and append the titles to the hot_list
        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        # Recursively call the function with the next page token
        return recurse(subreddit, hot_list, after)
    else:
        # Invalid subreddit or request error
        return None
