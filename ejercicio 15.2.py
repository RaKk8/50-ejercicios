while True:
    try:
        x1 = int(input("x1 = "))
        y1 = int(input("y1 = "))
        x2 = int(input("x2 = "))
        y2 = int(input("y2 = "))
    except:
        print("Por favor ingrese unicamente valores numericos")
        continue
    cx = 0
    if x1<x2:
        for x in range(x1,x2):
            cx +=1
    if x1>x2:
        for x in range(x2,x1):
            cx +=1
    cy = 0
    if y1<y2:
        for x in range(y1,y2):
            cy +=1
    if y1>y2:
        for x in range(y2,y1):
            cy +=1
    print("La distancia que hay en x es",cx,"y la distancia que hay en y es",cy)
    break

