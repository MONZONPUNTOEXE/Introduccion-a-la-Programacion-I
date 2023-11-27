import negocio
import utils

while True:
    utils.imprimirMenu()
    user = int(input('Ingrese una opcion: '))
    if user == 1:
        negocio.clienteNuevo()
    if user == 2:
        negocio.productoNuevo()
    if user == 3:
        negocio.ventaNueva()
    if user == 4:        
        negocio.listaOrdenada()
    if user == 5:
        negocio.listarVentaXCliente()
    if user == 6:
        print("No realizado")
        #negocio.ventaNueva()
    if user == 7:
        negocio.ventaMaxima()
    if user == 8:
       print("No realizado")
        #negocio.ventaNueva()
    if user == 9:
        print("Gracias por usar mi sistema")
        break
        