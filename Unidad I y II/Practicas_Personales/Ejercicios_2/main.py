import utils
import negocio

user = 0
while user != 5:
    utils.imprimirMenu()
    user = int(input("Ingrese la opcion que desea realizar: "));
    if user == 1:
        negocio.calcularPromedio()
    elif user == 2:
        print("none")
    elif user == 3:
        print("none")
    elif user == 4:
        print("none")
    elif user == 5:
        print("Gracias por utilizar el programa")
        print("Adios")
        user = 5
    else: print("***** Incorrecto *****\nIngrese una opción correcta")