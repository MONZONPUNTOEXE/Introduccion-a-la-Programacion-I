# Productos
producto_codigo = []
producto_nombre = []
producto_marca = []
producto_precio = []
producto_stock = []
producto_cantidad_vendida = []

# Clientes
cliente_codigo = []
cliente_nombre = []
cliente_apellido = []
cliente_obraSocial = []
cliente_nombreObraSocial = []
cliente_cantidad_vendida = []
cliente_venta_total_pesos = []

# Ventas
cliente_codigo_venta = []
nombre_cliente_venta = []
nombre_producto_venta = []
descuento_venta = []
precio_total_venta = []


def buscarCliente(x):
    for i in range(0,len(cliente_codigo)):
        if x == cliente_codigo[i]:
            print(i)
            return i
    return -1

def buscarProducto(x):
    for i in range(0,len(producto_codigo)):
        if x == producto_codigo[i]:
            print(i)
            return i
    return -1

def actualizarStock(codigo, cantidad):
    pos = buscarProducto(codigo)
    if pos != -1:
        producto_stock[pos] -= cantidad
        producto_cantidad_vendida[pos] += cantidad
        print('Se actualizo el Stock y cantidad de venta correctamente')
    else:
        print('No se actualizo el stock, producto no encontrado')

def agregarClientes(codigo,nombre,apellido,obrasocial,nombreObraSocial):
    cliente_codigo.append(codigo)    
    cliente_nombre.append(nombre)
    cliente_apellido.append(apellido)
    cliente_obraSocial.append(obrasocial)
    cliente_nombreObraSocial.append(nombreObraSocial)
    cliente_cantidad_vendida.append(0)
    cliente_venta_total_pesos.append(0)
    print('Los datos del cliente se ingresaron correctamente')
    
def agregarProductos(codigo,nombre,marca,precio,stock):
    producto_codigo.append(codigo)
    producto_nombre.append(nombre)    
    producto_marca.append(marca)
    producto_precio.append(precio)
    producto_stock.append(stock)
    producto_cantidad_vendida.append(0)
    print('Los datos del producto se ingresaron correctamente')

def agregarVenta(codigoCV,nombreCV,nombrePV):
    cliente_codigo_venta.append(codigoCV)
    nombre_cliente_venta.append(nombreCV)
    nombre_producto_venta.append(nombrePV)



def cargarCliente():
    while True:
        codigo = int(input('Ingrese el codigo de su cliente' ))
        nombre = input('Ingrese el nombre de su cliente ')
        apellido = input('Ingrese el apellido de su cliente ')
        obrasocial = int(input('Su cliente tiene obra social ? \nSI = 1 \nNO = 0\n'))
        if obrasocial == 1:
            obrasocialNombre = input('Ingrese el nombre de la obra social su cliente')
            agregarClientes(codigo,nombre,apellido,obrasocial,obrasocialNombre)
            print(cliente_codigo,cliente_nombre,cliente_apellido,cliente_obraSocial,cliente_nombreObraSocial,cliente_cantidad_vendida,cliente_venta_total_pesos)
        else:
            obrasocialNombre = 0
            agregarClientes(codigo,nombre,apellido,obrasocial,obrasocialNombre)
            print(cliente_codigo,cliente_nombre,cliente_apellido,cliente_obraSocial,cliente_nombreObraSocial,cliente_cantidad_vendida,cliente_venta_total_pesos)
        user = int(input('Desea agregar otro cliente ? \nSI = 1 \nNO = 0\n'))
        if user == 0:
            break

def cargarProducto():
    while True:
        codigo = int(input('Ingrese el codigo de su producto '))
        nombre = input('Ingrese el nombre de su producto ')
        marca = input('Ingrese la marca de su producto ')
        precio = int(input('Ingrese el precio de su producto '))
        stock = int(input('Ingrese el stock de su producto '))
        agregarProductos(codigo,nombre,marca,precio,stock)        
        user = int(input('Desea agregar otro producto ? \nSI = 1 \nNO = 0\n'))
        print(producto_codigo,producto_nombre,producto_marca,producto_precio,producto_stock,producto_cantidad_vendida)
        if user == 0:
            break

def cargarVenta():
    while True:
        user = int(input('Ingrese el codigo de su cliente: ' ))
        posCliente = buscarCliente(user)
        if posCliente != -1:
            print(f'Su cliente fue encontrado y es {cliente_nombre[posCliente]}')
            user = int(input('Ingrese el codigo del producto que desea vender: ' ))
            posProducto = buscarProducto(user)
            if posProducto != -1:
                print(f'Su producto fue encontrado y es {producto_nombre[posProducto]}')
                cantidad = int(input('Ingrese la cantidad que desea vender: '))
                if cantidad <= producto_stock[posProducto]:
                    agregarVenta(cliente_codigo[posCliente],cliente_nombre[posCliente],producto_nombre[posProducto])
                    if cliente_obraSocial[posCliente] == 1:
                        print(f'Su cliente posee obtra social y es {cliente_nombreObraSocial[posCliente]}')
                        print('Por lo tanto tiene un 40 porciento de descuento')

                        subtotal = cantidad * producto_precio[posProducto]
                        total = int(subtotal - 40 * subtotal/100)
                        descuento_venta.append(40)
                        precio_total_venta.append(total)
                        cliente_cantidad_vendida.append(cantidad)
                        cliente_venta_total_pesos[posCliente] += total
                        actualizarStock(user, cantidad)
                        print(cliente_codigo_venta,nombre_cliente_venta,nombre_producto_venta,descuento_venta,precio_total_venta)
                        print(f'producto stock:{producto_stock} cantidad : {producto_cantidad_vendida}')
                        print(cliente_venta_total_pesos[posCliente])
                    
                    else:
                        print(f'Su cliente no posee obtra social')
                        subtotal = cantidad * producto_precio[posProducto]
                        descuento_venta.append(0)
                        precio_total_venta.append(subtotal)
                        cliente_cantidad_vendida.append(cantidad)
                        actualizarStock(user, cantidad)
                        
                        cliente_venta_total_pesos[posCliente] += subtotal
                        print(cliente_codigo_venta,nombre_cliente_venta,nombre_producto_venta,descuento_venta,precio_total_venta)
                        print(f'producto stock:{producto_stock} cantidad : {producto_cantidad_vendida}')
                        print(cliente_venta_total_pesos[posCliente])
                        

                    

            else:
                print('Su producto no fue encontrado intentelo nuevamente')


        else:
            print('Su cliente no fue encontrado intentelo nuevamente')

        
        user = int(input('Desea hacer otra venta ? \nSI = 1 \nNO = 0\n'))        
        if user == 0:
            break
