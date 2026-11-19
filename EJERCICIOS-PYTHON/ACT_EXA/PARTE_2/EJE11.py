"""
Jaime Escriche Garcia
12/10/2026
"""

angulo = int(input("Introduce el ángulo: " ))

if angulo == 0:
    print("Angulo nulo")

elif 0 < angulo < 90:
    print("Angulo agudo")

elif angulo == 90:
    print("Angulo recto")

elif 90 < angulo < 180:
    print("Angulo obtuso")

elif angulo == 180:
    print("Angulo llano")

elif 180 < angulo < 360:
    print("Angulo concavo")

elif angulo == 360:
    print("Angulo completo")

