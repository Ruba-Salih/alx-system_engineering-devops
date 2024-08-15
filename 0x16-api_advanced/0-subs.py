#!/usr/bin/python3
"""Returns the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for the given subreddit. Returns 0 if the subreddit is invalid.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    int: The number of subscribers or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "0x16-api_advanced:v1.0.0 (by /u/your_username)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raises an HTTPError for bad responses
    except requests.RequestException:
        return 0

    if response.status_code == 404:
        return 0

    try:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0  # Return 0 if the response isn't JSON


# Example usage
if __name__ == "__main__":
    subreddit = "learnpython"  # Replace with any subreddit to test
    print(f"Subscribers: {number_of_subscribers(subreddit)}")
