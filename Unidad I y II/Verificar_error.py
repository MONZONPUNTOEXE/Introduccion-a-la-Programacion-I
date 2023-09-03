# Inicializamos las variables
maximo = 0
maximo2 = 0
pos_maximo = 0
pos_maximo2 = 0

# Iteramos 10 veces para ingresar números
for i in range(0,4):
    numero = int(input("Ingrese un número: "))
    
    # Comprobamos si es el número máximo
    print(maximo)
    print(numero)
    if maximo or numero > maximo:
            print(maximo > maximo);
            print(numero > maximo)
            print("Valor Maximo:", maximo);
            maximo2 = maximo
            print("Valor Maximo2:", maximo2);
            pos_maximo2 = pos_maximo        
            maximo = numero
            print("Valor Maximo:", maximo)
            pos_maximo = i + 1
    # Comprobamos si es el segundo número máximo
    elif maximo2 or numero > maximo2:
        print("Elif Cliente ingreso: ",numero,"Valor Maximo 2: ",maximo2);
        maximo2 = numero
        print("Elif Valor Maximo 2:",maximo2)
        pos_maximo2 = i + 1

# Imprimimos los resultados
print('El número máximo es', maximo, 'y su posición es el número', pos_maximo)
print('El segundo número más grande es', maximo2, 'y su posición es el número', pos_maximo2)