# Lista clientes
codigo_cliente = [1,2]
nombre_cliente = ['Franco','Matias']
descripcion_cliente = ['Es buen pibe','La tiene clasra']


# Lista productos
codigo_producto = [1,2,3,4]
nombre_producto = ['Bolita','Bulon','Lapiz','Comida']
precio_producto = [100,200,300,400]
stock_producto = [30,20,50,60]

# Lista de las ventas a C.Final
nombreClienteVentaCF = []
cantidadDeProductoClienteVentaCF = []
precioDeProductoClienteVentaCF = []
ventaConsumidorFinal = []
ventaPrecioProducto = []

# Lista de ventas a Clientes
codigoVentaCliente = []
nombreProductoVentaCliente = []
ventaCantidadProductoCliente = []
ventaPrecioProductoCliente = []
ventasClienteTotal = []

def cargarCliente():
    while True:
        codigo_cliente.append(int(input("Ingrese el codigo del Cliente: ")))
        nombre_cliente.append(input("Ingrese el nombre del Cliente: "))
        descripcion_cliente.append(input("Ingrese la descripcion del cliente: "))

        user = input("Desea ingresar otro cliente s/n: ")
        if user == "n":
            break

def cargarProducto():
    while True:
        codigo_producto.append(int(input("Ingrese el codigo del producto: ")))
        nombre_producto.append(input("Ingrese el nombre del producto: "))
        precio_producto.append(int(input("Ingrese el precio del producto: ")))
        stock_producto.append(int(input("Ingrese el stock del producto: ")))

        user = input("Desea ingresar otro producto s/n: ")
        if user == "n":
            break
        
def buscarCliente(codigo):
    for i in range(0,len(codigo_cliente)):
        if codigo == codigo_cliente[i]:
            return i
    return -1

def buscarProducto(codigo):
    for i in range(0,len(codigo_producto)):
        if codigo == codigo_producto[i]:
            return i
    return -1


def ventaFinal():
    while True:
        nombreClienteVentaCF.append(input('Ingrese el nombre del C.Final: '))
        user = int(input("Ingrese el código del producto que desea vender: "))
        codigo = buscarProducto(user)
        if user == codigo_producto[codigo]:
            print("Su producto es", nombre_producto[codigo])
            venta = int(input("cuanto desea vender "))
            if venta > stock_producto[codigo]:
                print("Su venta no se puede realizar, excede el maximo de Stock")
            else:
                totalVenta = venta * precio_producto[codigo]
                print('El total de venta es:')
                print(totalVenta)
                ventaConsumidorFinal.append(totalVenta)
                stock_producto[codigo] = stock_producto[codigo] - venta
                cantidadDeProductoClienteVentaCF.append(venta)
                precioDeProductoClienteVentaCF.append(precio_producto[codigo])


        pregunta = input("Desea ingresar otro producto s/n: ")
        if pregunta == "n":
            break

def ventaCliente():
    while True: 
        # Ingresamos el codigo del cliente
        cliente = int(input("Ingrese el código del cliente que le desea vender"))
        # buscamos el codigo del cliente, mediante una funcion creada
        posCliente = buscarCliente(cliente)
        if cliente == codigo_cliente[posCliente]:
            # si el cliente es encontrado, se busca el producto
            print("Su cliente es", nombre_cliente[posCliente])
            user = int(input("Ingrese el código del producto que desea vender"))
            posProducto = buscarProducto(user)
        if user == codigo_producto[posProducto]:
            # si el producto es encontrado se ingresa la cantidad de la venta
            print("Su producto es", nombre_producto[posProducto])
            venta = int(input("cuanto desea vender"))
            if venta > stock_producto[posProducto]:
                # si el stock del producto es mayor no se realiza la venta
                print("Su venta no se puede realizar, excede el maximo de Stock")
            else:
                # si el stock es producto es menor
                # registramos el codigo del cliente en una lista 
                codigoVentaCliente.append(codigo_cliente[posCliente])
                comprasDelClienteActual = []

                # buscamos las ventas del cliente en especifico con un for
                for i in range(len(codigoVentaCliente)):
                    if codigo_cliente[posCliente] == codigoVentaCliente[i]:
                        comprasDelClienteActual.append(codigoVentaCliente[i])
                    # Si encuentra las ventas apeneamos ese codigo en "compras del cliente actual"
                    # Para que si tiene mas de 10 ventas el sitema haga el descuento
                print(comprasDelClienteActual)

                if len(comprasDelClienteActual) >= 10:
                    print('Su Cliente compro mas de 10 productos por lo tanto tiene descuento')
                    descuento = int(input('Ingrese el descuento: '))                    
                    subTotalVenta2 = venta * precio_producto[posProducto]
                    print('El subtotal de venta es:')
                    print(subTotalVenta2)
                    totalVenta2 = subTotalVenta2 - (subTotalVenta2 * descuento/100)

                    print(f'El total de venta es más el {descuento}% es:')
                    print(totalVenta2)
                    stock_producto[posProducto] = stock_producto[posProducto] - venta

                    nombreProductoVentaCliente.append(nombre_producto[posProducto])
                    ventaPrecioProductoCliente.append(precio_producto[posProducto])
                    ventaCantidadProductoCliente.append(venta)
                    ventasClienteTotal.append(totalVenta2)

                    print(codigoVentaCliente)
                    print(nombreProductoVentaCliente)
                    print(ventaCantidadProductoCliente)
                    print(ventaPrecioProductoCliente)
                    print(ventasClienteTotal)


                else:                
                    totalVenta2 = venta * precio_producto[posProducto]
                    print(totalVenta2)
                    stock_producto[posProducto] = stock_producto[posProducto] - venta

                    nombreProductoVentaCliente.append(nombre_producto[posProducto])
                    ventaPrecioProductoCliente.append(precio_producto[posProducto])
                    ventaCantidadProductoCliente.append(venta)
                    ventasClienteTotal.append(totalVenta2)

                    print(codigoVentaCliente)
                    print(nombreProductoVentaCliente)
                    print(ventaCantidadProductoCliente)
                    print(ventaPrecioProductoCliente)
                    print(ventasClienteTotal)

        pregunta = input("Desea vender otro producto s/n: ")
        if pregunta == "n":
            break

def buscarVentaCliente():
    while True:
        user = int(input('Ingrese el codigo del cliente '))
        pos = buscarCliente(user)
        if user == codigo_cliente[pos]:
            print(f'Su cliente es: {nombre_cliente[pos]}')
            print(f'Descripcion: {descripcion_cliente[pos]}')
            print(f'Los productos que compro {nombre_cliente[pos]} son:')
            for i in range(len(nombreProductoVentaCliente)):
                if codigo_cliente[pos] == codigoVentaCliente[i]:
                    print('****************************')
                    print(nombreProductoVentaCliente[i])
                    print(f'Precio de producto: {ventaPrecioProductoCliente[i]}')
                    print(f'Cantidad vendida: {ventaCantidadProductoCliente[i]}')
                    print(f'Total de venta: {ventasClienteTotal[i]}')

        else:
            print('No encontramos tu cliente, intentalo nuevamente')
          
        user = input('Desea hacer otra busqueda ? s/n ')
        if user == "n":
            break





def listarClientes():
    print(codigo_cliente)
    print(nombre_cliente)


def listarProductos():
    print(codigo_producto)
    print(nombre_producto)
    print(precio_producto)
    print(stock_producto)
