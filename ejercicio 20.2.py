while True:
    try:
        num = (input("ingrese un numero de 4 digitos "))
        int(num)
        if len(num) != 4:
            print("solo numeros de 4 digitos")
            continue
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
    num = list(num)
    num.reverse()
    for x in range(len(num)):
        print(num[x], end="")
    break