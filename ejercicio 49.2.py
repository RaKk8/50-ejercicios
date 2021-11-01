promedio = []
try:
    for x in range(1,int(input("Digite la cantidad de numeros a promediar "))+1):
        while True:
            try:
                promedio.append(int(input("num"+str(x)+": ")))
                break
            except ValueError:
                print("Por favor ingrese unicamente valores numericos")
                continue
except:
    print("Por favor ingrese unicamente valores numericos")
print("El promdeio es igual a:",sum(promedio)/len(promedio))

