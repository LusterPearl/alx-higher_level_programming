#!/usr/bin/python3
""" A code that writes a file """


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
