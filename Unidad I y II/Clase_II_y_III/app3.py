## Declaracion de las variables
# nota = 2
# nota1 = 4
# nota2 = 4

nota = int(input(4))
nota1 = int(input(5))
nota2 = int(input(6))

# Sumamos las variables
suma = nota + nota1 + nota2
# Dividimos la suma por el total de variables
promedio = suma/3
# Imprimimos
print(promedio);

# Usamos las condicionales
if promedio >= 7: print("Promocion");
elif promedio >= 4 and promedio <= 6 : print("Aprueba");
else: print("Recursa");