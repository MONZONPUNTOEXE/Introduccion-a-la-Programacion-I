import menu
import funciones

user = 0
while user != 3:
    menu.imprimirMenu()
    user = int(input("Ingrese su numero: "))
    if user == 1:
        funciones.ingresarEmpleados()
    if user == 2:
        funciones.buscarEmpleado()
    if user == 3:
        print("Gracias por usar mi programa xD")