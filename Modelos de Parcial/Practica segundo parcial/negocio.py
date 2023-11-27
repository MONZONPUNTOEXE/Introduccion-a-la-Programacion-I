# Productos
producto_codigo = [10, 20]
producto_nombre = ['ibuprofeno', 'paracetamol']
producto_marca = ['actron 600', 'tafirol']
producto_precio = [500, 200]
producto_stock = [250, 500]
producto_cantidad_vendida = [10, 70]

# Clientes
cliente_codigo = [1, 2, 3]
cliente_nombre = ['franoc', 'nardioc', 'Francccoccco']
cliente_apellido = ['monzon', 'Maodi', 'MAaaario']
cliente_obra_social = [1, 0, 0]
cliente_nombre_obra = ['osde', '', '']
cliente_cantidad_vendida = [10, 70]
cliente_vendida_total = [0, 0, 0]

# Ventas
venta_codigo_cliente = [2, 3, 1]
venta_cliente = ['nardioc', 'Francccoccco', 'franoc']
venta_producto = ['paracetamol', 'ibuprofeno', 'paracetamol']
venta_cantidad = [20, 10, 50]
venta_descuento = [0, 0, 40]
venta_precio_total = [4000, 5000, 6000.0]

def buscarCliente(codigo):
    for i in range(0,len(cliente_codigo)):
        if codigo == cliente_codigo[i]:
            return i
    return -1  

def buscarProducto(codigo):
    for i in range(0,len(producto_codigo)):
        if codigo == producto_codigo[i]:
            return i
    return -1

def cargarCliente(codigo, nombre, apellido, obrasocial,nombreobrasocial):
    cliente_codigo.append(codigo)
    cliente_nombre.append(nombre)
    cliente_apellido.append(apellido)
    cliente_obra_social.append(obrasocial)
    cliente_nombre_obra.append(nombreobrasocial)
    cliente_cantidad_vendida.append(0)
    cliente_vendida_total.append(0)
    print("El cliente fue cargado exitosamente")
    
def cargarProducto(codigo, nombre, marca, precio,stock):
    producto_codigo.append(codigo)
    producto_nombre.append(nombre)
    producto_marca.append(marca)
    producto_precio.append(precio)
    producto_stock.append(stock)
    producto_cantidad_vendida.append(0)
    print("El producto fue cargado exitosamente")
    
def actualizarStock(codigo, cantidad):
    posP = buscarProducto(codigo)
    if posP != -1:
        producto_stock[posP] -= cantidad
        producto_cantidad_vendida[posP] += cantidad
    else: 
        print("Su producto no fue encontrado")
        
def cargarVenta(nombre_cliente, nombre_producto,cantidad_vendida,descuento,total_venta,ventaCodigoCliente):
    venta_codigo_cliente.append(ventaCodigoCliente)
    venta_cliente.append(nombre_cliente)
    venta_producto.append(nombre_producto)
    venta_cantidad.append(cantidad_vendida)
    venta_descuento.append(descuento)
    venta_precio_total.append(total_venta)
    
def clienteNuevo():
    while True:
        codigo = int(input("Ingrese el codigo del Cliente:"))
        nombre = input("Ingrese el nombre del Cliente: ")
        apellido = input('Ingrese el apellido del Cliente: ')
        user = int(input("Su cliente tiene Obra Social ? SI = 0 NO = 1"))
        cliente_obra_social = 0        
        cliente_nombre_obra = ''
        if user == 0:            
            cliente_obra_social = 1
            cliente_nombre_obra = input("Ingrese el nombre de la obra social: ")
            
        cargarCliente(codigo, nombre, apellido, cliente_obra_social,cliente_nombre_obra)
        
        
        user = input("Desea ingresar otro cliente? SI = 0 NO = 1")
        if user == 1:
            break
        
def productoNuevo():
    while True:
        codigo = int(input("Ingrese el codigo del Producto:"))
        nombre = input("Ingrese el nombre del Producto: ")
        marca = input('Ingrese el marca del Producto: ')
        precio = int(input("Ingrese el precio del Producto:"))
        stock = int(input("Ingrese el stock del Producto:"))

        cargarProducto(codigo, nombre, marca, precio,stock)       
        user = input("Desea ingresar otro Producto? SI = 0 NO = 1")
        if user == 1:
            break
        
def ventaNueva():
    while True:
        print("Inicio de proceso de venta!")
        
        codigoC = int(input("Ingrese el codigo del cliente al que desea vender: "))
        codigoP = int(input("Ingrese el codigo del producto que desea vender: "))
        posC = buscarCliente(codigoC)
        posP = buscarProducto(codigoP)
        if (posC and posP) != -1:
            nombre_cliente = cliente_nombre[posC]
            nombre_producto = producto_nombre[posP]
            print(f"Su cliente es: {nombre_cliente}")
            print(f"Su producto es: {nombre_producto}")            
            cantidad = int(input("Ingrese la cantidad del producto que desea vender: "))
            if cantidad < producto_stock[posP]:
                total_venta = cantidad * producto_precio[posP]
                descuento = 0
                if cliente_obra_social[posC] == 1:
                    print("Su cliente tiene obra social")
                    descuento = 40
                    subtotal = cantidad * producto_precio[posP] * descuento / 100
                    total_venta = cantidad * producto_precio[posP] - subtotal
                    
                venta_codigo_cliente = cliente_codigo[posC]
                print(f"El total es: {total_venta}")        
                cargarVenta(nombre_cliente, nombre_producto,cantidad,descuento,total_venta,venta_codigo_cliente)
                actualizarStock(codigoP, cantidad)
        else:
            print("No se econtro, intentelo mas tarde")
      
        user = int(input("Desea ingresar otro Producto? SI = 0 NO = 1"))
        if user == 1:
            break
        
def listaOrdenada():
    for h in range(0,len(venta_precio_total)-1):
        for i in range(0,len(venta_precio_total)-1):
            if venta_precio_total[i] >  venta_precio_total[i + 1]:
                aux = venta_precio_total[i]
                venta_precio_total[i] =  venta_precio_total[i+1]
                venta_precio_total[i + 1] = aux
    print(venta_precio_total)
    
def listarVentaXCliente():
    while True:
        codigoC = int(input("Ingrese el codigo del cliente al que desea buscar: "))
        posC = buscarCliente(codigoC)
        if posC != -1:
            nombre_cliente = cliente_nombre[posC]
            print(f"Su cliente es: {nombre_cliente}")
            for i in range(0, len(venta_codigo_cliente)):
                if venta_codigo_cliente[i] == cliente_codigo[posC]:
                    print(f"###################################")
                    print(f"Producto:  {venta_producto[i]}")
                    print(f"Precio total:  {venta_precio_total[i]}")
        else:
            print('No se encontro tu busqueda')
        
        user = int(input("Desea ingresar hacer otra busqueda? SI = 0 NO = 1"))
        if user == 1:
            break

def ventaMaxima():
    for i in range(0,len(venta_precio_total)-1):
        if venta_precio_total[i] <  venta_precio_total[i + 1]:
            aux = venta_precio_total[i + 1]
            cliente = venta_codigo_cliente[i]    
    pos = buscarCliente(cliente)
        
    print(f'La venta maxima fue de: {aux}')
    print(f'Y la realizo: {cliente_nombre[pos]}')

ventaMaxima()