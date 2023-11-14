import negocio
import utils

bucle = True

while bucle:
    utils.imprimirMenu()
    user = int(input('ingrese la opcion deseada: '))

    if user == 1:
        negocio.maximos()
    if user == 2:
        negocio.sublotes()
    if user == 3:
        print('Hasta al proxima !')
        bucle = False
