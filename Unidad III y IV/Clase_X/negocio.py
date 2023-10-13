# Ejercicio 1
def IngresarSueldo():
    sueldosEmpleados = []
    sueldosSuperiores = []
    ciclo = True

    while ciclo:
        user = int(input("Ingrese sueldo:\n"))
        if user >= 6000:
            sueldosSuperiores.append(user)
        else:
            sueldosEmpleados.append(user)

        pregunta = input("Desea ingresar un nuevo sueldo ? y/n ")
        if pregunta == "n":
            ciclo = False

    print("sueldo:\n", sueldosEmpleados)
    print("sueldo superior:\n", sueldosSuperiores)

# Ejercicio 2:
def cargaYBusquedaDeNumeros():
    ciclo = True
    numeros = []
    while ciclo:
        user = int(input("Ingrese un numero:\n"))
        if user > 0:
            numeros.append(user)
        pregunta = input("Desea ingresar un nuevo numero ? y/n ")
        if pregunta == "n":
            ciclo = False

    def buscar(iterar_numeros, user_search):
        for i in range(len(iterar_numeros)):
            if user_search == iterar_numeros[i]:
                return True
        return False

    resultado_de_busqueda = buscar(numeros, 80)
    print(resultado_de_busqueda)

# Ejercicio 3:
def ingresarEmpleado():
    codigosEmpleados = []
    nombreApellidoEmpleados = []
    sueldosEmpleados = []
    ciclo = True
    while ciclo:
        codigo = input("Ingrese el codigo del empleado:\n")
        nombre_apellido = input("Ingrese el nombre y apellido del empleado:\n")
        sueldo = int(input("Ingrese el sueldo del empleado:\n"))
        codigosEmpleados.append(codigo)
        nombreApellidoEmpleados.append(nombre_apellido)
        sueldosEmpleados.append(sueldo)
        pregunta = input("Desea ingresar un nuevo empleado ? y/n ")
        if pregunta == "n":
            ciclo = False
    print("codigos:\n", codigosEmpleados)
    print("nombre y apellido:\n", nombreApellidoEmpleados)
    print("sueldo:\n",sueldosEmpleados)

# Ejercicio 4

def listaInvertida():
    num = []
    numerosInvertidos = []

    for i in range(0,10):
        user = int(input("Ingrese un número: "))
        num.append(user)
        # print(num)
    # a "i" le asignamos la cantidad de elementos que tiene la lista
    i = len(num)
    # mientras "i" sea mayor a cero que siga iterando
    while i > 0:
        # a "i" le descontamos uno, recordemos que los arreglos empiezan a contar desde el cero
        # y el "len" cuenta desde el 1.
        # entonces para recorrer la lista debemos restarle 1, si colocamos la resta al final del while nos va a dar error
        # porque la lista esta fuera de rango.
        #  
        # Ejemplo: la lista tiene 5 elementos, pero el indice de cada elemento se cuenta desde el 0
        #  
        # len(list = [A,B,C,D,E]) = 5
        #             ^ ^ ^ ^ ^ 
        #             0 1 2 3 4 (indice de la lista)
        i -= 1
        # print(i)        
        invert = num[i]
        numerosInvertidos.append(invert)
    print("Aqui esta la lista de sus 10 numeros:")
    print(num)
    print("Aqui esta la lista pero con los números invertidos:")
    print(numerosInvertidos)

# Ejercicio 5
def tiendita():
    producto = ["Arroz","Fideo","Galletas","Pan","Gaseosa","Cerveza","Jugo","Leche","Manteca","Queso"]
    precio = [430,440,330,1000,450,1000,140,500,558,1050]
    stock = [5,4,35,6,45,65,63,7,34,65]

    
# Dar de alta un producto nuevo
    while True:
        user = input("Desea ingresar un producto nuevo y/n: ")
        if user == "y":
            productoNuevo = input("Ingrese el nombre del producto:\n")
            precioNuevo = int(input("Ingrese el precio del producto:\n"))
            stockNuevo = int(input("Ingrese el stock actual del producto:\n"))

            producto.append(productoNuevo)
            precio.append(precioNuevo)
            stock.append(stockNuevo)

            print(producto)
            print(precio)
            print(stock)

        elif user == "n":
            break
# Buscar Producto
    # La funcionalidad de "busqueda False y True". No pedia el enunciado, pero se lo agregue
    while True:
        user = input("Desea buscar un producto y/n: ")
        if user == "y":
                user = input("Introduzca el nombre del producto que desea buscar:\n")
                busqueda = False #Esta funcionalidad no estaba en el enunciado
                for i in range(len(producto)): #Con que encuentre las listas es mas que suficiente
                    if user == producto[i]:
                        print("Su producto fue encontrado exitosamente:")
                        print(producto[i])
                        print("Precio:",precio[i])
                        cambiar_precio = int(input("precio nuevo"))
                        precio[i] = cambiar_precio
                        print("Stock:",stock[i])

                        print(producto[i])
                        print("Precio:",precio[i])
                        print("Stock:",stock[i])

                        busqueda = True
                if busqueda == False:
                    print("Su producto no fue encontrado, Intentalo nuevamente")                          
                    print("Recuerde que Python es Case-Sensitive, distigue las minusculas y mayusculas")                          
        elif user == "n":
            break
# Modificar producto
    while True:
        user = input("Desea *Actualizar* el Precio y Stock de un producto y/n: ")
        if user == "y":
                user = input("Introduzca el nombre del producto que desea modificar:\n")
                busqueda = False 
                for i in range(len(producto)):
                    if user == producto[i]:
                        print("Su producto fue encontrado exitosamente:")
                        print(producto[i])
                        print("Precio:",precio[i])
                        print("Stock:",stock[i])
                        precio_viejo = precio[i]
                        stock_viejo = stock[i]
                        cambiar_precio = int(input("Ingrese el nuevo Precio\n"))
                        precio[i] = cambiar_precio
                        print("Genial su Precio se actualizado correctamente !")
                        print("Su precio anterior era", precio_viejo,"y ahora es:",precio[i])
                        cambiar_stock = int(input("Ingrese su nuevo Stock\n"))
                        stock[i] = cambiar_stock
                        print("Genial su Stock se actualizado correctamente !\n")
                        print("Su Stock anterior era", stock_viejo,"y ahora es:",stock[i])

                        print("Su producto se modifico exitosamente")
                        print(producto[i])
                        print("Precio:",precio[i])
                        print("Stock:",stock[i])

                        busqueda = True
                if busqueda == False:
                    print("Su producto no fue encontrado, Intentalo nuevamente")                          
                    print("Recuerde que Python es Case-Sensitive, distigue las minusculas y mayusculas")                          
        elif user == "n":
            break
# Guardar cantidad vendida
    while True:
        user = input("¿Desea ingresar una nueva Venta de un Producto? y/n: ")
        if user == "y":
                user = input("Introduzca el nombre del producto que vendio:\n")
                busqueda = False 
                for i in range(len(producto)):
                    if user == producto[i]:
                        print("Su producto fue encontrado exitosamente:")
                        print(producto[i])
                        print("Cuantas unidades se vendieron del producto ?",producto[i])
                        unidades_vendidas = int(input("Ingrese la cantidad vendida\n"))
                        stock_actual = stock[i] - unidades_vendidas
                        venta_total = precio[i] * unidades_vendidas
                        stock[i] = stock_actual
                        print("El Stock actual de",producto[i])
                        print("Es:",stock[i],"Unidades")
                        print("La venta total del producto es de:",venta_total)
                        busqueda = True
                if busqueda == False:
                    print("Su producto no fue encontrado, Intentalo nuevamente")                          
                    print("Recuerde que Python es Case-Sensitive, distigue las minusculas y mayusculas")                          
        elif user == "n":   
            break

# inventario actual (lo agregue, no lo pide la consigna) 
    suma = 0
    print("Su Inventario actual de la Tiendita es:")
    for i in range(len(producto)):
        print("**",producto[i],"**")
        print("Precio:",precio[i])
        print("Stock:",stock[i])
        subtotal_stock = precio[i]*stock[i]
        suma = subtotal_stock + suma
        print("________________")
    print("En total",len(producto),"productos")
    print("El total del fondo de comercio (solo mercaderia) es de:",suma,"pesos")
    print("Gracias por usar el sistema")
    print("Asta la procsima xD")