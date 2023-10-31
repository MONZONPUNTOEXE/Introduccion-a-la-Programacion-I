codigo_cliente = []
nombre_cliente = []

codigo_producto = []
nombre_producto = []
precio_producto = []
stock_producto = []

ventaConsumidorFinal = []
ventaCliente = []

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
        user = int(input("Ingrese el código del producto que desea vender"))
        codigo = buscarProducto(user)
        if user == codigo_producto[codigo]:
            print("Su producto es", nombre_producto[codigo])
            venta = int(input("cuanto desea vender"))
            if venta > stock_producto[codigo]:
                print("Su venta no se puede realizar, excede el maximo de Stock")
            else:
                totalVenta = venta * precio_producto[codigo]
                print(totalVenta)
                ventaConsumidorFinal.append(totalVenta)
                venta - stock_producto[codigo]
        pregunta = input("Desea ingresar otro producto s/n: ")
        if pregunta == "n":
            break

def ventaCliente():
    while True: 
        cliente = int(input("Ingrese el código del cliente que le desea vender"))
        codigo = buscarCliente(cliente)
        if cliente == codigo_cliente[codigo]:
            print("Su cliente es", nombre_cliente[codigo])
        user = int(input("Ingrese el código del producto que desea vender"))
        codigo = buscarProducto(user)
        if user == codigo_producto[codigo]:
            print("Su producto es", nombre_producto[codigo])
            venta = int(input("cuanto desea vender"))
            if venta > stock_producto[codigo]:
                print("Su venta no se puede realizar, excede el maximo de Stock")
            else:
                totalVenta2 = venta * precio_producto[codigo]
                print(totalVenta2)
                ventaCliente.append(totalVenta2)
                venta - stock_producto[codigo]

        pregunta = input("Desea ingresar otro producto s/n: ")
        if pregunta == "n":
            break



def listarClientes():
    print(codigo_cliente)
    print(nombre_cliente)


def listarProductos():
    print(codigo_producto)
    print(nombre_producto)
    print(precio_producto)
    print(stock_producto)
