"""
Jaime Escriche Garcia
23/10/26
"""

numero = int(input("¿cuántos números? "))

for i in range (1, numero + 1):
    n_numeros = int(input("Número" + str(i) + ":" ))

    if 1 == 1:
        mayor = n_numeros
    elif n_numeros > mayor:
        mayor = n_numeros

print("El mayor es", mayor)
