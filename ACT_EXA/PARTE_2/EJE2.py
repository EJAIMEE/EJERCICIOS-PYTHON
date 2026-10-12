"""
Jaime Escriche Garcia
13/10/2026
"""

lado_a = int(input("Introduce el lado a: " ))
lado_b = int(input("Introduce el lado b: " ))
lado_c = int(input("Introduce el lado c: " ))

if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
    print("Es un triángulo")

else:
    print("No es un triángulo")