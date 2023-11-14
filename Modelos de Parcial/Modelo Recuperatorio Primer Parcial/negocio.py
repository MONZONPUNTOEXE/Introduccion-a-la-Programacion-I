def maximos():
    maximo = 0
    maximo_dos = 0

    pos_uno = 0
    pos_dos = 0

    sumatoria = 0

    for i in range(0,10):
        user = int(input('ingrese su numero: '))
        sumatoria = user + sumatoria
        if i == 0:
            maximo = user
            maximo_dos = user
            pos_uno = i + 1
            pos_dos = i + 1

        if user > maximo:
            maximo_dos = maximo
            pos_dos = pos_uno

            maximo = user
            pos_uno = i + 1

        elif user > maximo_dos:
            maximo_dos  = user
            pos_dos = i + 1

    print(f'El numero maximo es: {maximo}')
    print(f'La posicion del numero maximo es: {pos_uno}')
    print(f'El numero segundo maximo es: {maximo_dos}')
    print(f'La posicion del numero segundo maximo es: {pos_dos}')
    print(f'La sumatoria de los numero es {sumatoria}')


def sublotes():
    sublote_uno = True 
    sublote_dos = True

    count_sub_uno_pos = 0
    count_sub_uno_neg = 0

    count_sub_dos_pos = 0
    count_sub_dos_neg = 0

    maximo_sublote_uno = 0
    maximo_sublote_dos = 0

    while sublote_uno:
        user = int(input('Ingrese numeros del sublote 1 ingrese cero para finalizarlo: \n'))
        if user > 0:
            count_sub_uno_pos += 1
        elif user < 0:
            count_sub_uno_neg += 1            
        if user > maximo_sublote_uno:
            maximo_sublote_uno = user
        elif user == 0:
            sublote_uno = False
            while sublote_dos:
                user = int(input('Ingresó al sublote 2 ingrese sus numeros e ingrese cero para finalizarlo: \n'))
                if user > 0:
                    count_sub_dos_pos += 1
                elif user < 0:
                    count_sub_dos_neg += 1            
                if user > maximo_sublote_dos:
                    maximo_sublote_dos = user
                if user == 0:
                    sublote_dos = False

    # sublote 1
    print(f'Cantidad de valores positivos del 1er Sublote: {count_sub_uno_pos}')
    print(f'Cantidad de valores negativos del 1er Sublote: {count_sub_uno_neg}')
    print(f'Maximo del 1er Sublote: {maximo_sublote_uno}')
    # sublote 2
    print(f'Cantidad de valores positivos del 2do Sublote: {count_sub_dos_pos}')
    print(f'Cantidad de valores negativos del 2do Sublote: {count_sub_dos_neg}')
    print(f'Maximo del 2do Sublote: {maximo_sublote_dos}')



        