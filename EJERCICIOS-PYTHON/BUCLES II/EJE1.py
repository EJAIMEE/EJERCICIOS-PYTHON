"""
Jaime Escriche Garcia
29/10/26
"""

total_sin_iva = 0
iva_total = 0
a = 0.21
b = 0.10
c = 0.04
producto = ""

while producto != "fin":
    producto = input("Producto: ")
    
    if producto == "fin":
        break
    
    precio = float(input("Precio: "))
    tipo = input("Tipo (A/B/C): ")

    if tipo == "A":
        iva_producto = precio * a
    elif tipo == "B":
        iva_producto = precio * b
    elif tipo == "C":
        iva_producto = precio * c

    total_sin_iva = total_sin_iva + precio
    iva_total = iva_total + iva_producto

total = total_sin_iva + iva_total 

print("Total sin IVA:", round(total_sin_iva, 2), "€")
print("IVA:", round(iva_total, 2), "€")
print("Total a pagar:", round(total, 2), "€")