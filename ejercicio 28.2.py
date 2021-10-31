print("La maxima base posible para este programa es nonaria = 9")
def binario():
    total = 0
    for x in range(len(numero)):
        total+=(int(numero[x])*(2**x))
    return total
def ternario():
    total = 0
    for x in range(len(numero)):
        total += int(numero[x]) * (3 ** x)
    return total
def cuaternario():
    total = 0
    for x in range(len(numero)):
        total += int(numero[x]) * (4 ** x)
    return total

def quinario():
    total = 0
    for x in range(len(numero)):
        total += int(numero[x]) * (5 ** x)
    return total

def senario():
    total = 0
    for x in range(len(numero)):
        total += int(numero[x]) * (6 ** x)
    return total

def heptal():
    total = 0
    for x in range(len(numero)):
        total += int(numero[x]) * (7 ** x)
    return total

def octal():
    total = 0
    for x in range(len(numero)):
        total += int(numero[x]) * (8 ** x)
    return total

def nonario():
    total = 0
    for x in range(len(numero)):
        total += int(numero[x]) * (9 ** x)
    return total

numero = []
while True:
    try:
        num = input("Ingrese un número ")
        int(num)
        base = int(input("El numero esta en base = "))
        if base == 2 and ("2" in num or "3" in num or "4" in num or "5" in num or "6" in num or "7" in num or "8" in num or "9" in num):
            print("la base no es valida")
            continue
        if base == 3 and ("3" in num or "4" in num or "5" in num or "6" in num or "7" in num or "8" in num or "9" in num):
            print("la base no es valida")
            continue
        if base == 4 and ("4" in num or "5" in num or "6" in num or "7" in num or "8" in num or "9" in num):
            print("la base no es valida")
            continue
        if base == 5 and ("5" in num or "6" in num or "7" in num or "8" in num or "9" in num):
            print("la base no es valida")
            continue
        if base == 6 and ("6" in num or "7" in num or "8" in num or "9" in num):
            print("la base no es valida")
            continue
        if base == 7 and ("7" in num or "8" in num or "9" in num):
            print("la base no es valida")
            continue
        if base == 8 and ("8" in num or "9" in num):
            print("la base no es valida")
            continue
        if base == 9 and ("9" in num):
            print("la base no es valida")
            continue
        if 2>base or 9<base:
            print("la base no es valida")
            continue
    except:
        print("Por favor ingrese unicamente valores numericos")
        continue
    for x in num:
        numero.append(x)
    if base == 2:
        print("El numero en base decimal es",binario())
    if base == 3:
        print("El numero en base decimal es",ternario())
    if base == 4:
        print("El numero en base decimal es",cuaternario())
    if base == 5:
        print("El numero en base decimal es",quinario())
    if base == 6:
        print("El numero en base decimal es",senario())
    if base == 7:
        print("El numero en base decimal es",heptal())
    if base == 8:
        print("El numero en base decimal es",octal())
    if base == 9:
        print("El numero en base decimal es",nonario())



