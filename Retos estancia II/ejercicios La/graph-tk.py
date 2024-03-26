# Clase para representar un objeto grafo
class Graph:
    # Constructor
    def __init__(self, adjList):
        # Inicializa la lista de adyacencia
        self.adjList = adjList

# Prueba todas las combinaciones posibles de colores para cada nodo
def isSafe(g, color, v, c):
    for u in g.adjList[v]:
        if color[u] == c:
            return False
    return True

# Encuentra todas las K configuraciones coloreables del grafo
def KColoreable(g, color, k, v, n):
    if v == n:
        # Imprime la configuración de color actual
        print([COLORS[color[i]] for i in range(n)])
        return
    for c in range(k):
        if isSafe(g, color, v, c):
            color[v] = c
            KColoreable(g, color, k, v + 1, n)
            color[v] = None  # Restablece el color para volver a probar con otros colores

# Solicitar al usuario el número de colores, número de aristas y colores a evaluar
num_colors = int(input("Ingrese el número de colores: "))
user_colors = [input(f"Ingrese el color {i + 1}: ") for i in range(num_colors)]

# Solicitar al usuario las aristas y sus listas adyacentes
n = int(input("Ingrese el número de nodos: "))
adjList = [[] for _ in range(n)]

for i in range(n):
    adjacent_list = input(f"Ingrese la lista adyacente para el nodo {i}, separada por espacios: ").split()
    adjacent_list = [int(vertex) for vertex in adjacent_list]
    adjList[i] = adjacent_list

# Construir el grafo a partir de los datos anteriores
g = Graph(adjList)
k = num_colors
color = [None] * n
COLORS = user_colors  # Usar los colores ingresados por el usuario

# Imprime todas las K configuraciones coloreables del grafo
KColoreable(g, color, k, 0, n)