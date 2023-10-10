#!/usr/bin/python3
""" A function that append """


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF8) and return the number.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to ppend to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
