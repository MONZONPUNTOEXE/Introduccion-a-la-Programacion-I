def sistemaAlfajores():
    i = 1
    unidad = 0
    caja = 0
    unidad_precio = 0.5
    caja_precio = 5

    cant_alfajores = int(input("Ingrese la cantidad de alfajores "));

    while i <= cant_alfajores:
        if i % 12 == 0:
            caja += 1
        elif i % 12 != 0:
            unidad += 1
        i += 1

    unidades = cant_alfajores - caja * 12
    subtotal_caja = caja * caja_precio
    subtotal_unidades = unidades*unidad_precio
    global total
    total = subtotal_caja + subtotal_unidades
    

    print("unidades =", unidades,"caja =", caja);
    print("El cliente compró por caja la cantidad de:", caja, "\n" "Por unidad la cantidad de:", unidades);
    print("Por lo tanto el subtotal por caja es de:", subtotal_caja,"Pesos" "\n" "y por unidad es de:", subtotal_unidades, "Pesos");
    print("********************* El total a pagar es de:", total, "*********************" )
    
def ventaMayor():
    venta_mayor = 0
    
    if total > venta_mayor:
        venta_mayor = total

    print("La venta mayor fue de:",int(venta_mayor),"Pesos")


