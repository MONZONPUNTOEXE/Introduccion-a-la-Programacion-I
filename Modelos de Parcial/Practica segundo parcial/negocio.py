# Productos
producto_codigo = [1, 2, 3, 4]
producto_nombre = ['Paracetamol', 'Ibuprofeno', 'Calmante', 'bayaspirina']
producto_marca = ['Tafirol', 'Actron 600', 'Anaflex', 'bayer']
producto_precio = [200, 250, 500, 100]
producto_stock = [500, 200, 100, 400]

# Clientes
cliente_codigo = [10, 20, 30]
cliente_nombre = ['Beto', 'Jose', 'MArcelin']
cliente_obra = [0, 1, 1]
cliente_nombre_obra = ['', 'Osde', 'Pilin']

# Venta
venta_cliente_codigo = [10,10,20,10,30]
venta_producto_codigo = [1,4,4,3,2]
venta_producto_cantidad = [0, 0, 0, 0]
venta_descuento = []
venta_precio_total = [2000, 760.0, 760.0,24,342]

def buscarCliente(codigo):
    for i in range(len(cliente_codigo)):
        if codigo == cliente_codigo[i]:
            print(f"Su cliente fue encontrado y es {cliente_nombre[i]}")
            return i
    return -1

def buscarProducto(codigo):
    for i in range(len(producto_codigo)):
        if codigo == producto_codigo[i]:
            print(f"Su producto fue encontrado y es {producto_nombre[i]}")
            return i
    return -1

def actualizarStock(codigo, cantidad):
    posicion = buscarProducto(codigo)
    if posicion != -1:
        venta_producto_cantidad[posicion] += cantidad
        producto_stock[posicion] -= cantidad
        print("EL STOCK A SIDO ACTUALIZADO CORRECTAMENTE")
    else:
        print("EL PRODUCTO NO SE AH ENCONTRADO")

def cargarCliente():
    noFinalizado = True
    while noFinalizado:
        cliente_codigo.append(int(input("Ingrese el codigo del Cliente ")))
        cliente_nombre.append(input("Ingrese el nombre del Cliente "))
        clienteObraNombre = ''
        obra = int(input("Su cliente tiene Obra Social ? SI = 1 NO = 0 : "))
        if obra == 1:
            clienteObraNombre = input("Ingrese el nombre de la Obra Social del Cliente ")
        
        cliente_obra.append(obra)
        cliente_nombre_obra.append(clienteObraNombre)
        
        if (input("Finalizado ? y/n : ") == "y"):
            noFinalizado = False

def cargarProducto():
    noFinalizado = True
    while noFinalizado:
        producto_codigo.append(int(input("Ingrese el codigo del Producto ")))
        producto_nombre.append(input("Ingrese el nombre del Producto "))
        producto_marca.append(input("Ingrese el marca del Producto "))
        producto_precio.append(int(input("Ingrese el precio del Producto ")))
        producto_stock.append(int(input("Ingrese el stock del Producto ")))
        venta_producto_cantidad.append(0)
        
        if (input("Finalizado ? y/n : ") == "y"):
            noFinalizado = False

def cargarVenta():
    noFinalizado = True
    while noFinalizado:
        producto = int(input("Ingrese el codigo del Producto "))
        cliente = int(input("Ingrese el codigo del Cliente "))
        posP = buscarProducto(producto)
        posC = buscarCliente(cliente)
        if (posC and posP) != -1:
            cantidad = int(input("Ingrese la cantidad del Producto que desea vender: "))
            if cantidad < producto_stock[posP]:
                precio_total = cantidad * producto_precio[posP]
                actualizarStock(producto, cantidad)
                descuento = 0
                if cliente_obra[posC] == 1:
                    print(f"Su cliente posee la obra social {cliente_nombre_obra[posC]} por lo tanto tiene un descuento del 40%")
                    descuento = 40
                    aux = precio_total * descuento / 100
                    precio_total = aux - descuento
                venta_cliente_codigo.append(cliente_codigo[posC])
                venta_producto_codigo.append(producto_codigo[posP])
                venta_descuento.append(descuento)
                venta_precio_total.append(precio_total)
            else:
                print("La cantidad excede la cantidad del stock total, intentelo nuevamente")
        else:
            print("Hubo un error a encontrar los productos y cliente intentelo nuevamente")        

        if (input("Finalizado ? y/n : ") == "y"):
            noFinalizado = False

def ventasOrdenadas():
    for h in range(len(venta_precio_total)-1):
        for i in range(len(venta_precio_total)-1):
            if venta_precio_total[i] < venta_precio_total[i + 1]:
                aux = venta_precio_total[i]
                venta_precio_total[i] = venta_precio_total[i+1]
                venta_precio_total[i+1] = aux
    
    print(venta_precio_total)

def listarCliente():
    cliente = int(input("Ingrese el codigo del Cliente al que desea listar las ventas: "))
    posC = buscarCliente(cliente)
    if posC != -1:
        print(f"Su cliente compro lo siguiente: ")
        for i in range(len(venta_cliente_codigo)):
            if cliente == venta_cliente_codigo[i]:
                print("#################################")
                buscarProducto(venta_producto_codigo[i])
                print(f"Precio de venta: {venta_precio_total[i]} ")
    else:
        print("Su cliente no fue encontrado intentelo de nuevo ")

def promedio():
    cantidad = len(venta_precio_total)
    suma = 0
    for i in range(len(venta_precio_total)):
        suma += venta_precio_total[i]
    promedio = suma / cantidad
    print(f"El promedio de las ventas es: {promedio}")

def clienteSinObra():
    cont = 0
    for i in range(len(cliente_obra)):
        if cliente_obra[i] == 0:
            cont += 1
    print(f"Hay {cont} clientes sin obra social ")

clienteSinObra()