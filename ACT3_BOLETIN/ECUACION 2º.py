""""
Ejercicio 1 - Ecuación de segundo grado
Autor/a: Jaime Escriche Garcia
Fecha: 06/10/2026
"""
import math

a = int(input("Coeficiente a: "))
b = int(input("Coeficiente b: "))
c = int(input("Coeficiente c: "))

if a == 0:
    print("No es una ecuación de 2º grado")

else:
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        sol1 = (-b + math.sqrt(discriminante)) / (2*a)
        sol2 = (-b - math.sqrt(discriminante)) / (2*a)
        print("Discriminante:", discriminante)
        print("Dos Soluciones: x1 =", sol1, "x2 =", sol2,)

    elif discriminante == 0:
        sol3 = (-b / (2*a))
        print("Hay sola una solución:", sol3)

    elif discriminante < 0:
        print("No hay solución real")
