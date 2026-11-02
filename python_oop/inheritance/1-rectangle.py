#!/usr/bin/env python3
"""Módulo que define la clase Rectangle derivada de BaseGeometry."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Clase Rectangle que utiliza validaciones de BaseGeometry."""

    def __init__(self, width, height):
        """Inicializa una nueva instancia de Rectangle.

        Args:
            width (int): Ancho del rectángulo.
            height (int): Alto del rectángulo.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
