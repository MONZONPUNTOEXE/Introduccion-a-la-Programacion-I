import menu
import funciones

user = 0
while user != 3:
    # hacer la llamada para imprimir el menú
    menu.imprimirMenu()
    # Entrada de datos para que ingrese el usuario
    user = int(input("Ingrese su numero: "))
    if user == 1:
        # llamada de función para ingresar empleados
        funciones.ingresarEmpleados()
    if user == 2:
        # llamada de función para buscar empleados
        funciones.buscarEmpleado()
    if user == 3:
        # Mensaje de despedida
        print("Gracias por usar mi programa xD")