while True:
    try:
        num = float(input("Ingrese un numero "))
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
    if num<0 and num%2 == 0:
        print("El numero es negativo, y es par")
    elif num>0 and num%2 == 0:
        print("El numero es positivo y es par")
    elif num<0:
        print("El numero es negativo y es impar")
    else:
        print("El numero es positivo y es impar")
    break
