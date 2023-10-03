import menu
def ingresarEmpleados():
# Ingresar por teclado "n" empleados, codigo de 4 digitos, nombre y apellido, calcular el sueldo bruto
# Para el sueldo bruto basico de 80mil, ingresar horas adicionales, precio de esas horas de 3mil
    global listacodigo
    global listanombre
    global listasueldo
    global listahoras
    listacodigo = []
    listanombre = []
    listasueldo = []
    listahoras = []


    sueldo_basico = 80000
    valor_por_hora = 3000


    user = "y"
    while user == "y":
        listacodigo.append(input("Ingrese el codigo del empleado: "))
        print(listacodigo)

        listanombre.append(input("Ingrese el nombre y apellido del empleado: "))
        print(listanombre)

        listahoras.append(int(input("Ingrese el horas del empleado: ")))
        print(listahoras)

        for i in range(len(listahoras)):
            listasueldo.append((listahoras[i]*valor_por_hora) + sueldo_basico)
            print(listasueldo)
        # listasueldo.append(input("Ingrese el sueldo del empleado: "))
        # print(listasueldo)

        user = input("Desea ingresar un empleado nuevo? y/n: ")

def buscarEmpleado():
    buscar = input("Ingrese el codigo que quiere buscar: ")

    for i in range(len(listacodigo)):
        if buscar == listacodigo[i]:
            print(listacodigo[i])
            print(listanombre[i])
            print(listasueldo[i])
            print(listahoras[i])