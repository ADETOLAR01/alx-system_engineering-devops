#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    # Set the custom User-Agent header
    headers = {'User-Agent': 'python:subscribers:v1.0.0 (by /u/wintermancer)'}

    # Construct the URL with the subreddit name
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    # Send a GET request to the URL
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check the status code and the response JSON
    if response.status_code == 200 and response.json().get('kind') == 't5':
        # Return the number of subscribers from the JSON data
        return response.json().get('data').get('subscribers')
    else:
        # Return 0 if the subreddit is invalid or an error occurs
        return 0
