################ LISTA CARGADA #################

# Productos
producto_codigo = [10, 20]
producto_nombre = ['Actron 600', 'paracetamol']
producto_marca = ['bayer', 'Tafirol Forte']
producto_precio = [260, 150]
producto_stock = [100, 200]
producto_cantidad_vendida = [100, 100]

# Clientes
cliente_codigo = [1, 2]
cliente_nombre = ['Franco', 'Marcelo']
cliente_apellido = ['Monzon', 'Polino']
cliente_obraSocial = [1,0]
cliente_nombreObraSocial = ['Osde', ' ']
cliente_cantidad_vendida = [2, 2]
cliente_venta_total_pesos = [12300, 20500]

# Ventas
cliente_codigo_venta = [1, 2, 1, 2]
nombre_cliente_venta = ['Franco', 'Marcelo', 'Franco', 'Marcelo']
nombre_producto_venta = ['Actron 600', 'Actron 600', 'paracetamol', 'paracetamol']
descuento_venta = [40, 0, 40, 0]
precio_total_venta = [13000, 7000, 7500, 7800]

# Clientes sin obra social
cantidadDeClienteSinObraN = []
cantidadDeClienteSinObraA = []


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
        codigo = int(input('Ingrese el codigo de su cliente ' ))
        nombre = input('Ingrese el nombre de su cliente ')
        apellido = input('Ingrese el apellido de su cliente ')
        obrasocial = int(input('Su cliente tiene obra social ? \nSI = 1 \nNO = 0\n'))
        if obrasocial == 1:
            obrasocialNombre = input('Ingrese el nombre de la obra social su cliente')
            agregarClientes(codigo,nombre,apellido,obrasocial,obrasocialNombre)
        else:
            obrasocialNombre = ' '
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
        if user == 0:
            break

def cargarVenta():
    while True:
        user = int(input('Ingrese el codigo de su cliente: ' ))
        posCliente = buscarCliente(user)
        userP = int(input('Ingrese el codigo del producto que desea vender: ' ))
        posProducto = buscarProducto(userP)
        if (posCliente and posProducto) != -1:
            print(f'Su cliente fue encontrado y es {cliente_nombre[posCliente]}')
            print(f'Su producto fue encontrado y es {producto_nombre[posProducto]}')
            cantidad = int(input('Ingrese la cantidad que desea vender: '))
            if cantidad <= producto_stock[posProducto]:
                agregarVenta(cliente_codigo[posCliente],cliente_nombre[posCliente],producto_nombre[posProducto])
                total = cantidad * producto_precio[posProducto]
                descuento = 0
                if cliente_obraSocial[posCliente] == 1:
                    print(f'Su cliente posee obra social y es {cliente_nombreObraSocial[posCliente]}')
                    print('Por lo tanto tiene un 40 porciento de descuento')
                    descuento = 40
                    subtotal = (cantidad * producto_precio[posProducto])
                    total = int(subtotal - (subtotal * descuento / 100))

                descuento_venta.append(descuento)
                precio_total_venta.append(total)
                cliente_cantidad_vendida[posCliente] += 1
                cliente_venta_total_pesos[posCliente] += total
                actualizarStock(userP, cantidad)                    

            else:
                print('Su producto supera nuestro stock, intentelo nuevamente')


        else:
            print('Su cliente o Producto no fue encontrado intentelo nuevamente')

        
        user = int(input('Desea hacer otra venta ? \nSI = 1 \nNO = 0\n'))        
        if user == 0:
            break

def ordenarVentas():
    for h in range(0,len(precio_total_venta)-1):
        for i in range(0,len(precio_total_venta)-1):
            if precio_total_venta[i] > precio_total_venta[i + 1]:
                aux = precio_total_venta[i]
                precio_total_venta[i] = precio_total_venta[i + 1]
                precio_total_venta[i + 1] = aux            
    print(f'Ordenacion de ventas {precio_total_venta}')

def promedioVentas():
    suma = 0
    for i in range(0,len(precio_total_venta)):
        suma += precio_total_venta[i]
    promedio = suma / len(precio_total_venta)
    print(f'El promedio de las ventas es {int(promedio)}')

def clientesSinObra():
    count = 0
    for i in range(0,len(cliente_obraSocial)):
        if cliente_obraSocial[i] == 0:
            cantidadDeClienteSinObraN.append(cliente_nombre[i])
            cantidadDeClienteSinObraA.append(cliente_apellido[i])
            count += 1
    print(f'Los cantidad de clientes sin obra social son: {count}')
    print(f'Sus nombres son: ')
    for i in range(0,len(cantidadDeClienteSinObraA)):
        print(cantidadDeClienteSinObraN[i],cantidadDeClienteSinObraA[i])

def ventaValorMaximo():
    aux = 0
    for i in range(0,len(precio_total_venta)):
        if precio_total_venta[i] > aux:
            aux = precio_total_venta[i]
            nombreMaximo = nombre_cliente_venta[i]
    print(f'El precio maximo es: {aux}')
    print(f'El nombre es: {nombreMaximo}')
####################################################

def maximos():
    maximo = 0
    maximo_dos = 0
    maximo_cliente = 0
    maximo_dos_cliente = 0
    for i in range(0,len(precio_total_venta)):
        num = precio_total_venta[i]
        codigo = cliente_codigo_venta[i]
        codigo_dos = cliente_codigo_venta[i]
        if num > maximo:
            maximo_dos = maximo
            maximo_dos_cliente = maximo_cliente

            maximo = num
            maximo_cliente = codigo
        elif num > maximo_dos:
            maximo_dos = num
            maximo_dos_cliente = codigo_dos

    print(f'El numero maximo de la lista es: {maximo}')
    print(f'El numero segundo maximo de la lista es: {maximo_dos}')
    print(f'El nombre del cliente de la venta maxima de la lista es: {cliente_nombre[buscarCliente(maximo_cliente)]}')
    print(f'El nombre del cliente de la segunda venta maxima de la lista es: {cliente_nombre[buscarCliente(maximo_dos_cliente)]}')

        