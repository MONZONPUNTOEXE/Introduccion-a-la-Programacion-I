import utils
import negocio

user = 0

print("\n ***** Bienvenido, ¿que desea hacer? *****")
while user != 3:
    utils.imprimirMenu()
    user = int(input("Ingrese un numero para acceder al menú "))
    if user == 1:
        negocio.sistemaAlfajores();
    if user == 2:
        print(user)
    if user == 3:
        print("Adios");
    else: 
        print("----- Opcion incorrecta ------ \n ------ Vuelva a intentarlo -----")

