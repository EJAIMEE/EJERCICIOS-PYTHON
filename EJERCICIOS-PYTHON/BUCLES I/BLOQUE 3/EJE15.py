"""
Jaime Escriche Garcia
27/10/26
"""

cont_buena = "smx2026"
contraseña = 0
intentos = 0

while contraseña != cont_buena and intentos < 3:
    contraseña = input("Contraseña: ")

    if contraseña == cont_buena:
        print("Acceso concedido")
    else:
        intentos = intentos + 1
        
    if intentos == 3 and contraseña != cont_buena:
        print("Acceso bloqueado")
    else:
        print("Contraseña incorrecta. Te qeudan", 3 - intentos, "intentos")

