# B) Diseña un sistema de gestión para calcular los sueldos de los empleados de una empresa.
# Cada empleado tiene un sueldo base de 80000 unidades.
# Sin embargo, sus sueldos pueden variar según sus ventas y las comisiones que generen.
# Si las ventas totales de un empleado alcanzan 10000 unidades, se le suma un 5% al sueldo base.
# Si las ventas están en el rango de 10001 a 20000 unidades, la suma es del 9%. 
# Para ventas que superen las 20001 unidades, la suma es del 15%. 
# El sistema debe pedir el nombre del empleado y el total de ventas, 
# y mostrar en pantalla el sueldo bruto resultante.


# Declaramos las variables
empleado = 0
cantidad_de_ventas = 0
sueldo_base = 80000
sueldo_total = 0



empleado = input("introduzca el nombre del empleado: ");
cantidad_de_ventas = int(input("Introduzca el monto de las ventas: "));

sueldo_total = sueldo_base * 5 / 100 
print(sueldo_total);
# if cantidad_de_ventas > 10000 :
#     sueldo_base = sueldo_base * 5 / 100


print("El empleado:", empleado, "realizo" , cantidad_de_ventas, "pesos en ventas");