"""
Jaime Escriche Garcia
¿Que numeros son pares?
"""

# Versión "While"
i = 0
while i < 51:
    if i % 2 == 0:
        print(i, "Es par")
    i += 1

# Versión "for"
for i in range(51):
    if i % 2 == 0:
        print(i)
