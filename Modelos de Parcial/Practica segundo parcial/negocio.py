def sueldoEmpleados():
    sueldo_empleado = []
    suledo_empleado_superior = []

    while True:
        user = int(input("Ingrese los Sueldos: "))
        if user >= 60000:
            suledo_empleado_superior.append(user)
        elif user < 60000:
            sueldo_empleado.append(user)
        numero = input("Desea ingresar otros sueldo ? s/n")
        if numero == "n":
            break

def cargarNumeros():
    numerosPositivos = []

    while True:
        user = int(input("Ingrese los Numeros: "))
        if user > 0:
            numerosPositivos.append(user)
        numero = input("Desea ingresar otros numero ? s/n")
        if numero == "n":
            break
