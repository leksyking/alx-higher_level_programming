#!/usr/bin/python3
"""Class to define a Square"""


class Square:
    def __init__(self. size=0):
        if type(size) is int:
            if size < 0:
                raise ValueError("Size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("Size must be an integer")
