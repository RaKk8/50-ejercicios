while True:
    try:
        num1 = int(input("num1 = "))
        num2 = int(input("num2 = "))
        num3 = int(input("num3 = "))
        if num1==num2 or num1==num3 or num2==num3:
            print("Hay dos o mas numeros iguales")
        else:
            print("Ningún numero se repite")
        break
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue

