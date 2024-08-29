#!/usr/bin/python3
"""
Retrieves titles of all hot articles for a given subreddit using
recursion and the Reddit API.

Args:
    subreddit (str): The name of the subreddit.

Returns:
    list: A list of titles of all hot articles (empty list if none
    found), or None for invalid subreddits.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Fetches titles of hot articles for a subreddit recursively,
    handling pagination.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): Accumulated list of titles (defaults to []).
        after (str, optional): Parameter for pagination (defaults to None).

    Returns:
        list: A list of titles (empty list if none found), or None for
        invalid subreddits.
    """
    LONG_PARAMS = f"?limit=100&allow_over18=true"
    BASE_URL = "https://www.reddit.com/r/"
    url = (
            f"{BASE_URL}{subreddit}/hot.json{LONG_PARAMS}" +
            (f"&after={after}" if after else "")
            )
    headers = {'User-Agent': 'My Reddit Script 0.1'}  # Custom User-Agent

    try:
        # Don't follow redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise exception for non-2xx status codes
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            return hot_list  # No posts found, return accumulated list

        for post in posts:
            title = post.get('data', {}).get('title')
            if title:
                hot_list.append(title)

        after = data.get('data', {}).get('after')  # Get next page token
        # Recursive call for next page
        return recurse(subreddit, hot_list, after)

    except requests.exceptions.RequestException:
        # Handle any request exceptions (e.g., network errors)
        return None


if __name__ == "__main__":
    result = recurse(sys.argv[1] if len(sys.argv) > 1 else None)
    if result is not None:
        print(len(result))
    else:
        print("None")
