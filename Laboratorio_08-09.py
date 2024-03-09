# Ejercicio parte 01:

# 1. Validar la edad de un usuario.
def validar_edad(edad):
    """
    Esta función valida si la edad proporcionada es un número entero positivo.
    """
    if isinstance(edad, int) and edad > 0:
        return True
    else:
        return False

# 2. Verificar el tipo de dato de una variable.
def verificar_tipo_dato(variable, tipo):
    """
    Esta función verifica si el tipo de dato de la variable coincide con el tipo especificado.
    """
    return isinstance(variable, tipo)

# 3. Validar el rango de una calificación.
def validar_calificacion(calificacion):
    """
    Esta función valida si la calificación está en el rango de 0 a 10.
    """
    return 0 <= calificacion <= 10

# 4. Asegurar que una lista no esté vacía.
def lista_no_vacia(lista):
    """
    Esta función asegura que una lista no esté vacía.
    """
    return bool(lista)

# 5. Validar la igualdad de dos objetos.
def validar_igualdad(objeto1, objeto2):
    """
    Esta función valida si dos objetos son iguales.
    """
    return objeto1 == objeto2

# 6. Asegurar que un ciclo while se ejecuta al menos una vez.
def ciclo_while_al_menos_una_vez(condicion):
    """
    Esta función asegura que un ciclo while se ejecute al menos una vez.
    """
    while True:
        # Bloque de código que se ejecuta al menos una vez.
        if condicion:
            break

# 7. Asegurar que una función retorna un valor específico.
def funcion_retorna_valor():
    """
    Esta función asegura que se retorne un valor específico.
    """
    return True

# 8. Validar el estado de una variable después de una operación.
def validar_estado_variable(valor_inicial, operacion, resultado_esperado):
    """
    Esta función valida el estado de una variable después de una operación.
    """
    if operacion == "suma":
        return valor_inicial + 1 == resultado_esperado
    elif operacion == "resta":
        return valor_inicial - 1 == resultado_esperado

# 9. Asegurar que un módulo se ha importado correctamente.
def modulo_importado(modulo):
    """
    Esta función asegura que un módulo se haya importado correctamente.
    """
    try:
        __import__(modulo)
        return True
    except ImportError:
        return False
# Ejercicio parte 02:

# 10. Desarrollar el código de buscar nodo en la lista enlazada simple.
class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Se inicializa el nodo con un dato.
        self.siguiente = None  # Se inicializa el siguiente nodo como None.

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Se inicializa la lista enlazada con la cabeza como None.

    def buscar_nodo(self, dato):
        """
        Busca un nodo con un dato específico en la lista enlazada.
        """
        actual = self.cabeza  # Se comienza desde la cabeza de la lista.
        while actual is not None:
            if actual.dato == dato:  # Si se encuentra el nodo con el dato especificado, se devuelve.
                return actual
            actual = actual.siguiente  # Se avanza al siguiente nodo.
        return None  # Si no se encuentra el nodo, se devuelve None.

# 11. Implementa una función que sume todos los nodos de una lista enlazada simple.
def suma_nodos(lista):
    """
    Calcula la suma de los valores de todos los nodos en una lista enlazada.
    """
    suma = 0
    actual = lista.cabeza
    while actual is not None:
        suma += actual.dato
        actual = actual.siguiente
    return suma

# 12. Crea una función que devuelva la longitud de una lista enlazada simple.
def longitud_lista(lista):
    """
    Calcula la longitud de una lista enlazada.
    """
    longitud = 0
    actual = lista.cabeza
    while actual is not None:
        longitud += 1
        actual = actual.siguiente
    return longitud

# 13. Implementa una función que concatene dos listas enlazadas simples.
def concatenar_listas(lista1, lista2):
    """
    Concatena dos listas enlazadas simples.
    """
    if lista1.cabeza is None:  # Si la primera lista está vacía, se devuelve la segunda lista.
        return lista2
    if lista2.cabeza is None:  # Si la segunda lista está vacía, se devuelve la primera lista.
        return lista1

    actual = lista1.cabeza
    while actual.siguiente is not None:  # Se recorre la primera lista hasta llegar al último nodo.
        actual = actual.siguiente
    actual.siguiente = lista2.cabeza  # Se conecta el último nodo de la primera lista con la cabeza de la segunda lista.
    return lista1

# 14. Crea una función que elimine los nodos duplicados de una lista enlazada simple.
def eliminar_duplicados(lista):
    """
    Elimina los nodos duplicados de una lista enlazada simple.
    """
    actual = lista.cabeza
    while actual is not None:
        temp = actual
        while temp.siguiente is not None:
            if temp.siguiente.dato == actual.dato:  # Si se encuentra un nodo duplicado, se elimina.
                temp.siguiente = temp.siguiente.siguiente
            else:
                temp = temp.siguiente
        actual = actual.siguiente

# 15. Implementa una función que invierta el orden de una lista enlazada simple.
def invertir_lista(lista):
    """
    Invierte el orden de una lista enlazada simple.
    """
    anterior = None
    actual = lista.cabeza
    siguiente_nodo = None
    while actual is not None:
        siguiente_nodo = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente_nodo
    lista.cabeza = anterior

      
