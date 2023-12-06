# Clientes
cliente_codigo = [10, 20]
cliente_nombre = ['Albert', 'Goku']
cliente_apellido = ['Aistani', 'Son']
cliente_obra = [1, 0]
cliente_obra_nombre = ['OSde', '']

# Productos
producto_codigo = [1, 2]
producto_nombre = ['manzana', 'Naranja']
producto_marca = ['pirulo', 'maddga']
producto_precio = [500, 250]
producto_stock = [200, 500]
producto_cantidad_vendida = [0, 0]

# Ventas
venta_cliente_codigo = []
venta_producto_codigo = []
venta_producto_precio_total = []
venta_descuento = []

def buscarCliente(codigo):
    for i in range(0,len(cliente_codigo)):
        if codigo == cliente_codigo[i]:
            print(f"Su cliente fue encontrado y es: {cliente_nombre[i]}")
            return i
    return -1

def buscarProducto(codigo):
    for i in range(0,len(producto_codigo)):
        if codigo == producto_codigo[i]:
            print(f"Su producto fue encontrado y es: {producto_nombre[i]}")
            return i
    return -1

def actualizarStock(codigo, cantidad):
    pos = buscarProducto(codigo)
    if pos != -1:
        producto_stock[pos] -= cantidad
        producto_cantidad_vendida[pos] += cantidad

def cargarCliente():
    finalizado = True
    while finalizado:
        cliente_codigo.append(int(input("Ingrese el Codigo de su Cliente: ")))
        cliente_nombre.append(input("Ingrese el Nombre de su Cliente: "))
        cliente_apellido.append(input("Ingrese el Apellido de su Cliente: "))
        obra = 0
        nombreObra = ''
        if ((input("Su cliente tiene Obra Social ? y/n ") == "y")):
            obra = 1
            nombreObra = input('Ingrese el nombre de la obra social: ')
        
        cliente_obra.append(obra)
        cliente_obra_nombre.append(nombreObra)
        if (input("Desea Finalizar ? y/n : ") == "y"):
            finalizado = False            
            
def cargarProducto():
    finalizado = True
    while finalizado:
        producto_codigo.append(int(input("Ingrese el Codigo de su Producto: ")))
        producto_nombre.append(input("Ingrese el Nombre de su Producto: "))
        producto_marca.append(input("Ingrese la marca de su Producto: "))
        producto_precio.append(int(input("Ingrese el precio de su Producto: ")))
        producto_stock.append(int(input("Ingrese el stock de su Producto: ")))
        producto_cantidad_vendida.append(0)        
        if (input("Desea Finalizar ? y/n : ") == "y"):
            finalizado = False
            
def cargarVenta():
    finalizado = True
    while finalizado:
        cliente = int(input("Ingrese el Codigo del cliente que desea vender: "))
        producto = int(input("Ingrese el Codigo del producto que desea vender: "))
        posC = buscarCliente(cliente)
        posP = buscarProducto(producto)
        if posC != -1 and posP != -1:
            cantidad = int(input('Ingrese la cantidad que desea comprar'))
            if cantidad < producto_stock[posP]:
                total = producto_precio[posP] * cantidad
                descuento = 0
                actualizarStock(producto, cantidad)
                if cliente_obra[posP] == 1:
                    print(f"Su cliente tiene Obra social y es: {cliente_obra_nombre[posP]}")
                    print(f"por lo tanto tiene un descuento del 40%")
                    descuento = 40
                    aux = total * 40 / 100
                    total = total - aux
                    
                print(f"El valor de la compra total es de: {total}")
                venta_cliente_codigo.append(cliente_codigo[posC])
                venta_producto_codigo.append(producto_codigo[posP])
                venta_producto_precio_total.append(total)
                venta_descuento.append(descuento)
            else:
                print("El Producto supera el stock maximo, intentelo nuevamente")
        else:
            print("El Producto no fue encontrado, intentelo nuevamente")
        if (input("Desea Finalizar ? y/n : ") == "y"):
            finalizado = False


cargarVenta()