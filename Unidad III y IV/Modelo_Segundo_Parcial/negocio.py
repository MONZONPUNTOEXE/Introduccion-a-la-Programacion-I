# Lista clientes
codigo_cliente = []
nombre_cliente = []


# Lista productos
codigo_producto = []
nombre_producto = []
precio_producto = []
stock_producto = []

# Lista de las ventas a C.Final
nombreClienteVentaCF = []
cantidadDeProductoClienteVentaCF = []
precioDeProductoClienteVentaCF = []
ventaConsumidorFinal = []

# Lista de ventas a Clientes
ventasCliente = []
nombreVentaCliente = []
nombreProductoVentaCliente = []

def cargarCliente():
    while True:
        codigo_cliente.append(int(input("Ingrese el codigo del Cliente: ")))
        nombre_cliente.append(input("Ingrese el nombre del Cliente: "))

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

                print(ventasCliente)
                print(nombreVentaCliente)
                print(nombreProductoVentaCliente)

        pregunta = input("Desea ingresar otro producto s/n: ")
        if pregunta == "n":
            break

def ventaCliente():
    while True: 
        cliente = int(input("Ingrese el código del cliente que le desea vender"))
        posCliente = buscarCliente(cliente)
        if cliente == codigo_cliente[posCliente]:
            print("Su cliente es", nombre_cliente[posCliente])
        user = int(input("Ingrese el código del producto que desea vender"))
        posProducto = buscarProducto(user)
        if user == codigo_producto[posProducto]:
            print("Su producto es", nombre_producto[posProducto])
            venta = int(input("cuanto desea vender"))
            if venta > stock_producto[posProducto]:
                print("Su venta no se puede realizar, excede el maximo de Stock")
            else:
                totalVenta2 = venta * precio_producto[posProducto]
                print('El total de venta es:')
                print(totalVenta2)
                ventasCliente.append(totalVenta2)
                stock_producto[posProducto] = stock_producto[posProducto] - venta
                nombreVentaCliente.append(nombre_cliente[posCliente])
                nombreProductoVentaCliente.append(nombre_producto[posCliente])

        pregunta = input("Desea vender otro producto s/n: ")
        if pregunta == "n":
            break



def buscarVentaCliente():
    while True:
        user = int(input('Ingrese el codigo del cliente '))
        pos = buscarCliente(user)
        if user == codigo_cliente[pos]:
            print(f'Su cliente es: {nombreVentaCliente[pos]}')
            print(f'Su sus producto es: {nombreProductoVentaCliente[pos]}')

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
