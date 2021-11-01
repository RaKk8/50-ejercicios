lista = {"Rodolfo":"1234"}
nombre = input("USUARIO: ")
contraseña = input("CONTRASEÑA ")
try:
    if lista[nombre] == contraseña:
        print("aceptado")
    else:
        print("La contraseña es incorrecta")
except:
    print("El nombre de usuario no existe")
