maximo = 0
maximo2 = 0
posicion_1 = 0
posicion_2 = 0
suma = 0

for i in range (0,10):
    user = int(input("Ingrese un numero mayor a cero: "))
    # hacemos uso del "While", si el usuario ingresa un valor menor a cero no lo deje ingresar
    # hasta que no sea mayor a cero 
    while user <= 0: # Mientras User sea "Verdadero" entrara en el bucle
        print("*ERROR*")
        print("Por favor ingrese un número mayor a cero: ")
        # Es importante actualizar la variable "user". Porque sino queda con el valor que se le asigno
        # y siempre va valer Verdadero y entra en el bucle siempre, creando un bucle infinito
        # Para esto le decimos al usuario que ingrese un valor mayor a Cero. 
        user = int(input("Ingrese un numero mayor a cero: "))
        # Si el usuario ingresa un valor mayor a Cero, la condicional será Falsa, por lo tanto rompe el bucle
    if maximo < user: # Si el dato es verdadeo ejecuta este codigo
        maximo2 = maximo
        posicion_2 = posicion_1
        maximo = user
        posicion_1 = i + 1
    # "if" user < maximo2: -> Esto tenia escrito en el codigo anterior, estaba mal porque en este caso el "if" hace que maximo y maximo2 iban a tener el mismo valor siempre 
    elif maximo2 < user: # Si el dato en el "if" es Falso, entrara en el "elif" y ejecuta este código
        maximo2 = user
        posicion_2 = i + 1

    # IMPORTANTE: En este caso es importante que si o si pongamos un "if" y luego un "elif" porque:
    # 1) Si el dato de "if" es falso ira al "elif" y actualizara el maximo2 si maximo es mayor a maximo2
    # 2) Si nosotros en vez de colocar "if" y "elif" colocamos "if" e "if" si el dato da Verdadero en ambos casos, 
    #     sobreescribira la variable (maximo2). Porque el dato fue Verdadero en ambas condicionales a la vez.
    #     Y en este caso no queremos eso 

# Sumamos
suma = maximo + maximo2

print("El valor máximo ingresado es:",maximo,"\nEl valor del segundo máximo ingresado es:",maximo2,"\nLa posición del valor máximo es:",posicion_1,"\nLa posición del segundo valor máximo es:",posicion_2,"\nLa sumatoria total de los números ingresados es:", suma)