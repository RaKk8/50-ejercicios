print("Para finalizar presione 'ENTER' sin digitar ningún numero")
mayor100 = 0
menor100 = 0
while True:
    try:
        n = input("Ingrese los numeros ")
        if not bool(n):
            break
        if int(n)>100:
            mayor100 += 1
        else:
            menor100 += 1
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
print("La cantidad de numeros ingresados mayores a 100 fueron",mayor100)
print("La cantidad de numeros ingresados menores a 100 fueron",menor100)