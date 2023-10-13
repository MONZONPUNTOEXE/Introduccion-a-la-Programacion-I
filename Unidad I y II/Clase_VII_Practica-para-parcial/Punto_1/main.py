print("\n \n 1) Escribe un programa que calcule la suma de todos los números pares desde 1 hasta un número ingresado por el usuario.\nSi el usuario ingresa el 100.  vamos a tener que sumar los numero pares del 1 al 100 (2,4,6, etc) \n \n")

# La variable i se utiliza para iterar sobre los números.
i = 1
# La variable suma se utiliza para almacenar la suma de los números pares.
suma = 0

# Se pide al usuario que ingrese un número.
numero = int(input("Ingrese un numero "));

# Se imprime un mensaje para informar al usuario que ingresó el número especificado.
print("Ingresó el numero" ,numero,"Los numeros pares entre 1 y ese número son:")
# El bucle while itera sobre todos los números desde 1 hasta el número ingresado por el usuario
while i <= numero:
    # Se verifica si el número actual es par.
    if i % 2 == 0:
        # Si el número actual es par, se agrega a la suma.
        suma = i + suma
        # Se imprime el número actual.
        print(i)
    # Se incrementa el valor de i para avanzar al siguiente número.    
    i += 1

# Se imprime la suma total de los números pares.
print("La suma total de esos numeros es",suma)