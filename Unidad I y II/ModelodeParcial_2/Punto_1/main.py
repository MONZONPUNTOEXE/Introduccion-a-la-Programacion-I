
user = 0
numero = 0
suma = 0
promedio = 0



for i in range (0, 5):
    user = int(input("Ingrese un numero "))
    if user != 0:
        i += 1
        suma = user + suma
    else: print("ingrese un numero valido")

promedio = suma / i

print("La sumatoria de los cinco números ingresados es", suma, "y el promedio es", int(promedio))