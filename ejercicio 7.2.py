while True:
    try:
        radio = float(input("Ingrese el diametro del circulo: "))
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
    print("El perimetro es",6.283*radio,"y el Área es",3.1416*radio**2)
    break
