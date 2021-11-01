print("Para finalizar presione 'ENTER' sin digitar ningún numero")
nump = 0
numn = 0
pares = 0
impa = 0
mlocho = 0
while True:
    try:
        n = input("Ingrese los numeros: ")
        if not bool(n):
            break
        if int(n)>0:
            nump += 1
        else:
            numn += 1
        if not int(n)%2:
            pares += 1
        else:
            impa += 1
        if not int(n)%8:
            mlocho += 1
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
print("La cantidad de numeros positivos es",nump)
print("La cantidad de numeros negativos es",numn)
print("La cantidad de numeros pares es",pares)
print("La cantidad de numeros impares es",impa)
print("La cantidad de numeros multiplos de 8 es",mlocho)

