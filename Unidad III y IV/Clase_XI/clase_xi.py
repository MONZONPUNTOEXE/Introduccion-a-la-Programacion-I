lista = [70,90 ,0, 80,60,85]
# lista = [70,90 ,0, 80,60,< 85]

# Guardamos en contador el valor de los elementos de la lista
count = len(lista) - 1

for i in range (0,count):
    for j in range (0,count):
        if lista[j] > lista[j + 1]:
                numero = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = numero

print(lista)
