"""
Jaime Escriche Garcia
12/10/2026
"""

KWh = float(input("Introduce los KWh consumidos: " ))   


if KWh <= 100:
    importe = KWh * 0.05
    print("Importe: ", importe, "€")

elif KWh <= 250:
    importe = 100 * 0.05 + (KWh - 100) * 0.10
    print("Importe: ", importe, "€")

elif KWh > 250:
    importe = 100 * 0.05 + 150 * 0.08 + (KWh - 250) * 0.10
    print("Importe: ", importe, "€")