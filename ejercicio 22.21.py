while True:
    try:
        num = float (input("Ingrese un numero: "))
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
    if num<0:
        print("El numero es negativo")
    else:
        print("el numero es positivo")

