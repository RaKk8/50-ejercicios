while True:
    try:
        num1 = float(input("Ingrese el numero 1 = "))
        num2 = float(input("Ingrese el numero 2 = "))
        if num1>num2:
            print(num1,"es mayor que",num2)
            break
        else:
            print(num2,"es mayor que",num1)
            break
    except:
        print("Por favor ingrese unicamente valores numericos")
        continue

