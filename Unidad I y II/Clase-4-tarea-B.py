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
mensaje_del_porcentaje = None



empleado = input("introduzca el nombre del empleado: ");
cantidad_de_ventas = int(input("Introduzca el monto de las ventas: "));

if cantidad_de_ventas < 10000:
    mensaje_del_porcentaje = "No cumple con las condiciones para el bonus.";
    sueldo_total = sueldo_base
if cantidad_de_ventas >= 10000 and cantidad_de_ventas < 10001:
    mensaje_del_porcentaje = "Por lo tanto se le aumento un 5 porciento mas al sueldo.";
    sueldo_total = sueldo_base + sueldo_base * 5 / 100
if cantidad_de_ventas >= 10001 and cantidad_de_ventas <= 20000 :
    mensaje_del_porcentaje = "Por lo tanto se le aumento un 9 porciento mas al sueldo.";
    print("-------------2");
    cantidad_de_ventas = cantidad_de_ventas
    sueldo_total = sueldo_base + sueldo_base * 9 / 100
if cantidad_de_ventas >= 20001:
    print("-------------3");
    mensaje_del_porcentaje = "Por lo tanto se le aumento un 15 porciento mas al sueldo.";
    sueldo_total = sueldo_base + sueldo_base * 15 / 100

print("El empleado:", empleado, "realizo un total en ventas de:" , cantidad_de_ventas,"pesos.", mensaje_del_porcentaje, "Su sueldo actual es de:",int(sueldo_total),"pesos");