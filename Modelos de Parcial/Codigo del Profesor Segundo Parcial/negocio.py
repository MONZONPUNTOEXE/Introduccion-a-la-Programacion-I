listaClienteNombre = []
listaClienteCodigo = []
listaClienteCantidadVenta = []
llistaClienteTotalComprasPesos = []

listaProductoNombre = []
listaProductoCodigo = []
listaProductoPrecio = []
listaProductoStock = []
listaProductoCantVendida = []


listaNoClienteNombre = []
listaNoClienteProducto = []
listaNoClienteCantidad = []
listaNoClienteTotal = []

listaVentaClienteCodigo  = []
listaVentaProductoCodigo  = []
listaVentaCantidad  = []
listaVentaTotal  = []


def getProducto(codigo):
    for i in range(0, len(listaProductoCodigo)):
        if codigo == listaProductoCodigo[i]:
            return i
    return -1 

def getCliente(codigo):
    for i in range(0, len(listaClienteCodigo)):
        print(i)
        if codigo == listaClienteCodigo[i]:
            return i 
    return -1


def updateStock(cantidad, codigo):
    pos = getProducto(codigo)
    if pos != -1:
        listaProductoStock[pos] -= cantidad
        listaProductoCantVendida[pos] += cantidad
    else:
        print('Producto no encontrado')


def saveVentaCliente(cliente, producto, cantidad, total ):
     listaVentaClienteCodigo.append(cliente)
     listaVentaProductoCodigo.append(producto)
     listaVentaCantidad.append(cantidad)
     listaVentaTotal.append(total)
     print('El proceso de venta se genero correctamente')


def saveVentaNoCliente(cliente, producto, cantidad, total ):
     listaNoClienteNombre.append(cliente)
     listaNoClienteProducto.append(producto)
     listaNoClienteCantidad.append(cantidad)
     listaNoClienteTotal.append(total)
     print('El proceso de venta se genero correctamente')


def saveCliente(nombre, codigo):
     listaClienteCodigo.append(codigo)
     listaClienteNombre.append(nombre)
     listaClienteCantidadVenta.append(0)
     llistaClienteTotalComprasPesos.append(0)
    
def saveProducto(nombre, codigo, precio, stock):
    listaProductoNombre.append(nombre)
    listaProductoCodigo.append(codigo)
    listaProductoPrecio.append(precio)
    listaProductoStock.append(stock)
    listaProductoCantVendida.append(0)


#funcion para cargar los cliente por telcado 
def cargarClienteTeclado():
    print('Incicio del proceso de carga de cliente')
    carga = True
    while carga:
          nombre = input('Ingrese un nombre ')
          codigo = int(input('Ingrese un codigo '))
          saveCliente(nombre, codigo)
          nuevo =int(input('Nuevo ingreso ? 1-Si  2-No ') )      
          if(nuevo == 2):
              carga = False
    print('Fin')

# funcion para cargar los producto por teclado 
def cargarProdcutoTeclado():
    print('Incio del proceso de carga de producto')
    carga= True
    while carga:
        nombre= input('Ingrese el nombre del producto ')
        codigo = int(input('Ingrese el codigo del producto '))
        stock = int(input('Ingrese el stock '))
        precio =  int(input('Ingrese el precio del producto '))
        saveProducto(nombre, codigo, stock, precio)
        nuevo = int(input('Nuevo ingreso ? 1-Si  2-No '))
        if(nuevo == 2):
            carga = False
    print('Fin')


    
def ventaCliente():
    print('Incio del proceso venta de cliente ')
    codigo= int(input('Ingrese el codigo del cliente '))
    posCliente = getCliente(codigo)
    if posCliente != -1:
        print("Venta para  " , listaClienteNombre[posCliente])
        codigoProducto= int(input('Ingrese el codigo del producto '))
        posProducto = getProducto(codigoProducto)
        print('Producto para vender  ' , listaProductoNombre[posProducto])
        cantidad = int(input('Ingrese la cantidad '))
        if (cantidad <= listaProductoStock[posProducto]):
            #verifico la cantidad de ventas para ver si aplica descuento
            cantVentas = listaClienteCantidadVenta[posCliente]
            descuento = 0
            precioTotalDeLaVenta = listaProductoPrecio[posProducto] * cantidad
            if(cantVentas > 10):
                descuento = int(input('Ingrese el descuento ')) 
                #le saco el descuento 
                precioTotalDeLaVenta = (precioTotalDeLaVenta * descuento ) /100
            print("El total de la venta es ", precioTotalDeLaVenta)
            #guardo la venta 
            saveVentaCliente(posCliente,posProducto,cantidad, precioTotalDeLaVenta)
            #actualizo el stock
            updateStock(cantidad,codigoProducto)
            # sumo una venta al cliente 
            listaClienteCantidadVenta[posCliente] += 1
            # voy acumluando el total de las venta del cliente
            llistaClienteTotalComprasPesos[posCliente] += precioTotalDeLaVenta
        else:
            print('La cantidad solicitada supera el stock del producto')  
    else:
            print('Cliente no encontrado')  


def ventaNoCliente():
    print('Incio del proceso venta de no cliente')
    cliente = input('Ingrese el nombre del cliente ')
    codigoProducto= int(input('Ingrese el codigo del producto '))
    posProducto = getProducto(codigoProducto)
    print('Producto para vender  ' , listaProductoNombre[posProducto])
    cantidad = int(input('Ingrese la cantidad '))
    if (cantidad <= listaProductoStock[posProducto]):
        precioTotalDeLaVenta = listaProductoPrecio[posProducto] *  cantidad
        print("El total de la venta es ", precioTotalDeLaVenta)
        #guardo el la venta de los no cliente 
        saveVentaNoCliente(cliente,codigoProducto,cantidad,precioTotalDeLaVenta)
        updateStock(cantidad,codigoProducto)
    else:
        print('La cantidad solicitada supera el stock del producto')  



def  listarClientes():
    for i in range(0, len(listaClienteNombre)):
        print("Cliente " ,listaClienteNombre[i] , " -  Codigo" ,
              listaClienteCodigo[i], " -  Cantidad de compras" ,
              listaClienteCantidadVenta[i] , " -  Total acumulado" ,
              llistaClienteTotalComprasPesos[i]
              )


def listarProductos():
    for i in range(0, len(listaProductoNombre)):
        print("Producto " ,listaProductoNombre[i]  ," - Codigo",
                listaProductoCodigo[i]  ," -  Precio",
                listaProductoPrecio[i]  ," -  Stock",
                listaProductoStock[i]  ," - Cantidad Vendidas",
                listaProductoCantVendida[i])
        




def mostrarClienteConMayoresCompras():
    for i in range(0, len(listaClienteCantidadVenta)-1):
        for a  in range(0, len(listaClienteCantidadVenta)-1):
            if  listaClienteCantidadVenta[a] < listaClienteCantidadVenta[a+1]:
                aux = listaClienteCantidadVenta[a]
                listaClienteCantidadVenta[a] = listaClienteCantidadVenta[a+1]
                listaClienteCantidadVenta[a+1] =aux
    listarClientes() 



def mostraVentasXclientes():
    codigo = int(input('Ingrese el codigo de busqueda '))
    for i in range(0, len(listaClienteCodigo)):
        if codigo == listaClienteCodigo[i]:
            print("Cliente " ,listaClienteNombre[i] , " -  Codigo" ,
              listaClienteCodigo[i], " -  Cantidad de compras" ,
              listaClienteCantidadVenta[i] , " -  Total acumulado" ,
              llistaClienteTotalComprasPesos[i]
              )