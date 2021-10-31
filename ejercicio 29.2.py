mayor = 0
menor = 0
for x in range(3):
    while True:
        try:
            num = float(input("numero"+str(x+1)+" = "))
            if x == 0:
                mayor = num
                menor = num
            elif mayor<num:
                mayor = num
            elif menor>num:
                menor = num
            break
        except:
            print("solo numeros")
            continue
print("El numero mayor es",mayor,"y el numero menor es",menor)

