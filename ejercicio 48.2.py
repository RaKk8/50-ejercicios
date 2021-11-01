promedio = 0
for x in range(1,11):
    while True:
        try:
            promedio += int(input("num"+str(x)+": "))
            break
        except ValueError:
            print("Por favor ingrese unicamente valores numericos")
            continue
print("El promdeio es igual a =",promedio/10)

