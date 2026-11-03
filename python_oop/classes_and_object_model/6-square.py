#!/usr/bin/env python3
"""Módulo que define la clase Square con coordenadas de posición."""


class Square:
    """Clase que define un cuadrado con tamaño y coordenadas."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa una nueva instancia de Square.

        Args:
            size (int): Tamaño del cuadrado (por defecto 0).
            position (tuple): Coordenadas (x, y) de 2 enteros positivos.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Obtiene las coordenadas de posición del cuadrado.

        Returns:
            tuple: Coordenadas del cuadrado.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Asigna las coordenadas de posición con validación.

        Args:
            value (tuple): Tupla de 2 enteros positivos.

        Raises:
            TypeError: Si value no es una tupla de 2 enteros positivos.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calcula y retorna el área actual del cuadrado.

        Returns:
            int: El área del cuadrado.
        """
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado considerando su posición."""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Representa el cuadrado como una cadena con formato."""
        if self.__size == 0:
            return ""
        lines = []
        for _ in range(self.__position[1]):
            lines.append("")
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)
