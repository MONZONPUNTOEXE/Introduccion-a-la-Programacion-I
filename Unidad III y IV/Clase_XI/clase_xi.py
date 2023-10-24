# Necesitamos ordenar esta lista de menor a mayor
lista = [70,90 ,0, 80,60,85]

# La idea es ir por bloques dentro de nuestra lista para poder ordenarla
# para ello podemos comparar entre 2 indices.
# por ejemplo por 70 y 90.
# comparamos 70 y 90 con un <
# 70 < 90 es verdadero entonce dejamos la lista tal cual esta
# Vamos con la segunda:
# 90 < 0 es falso. Lo que tendria que hacer mi algoritmo es cambiar de lugar el 90 por el cero
# y quedaria asi [70,0 ,90, 80,60,85]
# Vamos comparando en 2 en 2 hasta que nuestra lista quede ordenada.
# Tenemos que tener en cuenta que deje como este el ultimo indice de la lista.   

# lista = [70,90 ,0, 80,60,< 85]

# Guardamos en contador el valor de los elementos de la lista
count = len(lista) - 1

# Creamos 2 bucles 
# En el segundo le decimos que itere otra letra, esta vuelta se eligio "j" pero puede ser cualquira
for i in range (0,count):
    for j in range (0,count):
        # Le indicamos que si un indice es mayor al indice de la derecha
        if lista[j] > lista[j + 1]:
                # Ejecute este código:
                numero = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = numero

print(lista)
