#!/usr/bin/python3
"""
Retrieves titles of the top 10 hot posts from a given subreddit
using the Reddit API.

Args:
    subreddit (str): The name of the subreddit.

Prints:
    None: If the subreddit is invalid.
    Titles (str): Titles of the top 10 hot posts, one per line.
"""

import requests


def top_ten(subreddit):
    """
    Fetches titles of the top 10 hot posts from a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Prints:
        None: If the subreddit is invalid or less than 10 posts are found.
        Titles (str): Titles of the top 10 hot posts, one per line.
    """
    BASE_URL = "https://www.reddit.com/r/"
    url = f"{BASE_URL}{subreddit}/hot.json?limit=10&allow_over18=true"
    headers = {'User-Agent': 'Mozilla/128.0'}  # Custom User-Agent


    try:
        # Don't follow redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise exception for non-2xx status codes
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print(None)
            return

        for post in posts[:10]:  # Limit to top 10 posts
            title = post.get('data', {}).get('title')
            if title:
                print(title)

    except requests.exceptions.RequestException:
        # Handle any request exceptions (e.g., network errors)
        print(None)


if __name__ == "__main__":
    # Handle missing argument
    top_ten(sys.argv[1] if len(sys.argv) > 1 else None)
