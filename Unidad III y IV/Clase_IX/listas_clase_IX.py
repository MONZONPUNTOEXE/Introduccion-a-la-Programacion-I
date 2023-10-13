# Listas, Array
codigos = ['ASD1', 'ASD2', 'ASD6', 'ASD5']
nombres = ['Juan', 'Marcelo', 'Gerard', 'Ernesto']
sueldos = [3000, 4000, 5000, 3000]


primer_while = True

while primer_while:
    codigo = input("Introduzca el ID de la persona:\n")
    codigos.append(codigo)
    print(codigos)

    nombre = input("Introduzca el nombre de la persona:\n")
    nombres.append(nombre)
    print(nombres)

    sueldo = int(input("Introduzca el sueldo:\n"))
    sueldos.append(sueldo)
    print(sueldos)

    primer_while = input("Desea ingresar otra palabra y/n:\n")
    if primer_while == "n":
        primer_while = False



user_buscar = input("Introduzca el codigo que desea buscar: ")

for i in range(len(codigos)):
    if nombres[i] == user_buscar:
        print("Su codigo fue encontrado exitosamente y es:",codigos[i])
        print("Su ubicación es:", [i + 1])
        print("Su nombre es:", nombres[i])
        print("Su sueldo es", sueldos[i])