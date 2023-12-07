import main

finalizar = True
while finalizar:
    user  = int(input('Elija una opcion: '))
    if user == 1:
        main.cargarCliente()
    if user == 2:
        main.cargarProducto()
    if user == 3:
        main.cargarVenta()
    if (input("Desea finalizar ? y/n : ") == "y"):
        finalizar = False
    # end if
# end while