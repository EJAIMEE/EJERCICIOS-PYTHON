"""
Jaime Escriche Garcia
28/10/26
"""

import random
aleatorio = random.randint(1,10)
contador = 0

numero = int(input("Adivina el número(1-10): "))

while numero != aleatorio:
    contador = contador + 1

    if numero < aleatorio:
        print("El número es mayor")
    else:
        print("El número es menor")

    numero = int(input("Adivina el número(1-10): "))
