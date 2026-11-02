#!/usr/bin/env python3
"""Módulo que define la clase Square con atributo privado de tamaño."""


class Square:
    """Clase que define un cuadrado por su tamaño."""

    def __init__(self, size):
        """Inicializa una nueva instancia de Square.

        Args:
            size: Tamaño del cuadrado.
        """
        self.__size = size
