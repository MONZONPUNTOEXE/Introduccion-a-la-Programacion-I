# Esto lo corregimos en clase

maximo = 0
maximo2 = 0
pos_maximo = 0
pos_maximo2 = 0


for i in range(0, 4):
    num = int(input("Por favor ingrese un número: "))
    if i == 0:
        maximo = num
        maximo2 = num
        pos_maximo = i+1
        pos_maximo2 = i+1
    if num > maximo:
        maximo2 = maximo
        pos_maximo2 = pos_maximo

        maximo = num
        pos_maximo = i+1
    elif num > maximo2:
        maximo2 = num
        pos_maximo2 = i + 1
        
print("El número mas grande ingresado es el:", maximo,"y su posición es:", pos_maximo,"Y el segundo mas grande es el:", maximo2, "y su posición es:", pos_maximo2);



# ----------------- Lo de abajo hice yo no esta del todo bien -----------------------
# maximo = 0
# maximo2 = 0
# pos_maximo = 0
# pos_maximo2 = 0


# for i in range(0, 10):
#     num = int(input("Por favor ingrese un número: "))
#     if i == 0:
#         maximo = num
#         maximo2 = num
#         pos_maximo = i+1
#         pos_maximo2 = i+1
#     elif num > maximo:
#         maximo = num
#         pos_maximo = i+1
#     elif num > maximo2:
#         maximo2 = num
#         pos_maximo2 = i + 1
        
# print("El número mas grande ingresado es el:", maximo,"y su posición es:", pos_maximo,"Y el segundo mas grande es el:", maximo2, "y su posición es:", pos_maximo2);