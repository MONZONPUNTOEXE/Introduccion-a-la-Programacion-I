salario_xhora = int(input("Ingrese su salario por hora: "));

horas_trabajadas = int(input("Ingrese sus horas trabajadas de esta semana: "));

subtotal = salario_xhora * horas_trabajadas

if horas_trabajadas >= 40:
    horas_extras = horas_trabajadas - 40
    print(horas_extras)


    



