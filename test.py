"""
This a Hello World type script
"""

def banner(message: str, border='-') -> None:
    """
    Print a message with a border
    :param message: The message to print
    :param border: The border character
    :return: None
    """
    line = border * len(message)
    print(line)
    print(message)
    print(line)
    return None
 

NAME = 'World!'.capitalize()
banner('Hello ' + NAME, '/')
