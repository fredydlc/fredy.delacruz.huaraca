# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:04:18 2024

@author: USUARIO
"""

#Duplicar Nodos:
#1. Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e 
#imprime la lista original y la lista duplicada hacia adelante y hacia atrás.

# Definimos la clase Nodo que representa cada elemento de la lista
class Nodo:
    def __init__(self, valor):
        
 # Inicializamos el nodo con un valor dado
        self.valor = valor 

# Creamos una lista original con nodos x,y
lista_original = [Nodo('x'), Nodo('y'),Nodo("z"),Nodo("w")]

# Duplicamos los nodos en la lista original y creamos nueva lista duplicada directa
# Utilizamos una lista que recorre cada nodo en la lista original y
# agrega dos veces a la lista duplicada
lista_duplicada_directa = sum([[nodo, nodo] for nodo in lista_original], [])

# Duplicamos cada nodo en la lista original y creamos una nueva lista duplicada hacia atrás
# Invertimos la lista original usando slicing y luego aplicamos la misma lógica de duplicación
lista_duplicada_inversa = sum([[nodo, nodo] for nodo in lista_original[::-1]], [])


# creamos un ciclo for para iterar sobre cada lista y otro bucle for anidado
#para imprimir los valores de los nodos en cada lista
for lista, nombre in zip([lista_original, lista_duplicada_directa, lista_duplicada_inversa],
                         ["Original", "Duplicada directa", "Duplicada inversa"]):
    
# Imprimimos el nombre de la lista
    print(f"\nLista {nombre}:")  
    
#Iteramos sobre cada nodo en la lista
    for nodo in lista: 
# Imprimimos el valor del nodo
        print(nodo.valor)  


#Contar Nodos Pares e Impares:
#2. Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato 
#par y cuántos tienen un dato impar e imprime la lista hacia adelante y hacia atrás.

# Definimos la clase Nodo que representa cada elemento de la lista.
class Nodo:
    def __init__(self, valor):
        
 # Inicializamos el nodo con un valor dado
        self.valor = valor 

# Creamos lista con al menos 9 nodos utilizando una lista por comprensión
lista_nodos = [Nodo(i) for i in range(1, 10)]

# Inicializa contadores para nodos: pares e impares
contador_pares = 0
contador_impares = 0

# Recorre la lista de nodos para contar cuántos tienen un valor par e impar
for nodo in lista_nodos:

# Si el valor del nodo es par
    if nodo.valor % 2 == 0: 
        
# Incrementamos el contador de nodos pares
        contador_pares += 1 
        
# Si no, incrementamos el contador de nodos impares
    else:
        contador_impares += 1

# Imprimimos la lista hacia adelante
print("Lista hacia adelante:")
for nodo in lista_nodos:
    
# Imprimimos el valor de cada nodo
    print(nodo.valor)  

# Imprimimos lista hacia atrás utilizando la función reversed() para invertir la lista
print("\nLista hacia atrás:")
for nodo in reversed(lista_nodos):
    
# Imprimimos el valor de cada nodo en orden inverso
    print(nodo.valor)  

# Imprimimos el conteo de nodos pares e impares
print(f"\nNúmero de nodos pares: {contador_pares}")
print(f"Número de nodos impares: {contador_impares}")


#Insertar Nodo en Posición Específica:
#3. Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 
#en la posición 3 e imprime la lista hacia adelante y hacia atrás.

# Definimos la clase Nodo que representa cada elemento de la lista
class Nodo:
    def __init__(self, valor):
        
# Inicializamos el nodo con un valor dado.
        self.valor = valor 
 # Inicializamos el enlace al siguiente nodo como None
        self.siguiente = None 
# Inicializamos el enlace al nodo anterior como None
        self.anterior = None  

# Función para imprimir la lista hacia adelante
def imprimir_adelante(nodo):
    while nodo:
        print(nodo.valor)  # Imprimimos el valor del nodo actual
        nodo = nodo.siguiente  # Pasamos al siguiente nodo

# Función para imprimir la lista hacia atrás
def imprimir_atras(nodo):
    while nodo:
        print(nodo.valor)  # Imprimimos el valor del nodo actual
        nodo = nodo.anterior  # Pasamos al nodo anterior

# Creamos la lista inicial con al menos 5 nodos utilizando una lista por comprensión
lista_nodos = [Nodo(i) for i in range(1, 6)]

# Insertamos un nuevo nodo con el valor 15 en la posición 3 (índice 2)
# Establece enlaces entre los nodos para mantener la estructura de la lista 
#de doble enlazada

# Creamos un nuevo nodo con valor 15 y lo establecemos como el anterior al nodo en la posición 3
lista_nodos[2].anterior = Nodo(15)
# Establecemos el enlace siguiente del nuevo nodo al nodo en la posición 3  
lista_nodos[2].anterior.siguiente = lista_nodos[2]  
# Establecemos el enlace anterior del nuevo nodo al nodo en la posición 2
lista_nodos[2].anterior.anterior = lista_nodos[1]
# Establecemos el enlace siguiente del nodo en la posición 2 al nuevo nodo  
lista_nodos[1].siguiente = lista_nodos[2].anterior  

# Imprimimos la lista hacia adelante llamando a la función imprimir_adelante
print("Lista hacia adelante:")
imprimir_adelante(lista_nodos[0])

# Imprimimos la lista hacia atrás llamando a la función imprimir_atras
print("\nLista hacia atrás:")
imprimir_atras(lista_nodos[-1])


#Eliminar Nodos Duplicados:
#4. Crea una lista con nodos que contengan datos duplicados, elimina todos los 
#nodos duplicados, dejando solo una instancia de cada dato e imprime la lista 
#hacia adelante y hacia atrás.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

# Función para imprimir la lista hacia adelante
def imprimir_adelante(nodo):
    while nodo:
        print(nodo.valor)
        nodo = nodo.siguiente

# Función para imprimir la lista hacia atrás
def imprimir_atras(nodo):
    while nodo:
        print(nodo.valor)
        nodo = nodo.anterior

# Función para eliminar nodos duplicados de la lista
def eliminar_duplicados(nodo):
 # Utilizamos un conjunto para rastrear los valores únicos vistos
    valores = set()
    
# Iniciamos desde el primer nodo
    siguiente_nodo = nodo
    while siguiente_nodo:
#Si el valor ya está en el conjunto, es un duplicado
        if siguiente_nodo.valor in valores:  
# Eliminamos el nodo actual
            siguiente_nodo.anterior.siguiente = siguiente_nodo.siguiente  
# Si hay un nodo siguiente
            if siguiente_nodo.siguiente:  
                siguiente_nodo.siguiente.anterior = siguiente_nodo.anterior 
# Actualizamos el enlace del nodo siguiente
        else:
# Agregamos el valor al conjunto
            valores.add(siguiente_nodo.valor)  
# Pasamos al siguiente nodo
        siguiente_nodo = siguiente_nodo.siguiente  

# Creamos la lista con nodos que contienen datos duplicados
lista_nodos = [Nodo(i) for i in [1, 2, 2, 3, 3, 3, 4, 5, 5]]

# Establecemos los enlaces entre los nodos para formar una lista doblemente enlazada
for i in range(len(lista_nodos)):
    if i > 0:
        lista_nodos[i].anterior = lista_nodos[i - 1]
    if i < len(lista_nodos) - 1:
        lista_nodos[i].siguiente = lista_nodos[i + 1]

# Eliminamos los nodos duplicados de la lista
eliminar_duplicados(lista_nodos[0])

# Imprimimos la lista hacia adelante
print("Lista hacia adelante:")
imprimir_adelante(lista_nodos[0])

# Imprimimos la lista hacia atrás
print("\nLista hacia atrás:")
imprimir_atras(lista_nodos[-1])

#Invertir la Lista:
#5. Crea una lista con al menos 6 nodos, invierte el orden de la lista
#(el último elemento se convierte en el 
#primero y viceversa) e imprime la lista hacia adelante y hacia atrás.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

# Función para imprimir la lista hacia adelante
def imprimir_adelante(nodo):
    while nodo:
        print(nodo.valor)
        nodo = nodo.siguiente

# Función para imprimir la lista hacia atrás
def imprimir_atras(nodo):
    while nodo:
        print(nodo.valor)
        nodo = nodo.anterior

# Función para invertir la lista
def invertir_lista(nodo):
    ultimo_nodo = None
    while nodo:
        siguiente_nodo = nodo.siguiente
        nodo.siguiente = ultimo_nodo
        nodo.anterior = siguiente_nodo
        ultimo_nodo = nodo
        nodo = siguiente_nodo

# Creamos la lista con al menos 6 nodos
lista_nodos = [Nodo(i) for i in range(1, 7)]

# Establecemos los enlaces entre los nodos para formar una lista doblemente enlazada
for i in range(len(lista_nodos)):
    if i > 0:
        lista_nodos[i].anterior = lista_nodos[i - 1]
    if i < len(lista_nodos) - 1:
        lista_nodos[i].siguiente = lista_nodos[i + 1]

# Invertimos el orden de la lista llamando a la función invertir_lista
invertir_lista(lista_nodos[0])

# Imprimimos la lista hacia adelante
print("Lista invertida hacia adelante:")
imprimir_adelante(lista_nodos[-1])

# Imprimimos la lista hacia atrás
print("\nLista invertida hacia atrás:")
imprimir_atras(lista_nodos[0])



class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0
#apilar
    def apilar(self, item):
        self.items.append(item)
#desapilar
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
#ver tope
    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]

#6) invertir cadena
def invertir_cadena(cadena):
    pila = Pila()
    for caracter in cadena:   #inicia un bucle que itera sobre cada caracter en la cadena de entrada
        pila.apilar(caracter)   #cada caracter de la cadena se apila en la pila
    cadena_invertida = ""   #inicializa una cadena vacía que se utilizará para almacenar la cadena invertida
    while not pila.esta_vacia():      #se inicia un bucle que se ejecutará mientras la pila no esté vacía
        cadena_invertida += pila.desapilar() #se desapila un caracter de la pila y se concatena a la cadena invertida
    return cadena_invertida

#7. Convertir el número decimal a binario
def decimal_a_binario(decimal):
    pila = Pila()    #crear clase pila para almacenar digitos
    while decimal > 0:  #bucle que se ejecutará mientras el número decimal sea mayor que 0
        residuo = decimal % 2   #calcula el residuo de la división del número decimal entre 2 se utiliza el operador % para calcular el residuo.
        pila.apilar(residuo)    #residuo calculado se apila en la pila
        decimal //= 2    #divide el número decimal entre 2 y se asigna el resultado a decimal
    binario = ""     #inicializa una cadena vacía que se utilizará para almacenar
    while not pila.esta_vacia():      #inicia un bucle que se ejecutará mientras la pila no esté vacía
        binario += str(pila.desapilar())    #se desapila un dígito binario de la pila y se concatena a la cadena binario
    return binario if binario else "0"  #se devuelve esta cadena como el resultado de la función.

#8. Evaluar expresión posfija
def evaluar_expresion_posfija(expresion):
    pila = Pila()     #clase Pila para almacenar los operandos
    tokens = expresion.split()  #crea una lista de cadenas donde cada cadena representa un token individual en la expresión.
    for token in tokens:  #inicia un bucle que itera sobre cada token en la lista de tokens de la expresión
        if token.isdigit():   #verifica si el token es un dígito utilizando el método isdigit() de las cadenas
            pila.apilar(float(token))
        elif token in {'+', '-', '*', '/'}:  #Si el token no es un dígito, se verifica si es uno de los operadores básicos
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            elif token == '/':
                resultado = operando1 / operando2
            pila.apilar(resultado)
        else:
            raise ValueError("Expresión no válida")
    return pila.desapilar()

#9. Verificar operadores binarios.
def verificar_operadores_anidados(expresion):
    pila = Pila()   #clase Pila para almacenar los paréntesis de la expresión
    for caracter in expresion:   #inicia un bucle que itera sobre cada caracter
        if caracter == '(':   #verifica si el caracter es un paréntesis de apertura
            pila.apilar(caracter)   #se apila en la pila
        elif caracter == ')':  #verifica si el caracter
            if pila.esta_vacia() or pila.desapilar() != '(':   #indica que los paréntesis no están correctamente anidados.
                return False
    return pila.esta_vacia()

#10. Ordenar pila ascendente
def ordenar_pila_ascendente(pila):
    pila_temporal = Pila()  # Se crea una pila temporal para almacenar los elementos durante el proceso de ordenamiento.
    while not pila.esta_vacia():  # Se inicia un bucle para procesar todos los elementos de la pila original.
        temp = pila.desapilar()  # Se desapila un elemento de la pila original y se almacena temporalmente en 'temp'.
        while not pila_temporal.esta_vacia() and pila_temporal.ver_tope() > temp:
            # Se inicia un bucle interno para desapilar elementos de la pila temporal
            # y apilarlos en la pila original hasta que se encuentre un elemento menor o igual que 'temp'.
            pila.apilar(pila_temporal.desapilar())  # Se apila el elemento desapilado de 'pila_temporal' en la pila original.
        pila_temporal.apilar(temp)  # Se apila 'temp' en la pila temporal.
    while not pila_temporal.esta_vacia():
        # Una vez que se han procesado todos los elementos de la pila original y se han colocado en la pila temporal en orden ascendente,
        # se desapilan los elementos de la pila temporal y se apilan de nuevo en la pila original, lo que resulta en una pila ordenada de manera ascendente.
        pila.apilar(pila_temporal.desapilar())

#11.
def eliminar_duplicados_pila(pila):
    elementos_vistos = set()  # Se crea un conjunto para almacenar los elementos únicos que se han visto.
    pila_temporal = Pila()  # Se crea una pila temporal para almacenar los elementos únicos.
    while not pila.esta_vacia():  # Se inicia un bucle para procesar todos los elementos de la pila original.
        elemento = pila.desapilar()  # Se desapila un elemento de la pila original.
        if elemento not in elementos_vistos:  # Se verifica si el elemento ya ha sido visto.
            pila_temporal.apilar(elemento)  # Si el elemento no ha sido visto, se apila en la pila temporal.
            elementos_vistos.add(elemento)  # Se agrega el elemento al conjunto de elementos vistos para evitar duplicados.
    while not pila_temporal.esta_vacia():  # Se inicia un bucle para procesar todos los elementos de la pila temporal.
        pila.apilar(pila_temporal.desapilar())  # Se desapila un elemento de la pila temporal y se apila de nuevo en la pila original.


#12
def calcular_expresion(expresion):
    pila = Pila()  # Se crea una pila para almacenar los operandos y resultados de la expresión.
    tokens = expresion.split()  # Se dividen los tokens de la expresión utilizando el espacio como separador.
    for token in tokens:  # Se itera sobre cada token en la lista de tokens de la expresión.
        if token.isdigit():  # Si el token es un dígito, se convierte a un número de punto flotante y se apila en la pila.
            pila.apilar(float(token))
        elif token in {'+', '-', '*', '/'}:  # Si el token es un operador, se procede a evaluar la operación correspondiente.
            operando2 = pila.desapilar()  # Se desapila el segundo operando de la pila.
            operando1 = pila.desapilar()  # Se desapila el primer operando de la pila.
            if token == '+':  # Si el operador es suma, se suma los operandos.
                resultado = operando1 + operando2
            elif token == '-':  # Si el operador es resta, se resta los operandos.
                resultado = operando1 - operando2
            elif token == '*':  # Si el operador es multiplicación, se multiplica los operandos.
                resultado = operando1 * operando2
            elif token == '/':  # Si el operador es división, se divide los operandos.
                resultado = operando1 / operando2
            pila.apilar(resultado)  # El resultado de la operación se apila en la pila.
        else:
            raise ValueError("Expresión no válida")  # Si el token no es ni un dígito ni un operador, se levanta una excepción.
    return pila.desapilar()  # Una vez que se han procesado todos los tokens y se ha evaluado la expresión, se devuelve el resultado final.


#13
def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()  # Se elimina cualquier espacio en blanco y se convierte la palabra a minúsculas.
    pila = Pila()  # Se crea una pila para almacenar los caracteres de la palabra.
    for caracter in palabra:  # Se itera sobre cada caracter en la palabra.
        pila.apilar(caracter)  # Cada caracter se apila en la pila.
    palabra_invertida = ""  # Se inicializa una cadena vacía para almacenar la palabra invertida.
    while not pila.esta_vacia():  # Se inicia un bucle que se ejecuta mientras la pila no esté vacía.
        palabra_invertida += pila.desapilar()  # Se desapila un caracter de la pila y se agrega a la palabra invertida.
    return palabra == palabra_invertida  # Se compara la palabra original con la palabra invertida para determinar si es un palíndromo.


#14
class SistemaDeshacer:
    def __init__(self):
        self.acciones = []
        self.deshaceres = []

    def realizar_accion(self, accion):
        print("Realizando:", accion)
        self.acciones.append(accion)

    def deshacer_accion(self):
        if self.acciones:
            accion_deshacer = self.acciones.pop()
            print("Deshaciendo:", accion_deshacer)
            self.deshaceres.append(accion_deshacer)
        else:
            print("No hay acciones para deshacer")

    def rehacer_accion(self):
        if self.deshaceres:
            accion_rehacer = self.deshaceres.pop()
            print("Rehaciendo:", accion_rehacer)
            self.acciones.append(accion_rehacer)
        else:
            print("No hay acciones para rehacer")


# Ejemplos de uso
if __name__ == "__main__":
    # Ejemplo 6: Invertir una cadena
    cadena = "Hola mundo"
    print("Cadena original:", cadena)
    print("Cadena invertida:", invertir_cadena(cadena))

    # Ejemplo 7: Convertir número decimal a binario
    decimal = 27
    print("Número decimal:", decimal)
    print("Número binario:", decimal_a_binario(decimal))

    # Ejemplo 8: Evaluar expresión posfija
    expresion_posfija = "3 4 + 5 *"
    print("Resultado de la expresión posfija:", evaluar_expresion_posfija(expresion_posfija))

    # Ejemplo 9: Validar operadores anidados
    expresion_anidada = "(3 + 4) * 5"
    print("Los operadores en la expresión están anidados correctamente:", verificar_operadores_anidados(expresion_anidada))

    # Ejemplo 10: Ordenar una pila
    pila_desordenada = Pila()
    pila_desordenada.apilar(5)
    pila_desordenada.apilar(2)
    pila_desordenada.apilar(9)
    pila_desordenada.apilar(1)
    pila_desordenada.apilar(6)
    print("Pila desordenada:", pila_desordenada.items)
    ordenar_pila_ascendente(pila_desordenada)
    print("Pila ordenada de manera ascendente:", pila_desordenada.items)

    # Ejemplo 11: Eliminar duplicados de una pila
    pila_con_duplicados = Pila()
    pila_con_duplicados.apilar(5)
    pila_con_duplicados.apilar(2)
    pila_con_duplicados.apilar(5)
    pila_con_duplicados.apilar(1)
    pila_con_duplicados.apilar(2)
    print("Pila con duplicados:", pila_con_duplicados.items)
    eliminar_duplicados_pila(pila_con_duplicados)
    print("Pila sin duplicados:", pila_con_duplicados.items)

    # Ejemplo 12: Calculadora sencilla
    expresion_calculadora = "3 4 + 5 *"
    print("Resultado de la expresión de la calculadora:", calcular_expresion(expresion_calculadora))

    # Ejemplo 13: Comprobar palíndromos
    palabra_palindromo = "Anita lava la tina"
    print("¿Es palíndromo la palabra '{}'?".format(palabra_palindromo), es_palindromo(palabra_palindromo))

    # Ejemplo 14: Simular el proceso de deshacer (undo)
    sistema = SistemaDeshacer()
    sistema.realizar_accion("Abrir archivo")
    sistema.realizar_accion("Editar archivo")
    sistema.deshacer_accion()
    sistema.rehacer_accion()






