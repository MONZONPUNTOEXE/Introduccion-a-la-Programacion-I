# Se solicita al usuario su salario por hora.
salario_xhora = int(input("Ingrese su salario por hora: "));

# Se solicita al usuario las horas trabajadas en una semana.
horas_trabajadas = int(input("Ingrese sus horas trabajadas de esta semana: "));

# Se inicializa la variable total y subtotal con el valor 0.
total = 0
subtotal = 0

# Se utiliza una condición if para verificar si el número de horas trabajadas es mayor que 40.
if horas_trabajadas > 40:

    # Si el número de horas trabajadas es mayor que 40, se calcula el número de horas extras.
    horas_extras = horas_trabajadas - 40

    # Se imprime el número de horas extras.
    print(horas_extras)

    # Se calcula el costo de las horas extras, considerando un incremento de 10%.
    subtotal = horas_extras * salario_xhora  * 10 / 100
    
    # Se calcula el salario total, sumando el salario por hora de las horas regulares y el costo de las horas extras.
    total = horas_trabajadas * salario_xhora + subtotal

# Se utiliza una condición elif para verificar si el número de horas trabajadas es menor que 40.
elif horas_trabajadas < 40 :
    
    # Si el número de horas trabajadas es menor que 40, el salario total es igual al salario por hora multiplicado por el número de horas trabajadas.
    total = horas_trabajadas*salario_xhora

# Se imprime el salario total.
print("Tu salario es de ",int(total), "pesos");