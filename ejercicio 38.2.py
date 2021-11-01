while True:
    try:
        if 0<=int(input("num1: "))<=5 and 0<=int(input("num2: "))<=5:
            print("True")
        else:
            print("False")
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
