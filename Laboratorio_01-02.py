# Ejercicio 1
# Se solicita al usuario que ingrese dos números y se almacenan en las variables num1 y num2
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Se realizan las operaciones aritméticas y se almacenan en variables separadas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# Se verifica si el segundo número es cero para evitar la división por cero
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero"

# Se imprimen los resultados de las operaciones
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

# Ejercicio 2
# Se solicita al usuario que ingrese un número y se almacena en la variable numero
numero = int(input("Ingrese un número: "))

# Se verifica si el número ingresado es par o impar y se imprime el resultado
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")


# Ejercicio 3
# Se solicita al usuario que ingrese la base y la altura del triángulo y se almacenan en las variables base y altura
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

# Se calcula el área del triángulo utilizando la fórmula: área = (base * altura) / 2
area = (base * altura) / 2

# Se imprime el resultado del cálculo del área
print("El área del triángulo es:", area)


# Ejercicio 4
# Se define una función llamada factorial que calcula el factorial de un número utilizando recursión
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

# Se solicita al usuario que ingrese un número para calcular su factorial y se imprime el resultado
num = int(input("Ingrese un número para calcular su factorial: "))
print("El factorial de", num, "es:", factorial(num))


# Ejercicio 5
# Se define una función llamada es_primo que verifica si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Se solicita al usuario que ingrese un número para verificar si es primo y se imprime el resultado
num = int(input("Ingrese un número para verificar si es primo: "))
if es_primo(num):
    print(num, "es un número primo")
else:
    print(num, "no es un número primo")


# Ejercicio 6
# Se solicita al usuario que ingrese una cadena de texto y se almacena en la variable cadena
cadena = input("Ingrese una cadena de texto: ")

# Se invierte la cadena utilizando el slicing con paso -1 y se almacena en la variable inversa
inversa = cadena[::-1]

# Se imprime la cadena invertida
print("La cadena invertida es:", inversa)


# Ejercicio 7
# Se solicita al usuario que ingrese el número de inicio y el número final del rango
inicio = int(input("Ingrese el número de inicio del rango: "))
fin = int(input("Ingrese el número final del rango: "))

# Se inicializa la variable suma_pares para almacenar la suma de los números pares
suma_pares = 0

# Se itera sobre cada número en el rango especificado
for i in range(inicio, fin + 1):
    # Se verifica si el número es par
    if i % 2 == 0:
        # Si es par, se suma al total
        suma_pares += i

# Se imprime la suma de los números pares en el rango especificado
print("La suma de los números pares en el rango es:", suma_pares)


# Ejercicio 8
# Se define una función llamada contar_vocales que cuenta el número de vocales en una cadena de texto
def contar_vocales(cadena):
    # Se define una cadena que contiene todas las vocales tanto en minúsculas como en mayúsculas
    vocales = 'aeiouAEIOU'
    # Se inicializa la variable num_vocales para almacenar el número de vocales encontradas
    num_vocales = 0
    # Se itera sobre cada letra en la cadena de texto
    for letra in cadena:
        # Se verifica si la letra es una vocal
        if letra in vocales:
            # Si es una vocal, se incrementa el contador de vocales
            num_vocales += 1
    # Se devuelve el número total de vocales encontradas en la cadena de texto
    return num_vocales

# Se solicita al usuario que ingrese una cadena de texto y se llama a la función contar_vocales para contar las vocales
texto = input("Ingrese una cadena de texto: ")
# Se imprime el resultado del conteo de vocales
print("El número de vocales en la cadena es:", contar_vocales(texto))


# Ejercicio 9
# Se define una función llamada fibonacci que genera los primeros n números de la serie Fibonacci
def fibonacci(n):
    # Se inicializa la lista fib con los dos primeros números de la serie Fibonacci
    fib = [0, 1]
    # Se itera desde el tercer número hasta el n-ésimo número de la serie Fibonacci
    for i in range(2, n):
        # Se calcula el siguiente número de la serie Fibonacci sumando los dos números anteriores
        fib.append(fib[-1] + fib[-2])
    # Se devuelve la lista que contiene los primeros n números de la serie Fibonacci
    return fib

# Se llama a la función fibonacci para generar los primeros 10 números de la serie Fibonacci y se imprime el resultado
print("Los primeros 10 números de la serie Fibonacci son:", fibonacci(10))


# Ejercicio 10
# Se solicita al usuario que ingrese una lista de números separados por espacios y se convierte a una lista de floats
numeros = [float(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
# Se ordena la lista de números de menor a mayor
numeros.sort()
# Se imprime la lista ordenada de menor a mayor
print("Lista ordenada de menor a mayor:", numeros)


# Ejercicio 11
# Se define una función llamada es_palindromo que verifica si una palabra es un palíndromo
def es_palindromo(palabra):
    # Se convierte la palabra a minúsculas para hacer la comparación case-insensitive
    palabra = palabra.lower()
    # Se compara la palabra original con su versión invertida
    return palabra == palabra[::-1]

# Se solicita al usuario que ingrese una palabra para verificar si es un palíndromo
palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")
# Se llama a la función es_palindromo para verificar si la palabra es un palíndromo y se imprime el resultado
if es_palindromo(palabra):
    print("La palabra ingresada es un palíndromo")
else:
    print("La palabra ingresada no es un palíndromo")


# Ejercicio 12
# Se solicita al usuario que ingrese un número para generar su tabla de multiplicar
numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))
print("Tabla de multiplicar del", numero, ":")
# Se itera desde 1 hasta 10 para generar la tabla de multiplicar del número ingresado
for i in range(1, 11):
    # Se imprime la multiplicación del número ingresado por el número actual del ciclo
    print(numero, "x", i, "=", numero * i)


# Ejercicio 13
# Se importa el módulo math para utilizar la constante pi
import math

# Se solicita al usuario que ingrese el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))
# Se calcula el área del círculo utilizando la fórmula: área = pi * radio^2
area = math.pi * radio ** 2
# Se imprime el área del círculo
print("El área del círculo es:", area)


# Ejercicio 14
# Se define una función llamada suma_digitos que calcula la suma de los dígitos de un número entero
def suma_digitos(numero):
    # Se inicializa la variable suma para almacenar la suma de los dígitos
    suma = 0
    # Se itera mientras el número sea diferente de cero
    while numero:
        # Se suma el último dígito del número a la variable suma
        suma += numero % 10
        # Se elimina el último dígito del número dividiéndolo entre 10
        numero //= 10
    # Se devuelve la suma de los dígitos
    return suma

# Se solicita al usuario que ingrese un número entero para calcular la suma de sus dígitos
numero = int(input("Ingrese un número entero para calcular la suma de sus dígitos: "))
# Se llama a la función suma_digitos para calcular la suma de los dígitos del número ingresado
print("La suma de los dígitos de", numero, "es:", suma_digitos(numero))
