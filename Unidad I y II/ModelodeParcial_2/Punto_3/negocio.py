def ejercicioDeSublotes():
    sublote_1 = None
    sublote_2 = None
    count_primer_sublote = 0
    count_primer_sublote_neg = 0
    count_segundo_sublote = 0
    count_segundo_sublote_neg = 0
    global maximo_sublote
    maximo_sublote = 0
    global maximo_segundo_sublote
    maximo_segundo_sublote = 0

    print("Ingrese numeros negativos o positivos distintos a 0.\nSi ingresa 0 podra ingresar el 2do lote de numeros");
    while sublote_1 != 0:
        sublote_1 = int(input("Ingrese un lote de numeros "))
        if sublote_1 > 0:
            count_primer_sublote += 1
        if sublote_1 < 0:
            count_primer_sublote_neg += 1
        if maximo_sublote < sublote_1:
            maximo_sublote = sublote_1
        if sublote_1 == 0:
            while sublote_2 != 0:
                sublote_2 = int(input("Ingrese su segundo lote de numeros "))
                if sublote_2 > 0:
                    count_segundo_sublote += 1
                if sublote_2 < 0: 
                    count_segundo_sublote_neg += 1
                if maximo_segundo_sublote < sublote_2:
                   maximo_segundo_sublote = sublote_2


    # Primer Sublote
    if count_primer_sublote == 0: print("El primer sublote no contiene numeros positivos")
    else: print("La cantidad de valores positivos del primer sublote es:",count_primer_sublote)
    # Primer Sublote numeros negativos
    if count_primer_sublote_neg == 0: print("El primer sublote no contiene numeros negativos")
    else: print("La cantidad de valores negativos del primer sublote es:",count_primer_sublote_neg)

    # Segundo Sublote
    if count_segundo_sublote == 0: print("El segundo sublote no contiene numeros positivos")
    else: print("La cantidad de valores positivos del segundo sublote es:",count_segundo_sublote)
    # Segundo Sublote numeros negativos
    if count_segundo_sublote_neg == 0: print("El segundo sublote no contiene numeros negativos")
    else: print("La cantidad de valores negativos del segundo sublote es:",count_segundo_sublote_neg)



def valorMaximo():
    # Valor maximo Sublote 2
    print("El valor máximo del segundo sublote es:", maximo_segundo_sublote)
    # Valor maximo Sublote
    print("El valor máximo del primer sublote es:", maximo_sublote)
