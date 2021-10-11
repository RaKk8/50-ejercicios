while True:
    try:
        altura = float(input("Ingrese la altura desde la cual caerá el objeto: "))
    except:
        print("Por favor ingrese unicamente valores numericos")
        continue
    print("El tiempo de caida será de: ",((altura*2)/9.8)**0.5)
    break
