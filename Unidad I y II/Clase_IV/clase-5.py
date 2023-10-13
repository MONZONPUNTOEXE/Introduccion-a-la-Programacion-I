##### While
# informar los sueldos = siempre el sistema sin que se salga 
# Ingresar por teclado el numbre del empleado, el sueldo bruto e imprimir el sueldo basico, 
# Preguntar si desea continuar.

# Declaramos las variables 
empleado = 0
nueva_pregunta = 0
sueldo_neto = 0
s = True


 # Solicitar al usuario que ingrese un valor

while s == True:
    empleado = input("Ingrese el nombre del empleado" );
    numero = int(input("Ingrese un número entero positivo: "))
    sueldo_neto = numero - numero * 17 / 100
    print("El sueldo es de", int(sueldo_neto))
    nueva_pregunta = input("Desea ingresar otro nombre ? s/n ")
    # Verificar si el valor es válido (por ejemplo, un número entero positivo)
    if nueva_pregunta == "n":
        print("entro en el if");
        s = False
        
