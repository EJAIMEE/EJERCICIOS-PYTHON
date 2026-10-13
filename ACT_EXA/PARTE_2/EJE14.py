"""
Jaime Escriche Garcia
23/10/26
"""

importe = float(input("Introduce el importe de la compra:"))
zona = input("Introduce la zona de envió (A/B/C):")
socio = input("¿Eres socio (S/N):")

if zona != "A" and zona != "B" and zona != "C":
    print("No es una zona valida")
else:

    if importe <= 150:
        if socio == "S":
            gasto = 19
        else:
            gasto = 25

    elif importe <= 750:
        if socio == "S":
            gasto = 49
        else:
            gasto = 60

    elif importe <= 1500:
        if socio == "S":
            gasto = 89
        else:
            gasto = 120

    else:
        if socio == "S":
            gasto = importe * 0.06
        else:
            gasto = importe * 0.08


if zona == "B":
    gasto = gasto + 30
elif zona == "C":
    gasto = gasto + 69

print("Gastos de envío:", gasto, "€")