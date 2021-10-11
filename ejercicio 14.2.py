while True:
    try:
        masa = float(input("Ingrese la masa en Kg: "))
    except:
        print("Por favor ingrese unicamente valores numericos")
        continue
    print("La energia cinetica es",(masa*(299792458**2))/2,"J")
    break


