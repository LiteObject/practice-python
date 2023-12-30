#!/usr/bin/env python3

"""
The `words` module provides functions for retrieving and printing words from a URL.

Usage Example #1:

    from words import get, print_words, main

    main('http://www.example.com')
    print_words(get('http://www.example.com'))

Usage Example #2:

    $ python3 words.py http://www.example.com

"""
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get(url_string: str):
    """
    Fetches words from a URL.
    Args:
        url_string: The URL to fetch words from.
    Returns:
        list: A list of words fetched from the URL.
    """
    story_words = []

    try:
        story = urlopen(url_string)

        for line in story:
            line_words = line.decode('utf8').split()
            for word in line_words:
                txt = html_to_text(word)
                story_words.append(txt)
    except IOError as e:
        print(f"URLError: {e}")
        sys.exit(1)
    finally:
        story.close()

    return story_words


def print_words(items):
    """
    Prints the words in a list.
    Args:
        items (list): The list of words to print.
    """
    for item in items:
        print(item)

def html_to_text(html_str: str) -> str:
    """
    Converts HTML to plain text.
    Args:
        html_str: The HTML to convert.
    Returns:
        str: The plain text.
    """

    try:
        soup = BeautifulSoup(html_str, 'html.parser')
        text = soup.get_text()
        return text
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)   

def main(url_string_1: str):
    """
    The main function of the program.
    Args:
        url_string_1: The URL to fetch words from.
    """
    print("Words:")
    words = get(url_string_1)
    print_words(words)

# __name__ is a special variable in Python.
# It let's our module be executable and importable.

if __name__ == '__main__':
    url = sys.argv[1]
    print(f"Fetching words from {url}")
    print("Words:")
    main(url)
