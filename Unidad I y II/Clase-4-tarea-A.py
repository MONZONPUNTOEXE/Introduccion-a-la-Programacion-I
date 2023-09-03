# A)  Escribe un programa que permita al usuario ingresar 
# un conjunto de 10 números a través del teclado. 
# El programa debe determinar el número máximo en el conjunto, 
# indicar su posición en la secuencia y
# encontrar el segundo número más grande junto con su posición.

# Inicializamos las variables
maximo = 0
maximo2 = 0
pos_maximo = 0
pos_maximo2 = 0

# Iteramos 10 veces para ingresar números
for i in range(0,10):
    while True:
        try:
            # Solicitar al usuario que ingrese un valor
            numero = int(input("Ingrese un número entero positivo: "))

            # Verificar si el valor es válido (por ejemplo, un número entero positivo)
            if numero >= 0:
                break  # Salir del bucle si el valor es válido
            else:
                print("El valor debe ser un número entero positivo. Inténtelo nuevamente.")

        except ValueError:
            print("Ingrese un valor válido. Inténtelo nuevamente.")

# Hacer algo con el valor válido
    
    # Comprobamos si es el número máximo
    if numero > maximo:        
        maximo2 = maximo
        pos_maximo2 = pos_maximo        
        maximo = numero
        pos_maximo = i + 1
    # Comprobamos si es el segundo número máximo
    elif numero > maximo2:
        maximo2 = numero
        pos_maximo2 = i + 1

# Imprimimos los resultados
print('El número máximo es', maximo, 'y su posición es el número', pos_maximo)
print('El segundo número más grande es', maximo2, 'y su posición es el número', pos_maximo2)

#  ------ Sin corregir ----------

# Numero para guardar el numero del cliente
# numero = 0
# Maximo para guardar el numero maximo ingresado
# maximo = 0
# pos para guardar la posicion donde se encuentra el numero maximo
# pos = 0
# pos2 = 0
# # declaramos maximo2 para saber el segundo numero mas grande
# maximo2 = 0

# # iteramos 10 veces
# for i in range (0,3):
#     # ponemos int para asegurarnos que el numero ingresado sea un numero entero
#     numero = int(input("Ingrese un numero "));
#     # si el numero ingresado es 0 que me guarde el numero 0 como el numero maximo
#     # + su posicion
#     if numero == 0 : 
#         maximo = numero
#         pos = i +1
#     # Sino, que el pregunte si el numero es mayor al numero "maximo" de ese momento    
#     if numero > maximo :
#         maximo = numero        
#         pos = i +1
#         print(numero)
#         print(maximo)
#     if numero > maximo2 and maximo2 < maximo:
#         maximo2 = numero
#         print(maximo2)
#         print(i)


# # imprimimos el resultado
# print('el numero maximo es', maximo,'y su posicion es el numero ', pos, 'y el numero segundo mas grande es',maximo2 , 'y su posicion es el numero ', pos2)