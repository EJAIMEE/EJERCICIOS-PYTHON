"""
Jaime Escriche Garcia
2/11/26
"""

cambio = int(input("Cambio a devolver: "))

while cambio <= 0 or cambio % 5 != 0:
    print("La cantidad debe ser un múltiplo de 5 mayor que 0")
    cambio = int(input("Cambio a devolver: "))

pendiente = cambio

while pendiente > 0:
    if pendiente >= 50:
        print("Billete de 50")
        pendiente = pendiente - 50

    elif pendiente >= 20:
        print("Billete de 20")
        pendiente = pendiente - 20

    elif pendiente >= 10:
        print("Billete de 10")
        pendiente = pendiente - 10
    
    else:
        print("Billete de 5")
        pendiente = pendiente - 5