"""
Jaime Escriche Garcia
23/10/26
"""

edad = 0

while edad >= 0 and edad <= 120:
    edad = int(input("Introduce tu edad: "))
    if edad < 0 or edad > 120:
        print("Edad no valida")
    else: 
        print("Tu edad es: ", edad)