# Functions and Modules

Ejercicios sobre definición de funciones, modularización e importación en Python.

## Archivos

- `islower.py`: Función `islower(c)` que comprueba si un carácter es minúscula utilizando códigos ASCII (`ord()`).
- `uppercase.py`: Función `uppercase(str)` que imprime una cadena en mayúsculas usando conversión ASCII (`ord()` y `chr()`).
- `print_last_digit.py`: Función `print_last_digit(number)` que imprime y retorna el último dígito positivo de un número.
- `pow.py`: Función `pow(a, b)` que calcula la potencia iterativamente mediante un bucle sin usar `**`.
- `simple_add.py`: Función `add(a, b)` con protección de ejecución `if __name__ == "__main__":`.
- `test_import.py`: Script para verificar la importación limpia de `simple_add` sin ejecución de código a nivel superior.
- `add_0.py`: Función `add(a, b)` que retorna la suma de dos números.
- `add.py`: Programa que importa `add` desde `add_0.py` e imprime `1 + 2 = 3`.
- `calculator_1.py`: Módulo con funciones aritméticas (`add`, `sub`, `mul`, `div`).
- `calculation.py`: Programa que realiza operaciones básicas usando `calculator_1.py`.
- `variable_load_5.py`: Archivo que define la variable `a = 98`.
- `variable_load.py`: Programa que importa la variable `a` desde `variable_load_5.py` e imprime su valor.
