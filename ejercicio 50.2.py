promedioimpares= []
promediopares = []
try:
    for x in range(1,int(input("Ingrese cuantos numeros desea promediar: "))+1):
        while True:
            try:
                n = int(input("num"+str(x)+": "))
                if n%2:
                    promedioimpares.append(n)
                else:
                    promediopares.append(n)
                break
            except ValueError:
                print("Por favor ingrese unicamente valores numericos")
                continue
except:
    print("solo numeros")
print("El promedio de los numeros pares es: ",sum(promediopares)/len(promediopares))
print("El promedio de los numeros impares es: ",sum(promedioimpares)/len(promedioimpares))

