import negocio
import utils

finalizar = True
while finalizar:
    utils.imprimirMenu()
    user = int(input('Ingrese la opcion'))
    if user == 1:
        negocio.cargarProducto()
    if user == 2:
        negocio.venta()
    if user == 3:
        negocio.ventaMayor()
    if user == 4:
        negocio.listarVentas()
    if user == 5:
        listarUltimasVentas()
    if user == 6:
        negocio.ordenar()
    if user == 7:
        finalizar = False
