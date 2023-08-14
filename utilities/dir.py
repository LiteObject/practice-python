"""
This is the module docstring - short description.
"""

from pathlib import Path

def get_children(str_path):
    """
    In this example, we work with local file system
    """
    path = Path(str_path)

    if path.exists():
        files = path.glob("*")

        for file in files:
            print(file)
    else:
        print(f'The folder "{str_path}" is empty')
