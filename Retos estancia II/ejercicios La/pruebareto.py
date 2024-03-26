class Graph:
    def __init__(self, edges, n):
        self.adj = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)

def isSafe(g, color, v, c):
    for u in g.adj[v]:
        if color[u] == c:
            return False
    return True

def kColorableWithColors(g, color, k, v, n, count):
    if v == n:
        count[0] += 1
        return
    for c in range(1, k + 1):
        if isSafe(g, color, v, c):
            color[v] = c
            kColorableWithColors(g, color, k, v + 1, n, count)
            color[v] = 0

if __name__ == '__main__':
    edges = [(0, 1), (0, 2), (0, 7), (0, 3), (1, 2), (1, 3), (1, 4), (1, 6), (1, 7), (2, 4), (2, 5), (2, 6), (3, 4), (3, 7), (4, 6), (5, 7), (6, 7)]
    n = 8
    k = 7
    g = Graph(edges, n)
    color = [None] * n
    count = [0]
    kColorableWithColors(g, color, k, 0, n, count)
    print(f"Total de iteraciones: {count[0]}")