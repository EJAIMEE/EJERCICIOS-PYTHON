"""
Jaime Escriche Garcia
29/10/26
"""

ip = ""
primer_octeto = 0
octetos_correctos = 0

for numero_octeto in range(1, 5):
    octeto = int(input("Octeto " + str(numero_octeto) + ": "))

    if octeto < 0 or octeto > 255:
        print("IP no válida: el octeto", numero_octeto, "vale", octeto)
        break

    if numero_octeto == 1:
        primer_octeto = octeto

    if numero_octeto > 1:
        ip = ip + "."

    ip = ip + str(octeto)
    octetos_correctos = octetos_correctos + 1

if octetos_correctos == 4:
    if primer_octeto >= 1 and primer_octeto <= 126:
        clase = "A"

    elif primer_octeto == 127:
        clase = "Loopback"

    elif primer_octeto >= 128 and primer_octeto <= 191:
        clase = "B"

    elif primer_octeto >= 192 and primer_octeto <= 223:
        clase = "C"
    else:
        clase = "Otra"

    print("IP:", ip, "Clase:", clase)