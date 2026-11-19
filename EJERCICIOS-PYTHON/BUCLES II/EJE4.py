"""
Jaime Escriche Garcia
30/10/26
"""

articulo = "Zapatillas"
precio = 35
falta = precio

print("Artículo:", articulo)
print("Precio:", precio, "€")

while falta > 0:
    billete = int(input("Introduce un billete: "))

    if billete != 5 and billete != 10 and billete != 20 and billete != 50:
        print("Billete no válido")
    else:
        falta = falta - billete

        if falta > 0:
            print("Faltan", falta, "€")

if falta < 0:
    cambio = 0 - falta
else:
    cambio = 0

print("Cambio:", cambio, "€")