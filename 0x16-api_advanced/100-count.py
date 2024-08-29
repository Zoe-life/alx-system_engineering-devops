#!/usr/bin/python3
"""
Analyzes hot articles from a subreddit and prints a sorted count of
given keywords.

Args:
    subreddit (str): The name of the subreddit.
    word_list (list): A list of keywords for counting.
"""

import requests
from collections import Counter
from string import punctuation


def count_words(subreddit, word_list, word_counts={}, after=None):
    """
    Fetches hot articles recursively, extracts keywords, and calculates
    their counts.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords for counting.
        word_counts (dict, optional): Accumulated word counts (defaults to {}).
        after (str, optional): Parameter for pagination (defaults to None).

    Prints:
        None: If no posts match or the subreddit is invalid.
        Sorted word counts: Keywords and their counts, sorted by count
        (descending) and then alphabetically (ascending).
    """
    BASE_URL = "https://www.reddit.com/r/"
    url = f"{BASE_URL}{subreddit}/hot.json?limit=100&allow_over18=true"
    url += f"&after={after}" if after else ""
    headers = {'User-Agent': 'My Reddit Script 0.1'}  # Custom User-Agent

    try:
        # Don't follow redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise exception for non-2xx status codes
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            return  # No posts found

        for post in posts:
            title = post.get('data', {}).get('title', '')
            for word in word_list:
                clean_word = ''.join(
                    c.lower() for c in word if c not in punctuation).strip()
                if clean_word in title and clean_word != word:
                    continue
                word_counts[clean_word] = word_counts.get(clean_word, 0) + 1

        after = data.get('data', {}).get('after')  # Get next page token
        # Recursive call for next page
        return recurse(subreddit, word_list, word_counts, after)

    except requests.exceptions.RequestException:
        # Handle any request exceptions (e.g., network errors)
        return

    if not word_counts:
        return  # No keyword matches

    # Sort word counts by count and then alphabetically
    sorted_counts = sorted(word_counts.items(),
                           key=lambda item: (-item[1], item[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(
            sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
