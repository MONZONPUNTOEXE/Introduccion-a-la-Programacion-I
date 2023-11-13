# Ejerciocio 1
def primerYSegundoMaximo ():
    maximo = 0
    maximo_dos = 0
    pos_maximo = 0
    pos_maximo_dos = 0

    for i in range (0,10):
        user = int(input('Ingrese su numero\n'))
        if user > maximo:
            maximo_dos = maximo
            maximo = user

            pos_maximo_dos = pos_maximo        
            pos_maximo = i + 1
        elif user > maximo_dos:
            maximo_dos = user           
            pos_maximo_dos = i + 1
    
    print(f'Su numero maximo es: {maximo} ')  
    print(f'Su posicion es: {pos_maximo}')  
    print(f'Su numero segundo maximo es: {maximo_dos}')  
    print(f'Su posicion es: {pos_maximo_dos}')


# Ejerciocio 2
def numerosPares ():
    count = 0
    for i in range(0,10):
        user = int(input('Ingrese su numero\n'))
        if user % 2 == 0:
            count += 1
    
    print(f'Usted ingresó {count} números pares')


# Ejerciocio 3
def calcularSalarios ():
    horas_trabajadas = int(input('Ingrese la cantidad de horas'))
    tarifa_por_hora = int(input('Ingrese su tarifa por horas'))
    pago_semanal = horas_trabajadas * tarifa_por_hora
    if horas_trabajadas > 40:
        horas_extras = (horas_trabajadas - 40) * tarifa_por_hora * 2
        print(horas_extras)
        salario_total = horas_extras + pago_semanal
        print('Usted posee horas extras')
        print(f'Su salario total es de: {salario_total}')
    else:       
        print('usted no posee horas extras')
        print(f'Su pago semanal es de: {pago_semanal}')

# Ejercicio 4:

def sublotesDeNumeros():
    lote_uno = 1
    lote_dos = 1
    count_uno = 0
    count_dos = 0

    while lote_uno != 0:
        lote_uno = int(input('Ingrese los numeros para el sublote 1 para finalizar ingrese 0\n'))
        if lote_uno > 0:
            count_uno += 1
            print(count_uno)

        if lote_uno == 0:
            while lote_dos != 0:
                lote_dos = int(input('Ingrese los numeros para el sublote 2 para finalizar ingrese 0\n'))
                if lote_dos > 0:
                    count_dos += 1
                    print(count_dos)    
                        