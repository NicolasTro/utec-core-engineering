#!/usr/bin/env python3
"""Módulo que define la clase Rectangle con propiedades de ancho y alto."""


class Rectangle:
    """Clase que define un rectángulo mediante su ancho y alto."""

    def __init__(self, width=0, height=0):
        """Inicializa una nueva instancia de Rectangle.

        Args:
            width (int): Ancho del rectángulo (por defecto 0).
            height (int): Alto del rectángulo (por defecto 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Obtiene el ancho del rectángulo.

        Returns:
            int: El ancho del rectángulo.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Asigna el ancho del rectángulo con validación.

        Args:
            value (int): Ancho del rectángulo.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Obtiene el alto del rectángulo.

        Returns:
            int: El alto del rectángulo.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Asigna el alto del rectángulo con validación.

        Args:
            value (int): Alto del rectángulo.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
