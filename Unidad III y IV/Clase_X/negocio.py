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
