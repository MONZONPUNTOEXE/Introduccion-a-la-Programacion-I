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

ciclo = True
numeros = [1,3,8,10,45]


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