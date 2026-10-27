#!/usr/bin/env python3
"""Módulo que contiene la función append_write."""


def append_write(filename="", text=""):
    """Añade texto a un archivo UTF-8 y devuelve los caracteres añadidos."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
