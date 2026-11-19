"""
Jaime Escriche Garcia
12/10/2026
"""

num_1 = int(input("Introduce el primer número: " ))
num_2 = int(input("Introduce el segundo número: " ))

producto = num_1 * num_2

if producto > 0:
    print("El producto es positivo")

elif producto < 0:
    print("El producto es negativo") 

else:
    print("El producto es nulo")