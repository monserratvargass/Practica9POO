# Clase para representar un objeto grafo
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # Una lista de listas para representar una lista adyacencia
        self.adjList = [[] for _ in range(n)]
        # Agrega bordes al grafo no dirigido
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

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

if __name__ == '_main_':
    # Lista de bordes del grafo
    edges =[(1,2),(1,3),(2,3),(2,5),(2,4),(4,5),(4,7),(5,7),(5,6),(6,7)]
    # Lista para almacenar colores (puede manejar 10 grafos coloreables)
    COLORS = ['BLUE', 'GREEN', 'RED', 'YELLOW', 'ORANGE', 'PINK', 'BLACK', 'BROWN', 'WHITE', 'PURPLE']
    # Establecer el número de vértices (nodos) en el grafo
    n = 6
    # Construir el grafo a partir de los datos anteriores
    g = Graph(edges, n)
    k = 2
    color = [None] * n
    # Imprime todas las K configuraciones coloreables del grafo
    KColoreable(g, color, k, 0, n)