import utils

global codigo
codigo = ["001","002","003","004"]
global producto
producto = ["Arroz","Fideo","Galletas","Pan"]
global precio
precio = [430,440,330,1000]
global stock
stock = [5,4,35,6]

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

    user_search = int(input("Ingrese el numero que quiera buscar en la lista:\n"))
    resultado_de_busqueda = buscar(numeros, user_search)
    print(resultado_de_busqueda)

# Ejercicio 3:
global codigosEmpleados
codigosEmpleados = []
global nombreApellidoEmpleados
nombreApellidoEmpleados = []
global sueldosEmpleados
sueldosEmpleados = []

def ingresarEmpleado():
    pregunta = 1
    while pregunta != 0:
        codigo = input("Ingrese el codigo del empleado:\n")
        nombre_apellido = input("Ingrese el nombre y apellido del empleado:\n")
        sueldo = int(input("Ingrese el sueldo del empleado:\n"))
        codigosEmpleados.append(codigo)
        nombreApellidoEmpleados.append(nombre_apellido)
        sueldosEmpleados.append(sueldo)
        pregunta = int(input("¿Desea continuar ingresando empleados?\n0. Para Finalizar\n1. Para Continuar\n"))
    print("codigos:\n", codigosEmpleados)
    print("nombre y apellido:\n", nombreApellidoEmpleados)
    print("sueldo:\n",sueldosEmpleados)
# Busqueda de empleado
def buscarEmpleado():
    while True:
        user = input("Ingrese el codigo del empleado que desea buscar: ")
        busqueda_exitosa = False
        for i in range (len(codigosEmpleados)):
            if user == codigosEmpleados[i]:
                print("Su empleado a sido encontrado exitosamente!")
                print("Su Empleado es:", nombreApellidoEmpleados[i])
                print("Su sueldo es:", sueldosEmpleados[i])
                busqueda_exitosa = True
        if busqueda_exitosa == False:
            print("El codigo del empleado no fue encontrado")
            print("Intente nuevamente")
        pregunta = input("¿Desea seguir buscando y/n?")
        if pregunta == "n":
            print("Gracias por utilizar mi programa")
            break

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
  
# Dar de alta un producto nuevo
def agregarProducto():
        while True:
            coodigoNuevo = input("Ingrese el Código:\n")
            productoNuevo = input("Ingrese el nombre del producto:\n")
            precioNuevo = int(input("Ingrese el precio del producto:\n"))
            stockNuevo = int(input("Ingrese el stock actual del producto:\n"))
            codigo.append(coodigoNuevo)
            producto.append(productoNuevo)
            precio.append(precioNuevo)
            stock.append(stockNuevo)            
            print(codigo)
            print(producto)
            print(precio)
            print(stock)

            user = input("Desea ingresar un producto nuevo y/n: ")
            if user == "n":
                break
# Buscar Producto
def buscarProducto():
        # La funcionalidad de "busqueda False y True". No pedia el enunciado, pero se lo agregue
        while True:
            user = input("Introduzca el código del producto que desea buscar:\n")
            busqueda = False #Esta funcionalidad no estaba en el enunciado
            for i in range(len(codigo)): #Con que encuentre las listas es mas que suficiente
                if user == codigo[i]:
                    print("Su producto fue encontrado exitosamente:")
                    print("Código: ",codigo[i])
                    print("Nombre: ", producto[i])
                    print("Precio:",precio[i])
                    print("Stock:",stock[i])
                    busqueda = True
            if busqueda == False:
                print("Su producto no fue encontrado, Intentalo nuevamente")                          
                print("Recuerde que Python es Case-Sensitive, distigue las minusculas y mayusculas")                          
            user = input("Desea buscar otro producto y/n: ")
            if user == "n":
                break
# Modificar producto
def modificarProducto():
        while True:            
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
            user = input("Desea *Actualizar* el Precio y Stock de otro producto y/n: ")
            if user == "n":
                break
# Guardar cantidad vendida
def cantidadVendida():       
        while True:            
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
            user = input("¿Desea ingresar una nueva Venta de un Producto? y/n: ")
            if user == "n":   
                break

# inventario actual (lo agregue, no lo pide la consigna)
def inventarioActual():
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