"""
Jaime Escriche Garcia
17/11/26
"""

cadena = "TRWAGMYFPDXBNJZSQVHLCKE"

dni = input("DNI (8 cifras y una letra): ")
dni = dni.strip().upper()
letra = dni[-1]
numeros = int(dni[0:8])

if len(dni) == 9:
    resto = numeros % 23
    letra_correcta = cadena[resto]
    print("Resto de dividir", numeros, "entre 23:", resto)

    if letra == letra_correcta:
        print("El DNI", dni, "es correcta")
    else:
        print("El DNI", dni, "es incorrecto: la letra debe ser", letra_correcta)

else: 
    print("No es válido: tiene ", len(dni), "caracteres y debe tener 9")


    