#!/usr/bin/env python3
"""Module that contains the append_write function."""


def append_write(filename="", text=""):
    """Appends a string to a UTF-8 text file and returns characters added."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
