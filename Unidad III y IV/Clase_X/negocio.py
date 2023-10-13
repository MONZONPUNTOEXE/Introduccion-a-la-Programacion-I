# Ejercicio 1
def IngresarSueldo():
    sueldosEmpleados = []
    sueldosSuperiores = []
    ciclo = True

    while ciclo:
        user = int(input("Ingrese sueldo:\n"))
        if user >= 6000:
            sueldosSuperiores.append(user)
        else:
            sueldosEmpleados.append(user)

        pregunta = input("Desea ingresar un nuevo sueldo ? y/n ")
        if pregunta == "n":
            ciclo = False

    print("sueldo:\n", sueldosEmpleados)
    print("sueldo superior:\n", sueldosSuperiores)

# Ejercicio 2:
def cargaYBusquedaDeNumeros():
    ciclo = True
    numeros = []
    while ciclo:
        user = int(input("Ingrese un numero:\n"))
        if user > 0:
            numeros.append(user)
        pregunta = input("Desea ingresar un nuevo numero ? y/n ")
        if pregunta == "n":
            ciclo = False

    def buscar(iterar_numeros, user_search):
        for i in range(len(iterar_numeros)):
            if user_search == iterar_numeros[i]:
                return True
        return False

    resultado_de_busqueda = buscar(numeros, 80)
    print(resultado_de_busqueda)

# Ejercicio 3:
def ingresarEmpleado():
    codigosEmpleados = []
    nombreApellidoEmpleados = []
    sueldosEmpleados = []
    ciclo = True
    while ciclo:
        codigo = input("Ingrese el codigo del empleado:\n")
        nombre_apellido = input("Ingrese el nombre y apellido del empleado:\n")
        sueldo = int(input("Ingrese el sueldo del empleado:\n"))
        codigosEmpleados.append(codigo)
        nombreApellidoEmpleados.append(nombre_apellido)
        sueldosEmpleados.append(sueldo)
        pregunta = input("Desea ingresar un nuevo empleado ? y/n ")
        if pregunta == "n":
            ciclo = False
    print("codigos:\n", codigosEmpleados)
    print("nombre y apellido:\n", nombreApellidoEmpleados)
    print("sueldo:\n",sueldosEmpleados)

# Ejercicio 4

def listaInvertida():
    num = []
    numerosInvertidos = []

    for i in range(0,10):
        user = int(input("Ingrese un número: "))
        num.append(user)
        # print(num)
    # a "i" le asignamos la cantidad de elementos que tiene la lista
    i = len(num)
    # mientras "i" sea mayor a cero que siga iterando
    while i > 0:
        # a "i" le descontamos uno, recordemos que los arreglos empiezan a contar desde el cero
        # y el "len" cuenta desde el 1.
        # entonces para recorrer la lista debemos restarle 1, si colocamos la resta al final del while nos va a dar error
        # porque la lista esta fuera de rango.
        #  
        # Ejemplo: la lista tiene 5 elementos, pero el indice de cada elemento se cuenta desde el 0
        #  
        # len(list = [A,B,C,D,E]) = 5
        #             ^ ^ ^ ^ ^ 
        #             0 1 2 3 4 (indice de la lista)
        i -= 1
        # print(i)        
        invert = num[i]
        numerosInvertidos.append(invert)
    print("Aqui esta la lista de sus 10 numeros:")
    print(num)
    print("Aqui esta la lista pero con los números invertidos:")
    print(numerosInvertidos)

