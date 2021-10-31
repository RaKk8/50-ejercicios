notas = []
for x in range(5):
    while True:
        try:
            num=float(input("Nota "+str(x+1)+"= "))
            if num>=0 and num<=5:
                notas.append(num)
                break
            else:
                print("Ingrese unicamente notas entre 0 y 5")
                continue
        except:
            print("Por favor ingrese unicamente valores numericos")
            continue
notaf = ((notas[0]*3)+(notas[1]*4)+(notas[2]*3)+(notas[3]*6)+(notas[4]*4))*0.05
if notaf<2:
    print("No puede habilitar")
elif notaf<3:
    print("Reprobo")
elif notaf>4.5:
    print("Aprobo, felicidades tiene muy buena nota")
else:
    print("Aprobo, mediocre")

