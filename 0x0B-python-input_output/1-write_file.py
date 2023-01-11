#!/usr/bin/python3
"""A function that writes a string to text file"""


def write_file(filename="", text=""):
    """Return the numbers of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
