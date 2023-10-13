def escribirHolaMundo():
    print("Hola Mundo");

def numeros1Al5():
    n = "1"
    for i in range (0,1):
        n += "2345"
        print(n)

def repeticionDeA():
    for i in range(0,3):
        print("a")

def triangulo():
    simbolo = "a"
    print(simbolo)
    for i in range(0,5):
       simbolo += "a"
       print(simbolo)


def nameAndLastName():
    name = input("Ingrese su nombre: ")
    lastname = input("Ingrese su apellido: ")

    print("Su nombre y apellido es:", name,lastname)

    comentario = input("Agregue un comentario: ")
    print("Su nombre es:", name,", su comentario es", comentario,"y su apellido es", lastname)

def operacion():
    numero1 = 15
    numero2 = 20
    
    resultado = ((numero1 + numero2))/2
    print(numero1, "+" ,numero2,"/","2 =",resultado )

    print("La operacion que hace este programa es Promediar \nPorque suma",numero1,"Con",numero2,"\ny divide por 2, que es la cantidad de números que se sumaron")


