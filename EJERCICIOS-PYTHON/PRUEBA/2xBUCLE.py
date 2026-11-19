"""
Jaime Escriche Garcia
23/10/26
"""

alto = int(input("Introduce el alto: "))
ancho = int(input("Introduce el ancho: "))

for i in range (1, alto +1):
    for i in range (1, ancho +1):
        print("*", end=" ")
    print()