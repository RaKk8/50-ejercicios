while True:
    try:
        lado = float(input("Ingrese un lado del hexagono: "))
        altura = float(input("Ingrese la altura del hexagono: "))
    except:
        print("Por favor ingrese unicamente valores numericos")
        continue
    print("El área del hexagono es ",((lado*6)*altura)/2)
    break

