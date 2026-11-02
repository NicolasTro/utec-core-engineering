#!/usr/bin/env python3
"""Módulo que define la clase Rectangle completa derivada de BaseGeometry."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Clase Rectangle con cálculo de área y representación en string."""

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

    def area(self):
        """Calcula y retorna el área del rectángulo.

        Returns:
            int: El área del rectángulo.
        """
        return self.__width * self.__height

    def __str__(self):
        """Retorna la representación formal en string del rectángulo.

        Returns:
            str: Representación con formato [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
