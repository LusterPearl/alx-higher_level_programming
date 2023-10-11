#!/usr/bin/python3
""" A function that add all arguments to the script """

import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args):
    """
    Add command-line arguments to a Python list and save it in JSON file.

    Args:
        args (list): A list of command-line arguments.

    Returns:
        None
    """
    if path.exists("add_item.json"):
        my_list = load_from_json_file("add_item.json")
    else:
        my_list = []

    my_list.extend(args)

    save_to_json_file(my_list, "add_item.json")
