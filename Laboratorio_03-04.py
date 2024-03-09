# Definición de la función recursiva para imprimir los números pares
def imprimir_pares(n):
    # Caso base: si n es menor o igual a 0, se detiene la recursión
    if n <= 0:
        return
    # Se verifica si n es par
    if n % 2 == 0:
        # Si n es par, se imprime
        print(n)
    # Se llama recursivamente a la función con el número anterior
    imprimir_pares(n - 1)

# Llamada a la función con el parámetro inicial 100
print("Números pares del 1 al 100:")
imprimir_pares(100)


# Definición de la función recursiva para calcular la suma de los números
def suma_hasta_n(n):
    # Caso base: si n es igual a 1, se devuelve 1 (el primer número)
    if n == 1:
        return 1
    # Se realiza la suma del número actual (n) con la llamada recursiva para n-1
    return n + suma_hasta_n(n - 1)

# Se solicita al usuario que ingrese un número para calcular la suma
numero = int(input("Ingrese un número para calcular la suma hasta ese número: "))
# Se llama a la función con el número ingresado como argumento
print("La suma de los números del 1 al", numero, "es:", suma_hasta_n(numero))


# Definición de la función recursiva para imprimir la pirámide de números
def imprimir_piramide(n):
    # Caso base: si n es menor o igual a 0, se detiene la recursión
    if n <= 0:
        return
    # Se llama recursivamente a la función con n-1 para imprimir los números anteriores
    imprimir_piramide(n - 1)
    # Se imprime la línea actual de la pirámide, con números del 1 al n separados por espacios
    print(" ".join(str(i) for i in range(1, n + 1)))

# Se llama a la función con el valor deseado de n
print("Pirámide de números del 1 al n:")
imprimir_piramide(5)  # Cambiar el número por el valor deseado de n


# Definición de la función recursiva para imprimir la pirámide de números invertidos
def imprimir_piramide_invertida(n):
    # Caso base: si n es menor o igual a 0, se detiene la recursión
    if n <= 0:
        return
    # Se imprime la línea actual de la pirámide invertida, con números del 1 al n
    print(" ".join(str(i) for i in range(1, n + 1)))
    # Se llama recursivamente a la función con n-1 para imprimir los números restantes
    imprimir_piramide_invertida(n - 1)

# Se llama a la función con el valor deseado de n
print("Pirámide de números invertidos del 1 al n:")
imprimir_piramide_invertida(5)  # Cambiar el número por el valor deseado de n




# Definición de la función recursiva para imprimir la tabla de multiplicar
def tabla_multiplicar(n, multiplicador=1):
    # Caso base: si el multiplicador es mayor que 10, se detiene la recursión
    if multiplicador > 10:
        return
    # Se imprime la multiplicación correspondiente al número y al multiplicador actual
    print(f"{n} x {multiplicador} = {n * multiplicador}")
    # Se llama recursivamente a la función con el siguiente multiplicador
    tabla_multiplicar(n, multiplicador + 1)

# Se solicita al usuario que ingrese un número para mostrar su tabla de multiplicar
numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
print("Tabla de multiplicar de", numero, ":")
# Se llama a la función con el número ingresado como argumento
tabla_multiplicar(numero)


#1. Crear una matriz de números reales:
# Crear una matriz de números reales utilizando una lista de listas
matriz_reales = [[1.0, 2.0, 3.0],
                 [4.0, 5.0, 6.0],
                 [7.0, 8.0, 9.0]]

# Imprimir la matriz
print("Matriz de números reales:")
for fila in matriz_reales:
    print(fila)


#2. Crear una matriz de números complejos:
# Importar el módulo de números complejos
import numpy as np

# Crear una matriz de números complejos utilizando numpy
matriz_complejos = np.array([[1 + 2j, 3 + 4j],
                             [5 + 6j, 7 + 8j]])

# Imprimir la matriz
print("Matriz de números complejos:")
print(matriz_complejos)


#3. Crear una matriz de matrices:
# Crear dos matrices internas
matriz_interna1 = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

matriz_interna2 = [[10, 11, 12],
                   [13, 14, 15],
                   [16, 17, 18]]

# Crear una matriz de matrices utilizando una lista de listas
matriz_de_matrices = [matriz_interna1, matriz_interna2]

# Imprimir la matriz de matrices
print("Matriz de matrices:")
for matriz in matriz_de_matrices:
    for fila in matriz:
        print(fila)
    print()  # Imprimir una línea en blanco entre las matrices internas


# Función para obtener el elemento central de una matriz
def elemento_central(matriz):
    # Calcular las dimensiones de la matriz
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0

    # Calcular las coordenadas del elemento central
    fila_central = filas // 2
    columna_central = columnas // 2

    # Obtener el elemento central
    elemento = matriz[fila_central][columna_central]
    return elemento

# Ejemplo de matriz
mi_matriz = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

# Obtener y imprimir el elemento central de la matriz
elemento = elemento_central(mi_matriz)
print("Elemento central de la matriz:", elemento)


# Función para sumar dos matrices
def sumar_matrices(matriz1, matriz2):
    # Verificar que las matrices tengan las mismas dimensiones
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("No se pueden sumar matrices de diferentes tamaños")
        return None

    # Inicializar una matriz para almacenar el resultado
    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0])):
            suma_elemento = matriz1[i][j] + matriz2[i][j]
            fila_resultado.append(suma_elemento)
        resultado.append(fila_resultado)

    return resultado

# Ejemplo de matrices a sumar
matriz_a = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matriz_b = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

# Sumar las matrices y mostrar el resultado
resultado_suma = sumar_matrices(matriz_a, matriz_b)
if resultado_suma is not None:
    print("Resultado de la suma de las matrices:")
    for fila in resultado_suma:
        print(fila)


# Función para multiplicar una matriz por un número
def multiplicar_matriz_por_numero(matriz, numero):
    # Inicializar una matriz para almacenar el resultado
    resultado = []
    for fila in matriz:
        fila_resultado = [elemento * numero for elemento in fila]
        resultado.append(fila_resultado)
    return resultado

# Ejemplo de matriz y número
mi_matriz = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
mi_numero = 2

# Multiplicar la matriz por el número y mostrar el resultado
resultado_multiplicacion = multiplicar_matriz_por_numero(mi_matriz, mi_numero)
print("Resultado de la multiplicación de la matriz por el número:")
for fila in resultado_multiplicacion:
    print(fila)


# Función para calcular la media de los elementos de una matriz
def media_matriz(matriz):
    # Obtener el total de elementos y la suma de todos los elementos de la matriz
    total_elementos = sum(len(fila) for fila in matriz)
    suma_total = sum(sum(fila) for fila in matriz)

    # Calcular la media dividiendo la suma total entre el total de elementos
    media = suma_total / total_elementos
    return media

# Ejemplo de matriz
mi_matriz = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

# Calcular y mostrar la media de los elementos de la matriz
media = media_matriz(mi_matriz)
print("La media de los elementos de la matriz es:", media)


import random

# Función para crear una matriz de números aleatorios
def matriz_aleatoria(filas, columnas):
    matriz = []
    for _ in range(filas):
        fila = [random.randint(1, 100) for _ in range(columnas)]
        matriz.append(fila)
    return matriz

# Crear una matriz de números aleatorios de tamaño 100x100
matriz_aleatoria_100x100 = matriz_aleatoria(100, 100)

# Mostrar una parte de la matriz (para evitar imprimir 10000 números)
print("Parte de la matriz de números aleatorios:")
for fila in matriz_aleatoria_100x100[:3]:
    print(fila)


import numpy as np

# Función para calcular la media de una matriz
def media_matriz(matriz):
    return np.mean(matriz)

# Función para calcular la mediana de una matriz
def mediana_matriz(matriz):
    return np.median(matriz)

# Función para calcular la desviación estándar de una matriz
def desviacion_estandar_matriz(matriz):
    return np.std(matriz)

# Ejemplo de matriz
mi_matriz = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

# Calcular la media, la mediana y la desviación estándar de los elementos de la matriz
media = media_matriz(mi_matriz)
mediana = mediana_matriz(mi_matriz)
desviacion_estandar = desviacion_estandar_matriz(mi_matriz)

# Mostrar los resultados
print("Media de la matriz:", media)
print("Mediana de la matriz:", mediana)
print("Desviación estándar de la matriz:", desviacion_estandar)


# Función para encontrar el elemento máximo de una matriz
def maximo_matriz(matriz):
    # Convertir la matriz a un array de numpy para utilizar la función de máximo
    matriz_np = np.array(matriz)
    # Encontrar el máximo elemento en la matriz
    maximo = np.max(matriz_np)
    return maximo

# Ejemplo de matriz
mi_matriz = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

# Encontrar el elemento máximo de la matriz
maximo = maximo_matriz(mi_matriz)

# Mostrar el resultado
print("El elemento máximo de la matriz es:", maximo)


# Función para encontrar la submatriz de mayor suma de una matriz
def submatriz_mayor_suma(matriz):
    # Convertir la matriz a un array de numpy para utilizar las funciones de suma
    matriz_np = np.array(matriz)
    # Obtener el tamaño de la matriz
    filas, columnas = matriz_np.shape
    # Inicializar las variables para la submatriz de mayor suma y su suma máxima
    submatriz_max = None
    suma_max = float('-inf')

    # Iterar sobre todas las submatrices posibles
    for i in range(filas):
        for j in range(columnas):
            for k in range(i, filas):
                for l in range(j, columnas):
                    # Obtener la submatriz actual
                    submatriz_actual = matriz_np[i:k+1, j:l+1]
                    # Calcular la suma de la submatriz actual
                    suma_actual = np.sum(submatriz_actual)
                    # Actualizar la submatriz de mayor suma si es necesario
                    if suma_actual > suma_max:
                        suma_max = suma_actual
                        submatriz_max = submatriz_actual.tolist()

    return submatriz_max

# Ejemplo de matriz
mi_matriz = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

# Encontrar la submatriz de mayor suma de la matriz
submatriz_maxima = submatriz_mayor_suma(mi_matriz)

# Mostrar la submatriz de mayor suma
print("La submatriz de mayor suma es:")
for fila in submatriz_maxima:
    print(fila)


# Función para calcular la matriz de covarianza de dos matrices
def matriz_covarianza(matriz1, matriz2):
    # Convertir las matrices a arrays de numpy
    matriz1_np = np.array(matriz1)
    matriz2_np = np.array(matriz2)
    
    # Calcular la matriz de covarianza utilizando la función cov de numpy
    covarianza = np.cov(matriz1_np, matriz2_np)
    
    return covarianza

# Ejemplo de matrices
matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

# Calcular y mostrar la matriz de covarianza
matriz_cov = matriz_covarianza(matriz1, matriz2)
print("Matriz de covarianza de las matrices:")
print(matriz_cov)
