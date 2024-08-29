#!/usr/bin/python3
"""
Retrieves the number of subscribers for a given subreddit using the Reddit API.

Returns:
    int: The number of subscribers (0 if invalid subreddit).
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the subscriber count for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json?allow_over18=true"
    headers = {'User-Agent': 'My Reddit Script 0.1'}  # Custom User-Agent

    try:
        # Don't follow redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise exception for non-2xx status codes
        data = response.json()
        # Handle missing data gracefully
        return data.get('data', {}).get('subscribers', 0)
    except requests.exceptions.RequestException:
        # Handle any request exceptions (e.g., network errors)
        return 0


if __name__ == "__main__":
    if __name__ == "__main__":
        if len(sys.argv) < 2:
            print("Usage: 0-subs.py <subreddit>")
    exit(1)

    subreddit = sys.argv[1]
    subscribers = number_of_subscribers(subreddit)
    print(subscribers)
