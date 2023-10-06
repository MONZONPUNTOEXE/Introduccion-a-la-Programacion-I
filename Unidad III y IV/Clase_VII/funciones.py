# Ingresar por teclado "n" empleados, codigo de 4 digitos, nombre y apellido, calcular el sueldo bruto
# Para el sueldo bruto basico de 80mil, ingresar horas adicionales, precio de esas horas de 3mil


# Función para ingresar los datos de los empleados
def ingresarEmpleados():
    # Declaramos las variables globales para reutilizarlas
    # fuera de esta la funcion
    global listacodigo
    global listanombre
    global listasueldo
    global listahoras
    
    # Inicializamos las variables
    listacodigo = []
    listanombre = []
    listasueldo = []
    listahoras = []


    sueldo_basico = 80000
    valor_por_hora = 3000

    # Solicitamos al usuario que ingrese los datos de los empleados
    user = "y"
    while user == "y":
        # Hacemos la entrada de datos para agregarselas a las listas
        listacodigo.append(input("Ingrese el codigo del empleado: "))
        print(listacodigo)
        listanombre.append(input("Ingrese el nombre y apellido del empleado: "))
        print(listanombre)
        # Calculamos el sueldo bruto del empleado
        horas = int(input("Ingrese el horas del empleado: "))
        total_sueldo = sueldo_basico + (valor_por_hora * horas)
        listahoras.append(horas)
        print(listahoras)
        listasueldo.append(total_sueldo)
        print(listasueldo)        

        # Solicitamos al usuario si desea ingresar otro empleado
        user = input("Desea ingresar un empleado nuevo? y/n: ")


# Función para buscar un empleado por código
def buscarEmpleado():
    # Declaramos las variables donde el usuario va a buscar
    buscar = input("Ingrese el codigo que quiere buscar: ")

    for i in range(len(listacodigo)):
        if buscar == listacodigo[i]:
            # Imprimimos los datos del empleado
            print(listacodigo[i])
            print(listanombre[i])
            print(listasueldo[i])
            print(listahoras[i])
