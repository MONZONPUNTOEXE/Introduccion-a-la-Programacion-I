import utils
import negocio

while True:
    utils.imprimirMenu()
    user = int(input("Ingrese la venta que desea realizar\nIngrese 7 para salir"))

    if user == 1:
        negocio.cargarCliente()
    elif user == 2:
        negocio.cargarProducto()        
    elif user == 3:
        negocio.ventaFinal()
    elif user == 4:
        negocio.ventaCliente()
    elif user == 5:
         negocio.listarClientes()
    elif user == 6:
         negocio.listarProductos()        
    elif user == 7:
        negocio.buscarVentaCliente()
    elif user == 8:
        negocio.listarProductosSort()
    elif user == 9:
        break
        # salir