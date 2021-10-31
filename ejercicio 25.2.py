while True:
    try:
        num = int(input("Ingrese un numero "))
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
    if num>=10:
        print(num*3)
    else:
        print(num/4)

