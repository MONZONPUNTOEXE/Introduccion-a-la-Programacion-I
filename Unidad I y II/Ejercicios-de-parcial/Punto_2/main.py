salario_xhora = int(input("Ingrese su salario por hora: "));
horas_trabajadas = int(input("Ingrese sus horas trabajadas de esta semana: "));
total = 0


if horas_trabajadas > 40:
    horas_extras = horas_trabajadas - 40
    print(horas_extras)
    subtotal = horas_extras * salario_xhora  * 10 / 100
    total = horas_trabajadas * salario_xhora + subtotal
    print(int(total))
elif horas_trabajadas < 40 :
    total = horas_trabajadas*salario_xhora

print("Tu salario es de ",total, "pesos");


    



