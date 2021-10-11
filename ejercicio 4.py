while True:
    try:
        numero1 = int(input("Primer número: "))
        numero2 = int(input("Segundo número: "))
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
    print("suma =",numero1+numero2)
    print("resta =",numero1-numero2)
    print("multiplicacion =",numero1*numero2)
    print("divicion =",numero1//numero2)
    print("residuo =",numero1%numero2)
    break

