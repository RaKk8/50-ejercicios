while True:
    try:
        ano = int(input("Ingrese un año "))
        break
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
print("Es bisiesto" if not ano % 4 and (ano % 100 or  not ano % 400) else "No es bisiesto")

