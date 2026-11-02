#!/usr/bin/env python3
"""Módulo que define la clase Square con representación de texto."""

SquareBase = __import__('1-square').Square


class Square(SquareBase):
    """Clase Square con representación en string personalizada."""

    def __init__(self, size):
        """Inicializa una nueva instancia de Square.

        Args:
            size (int): Tamaño del cuadrado.
        """
        super().__init__(size)

    def __str__(self):
        """Retorna la representación formal en string del cuadrado.

        Returns:
            str: Representación con formato [Square] <size>/<size>.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
