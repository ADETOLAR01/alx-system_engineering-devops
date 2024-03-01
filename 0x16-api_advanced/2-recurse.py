#!/usr/bin/python3
"""Contains recurse function"""
"""
100-count
"""
import requests


def count_words(subreddit, word_list, after=None, count={}):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords
    """
    # Base case
    if after is None:
        # Initialize count dictionary with keywords and zero values
        for word in word_list:
            word = word.lower()
            if word not in count:
                count[word] = 0
        # Make the first request with no after parameter
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        headers = {'User-Agent': 'custom'}
        response = requests.get(url, headers=headers, allow_redirects=False)
    else:
        # Make the subsequent requests with after parameter
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after)
        headers = {'User-Agent': 'custom'}
        response = requests.get(url, headers=headers, allow_redirects=False)

    # Check status code
    if response.status_code != 200:
        return None

    # Get the data as a dictionary
    data = response.json()

    # Get the list of posts
    posts = data.get('data').get('children')

    # Iterate over the posts
    for post in posts:
        # Get the title of the post
        title = post.get('data').get('title').lower()
        # Split the title into words
        words = title.split()
        # Iterate over the word_list
        for word in word_list:
            word = word.lower()
            # Count the occurrences of the word in the title
            count[word] += words.count(word)

    # Get the next page parameter
    after = data.get('data').get('after')

    # Check if there is a next page
    if after is None:
        # Sort the count dictionary by values and keys
        sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        # Print the results
        for key, value in sorted_count:
            # Skip the words with zero count
            if value == 0:
                continue
            print('{}: {}'.format(key, value))
    else:
        # Recursive call with the next page parameter
        return count_words(subreddit, word_list, after, count)
