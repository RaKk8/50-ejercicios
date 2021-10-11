while True:
    try:
        numero1 = int(input("El primer numero es = "))
        numero2 = int(input("El segundo numero es = "))
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
    print("la suma de",numero2,"+",numero1,"=",numero1+numero2)
    break


