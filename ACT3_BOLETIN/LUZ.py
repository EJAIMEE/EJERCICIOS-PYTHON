"""
Ejercicio 2 - ¿Cuanto cuesta la luz?
Autor: Jaime Escriche Garcia
Fecha: 06/10/26
"""

precio_base = 5
precio_barato = 0.10 
precio_caro = 0.20
 
eng_consumida = float(input("KWh consumido: "))
hora = int(input("Hora del consumo (0-23): "))

if hora < 0 or hora > 23:
    print("Los valores no son validos")

elif hora < 8:
    importe_barato = (precio_base + (eng_consumida * precio_barato)) * 1.21
    print("Franja Barata")
    print("Importe:", round(importe_barato, 2), "€")

else: 
    importe_caro = (precio_base + (eng_consumida * precio_caro)) * 1.21
    print("Franja Cara")
    print("Importe", round(importe_caro, 2), "€")