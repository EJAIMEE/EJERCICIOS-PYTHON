gg_consumidas = float(input("Ingresa las gigas consumidas: "))

if gg_consumidas <= 5:
    print("el importe de la factura son: 3 €")
elif gg_consumidas <= 10:
    importe = 3 +(gg_consumidas - 5)* 1.5
    print("El importe de la factura son:", importe, "€")
elif gg_consumidas > 10:
    importe_2 = 3 + (5 * 1.5) + (gg_consumidas - 10) * 1
    print("El importe de la factura son:", importe_2, "€")

