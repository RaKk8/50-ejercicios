while True:
    try:
        tiempo = float(input("Ingrese el tiempo en segundos: "))
        aceleracion = float(input("Ingrese la aceleración en m/s2: "))
        velocidadi = float(input("Ingrese la velocidad inicial m/seg: "))
    except:
        print("Por favor ingrese unicamente valores numericos")
        continue
    print("La velocidad final es",(velocidadi)+(aceleracion*tiempo),"m/s")
    break

