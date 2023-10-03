def calcularPromedio():
    user = 0
    suma = 0
    cont = 0
    for i in range(0,5):
        user = int(input("Ingrese su numero mayor a 0: "));
        if user <= 0:
            while user <= 0:
                print("Ingrese un numero valido mayor a 0")
                user = int(input("Ingrese su numero mayor a 0: "));                
        if user > 0:
            suma = user + suma
            print(suma)
            cont = i + 1
            print(cont)
    promedio = suma / cont
    print("La suma de sus numeros es:",suma,"\nY su promedio es:",promedio)

def maximos():
    user = 0
    maximo = 0
    segundo_maximo = 0
    suma = 0
    pos = 0
    pos2 = 0

    for i in range(0,4):
        user = int(input("Ingrese su número: "))
        if user <= 0:
            while user <= 0:
                print("*ERROR* Ingrese un número mayor a 0")
                user = int(input("Ingrese su número: "))
        if user > maximo:
            segundo_maximo = maximo
            pos2 = pos
            maximo = user
            pos = i + 1            
        elif user > segundo_maximo:
            segundo_maximo = user
            pos2 = i + 1
        suma = suma + user
            

    print("El Maximo ingresado es: ",maximo)
    print("La posicion del número maximo ingresado es:", pos)
    print("El segundo Maximo ingresado es:",segundo_maximo)
    print("La posicion del número 2do maximo ingresado es:", pos2)
    print("La suma total es de:", suma)


#maximos()

def maximo2():
    for i in range(0, 4):
        num = int(input("Por favor ingrese un número: "))
        if i == 0:
            maximo = num
            print(maximo)
            maximo2 = num
            print(maximo2)
            pos_maximo = i+1
            pos_maximo2 = i+1
        if num > maximo:
            maximo2 = maximo
            pos_maximo2 = pos_maximo

            maximo = num
            pos_maximo = i+1
        elif num > maximo2:
            maximo2 = num
            pos_maximo2 = i + 1
    
    print("El número mas grande ingresado es el:", maximo,"y su posición es:", pos_maximo,"Y el segundo mas grande es el:", maximo2, "y su posición es:", pos_maximo2);

maximo2();