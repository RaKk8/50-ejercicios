print("Ingrese un dia de la semana utilizando valores numericos entre 1 y 7")
numeros = [":c","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
while True:
    try:
        print(numeros[int(input("Numero: "))])
        break
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
    except IndexError:
        print("Solo valores entre 1 y 7")

