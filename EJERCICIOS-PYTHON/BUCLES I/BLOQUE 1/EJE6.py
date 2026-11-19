"""
Jaime Escriche Garcia
20/10/26
"""

numero = int(input("Introduce el numero entero: "))
limite = int(input("¿Hasta qué número? "))

for i in range (1, limite + 1):
        print(numero, "x", i, "=", numero * i)