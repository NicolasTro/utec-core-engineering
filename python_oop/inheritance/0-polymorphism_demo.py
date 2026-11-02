#!/usr/bin/env python3
"""Módulo de demostración conceptual de herencia y polimorfismo."""


class Animal:
    """Clase base que representa un animal."""

    def speak(self):
        """Sonido genérico del animal."""
        return "Some generic sound"


class Dog(Animal):
    """Clase derivada que representa un perro."""

    def speak(self):
        """Ladrido del perro."""
        return "Woof!"


class Cat(Animal):
    """Clase derivada que representa un gato."""

    def speak(self):
        """Maullido del gato."""
        return "Meow!"


if __name__ == "__main__":
    animals = [Dog(), Cat(), Animal()]
    for animal in animals:
        print(animal.speak())
