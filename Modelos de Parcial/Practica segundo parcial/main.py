import negocio
import utils

noFinalizado = True
while noFinalizado:
    print("Bienvenido")
    utils.imprimirMenu()    
    user = int(input("Ingrese la opción: "))
    if user == 1:        
        negocio.cargarProducto()
    if user == 2:
        negocio.cargarCliente()
    if user == 3:
        negocio.cargarVenta()
    if user == 4:
        negocio.ventasOrdenadas()
    if user == 5:
        print("No realizado")
    if user == 6:
        print("No realizado")
    if user == 7:
        print("No realizado")
    if user == 8:
        print("No realizado")
    if user == 9:
        noFinalizado = False
