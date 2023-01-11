#!/usr/bin/python3
"""define a text reading file function"""


def read_file(filename=""):
    """Print the  UTF8 to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
