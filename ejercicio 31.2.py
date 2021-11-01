while True:
    try:
        km =5000*float(input("Ingrese los kilimetros a recorrer: "))
        dias = float(input("Ingrese los dias de estancia: "))
        if km<100000:
            print("se le cobra lo minimo 100000 pesos")
        else:
            if dias>7:
                print("Se cobrarán ",km-(km*0.15))
            else:
                print("Se cobrarán ",km)
        break
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue

