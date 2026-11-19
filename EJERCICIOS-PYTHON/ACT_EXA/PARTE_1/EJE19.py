"""
Jaime Escriche Garcia
12/10/2026
"""

cadena = input("Introduce una cadena: ")
separador = input("Introduce un separador: ")
numero = int(input("Introduce un número entero: "))

resultado = (cadena + separador) *(numero - 1) + cadena
print(resultado)