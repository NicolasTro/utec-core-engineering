#!/usr/bin/env python3
"""Módulo que define la clase BaseGeometry."""


class BaseGeometry:
    """Clase base de geometría con validaciones."""

    def area(self):
        """Calcula el área geométrica.

        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que un valor sea entero mayor que 0.

        Args:
            name (str): Identificador del parámetro.
            value (int): Valor a validar.

        Raises:
            TypeError: Si value no es entero.
            ValueError: Si value es menor o igual a 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
