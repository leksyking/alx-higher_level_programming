#!/usr/bin/python3
"""A function that appends a string at the end of a file"""


def append_write(filename="", text=""):
    """Returns the number of characters appended"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
