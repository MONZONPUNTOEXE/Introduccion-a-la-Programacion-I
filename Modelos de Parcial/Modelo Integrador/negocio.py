# Productos
producto_codigo = []
producto_nombre  = []
producto_precio = []
producto_precio_cantidad = []
producto_stock = []

# Venta
venta_cliente_nombre = []
venta_producto_nombre = []
venta_cantidad_producto = []
venta_precio_producto = []
venta_total = []

def buscarProducto(codigo):
    for i in range(0,len(producto_codigo)):
        if codigo == producto_codigo[i]:
            print(f"Su producto se ah encontrado y es: {producto_nombre[i]}")
            return i
    return -1

def updateStock(codigo, cantidad):
    pos = buscarProducto(codigo)
    if pos != -1:
        producto_stock[pos] -= cantidad
        venta_cantidad_producto[pos] += cantidad
        print(f"El Stock se actualizo exitosamente:")
    else:
        print("El Producto no se a encontrado para validar el Stock")

def cargarProducto():
    finalizar = True
    while finalizar:
        producto_codigo.append(int(input('Ingrese el codigo de su producto: ')))
        producto_nombre.append(input("Ingrese el nombre de su producto: "))
        producto_precio.append(int(input('Ingrese el precio de su producto: ')))
        producto_precio_cantidad.append(int(input('Ingrese el precio x cantidad de su producto: ')))
        producto_stock.append(int(input('Ingrese el stock de su producto: ')))
        venta_cantidad_producto.append(0)
        if (input("Desea Finalizar ? y/n : ") == "y"):
            finalizar = False
def venta():
    finalizar = True
    while finalizar:
        venta_cliente_nombre.append(input("Ingrese el nombre de su Cliente: "))
        producto = int(input('Ingrese el codigo del producto: '))
        pos = buscarProducto(producto)
        venta_producto_nombre.append(producto_nombre[pos])
        cantidad = int(input('Ingrese la cantidad del producto: '))

        precioProducto = producto_precio[pos]
        total = producto_precio[pos] * cantidad
        if cantidad > 10:
            precioProducto = producto_precio_cantidad[pos]
            total = producto_precio_cantidad[pos] * cantidad
        
        updateStock(producto, cantidad)
        venta_precio_producto.append(precioProducto)
        venta_total.append(total)        
        
        if (input("Desea Finalizar ? y/n : ") == "y"):
            finalizar = False

def listarVentas():
    print(venta_total)

def ordenar():
    for k in range(len(venta_total)-1):
        for i in range(len(venta_total)-1):
            if venta_total[i] > venta_total[i + 1]:
                aux = venta_total[i]
                venta_total[i + 1] = venta_total[i] 
                venta_total[i] = aux
    print(venta_total)

def ventaMayor():
    for k in range(len(venta_total)-1):
        for i in range(len(venta_total)-1):
            if venta_total[i] > venta_total[i + 1]:
                aux = venta_total[i]
            elif venta_total[i] < venta_total[i + 1]:
                aux = venta_total[i + 1]
            
    print(aux)

def listarUltimasVentas():
    for i in range(0,len(venta_total)):
        if i > 1:            
            print(venta_total[i])





