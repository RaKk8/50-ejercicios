while True:
    try:
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
        num3 = int(input("num3: "))
        if num1>num2>num3:
            print("Los numeros estan disminuyendo")
        elif num1<num2<num3:
            print("Los numeros estan incrementando")
        else:
            print("Los numeros no incrementan ni disminuyen")
        break
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue

