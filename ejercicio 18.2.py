while True:
    try:
        segundos = int(input("segundos = "))
    except:
        print("Por favor ingrese unicamente valores numericos")
        continue
    print("{}:{}:{}".format(segundos//3600,(segundos%3600)//60,(segundos%3600)%60))
    break

