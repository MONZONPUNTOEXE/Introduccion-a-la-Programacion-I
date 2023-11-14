
user = 0
numero = 0
suma = 0
promedio = 0

# La actividad dice que los numeros tienen que ser distintos a 0 y positivos, en este ejemplo no esta hecho

for i in range (0, 5):
    user = int(input("Ingrese un numero "))
    if user != 0:
        i += 1
        suma = user + suma
    else: print("ingrese un numero valido")

promedio = suma / i

# Importante: No siempre es buena practica usar a "i" como "contador"
# Es mejor crear una variable que cumpla esa funcion. Por Ejemplo:

# cont = 0
# for i in range (0, 5):
#     user = int(input("Ingrese un numero "))
#     if user != 0:
#         cont += 1
#         suma = user + suma
#     else: print("ingrese un numero valido")
# promedio = suma / cont

print("La sumatoria de los cinco números ingresados es", suma, "y el promedio es", int(promedio))