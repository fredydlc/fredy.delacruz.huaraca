# Ejercicio 1: Números primos
def numeros_primos(conjunto):
    primos = set()  # Creamos un conjunto vacío para almacenar los números primos.
    for num in conjunto:  # Iteramos a través de cada número en el conjunto.
        if num > 1:  # Comprobamos si el número es mayor que 1, ya que los números primos son mayores que 1.
            for i in range(2, num):  # Iteramos a través de los posibles divisores del número.
                if (num % i) == 0:  # Comprobamos si el número es divisible por algún divisor.
                    break  # Si es divisible, salimos del bucle for.
            else:  # Si el bucle for no se detiene por el break, entonces el número es primo.
                primos.add(num)  # Añadimos el número al conjunto de primos.
    return primos  # Devolvemos el conjunto de números primos.

# Ejercicio 2: Palabras que comienzan con una letra determinada
def palabras_comienzan_con_letra(conjunto, letra):
    palabras = set()  # Creamos un conjunto vacío para almacenar las palabras que comienzan con la letra.
    for palabra in conjunto:  # Iteramos a través de cada palabra en el conjunto.
        if palabra.startswith(letra):  # Comprobamos si la palabra comienza con la letra especificada.
            palabras.add(palabra)  # Añadimos la palabra al conjunto de palabras.
    return palabras  # Devolvemos el conjunto de palabras que comienzan con la letra especificada.
# Ejercicio 3: Números divisibles por un número determinado
def numeros_divisibles(conjunto, divisor):
    divisibles = set()  # Creamos un conjunto vacío para almacenar los números divisibles.
    for num in conjunto:  # Iteramos a través de cada número en el conjunto.
        if num % divisor == 0:  # Comprobamos si el número es divisible por el divisor.
            divisibles.add(num)  # Si es divisible, añadimos el número al conjunto de divisibles.
    return divisibles  # Devolvemos el conjunto de números divisibles.
# Ejercicio 4: Números en ambos conjuntos
def numeros_en_ambos(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)
# Ejercicio 5: Números en el primer conjunto pero no en el segundo
def numeros_en_primer_no_segundo(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)
# Ejercicio 6: Números en el segundo conjunto pero no en el primero
def numeros_en_segundo_no_primer(conjunto1, conjunto2):
    return conjunto2.difference(conjunto1)


# Ejercicio 7: Palabras que son anagramas
def palabras_anagramas(conjunto):
    anagramas = set()  # Creamos un conjunto vacío para almacenar los anagramas.
    for palabra in conjunto:  # Iteramos a través de cada palabra en el conjunto.
        if len(set(palabra)) == len(palabra):  # Comprobamos si todos los caracteres son únicos en la palabra.
            anagramas.add(palabra)  # Si son únicos, añadimos la palabra al conjunto de anagramas.
    return anagramas  # Devolvemos el conjunto de palabras que son anagramas.


# Ejercicio 8: Palabras que son palíndromos
def palabras_palindromos(conjunto):
    palindromos = set()  # Creamos un conjunto vacío para almacenar los palíndromos.
    for palabra in conjunto:  # Iteramos a través de cada palabra en el conjunto.
        if palabra == palabra[::-1]:  # Comprobamos si la palabra es igual a su reverso.
            palindromos.add(palabra)  # Si es un palíndromo, añadimos la palabra al conjunto de palíndromos.
    return palindromos  # Devolvemos el conjunto de palabras que son palíndromos.


# Ejercicio 9: Palabras de una longitud determinada
def palabras_longitud(conjunto, longitud):
    palabras = set()  # Creamos un conjunto vacío para almacenar las palabras.
    for palabra in conjunto:  # Iteramos a través de cada palabra en el conjunto.
        if len(palabra) == longitud:  # Comprobamos si la longitud de la palabra es igual a la longitud especificada.
            palabras.add(palabra)  # Si es así, añadimos la palabra al conjunto de palabras.
    return palabras  # Devolvemos el conjunto de palabras con la longitud determinada.
# Ejercicio 10: Palabras que contienen una letra determinada
def palabras_con_letra(conjunto, letra):
    palabras = set()  # Creamos un conjunto vacío para almacenar las palabras.
    for palabra in conjunto:  # Iteramos a través de cada palabra en el conjunto.
        if letra in palabra:  # Comprobamos si la letra está presente en la palabra.
            palabras.add(palabra)  # Si es así, añadimos la palabra al conjunto de palabras.
    return palabras  # Devolvemos el conjunto de palabras que contienen la letra determinada.


# Ejercicio 11: Números ordenados de menor a mayor
def numeros_ordenados_menor_a_mayor(conjunto):
    return sorted(conjunto)


# Ejercicio 12: Números ordenados de mayor a menor
def numeros_ordenados_mayor_a_menor(conjunto):
    return sorted(conjunto, reverse=True)


# Ejercicio 13: Números duplicados
def numeros_duplicados(conjunto):
    duplicados = set()  # Creamos un conjunto vacío para almacenar los números duplicados.
    unicos = set()  # Creamos un conjunto vacío para almacenar los números únicos.
    for num in conjunto:  # Iteramos a través de cada número en el conjunto.
        if num in unicos:  # Comprobamos si el número ya está presente en el conjunto de números únicos.
            duplicados.add(num)  # Si es así, lo añadimos al conjunto de números duplicados.
        else:
            unicos.add(num)  # Si no está presente, lo añadimos al conjunto de números únicos.
    return duplicados  # Devolvemos el conjunto de números duplicados.


# Ejercicio 14: Números no duplicados
def numeros_no_duplicados(conjunto):
    return set([num for num in conjunto if conjunto.count(num) == 1])


# Ejercicio 15: Números primos ordenados de menor a mayor
def numeros_primos_ordenados(conjunto):
    primos = set()  # Creamos un conjunto vacío para almacenar los números primos.
    for num in conjunto:  # Iteramos a través de cada número en el conjunto.
        if num > 1:  # Comprobamos si el número es mayor que 1, ya que los números primos son mayores que 1.
            for i in range(2, num):  # Iteramos a través de los posibles divisores del número.
                if (num % i) == 0:  # Comprobamos si el número es divisible por algún divisor.
                    break  # Si es divisible, salimos del bucle for.
            else:  # Si el bucle for no se detiene por el break, entonces el número es primo.
                primos.add(num)  # Añadimos el número al conjunto de primos.
    return sorted(primos)  # Devolvemos el conjunto de números primos ordenados de menor a mayor.


# Ejercicio 16: Palabras palíndromas ordenadas de menor a mayor
def palabras_palindromos_ordenadas(conjunto):
    palindromos = set()  # Creamos un conjunto vacío para almacenar los palíndromos.
    for palabra in conjunto:  # Iteramos a través de cada palabra en el conjunto.
        if palabra == palabra[::-1]:  # Comprobamos si la palabra es igual a su reverso.
            palindromos.add(palabra)  # Si es un palíndromo, añadimos la palabra al conjunto de palíndromos.
    return sorted(palindromos)  # Devolvemos el conjunto de palabras palíndromas ordenadas de menor a mayor.
# Ejercicio 10: Palabras que contienen una letra determinada
def palabras_con_letra(conjunto, letra):
    """
    Esta función recibe un conjunto de palabras y una letra determinada.
    Devuelve un conjunto con las palabras que contienen la letra especificada.
    """
    palabras = set()  # Creamos un conjunto vacío para almacenar las palabras.
    for palabra in conjunto:  # Iteramos a través de cada palabra en el conjunto.
        if letra in palabra:  # Comprobamos si la letra está presente en la palabra.
            palabras.add(palabra)  # Si es así, añadimos la palabra al conjunto de palabras.
    return palabras  # Devolvemos el conjunto de palabras que contienen la letra determinada.


# Ejercicio 11: Números ordenados de menor a mayor
def numeros_ordenados_menor_a_mayor(conjunto):
    """
    Esta función recibe un conjunto de números.
    Devuelve un conjunto con los números ordenados de menor a mayor.
    """
    return sorted(conjunto)


# Ejercicio 12: Números ordenados de mayor a menor
def numeros_ordenados_mayor_a_menor(conjunto):
    """
    Esta función recibe un conjunto de números.
    Devuelve un conjunto con los números ordenados de mayor a menor.
    """
    return sorted(conjunto, reverse=True)


# Ejercicio 13: Números duplicados
def numeros_duplicados(conjunto):
    """
    Esta función recibe un conjunto de números.
    Devuelve un conjunto con los números que están duplicados en el conjunto original.
    """
    duplicados = set()
    unicos = set()
    for num in conjunto:
        if num in unicos:
            duplicados.add(num)
        else:
            unicos.add(num)
    return duplicados


# Ejercicio 14: Números no duplicados
def numeros_no_duplicados(conjunto):
    """
    Esta función recibe un conjunto de números.
    Devuelve un conjunto con los números que no están duplicados en el conjunto original.
    """
    return set([num for num in conjunto if conjunto.count(num) == 1])


# Ejercicio 15: Números primos ordenados de menor a mayor
def numeros_primos_ordenados(conjunto):
    """
    Esta función recibe un conjunto de números.
    Devuelve un conjunto con los números primos ordenados de menor a mayor.
    """
    primos = set()
    for num in conjunto:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primos.add(num)
    return sorted(primos)


# Ejercicio 16: Palabras palíndromas ordenadas de menor a mayor
def palabras_palindromos_ordenadas(conjunto):
    """
    Esta función recibe un conjunto de palabras.
    Devuelve un conjunto con las palabras palíndromas ordenadas de menor a mayor.
    """
    palindromos = set()
    for palabra in conjunto:
        if palabra == palabra[::-1]:
            palindromos.add(palabra)
    return sorted(palindromos)


# Ejercicio 17: Palabras de longitud determinada ordenadas de menor a mayor
def palabras_longitud_ordenadas(conjunto, longitud):
    """
    Esta función recibe un conjunto de palabras y una longitud determinada.
    Devuelve un conjunto con las palabras de longitud determinada, ordenadas de menor a mayor.
    """
    palabras = set()
    for palabra in conjunto:
        if len(palabra) == longitud:
            palabras.add(palabra)
    return sorted(palabras)


# Ejercicio 18: Palabras que contienen una letra determinada y están ordenadas de mayor a menor
def palabras_con_letra_ordenadas(conjunto, letra):
    """
    Esta función recibe un conjunto de palabras y una letra determinada.
    Devuelve un conjunto con las palabras que contienen la letra especificada, ordenadas de mayor a menor.
    """
    palabras = set()
    for palabra in conjunto:
        if letra in palabra:
            palabras.add(palabra)
    return sorted(palabras, reverse=True)


# Ejercicio 19: Números ordenados de menor a mayor y no duplicados
def numeros_ordenados_no_duplicados(conjunto):
    """
    Esta función recibe un conjunto de números.
    Devuelve un conjunto con los números ordenados de menor a mayor y sin duplicados.
    """
    return sorted(set(conjunto))


# Ejercicio 20: Palabras palíndromas de longitud determinada ordenadas de menor a mayor
def palabras_palindromos_longitud_ordenadas(conjunto, longitud):
    """
    Esta función recibe un conjunto de palabras y una longitud determinada.
    Devuelve un conjunto con las palabras palíndromas de la longitud especificada, ordenadas de menor a mayor.
    """
    palindromos = set()
    for palabra in conjunto:
        if palabra == palabra[::-1] and len(palabra) == longitud:
            palindromos.add(palabra)
    return sorted(palindromos)
