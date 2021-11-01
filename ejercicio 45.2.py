while True:
    try:
        n = int(input("Ingrese los numeros a imprimir "))
        break
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
for x in range(1,n,2):
    print(x, end=" /{}/ ".format(x+1))
if n%2:
    print(n,end="")


