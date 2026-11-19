"""
Jaime Escriche Garcia
27/10/26
"""

numero = float(input("Introduce el numero: "))
suma = 0
contandor = 0

if numero < 0:
    print("No se ha introducido datos")

while numero >= 0:
    otro = float(input("Introduce otro número: "))
    suma = suma + numero
    contandor = contandor + 1    
    
    if otro < 0:
        media = suma / contandor
        print ("Media:", media)