# Declaramos variables
numero = 0
maximo = 0
pos = 0

for i in range(0,3):
    # No prestar atencion a esto, es una cosa que hice aparte
    if i == 0 : print("Ingrese su Primer número (puede ser negativo o positivo)")
    if i == 1 : print("Ingrese su Segundo número (puede ser negativo o positivo)")
    if i == 2 : print("Ingrese su Tercer número (puede ser negativo o positivo)")
    if i == 3 : print("Ingrese su Cuarto número (puede ser negativo o positivo)")
    if i == 4 : print("Ingrese su Quinto número (puede ser negativo o positivo)")
    if i == 5 : print("Ingrese su Sexto número (puede ser negativo o positivo)")
    if i == 6 : print("Ingrese su Septimo número (puede ser negativo o positivo)")
    if i == 7 : print("Ingrese su Octavo número (puede ser negativo o positivo)")
    if i == 8 : print("Ingrese su Noveno número (puede ser negativo o positivo)")
    if i == 9 : print("Ingrese su Decimo número (puede ser negativo o positivo)")
# Numero que va a ingresar el cliente
    numero = int(input())
    # Si el numero es igual a 0 que me lo guarde como maximo
    if numero == 0 :
        maximo = numero
        # Me guarda la posicion de ese numero
        pos = i + 1
        # Si el numero no es igual a 0 que condicione si el numero es mayor 
    elif numero > maximo : 
        # si el numero es mayor que me lo guarde en Maximo y la posicion del mismo en Pos
        maximo = numero
        # Le agrego un + 1 paorque i empieza a contar desde el 0 y no desde el 1
        pos = i + 1

    
print("El Número más alto que ingreso fue el numero", maximo, "la posicion es", pos)

