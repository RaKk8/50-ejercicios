while True:
    try:
        numero = int(input("numero = "))
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
    print("El cuadrado del numero",numero,"es",numero**2)
    break