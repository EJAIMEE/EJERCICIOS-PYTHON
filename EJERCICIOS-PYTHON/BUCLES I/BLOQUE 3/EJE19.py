"""
Jaime Escriche Garcia
28/10/26
"""

opcion = -1

while opcion != 0:
    print("=== CALCULADORA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("0. Salir")
    opcion = int(input("Elige una opción: "))

    while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion !=0:
        print("Opción no valida")
        opcion = int(input("Elige una opción: "))

    if opcion == 0:
        print("¡Hasta pronto!")
    else:
        n1 = int(input("Primer número: "))
        n2 = int(input("Segundo número: "))

        if opcion == 1:
            suma = n1 + n2
            print("Resultado:", suma)

        elif opcion == 2:
            resta = n1 - n2
            print("Resultado:", resta)

        elif opcion == 3:
            multiplicacion = n1 * n2
            print("Resultado:", multiplicacion)

        elif opcion == 4:
            if n2 == 0:
                print("No se puede dividir entre 0")
            else:
                division = n1 / n2
                print("Resultado:", division)