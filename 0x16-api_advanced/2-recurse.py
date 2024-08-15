#!/usr/bin/python3
"""Contains the recurse function for retrieving hot post titles from a subreddit."""
import requests


def recurse(subreddit, hot_list=None, after="", count=0):
    """
    Returns a list of titles of all hot posts on a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.
    hot_list (list): Accumulator for storing the titles of hot posts.
    after (str): Pagination parameter for Reddit API to fetch posts after this ID.
    count (int): The current number of posts retrieved.

    Returns:
    list: A list of hot post titles, or None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raises an HTTPError for bad responses
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

    if response.status_code == 404:
        return None

    results = response.json().get("data", {})
    after = results.get("after")
    count += results.get("dist", 0)

    for c in results.get("children", []):
        hot_list.append(c.get("data", {}).get("title"))

    if after:
        return recurse(subreddit, hot_list, after, count)
    
    return hot_list
