"""
Jaime Escriche Garcia
29/10/26
"""
contador = 0
año_inicio = int(input("Año inicial: "))
año_final = int(input("Año final: "))

while año_inicio > año_final:
    print("El año inicial no puede ser mayor que el final")
    año_inicio = int(input("Año inicial: "))
    año_final = int(input("Año final: "))

for año in range(año_inicio, año_final + 1):
    if (año % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        print(año)
        contador = contador + 1

print("Hay", cantidad, "años bisiestos")