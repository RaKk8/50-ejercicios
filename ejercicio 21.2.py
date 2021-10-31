while True:
    try:
        num = int(input("Ingrese un numero "))
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
    if num%2 == 0:
        print("el numero es par")
    else:
        print("el numer es impar")


