while True:
    try:
        num1 = float(input("numero 1 = "))
        num2 = float(input("numero 2 = "))
        num3 = float(input("numero 3 = "))
        if num1+num2>num3:
            print("La suma del primero y segundo es mayor que el tercero")
        else:
            print("La suma del primero y seguno NO es mayor que el tercero")
        break
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue

