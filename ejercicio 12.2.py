while True:
    try:
        tiempo = float(input("Ingrese el tiempo en segundos: "))
        aceleracion = float(input("Ingrese la aceleración en m/s2: "))
        velocidadi = float(input("Ingrese la velocidad inicial m/seg: "))
        velocidadf = float(input("Ingrese la velocidad final m/seg: "))
    except:
        print("Por favor ingrese unicamente valores numericos")
        continue
    print("La distancia recorrida es",(velocidadi*tiempo)+((aceleracion*(tiempo**2))/2),"metros")
    break

