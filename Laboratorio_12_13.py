# Ejercicio parte 01 - Colas:

# 1. Verificar si una palabra es palíndroma
from collections import deque

def es_palindroma(palabra):
    """
    Verifica si una palabra es palíndroma o no.
    Utiliza una cola para comparar los caracteres de la palabra en orden original y reverso.
    """
    cola = deque(palabra.lower())  # Convertimos la palabra a minúsculas y la almacenamos en una cola.
    while len(cola) > 1:
        if cola.popleft() != cola.pop():  # Comparamos los caracteres en orden original y reverso.
            return False
    return True

# Ejemplo:
print(es_palindroma("radar"))  # True
print(es_palindroma("python"))  # False


# 2. Diseño de un sistema de gestión de pedidos
class SistemaGestionPedidos:
    def __init__(self):
        """
        Inicializa un sistema de gestión de pedidos con una cola vacía.
        """
        self.cola_pedidos = deque()  # Inicializamos una cola para almacenar los pedidos.

    def agregar_pedido(self, pedido):
        """
        Agrega un pedido a la cola de pedidos.
        """
        self.cola_pedidos.append(pedido)  # Agregamos el pedido a la cola de pedidos.

    def procesar_pedido(self):
        """
        Procesa el próximo pedido en la cola de pedidos.
        """
        if self.cola_pedidos:
            return self.cola_pedidos.popleft()  # Procesamos el próximo pedido en la cola.
        else:
            return "No hay pedidos pendientes."

    def mostrar_estado_cola(self):
        """
        Muestra el estado actual de la cola de pedidos.
        """
        return list(self.cola_pedidos)  # Devolvemos una lista con el estado actual de la cola.

# Ejemplo:
sistema_pedidos = SistemaGestionPedidos()
sistema_pedidos.agregar_pedido("Pizza")
sistema_pedidos.agregar_pedido("Hamburguesa")
print(sistema_pedidos.mostrar_estado_cola())  # ['Pizza', 'Hamburguesa']
print(sistema_pedidos.procesar_pedido())  # Pizza
print(sistema_pedidos.mostrar_estado_cola())  # ['Hamburguesa']


# 3. Búsqueda de rutas en un laberinto
from collections import defaultdict

def encontrar_camino_laberinto(laberinto, inicio, destino):
    """
    Encuentra el camino más corto a través de un laberinto utilizando BFS.
    """
    if inicio == destino:
        return [inicio]
    
    visitados = set()
    cola = deque([(inicio, [])])
    
    while cola:
        actual, camino = cola.popleft()
        visitados.add(actual)
        
        for vecino in laberinto[actual]:
            if vecino == destino:
                return camino + [actual, vecino]
            if vecino not in visitados:
                cola.append((vecino, camino + [actual]))
                visitados.add(vecino)
    
    return "No se encontró camino."

# Ejemplo:
laberinto = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"]
}
print(encontrar_camino_laberinto(laberinto, "A", "G"))  # ['A', 'C', 'F', 'G']


# 4. Diseño de un sistema de gestión de tareas (Avanzado)
class SistemaGestionTareas:
    def __init__(self):
        """
        Inicializa un sistema de gestión de tareas con una cola vacía.
        """
        self.cola_tareas = deque()  # Inicializamos una cola para almacenar las tareas.

    def agregar_tarea(self, tarea):
        """
        Agrega una tarea a la cola de tareas.
        """
        self.cola_tareas.append(tarea)  # Agregamos la tarea a la cola de tareas.

    def marcar_completada(self):
        """
        Marca la próxima tarea en la cola de tareas como completada.
        """
        if self.cola_tareas:
            return self.cola_tareas.popleft()  # Marcamos como completada la próxima tarea en la cola.
        else:
            return "No hay tareas pendientes."

    def mostrar_proxima_tarea(self):
        """
        Muestra la próxima tarea pendiente en la cola de tareas.
        """
        if self.cola_tareas:
            return self.cola_tareas[0]  # Devolvemos la próxima tarea pendiente en la cola.
        else:
            return "No hay tareas pendientes."

# Ejemplo:
sistema_tareas = SistemaGestionTareas()
sistema_tareas.agregar_tarea("Lavar la ropa")
sistema_tareas.agregar_tarea("Hacer la compra")
print(sistema_tareas.mostrar_proxima_tarea())  # Lavar la ropa
print(sistema_tareas.marcar_completada())  # Lavar la ropa
print(sistema_tareas.mostrar_proxima_tarea())  # Hacer la compra

# Ejercicios parte 02 - Árboles:

# 5. Contar nodos
def contar_nodos(raiz):
    """
    Cuenta la cantidad de nodos en el árbol.
    """
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz.izquierda) + contar_nodos(raiz.derecha)

# Ejemplo:
# Supongamos que tenemos el siguiente árbol:
#       1
#      / \
#     2   3
#    / \
#   4   5
# La cantidad de nodos es 5.
