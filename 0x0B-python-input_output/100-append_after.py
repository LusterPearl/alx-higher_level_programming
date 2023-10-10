#!/usr/bin/python3
""" A function that inserts a line of text to a file. """


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The specific string to search for.
        new_string (str): The line to insert.

    Returns:
            None
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
