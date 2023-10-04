def ejercicioDeSublotes():
    # sublote_1 = None 
    # sublote_2 = None
    # Cambie el valor de la variable de "None" a "True", porque no vimos ·None· en clase
    sublote_1 = True
    sublote_2 = True
    count_primer_sublote = 0
    count_primer_sublote_neg = 0
    count_segundo_sublote = 0
    count_segundo_sublote_neg = 0
    # Si necesitamos utilizar el valor de una variable que esta en otra función, necesitamos declarar
    # esa variable como una variable "global", para poder acceder a ese dato desde otra función.


    # Por ejemplo:  a "maximo_sublote" lo voy a usar en la función "valorMaximo" mas abajo
    #               por lo tanto "maximo_sublote" y "maximo_segundo_sublote" las declaro como globales

    # Las variables globales se declaran asi, siempre y cuando necesitemos reutilizarlas.
    global maximo_sublote
    maximo_sublote = 0
    global maximo_segundo_sublote
    maximo_segundo_sublote = 0

    print("Ingrese numeros negativos o positivos distintos a 0.\nSi ingresa 0 podra ingresar el 2do lote de numeros");
    # No era necesario usar el "while sublote =! 0" para inicializar, ya que sublote_1 inicializa "True".
    # Por lo tanto el while inicializa con un dato "True" 
    while sublote_1:
        sublote_1 = int(input("Ingrese un lote de numeros "))
        if sublote_1 > 0:
            count_primer_sublote += 1
        elif sublote_1 < 0:
            count_primer_sublote_neg += 1
        elif maximo_sublote < sublote_1:
            maximo_sublote = sublote_1
            # Ahora si el usuario ingresa un cero, le ponemos una condicion
        elif sublote_1 == 0:
            # Detenemos el while, diciendole que sublote_1 ahora es "False"
            sublote_1 = False
            # E inmediatamente le damos otra condicion.
        if sublote_1 == False:
            # Si, sublote_1 es "Falso" que inicie un nuevo while pero esta vez con "sublote_2"    
            while sublote_2: # Inicia automaticamente, recuerden que "sublote_2" lo declaramos como "True" 
                sublote_2 = int(input("Ingrese su segundo lote de numeros "))
                if sublote_2 > 0:
                    count_segundo_sublote += 1
                elif sublote_2 < 0: 
                    count_segundo_sublote_neg += 1
                elif maximo_segundo_sublote < sublote_2:
                   maximo_segundo_sublote = sublote_2
                elif sublote_2 == 0:
                    sublote_2 = False


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

ejercicioDeSublotes()

def valorMaximo():
    # Valor maximo Sublote
    print("El valor máximo del primer sublote es:", maximo_sublote)
    # Valor maximo Sublote 2
    print("El valor máximo del segundo sublote es:", maximo_segundo_sublote)
