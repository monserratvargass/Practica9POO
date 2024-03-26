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
# Eliminar nodos aislados
def remove_isolated_nodes(g, color, n):
    non_isolated_nodes = []
    for i in range(n):
        if len(g.adjList[i]) > 0:
            non_isolated_nodes.append(i)
    return non_isolated_nodes

# Ordenar nodos por grado
def order_nodes_by_degree(g):
    return sorted(range(len(g.adjList)), key=lambda x: len(g.adjList[x]))

def KColoreable(g, color, k, v, n):
    if v == n:
        return 1  # Una combinación válida encontrada
    combinations = 0
    for c in range(k):
        if isSafe(g, color, v, c):
            color[v] = c
            combinations += KColoreable(g, color, k, v + 1, n)
            color[v] = None
    return combinations

 #Solicitar al usuario el número de colores, número de aristas y colores a evaluar
num_colors = int(input("Ingrese el número de libros: "))
user_colors = [input(f"Ingrese el libro {i + 1}: ") for i in range(num_colors)]

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
COLORS = user_colors

# Encuentra todas las K configuraciones coloreables del grafo
total_combinations = KColoreable(g, color, k, 0, n)

# Eliminar nodos aislados
non_isolated_nodes = remove_isolated_nodes(g, color, n)
n = len(non_isolated_nodes)

# Ordenar nodos por grado
ordered_nodes = order_nodes_by_degree(g)

# Imprimir el total de combinaciones posibles
print(f"Total de combinaciones posibles: {total_combinations}")
