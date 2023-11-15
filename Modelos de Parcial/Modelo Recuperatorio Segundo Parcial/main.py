import negocio
import utils

while True:
    utils.imprimirMenu()
    user = int(input('Escoja una opcion: '))
    if user == 1:
        negocio.ingresarProducto()
    elif user == 2:
        negocio.ingresarCliente()
    elif user == 3:
        negocio.venta()
    elif user == 4:
        print('opcion')
    elif user == 5:
        print('opcion')
    elif user == 6:
        print('opcion')
    elif user == 7:
        print('opcion')
    elif user == 8:
        print('Gracias por utilizar mi sistema')
        break
    else:
        print('*** INGRESE UN VALOR VALIDO ***')