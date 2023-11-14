import negocio
# import menu
while True:
    #menu.imprimirMenu()
    user = int(input("Ingrese el numero que desea realizar"))
    print("hola")
    if user == 1:
        negocio.gestionDeEmpleados()
        print(negocio.codigo_empleado)        
        print(negocio.nombre_empleado)        
        print(negocio.sueldo_empleado)

        search = int(input("Ingrese el codigo del empleado que desea buscar: "))
        def busquedaDeEmpleados(codigo):
            for i in range(0,len(negocio.codigo_empleado)):
                if codigo == negocio.codigo_empleado[i]:
                    return i
            return -1
        
        resultado = busquedaDeEmpleados(search)
        if resultado == -1:
            print("No se encontro su empleado")
        elif resultado >= 0:  
            print("Su empleados se encontro exitosamente")
            print("Su empleado es:", negocio.nombre_empleado)
            print("Su sueldo es:", negocio.sueldo_empleado)
        

    if user == 2:
        print("Elija una opcion correcta2")
    if user == 3:
        print("Elija una opcion correcta34")
    if user == 4:
        print("Elija una opcion correcta4")
    if user == 5:
        print("Elija una opcion correcta5")
    if user == 6:
        print("Elija una opcion correcta6")
    if user == 7:
        print("Elija una opcion correcta6")
        break

  
