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
        negocio.ordenarVentas()
    if user == 5:
        negocio.promedioVentas()
    if user == 6:
        negocio.clientesSinObra()
    if user == 7:
        negocio.ventaValorMaximo()
    if user == 8:
        negocio.maximos()
    if user == 9:
        print('Gracias por utilizar el sistema !')
        break