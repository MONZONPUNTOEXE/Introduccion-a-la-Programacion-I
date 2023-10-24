# Codigo del profesor agregar, buscar, modificar productos

listaCodigo = []
listaDescripcion = []
listaPrecio = []
listaStock = []
listaVentas = []





def cargarProducto():
    listaCodigo.append(int(input('Ingrese un codigo')))
    listaDescripcion.append(input('Ingrese una descripcion'))
    listaPrecio.append(int(input('Ingrese el precio')))
    listaStock.append(int(input('ingrese el stock')))
    listaVentas.append(0)


def buscarProducto(codigo):
    for i in range(0, len(listaCodigo)):
        if codigo == listaCodigo[i]:
            return i
    return -1



def buscarProductoNombre(des):
    for i in range(0,len(listaDescripcion)):
        if  des == listaDescripcion[i]:
            return i
    return -1



def vender():
    print("Hola que queres vender")
    codigo = int(input('Ingrese el codigo del producto para la venta '))
    pos = buscarProducto(codigo)
    if pos != -1:
        print("El producto es ",  listaDescripcion[pos])
        cantidad = int(input("que cantidad queres vender ? "))
        if cantidad  <= listaStock[pos]:
            precio  = cantidad *  listaPrecio[pos]
            print("El total de la venta es  " , precio)
            listaStock[pos] = listaStock[pos] - cantidad
            listaVentas[pos] = cantidad
        else:
            print("El valor solicitado es mayor a la cantidad de stock")
    else:
         print("producto no encontrado")





def actualizarProducto(codigo):
      pos =  buscarProducto(codigo)
      if pos != -1:
          stockNuevo = int(input('Ingrese un nuevo stock'))
          precioNuevo = int(input('Ingrese un nuevo Precio'))
          listaStock[pos] = stockNuevo
          listaPrecio[pos] = precioNuevo
      else:
          print('Producto no encontrado')






menu = """
1- cargar productos
2- vender

"""





# JavierM