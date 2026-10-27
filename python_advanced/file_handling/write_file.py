#!/usr/bin/env python3
"""Module that contains the write_file function."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns characters written."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
