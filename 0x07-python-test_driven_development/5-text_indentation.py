#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = [".", "?", ":"]
    result = ""

    for char in text:
        result += char
        if char in punctuation_marks:
            result += "\n\n"

    lines = result.split("\n")
    for line in lines:
        print(line.strip())
