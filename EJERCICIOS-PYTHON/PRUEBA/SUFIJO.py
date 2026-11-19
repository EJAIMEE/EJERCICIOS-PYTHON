"""
Jaime Escriche Garcia
13/11/26
"""
# Version While

# Version for

c1 = input("Escribe una cadena de texto: ")
c2 = input("Escribe otra cadena de texto: ")

es_sufijo = True

for i in range (0, -1*len(c2), 1):
    if c1[-i] != c2[-i]:
        es_sufijo = False
        break

if es_sufijo == True:
    print("Es Sufijo")
else:
    print("No es Sufijo")

    