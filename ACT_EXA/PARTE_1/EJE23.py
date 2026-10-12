"""
Jaime Escriche Garcia
12/10/2026
"""

import math

lado1 = float(input("Introduce el lado 1 del triángulo: "))
lado2 = float(input("Introduce el lado 2 del triángulo: "))
angulo = float(input("Introduce el ángulo (en grados): "))

radianes = (angulo * math.pi) / 180
area = (lado1 * lado2 * math.sin(radianes)) / 2

print("El área del triángulo es: ",area)