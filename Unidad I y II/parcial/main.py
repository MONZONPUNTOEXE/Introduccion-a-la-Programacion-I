## Main va a tener las llamadas a las funciones

## con import es traer toda la funcionalidad de menu

import utils
import negocio

numero = 0

negocio.saludar()
utils.imprimirMenu()

while numero != 4:
    negocio.IngreseUnNumero()
    if numero == 1:
        print("ingresar un numero")
    elif numero == 2:
        print("dos")    
    elif numero == 3:
        print("tres");
    elif numero == 4:
        print("Gracias, vuelva pronto");
    