"""
Jaime Escriche Garcia
20/10/26
"""

notas = int(input("¿Cuántas notas? "))

suma = 0

for i in range (1, notas + 1):
    n_notas = int(input("Nota" + str(i) + ":"))
    suma = suma + n_notas
    media = suma / notas

print("nota media:", media)