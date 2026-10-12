"""
Jaime Escriche Garcia
12/10/2026
"""

num_1 = int(input("Introduce el primer número: " ))
num_2 = int(input("Introduce el segundo número: " ))
num_3 = int(input("Introduce el tercer número: " ))

if num_1 < num_2 and num_1 < num_3:
    print("El menor es ", num_1)
elif num_2 < num_1 and num_2 < num_3:
    print("El menor es ", num_2)
else:
    print("El menor es ", num_3)