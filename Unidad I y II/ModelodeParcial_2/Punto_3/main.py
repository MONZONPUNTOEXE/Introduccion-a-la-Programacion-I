import negocio
import utils


user = 0

while user != 2:
    utils.mostrarMenu1()
    user = int(input("Que desea hacer ?\n"))
    if user == 1:
        negocio.ejercicioDeSublotes()
        utils.mostrarMenu2()
        while user != 2:
            user = int(input("Que desea hacer ?\n"))
            if user == 1:
                negocio.valorMaximo()
            if user == 2:
                print("Adios!")
    if user == 2:
        print("Adios!")
    else: print("*******Opcion Incorrecta***********\n*******Vuelva a intentarlo***********")


