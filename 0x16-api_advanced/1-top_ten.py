#!/usr/bin/python3
"""Contains top_ten function"""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit."""
    # Set the headers and parameters for the request
    headers = {"User-Agent": "0x16-api_advanced"}
    params = {"limit": 10}
    # Make a GET request to the subreddit's hot section
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json", headers=headers, params=params)
    # Check the status code and the data type of the response
    if response.status_code == 200 and response.headers["content-type"] == "application/json":
        # Parse the JSON data
        data = response.json()
        # Get the list of posts
        posts = data["data"]["children"]
        # Loop through the posts and print their titles
        for post in posts:
            print(post["data"]["title"])
    else:
        # If the request failed or the response was not JSON, print None
        print(None)
