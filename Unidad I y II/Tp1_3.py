count = 0
count2 = 0

acu = 0
acu2 = 0

for i in range (0, 10):
    n = int(input())
    # if n/2 == int(n/2) : print("par")
    # elif n/2 != int(n/2) : print("impar")
    if n/2 == int(n/2) :
        count = count + 1
        acu = acu + n
    elif n/2 != int(n/2) : 
        count2 = count2 + 1
        acu2 = acu2 + n

print("Ingresaste", count,"números Pares y", count2, "números Impares")
print("El promedio de los números Pares es:", acu/count, "y el promedio de los números impares es:", acu2/count2)