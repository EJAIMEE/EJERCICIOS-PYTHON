"""
Jaime Escriche Garcia
12/10/2026
"""

lado_a = int(input("Introduce el lado a: " ))
lado_b = int(input("Introduce el lado b: " ))
lado_c = int(input("Introduce el lado c: " ))

if lado_a != lado_b != lado_c:
    print("Es un triángulo escaleno")

else:
    print("No es un triángulo escaleno")