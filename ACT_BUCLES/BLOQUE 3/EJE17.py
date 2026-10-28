"""
Jaime Escriche Garcia
28/10/26
"""

numero = float(input("Introduce el numero: "))

suma = 0
contandor = 0
minimo = numero
maximo = numero

while numero >= 0:
    suma = suma + numero
    contandor = contandor + 1    
    
    if numero < minimo:
        minimo = numero

    if numero > maximo:
        maximo = numero

    numero = float(input("Introduce otro número: "))
    

if numero < 0:
    print("No se ha introducido datos")
else:
    media = suma / contandor
    print("Media:", media)
    print("Minimo:", minimo)
    print("Maximo:", maximo)
