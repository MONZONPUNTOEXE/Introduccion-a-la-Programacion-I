# listas Productos
codigo_producto = [1]
nombre_producto = ['actron']
marca_producto = ['bayer']
precio_producto = [200] 
stock_producto = [20]

# listas Clientes
codigo_cliente = [11]
nombre_cliente = ['franco']
apellido_cliente = ['monzon']
obraSocial_cliente = ['n'] 
nombreObraSocial_cliente = ['nada']

# listas Ventas
# listas Ventas por Cliente
venta_codigo_cliente = []
venta_nombre_cliente = []
venta_producto = []
venta_producto_cantidad = []
venta_precio_total = []
venta_descuento_porcentaje = []

def ingresarProducto():
    while True:
        codigo_producto.append(int(input('Ingrese el codigo de su producto: ')))
        nombre_producto.append(input('Ingrese el nombre de su producto: '))
        marca_producto.append(input('Ingrese la marca de su producto: '))
        precio_producto.append(int(input('Ingrese el precio de su producto: ')))
        stock_producto.append(int(input('Ingrese el stock de su producto: ')))
        
        user = (input('Desea ingresar otro producto ? s/n \n'))
        if user == 'n':
            print('Gracias por utilizar mi sistema')
            break

# Ingresar clientes
def ingresarCliente():
    while True:
        codigo_cliente.append(int(input('Ingrese el codigo de su cliente: ')))
        nombre_cliente.append(input('Ingrese el nombre de su cliente: '))
        apellido_cliente.append(input('Ingrese el apellido de su cliente: '))
        
        obra = input('Tiene Obra Social su cliente ?: s/n ')
        if obra == 's':
            nombreObraSocial_cliente.append(input('Ingrese nombre de la Obra Social de su cliente: '))
        else:
            obraSocial_cliente.append('n')
            nombreObraSocial_cliente.append(0)
        print(obraSocial_cliente)
        print(nombreObraSocial_cliente)

        
        user = (input('Desea ingresar otro cliente ? s/n \n'))
        if user == 'n':
            print('Gracias por utilizar mi sistema')
            break

def buscarCliente(posCliente):
    for i in range(len(codigo_cliente)):
        if posCliente == codigo_cliente[i]:
            return i
    return -1

def buscarProducto(posProducto):
    for i in range(len(codigo_producto)):
        if posProducto == codigo_producto[i]:
            return i
    return -1


def venta():
    while True:
        # Buscamos el producto
        user = int((input('Ingrese el codigo del Producto que desea vender \n')))
        posProducto = buscarProducto(user)
        print(posProducto)
        for i in range(len(codigo_producto)):
            if user == codigo_producto[posProducto]:
                print('Producto encontrado')
                venta_producto.append(venta_producto[posProducto])
                cantidad = int(input('Ingrese la cantidad a vender del Producto: \n')) 
                venta_producto_cantidad.append(cantidad)
                subtotal = cantidad * precio_producto[posProducto]
                print(venta_producto)
                print(venta_producto_cantidad)

                ############ usar para finalizar la venta
                # venta_precio_total.append(cantidad * precio_producto[posProducto])
                # print(venta_precio_total)

        # Buscamos el cliente
        user = int(input('Ingrese el codigo del Cliente que le va a vender \n'))
        posCliente = buscarCliente(user)
        for i in range(len(codigo_cliente)):
            if user == codigo_cliente[posCliente]:
                print('Cliente encontrado')
                venta_codigo_cliente.append(codigo_cliente[posCliente])
                venta_nombre_cliente.append(nombre_cliente[posCliente])
                print(f'Su Cliente es: {nombre_cliente[posCliente]} {apellido_cliente[posCliente]}')

                if obraSocial_cliente[posCliente] == 's':
                    print(f'Su obra social es: {nombreObraSocial_cliente}')
                    print('Por lo tanto tiene un descuento del 40%')
                    venta_descuento_porcentaje.append(40)
                    venta_total_des = subtotal - subtotal*40/100
                    print(f'La total de la venta es de: {venta_total_des}')
                    venta_precio_total.append(venta_total_des)
                    


                else:
                    print(f'No posee obra social por lo tanto no tiene descuento')
                    print(f'La total de la venta es de: {subtotal}')
                    venta_descuento_porcentaje.append(0)
                    venta_precio_total.append(subtotal)
        
        print(venta_codigo_cliente)
        print(venta_nombre_cliente)
        print(venta_producto)
        print(venta_producto_cantidad)
        print(venta_precio_total)
        print(venta_descuento_porcentaje)
                    



        
        user = (input('Desea hacer otra venta ? s/n \n'))
        if user == 'n':
            print('Gracias por utilizar mi sistema')
            break

