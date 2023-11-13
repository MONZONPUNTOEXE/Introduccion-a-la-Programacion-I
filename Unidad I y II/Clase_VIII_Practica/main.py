import utils
import negocio

bucle = 0

while bucle == 0:
    utils.imprimirMenu()
    user = int(input('Eliga una opción del menú, ingresando un número:\n'))
    if user == 1:
        print('Opcion 1')
    if user == 2:
        print('Opcion 2')
    if user == 3:
        print('Opcion 3')
    if user == 4:
        print('Opcion 4')
        #salir
        bucle = 1
    else:
        print('Opcion incorrecta vuelva a intentarlo')