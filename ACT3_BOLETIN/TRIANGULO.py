""""
Ejercicio 3 - ¿Forman un triángulo?
Autor: Jaime Escriche Garcia
Fecha: 06/10/26
"""
a = float(input("lado a: "))
b = float(input("lado b: "))
c = float(input("lado c: "))

if a > b + c and b > a + c and c > a + b: 
    print("No forman un triángulo")

elif a == b and b == c:
    print("Forman un triángulo equilátero")

elif a == b or b == c or a == c:
    print("Forman un triángulo isósceles")

else:
    print("Forman un triángulo escaleno")