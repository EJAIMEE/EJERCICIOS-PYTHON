"""
Jaime Escriche Garcia
20/10/26
"""

notas = int(input("¿Cuántas notas? "))

suma = 0
suspensos = 0
aprobados = 0

for i in range (1, notas + 1):
    n_notas = int(input("Nota" + str(i) + ":"))
    suma = suma + n_notas
    if n_notas >= 5:
        aprobados = aprobados + 1
    else:
        suspensos = suspensos + 1



media = suma / notas
        
print("nota media:", media)
print("Aprobados:", aprobados)
print("Suspensos:", suspensos)
