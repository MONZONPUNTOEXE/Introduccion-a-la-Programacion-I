import utils
import negocio

while True: 
    utils.imprimirMenu()
    user = int(input('Ingrese la opcion que desea realizar: '))
    if user == 1:
        negocio.cargarCliente()
    if user == 2:
        negocio.cargarProducto()
    if user == 3:
        negocio.cargarVenta()
    if user == 4:
        print('no realizado')
    if user == 5:
        print('no realizado')
    if user == 6:
        print('no realizado')
    if user == 7:
        print('no realizado')
    if user == 8:
        print('no realizado')
    if user == 9:
        print('no realizado')
    if user == 10:
        print('no realizado')
    if user == 11:
        print('opcion')
    if user == 12:
        print('Gracias por utilizar el sistema !')
        break