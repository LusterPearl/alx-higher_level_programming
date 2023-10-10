#!/usr/bin/python3
""" Scrips that read line by line. """

import sys


def print_metrics(status_codes, total_size):
    """
    Print the metrics based on status codes and total size.

    Args:
        status_codes (dict): A dictionary with status codes as keys
        total_size (int): Total file size.

    Returns:
        None
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[codes] > 0:
            print("{}: {}".format(code, status_codes[code]))
