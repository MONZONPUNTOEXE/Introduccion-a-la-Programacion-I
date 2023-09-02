n = 0
n2 = 0



for i in range(0,3):
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
    
    n = int(input())
    if n > n2 : n2 = 0 + n
    elif n < 0 and n > n2 : n2 = 0 + n

print("El Número más alto que ingreso fue el numero", n2)

