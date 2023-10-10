#!/usr/bin/python3
""" A code that read files """


def read_file(filename=""):
    """
    Read and print the content of a text file to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
