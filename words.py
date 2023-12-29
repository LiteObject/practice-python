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
                story_words.append(word)
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
# It is a string that is set to the name of the current module.
# When you import a module, the name of the module is set to the module's name.
# This allows you to check whether the code is being run as a script or as a module.
# If the code is being run as a script, __name__ will be set to __main__,
# and the code inside the if block will be executed.

if __name__ == '__main__':
    url = sys.argv[1]
    print(f"Fetching words from {url}")
    print("Words:")
    main(url)
