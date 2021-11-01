while True:
    try:
        n = int(input("Ingrese un numero positivo: "))
        if n<0:
            print("El numero es negativo")
            continue
        else:
            print(n)
            break
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue

