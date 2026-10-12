"""
Jaime Escriche Garcia
12/10/2026
"""

lado_a = int(input("Introduce el lado a: " ))
lado_b = int(input("Introduce el lado b: " ))
lado_c = int(input("Introduce el lado c: " ))

if lado_a**2 + lado_b**2 == lado_c**2 or lado_a**2 + lado_c**2 == lado_b**2 or lado_b**2 + lado_c**2 == lado_a**2:
    print("Es un triángulo rectángulo")

else:
    print("No es un triángulo rectángulo")