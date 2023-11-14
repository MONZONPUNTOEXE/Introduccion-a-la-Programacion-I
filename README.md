# Introducción a la Programación I
- Lenguaje que vamos a aprender en esta etapa son los conceptos fundamentales de Python
# Python
![](https://logos-world.net/wp-content/uploads/2021/10/Python-Symbol.png)
Contenidos:
- [Unidad I y II](#unidad-i-y-ii)
  - [Clase I](#clase-i)
  - [Clase II y III](#clase-ii-y-iii)
  - [Clase IV](#clase-iv)
  - [Clase V](#clase-v)
  - [Clase VI](#clase-vi)
  - [Clase VII](#clase-vii)
  - [Clase VIII](#clase-viii)
- [Unidad I y III](#unidad-iii-y-iv)
  - [Clase IX](#clase-ix)
  - [Clase X](#clase-x)
  - [Clase XI](#clase-xi)
- [Modelos de Parcial](#)
  - [Primer Parcial](#)
  - [Segundo Parcial](#)
  - [Recuperatorio de Primer y Segundo Parcial](#)
  - [Integrador](#)
  - [Final](#)

# Unidad I y II
## Clase I
- Tuvimos la presentación de la materia
- Vimos un poco de lógica con Psint
## [Clase II y III](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/tree/main/Unidad%20I%20y%20II/Clase_II_y_III)
> - En esta clase dimos nuestros primeros pasos con las condicionales e iteraciones exactas.<br>
> - [Codigo de la actividad](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_II_y_III/app.py)<br>
> Aprendimos a Declarar las variables:
```
numero = 10
numero1 = 1
numero2 = 7

> Sumar y promediar numeros:

suma = numero + numero1 + numero2

# Dividimos por 3 (para poder promediar es suma total de los números, dividido por la cantidad de números)
total = suma/3
```
> Imprimir por pantalla los resultados:
```
  # Imprimimos
print ( "la suma es ", suma)
print ("el promedio es", total)
```
> Condicionales<br>
> - [Codigo de la actividad](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_II_y_III/app.py)
```
numero = 12
if numero > 15: print ("Es mayor")
else: print("el numero es menor")
```
- Todo junto se veria así
> - [Codigo de la actividad](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_II_y_III/app3.py)
```
## Declaracion de las variables
# nota = 2
# nota1 = 4
# nota2 = 4

nota = int(input(4))
nota1 = int(input(5))
nota2 = int(input(6))

# Sumamos las variables
suma = nota + nota1 + nota2
# Dividimos la suma por el total de variables
promedio = suma/3
# Imprimimos
print(promedio);

# Usamos las condicionales
if promedio >= 7: print("Promocion");
elif promedio >= 4 and promedio <= 6 : print("Aprueba");
else: print("Recursa");
```
> Iteraciones exactas con "for"
> - [Codigo de la actividad](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_II_y_III/app4.py)
```
numero = 0
pepapig = 0
promedio= 0

for i in range (0,3):
    numero= int(input())
    pepapig = pepapig + numero

promedio= pepapig/3
print(promedio)
```
## Clase IV
- En esta clase profundizamos los conceptos de las condicionales, los bucles exactos "for", operadores lógicos y matematicos
- Ejercitamos buscando el maximo y segundo maximo de un lote de números y calculando sueldos usando condicionales
- [Ejercicios de la clase IV](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_IV/readme.md)
- [Codigo del ejercicio Maximo y 2do Maximo "A" resuelto](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_IV/Clase-4-tarea-A.py)
- [Codigo del ejercicio Calcular Sueldos "B" resuelto](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_IV/Clase-4-tarea-B.py)
## Clase V
- Esta vuelta vimos funciones y bucles inexactos (while)
- [Bucle inexacto while](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_V/clase-5.py)
- [Funciones](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_V/clase-5-funciones.py)
## Clase VI
- Vimos como crear un menu, modulo principal y archivo de funciones
- Tambien repasamos los temas vistos en clase
## Clase VII
- Practicamos antes del Parcial
- [Enunciados de los ejercicios](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_VII_Practica-para-parcial/readme.md)
> El codigo esta comentado
- [Codigo de ejercicio 1 (suma de números pares) resuelto](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_VII_Practica-para-parcial/Punto_1/main.py)
- [Codigo de ejercicio 2 (horas trabajadas) resuelto](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_VII_Practica-para-parcial/Punto_2/main.py)
- [Codigo de ejercicio 3 (venta de alfajores) resuelto](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/tree/main/Unidad%20I%20y%20II/Clase_VII_Practica-para-parcial/Punto_3)
  - [main](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_VII_Practica-para-parcial/Punto_3/main.py)
  - [negocio](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_VII_Practica-para-parcial/Punto_3/negocio.py)
  - [utils](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_VII_Practica-para-parcial/Punto_3/utils.py)  
# Unidad III y IV
## Clase VIII
- La clase fue toda de practica (No realizado)
- [Enunciado del ejercicio](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Clase_VIII_Practica/ejercicios_clase_VIII.md)
- NO REALIZADO
## Clase IX
- En esta clase vimos Listas
- [Listas aspectos fundamentales](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Clase_IX/listas_clase_IX.py)
- [Ejercicios Listas](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/tree/main/Unidad%20III%20y%20IV/Clase_IX)
  - [Main](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Clase_IX/main.py)
  - [Negocio](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Clase_IX/funciones.py)
  - [Menu](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Clase_IX/menu.py)
## Clase X
- En esta clase profundizamos mas sobre Listas
- [Enunciado de ejercicios de Clase X](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Clase_X/Ejercicios_clase_x.md)
- [Codigo del Ejercicio resuelto](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/tree/main/Unidad%20III%20y%20IV/Clase_X)
  - [Main](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Clase_X/main.py)
  - [Negocio](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Clase_X/negocio.py)
  - [Utils](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Clase_X/utils.py)
## Clase XI
> En esta clase aprendimos sobre ORDENAMIENTO y Return más a fondo
- [Carpeta Completa de la Clase XI](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Clase_XI)

  - [Enunciado de ejercicios de Clase XI](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Clase_XI/readme.md)
  - [Codigo del Ejercicio Clase XI](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Clase_XI/clase_xi.py)
  - [Codigo del Profesor sobre Return Clase XI](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Clase_XI/codigo_profesor.py)
# Modelos de Parcial
> Primer Parcial
> El Código esta comentado
- [Carpeta Completa Parcial I](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/tree/main/Unidad%20III%20y%20IV/Modelo_Segundo_Parcial)

  - [Enunciado](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Modelo_Segundo_Parcial/readme.md)
  - [Punto I](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Modelo_Segundo_Parcial/main.py)
  - [Punto II](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Modelo_Segundo_Parcial/negocio.py)
  - [Punto III](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Modelo_Segundo_Parcial/utils.py)
    - [main](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Modelo_de_Parcial/Punto_3/main.py)
    - [negocio](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Modelo_de_Parcial/Punto_3/main.py)
    - [utils](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Modelo_de_Parcial/Punto_3/main.py)
- [Codigo de ejercicio 1 (Suma y Promedio de números) resuelto](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Modelo_de_Parcial/Punto_1/main.py)
- [Codigo de ejercicio 2 (Maximos y su sumatoria) resuelto](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Modelo_de_Parcial/Punto_2/main.py)
- [Codigo de ejercicio 3 (Sublotes de números) resuelto](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/tree/main/Unidad%20I%20y%20II/Modelo_de_Parcial/Punto_3)
  - [main](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Modelo_de_Parcial/Punto_3/main.py)
  - [negocio](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Modelo_de_Parcial/Punto_3/negocio.py)
  - [utils](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20I%20y%20II/Modelo_de_Parcial/Punto_3/utils.py)  
## Modelo Segundo Parcial
> Segundo Parcial del 1er Turno
- [Carpeta Completa Parcial II](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/tree/main/Unidad%20III%20y%20IV/Modelo_Segundo_Parcial)

  - [Enunciado del Parcial II](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Modelo_Segundo_Parcial/readme.md)
 - [Main](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Modelo_Segundo_Parcial/main.py)
  - [Negocio](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Modelo_Segundo_Parcial/negocio.py)
  - [Utils](https://github.com/MONZONPUNTOEXE/Introduccion-a-la-Programacion-I/blob/main/Unidad%20III%20y%20IV/Modelo_Segundo_Parcial/utils.py)