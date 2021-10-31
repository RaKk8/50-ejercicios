while True:
    try:
        segundos = int(input("Segundos = "))
    except:
        print("Por favor ingrese unicamente valores numericos")
        continue
    print(segundos,"La conversión es",segundos/3600)
    break

