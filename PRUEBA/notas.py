nota = int(input("Dime que nota has sacado: "))
if nota < 5:
    print("Has sacado un insuficiente")
elif nota < 7:
    print("Has sacado un bien")
elif nota <=7:
    print("Has sacado un notable")
elif nota >=9:
    print("Has sacado un sobresaliente")