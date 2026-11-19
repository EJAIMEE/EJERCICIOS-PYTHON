numero = 6
'''
Autor: JAIME
VERSION: 1.0
'''
print("=== BIENVENIDO AL RETO DE EL GUARDIÁN ===")
print("Si el puente quieres cruzar, un numero tendras que adivinar entre el 1 y el 10")
'''
ahora en el siguiente parrafo tendras que poner un número
'''
respuesta = int(input("Introduce el numero: "))
if not(respuesta == numero):
    print("ERROR!!!, no puedes pasar.")
else:
    print("CORRECTO!!!, puedes pasar.")
