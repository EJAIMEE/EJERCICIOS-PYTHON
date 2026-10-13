"""
jaime Escriche Garcia
12/10/2026
"""
import math

a = int(input("Introduce el número a: "))
b = int(input("Introduce el número b: "))
c = int(input("Introduce el número c: "))

if a == 0:
    print("No existe la ecuación de segundo grado")

else:
    discriminante = b**2 - 4*a*c
    
    if discriminante < 0:
        print("no existen soluciones reales")
        
    elif discriminante > 0:
        sol1 = (-b + math.sqrt(discriminante)) / (2*a)
        sol2 = (-b - math.sqrt(discriminante)) / (2*a)
        print("x1 = ", sol1)
        print("x2 = ", sol2)
        print("no existen soluciones reales")

    elif discriminante == 0:
        sol3 = (-b / (2*a))
        print("x1 = ", sol3)
        print("x2 = ", sol3)
        