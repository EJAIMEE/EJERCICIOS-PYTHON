"""
Jaime Escriche Garcia
17/11/26
"""

fecha = input("Fecha (dd/mm/aaaa): ")

dia = int(fecha[0:2])
mes = int(fecha[3:5])
año = int(fecha[6:10])

match mes:
    case 1:
        n_mes = "Enero"
    case 2:
        n_mes = "Febrero"
    case 3:
        n_mes = "Marzo"
    case 4:
        n_mes = "Abril"
    case 5:
        n_mes = "Mayo"
    case 6:
        n_mes = "Junio"
    case 7:
        n_mes = "Julio"
    case 8:
        n_mes = "Agosto"
    case 9:
        n_mes = "Septiembre"
    case 10:
        n_mes = "Octubre"
    case 11:
        n_mes = "Noviembre"
    case 12:
        n_mes = "Diciembre"
    case _:
        n_mes = "El mes", mes, "no existe"

if n_mes == ("El mes", mes, "no existe"):
    print("El mes", mes, "no existe")
else:
    print("{} de {} de {}".format(dia, n_mes, año))