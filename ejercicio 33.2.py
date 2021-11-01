while True:
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        c = int(input("c = "))
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
    try:
        print("las soluciones son",(-b+(((b**2)-(4*a*c))**(0.5)))/(a*2),(-b-((b**2-(4*a*c))**(0.5)))/a*2)
        break
    except:
        print("Solucion no valida")
        break

