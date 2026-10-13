#!/usr/bin/env python3

number = __import__('random').randint(-10000, 10000)

if number < 0:
    ult_digito = -((-number) % 10)
else:
    ult_digito = number % 10

if ult_digito > 5:
    print(f"Last digit of {number} is {ult_digito} and is greater than 5")
elif ult_digito == 0:
    print(f"Last digit of {number} is {ult_digito} and is 0")
else:
    print(f"Last digit of {number} is {ult_digito} "
    "and is less than 6 and not 0")
