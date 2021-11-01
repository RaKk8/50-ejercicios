print("Ingrese un numero entre 0 y 10")
numeros = ["Cero","Uno","Dos","Tres","Cuatro","Cinco","Seis","Siete","Ocho","Nueve","Diez"]
while True:
    try:
        print(numeros[int(input("Numero: "))])
        break
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
    except IndexError:
        print("Unicamente numeros entre 0 y 10")
