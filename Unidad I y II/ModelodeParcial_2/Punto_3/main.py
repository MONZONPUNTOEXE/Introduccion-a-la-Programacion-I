# Dependencias
import negocio
import utils

# Declaracion de variables
user = 0


# Este codigo lo deje comentado porque.
# Funciona para limitar al usuario a que primero:
# Ingrese los sublotes y luego pueda elegir ver los maximos. 
# Pero si o si debe ingresar los sublotes, para poder ver los maximos

# while user != 2:
#     utils.mostrarMenu1()
#     user = int(input("Que desea hacer ?\n"))
#     if user == 1:
#         negocio.ejercicioDeSublotes()
#         utils.mostrarMenu2()
#         while user != 2:
#             user = int(input("Que desea hacer ?\n"))
#             if user == 1:
#                 negocio.valorMaximo()
#             if user == 2:
#                 print("Adios!")
#     if user == 2:
#         print("Adios!")
#     else: print("*******Opcion Incorrecta***********\n*******Vuelva a intentarlo***********")


# ---------------------------------------------------------------------------

# Este es el codigo actual. 
# El usuario puede elegir ingresar los sublotes y ver los maximos.
# El problema es que si elige ver primero los maximos de los sublotes antes que ingresar los sublotes
# va a tirar error porque. La variable "maximo_sublote" de la funcion "valorMaximo()" esta vacía.
# y esto es logíco porque no ingresamos los sublotes, por lo tanto no va a tener que numeros comparar.   


while user != 3:
    utils.mostrarMenu1()
    user = int(input("Que desea hacer ?\n"))
    if user == 1:
        negocio.ejercicioDeSublotes()
    elif user == 2:
        negocio.valorMaximo()
    elif user == 3:
        print("Adios!")
    else: print("*******Opcion Incorrecta***********\n*******Vuelva a intentarlo***********")





