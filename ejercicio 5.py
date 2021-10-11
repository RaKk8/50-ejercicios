entero = ""
decimal =""
while True:
    try:
        numero = input("Ingrese un número decimal // ")
        float(numero)
    except ValueError:
        print("Por favor ingrese unicamente valores numericos o utilice un punto en lugar de una coma")
        continue
    coma = False
    for x in numero:
        if coma:
            decimal +=x
        elif x == ".":
            coma = True
        else:
            entero +=x
    break
print("la parte entera es",entero,)
print("la parte decimal es",decimal)

