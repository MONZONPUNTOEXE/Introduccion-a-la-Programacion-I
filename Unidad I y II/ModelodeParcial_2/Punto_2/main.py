maximo = 0
maximo2 = 0
posicion_1 = 0
posicion_2 = 0
suma = 0

for i in range (0,5):
    user = int(input("Ingrese un numero"))    
    if maximo < user:
        maximo2 = maximo
        maximo = user
        posicion_1 = i + 1
        posicion_2 = i
    elif maximo2 < user:
        maximo2 = user
        posicion_2 = i + 1


print(i)
suma = maximo + maximo2

print("El valor máximo ingresado es:",maximo,"\nEl valor del segundo máximo ingresado es:",maximo2,"\nLa posición del valor máximo es:",posicion_1,"\nLa posición del segundo valor máximo es:",posicion_2,"\nLa sumatoria total de los números ingresados es:", suma)