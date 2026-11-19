"""
Jaime Escriche Garcia
27/10/26
"""

con_buena = "smx2026"
contraseña = 0

while contraseña != con_buena:
    contraseña = input("Contraseña: ")
    print("Contraseña incorrecta")

    if contraseña == con_buena:
        print("Acceso concedido")

