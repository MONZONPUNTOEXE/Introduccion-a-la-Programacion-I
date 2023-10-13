menu = """
Binvenidos a Ejercicios Clase X

******** Menu Principal ************

1. Ingresar los sueldos de los empleado, agregarlos a una lista.
    e imprimir los sueldos superiores

2. Cargar un numero a una lista y buscar.
    retornar true si lo encuentra o false si no esta 
    dentro de la lista.

3.  Hacer un programa que ingrese el codigo de empleado sueldo,
    nombre y apellido de los empleados hasta que se ingrese un 0,
    crear las lista necesarias para que desde un menu el adminstrador
    ingrese el codigo y nos muestre el por pantalla el codigo,
    el sueldo y nombre y apellido

4. Ingresar 10 numeros por telcado y agregarlos a una lista,
    los numeros ingresados pasarlos a una nueva lista pero 
    invertidos

5.  Gestion  de stock de una tienda de comestibles

6. Para Salir
"""
menu_empleados = """
Bienvenidos al sistema de empleados

******** Menu Ingreso de empleado ************

1. Ingresar empleados
2. Buscar empleado
3. Salir
"""

menu_tiendita = """
Bienvenidos al sistema de la tiendita

******** Menu Tiendita ************

1. Dar de alta un producto
2. Buscar un producto
3. Modificar un producto
4. Guardar la cantidad vendida
5. Inventario actual
6. Salir
"""

def imprimirMenu():
    print(menu)

def imprimirMenuSueldos():
    print(menu_empleados)

def imprimirMenuTiendita():
    print(menu_tiendita)