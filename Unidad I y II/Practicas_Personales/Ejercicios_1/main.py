import utils
import funciones_practicas

user = 0

while user != 7:
    utils.imprimirMenu()
    user = int(input("Seleccione un número:"))
    if user == 1:
        funciones_practicas.escribirHolaMundo();
    elif user == 2:
        funciones_practicas.numeros1Al5();
    elif user == 3:
        funciones_practicas.repeticionDeA();
    elif user == 4:
        funciones_practicas.triangulo();
    elif user == 5:
        funciones_practicas.nameAndLastName();
    elif user == 6:
        funciones_practicas.operacion();
    elif user == 7:
        print("Adios")
    else: print("******* Ingrese un dato valido\nVuelva a intentarlo ********")

