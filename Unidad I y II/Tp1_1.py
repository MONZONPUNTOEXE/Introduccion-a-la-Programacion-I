n = 0
count = 0
acu = 0

# iteramos 10 veces para que el usuario pueda ingresar un numero 10 veces

for i in range (0,10):
    n = int(input("Ingrese un numero"));
    if n > 10:
        count = count + 1
        acu = acu + n
    
if count == 1 : print("En el lote hay un solo número mayor a 10 y el promedio es", acu/count)
elif count > 0 : print("En el lote, hay", count, "números mayores a 10 y el promedio es", acu/count)
else: print ("En el lote, no se encontraron números mayores a 10. Por lo tanto no se puede promediar")