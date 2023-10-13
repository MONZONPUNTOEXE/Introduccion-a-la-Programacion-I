import negocio
import utils

while True:
    utils.imprimirMenu()
    user = int(input("Ingrese la opción que desea realizar:\n"))
    if user == 1:
        negocio.IngresarSueldo()
    elif user == 2:
        negocio.cargaYBusquedaDeNumeros()        
    elif user == 3:
        while True:
            utils.imprimirMenuSueldos()
            user = int(input("Ingrese la opción que desea realizar: "))
            if user == 1:
                negocio.ingresarEmpleado()                
            elif user == 2:
                negocio.buscarEmpleado()                
            elif user == 3:
                print("Gracias, vuelva pronto")
                break
            elif user > 3 or user < 0:
                print("La opción es incorrecta, Vuelva a intentarlo")
    elif user == 4:
        negocio.listaInvertida()
    elif user == 5:
        while True:
            utils.imprimirMenuTiendita()
            user = int(input("Ingrese la opción que desea realizar: "))
            if user == 1:
                negocio.agregarProducto()               
            elif user == 2:
                negocio.buscarProducto()                
            elif user == 3:
                negocio.modificarProducto()                
            elif user == 4:
                negocio.cantidadVendida()                
            elif user == 5:
                negocio.inventarioActual()                
            elif user == 6:
                print("Gracias, asta la procsima")
                break
            elif user > 3 or user < 0:
                print("\n\n\n*** ERROR: LA OPCIÓN ES INCORRECTA, VUELVA A INTENTARLO ****")
    elif user == 6:
        print("Gracias por usar mi sistema")
        break
    elif user > 6 or user < 0:
        print("\n\n\n*** ERROR: LA OPCIÓN ES INCORRECTA, VUELVA A INTENTARLO ****")