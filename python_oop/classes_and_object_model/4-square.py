#!/usr/bin/env python3
"""Módulo que define la clase Square con getters y setters para su tamaño."""


class Square:
    """Clase que define un cuadrado con getter y setter para size."""

    def __init__(self, size=0):
        """Inicializa una nueva instancia de Square.

        Args:
            size (int): Tamaño del cuadrado (por defecto 0).
        """
        self.size = size

    @property
    def size(self):
        """Obtiene el tamaño del cuadrado.

        Returns:
            int: El tamaño del cuadrado.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Asigna el tamaño del cuadrado con validación.

        Args:
            value (int): Nuevo tamaño del cuadrado.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcula y retorna el área actual del cuadrado.

        Returns:
            int: El área del cuadrado.
        """
        return self.__size ** 2
