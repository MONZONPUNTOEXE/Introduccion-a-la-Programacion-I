# Ejerciocio 1
def primerYSegundoMaximo ():
    maximo = 0
    maximo_dos = 0
    pos_maximo = 0
    pos_maximo_dos = 0

    for i in range (0,10):
        user = int(input('Ingrese su numero\n'))
        if user > maximo:
            maximo_dos = maximo
            maximo = user

            pos_maximo_dos = pos_maximo        
            pos_maximo = i + 1
        elif user > maximo_dos:
            maximo_dos = user           
            pos_maximo_dos = i + 1
    
    print(f'Su numero maximo es: {maximo} ')  
    print(f'Su posicion es: {pos_maximo}')  
    print(f'Su numero segundo maximo es: {maximo_dos}')  
    print(f'Su posicion es: {pos_maximo_dos}')

# Ejerciocio 2
def numerosPares ():
    count = 0
    for i in range(0,10):
        user = int(input('Ingrese su numero\n'))
        if user % 2 == 0:
            print('numero par')
            count += 1
            print(f'{count}')
    
    print('Hay ')

numerosPares()

# Ejerciocio 3
def calcularSalarios ():
    print('ejercicio')
