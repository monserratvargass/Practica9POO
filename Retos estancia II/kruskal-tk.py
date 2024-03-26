import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def kruskal(graph):
    mst = nx.Graph()
    edges = list(graph.edges(data=True))
    edges.sort(key=lambda x: x[2]['weight'])
    sets = {node: set([node]) for node in graph.nodes()}
    
    for edge in edges:
        u, v, w = edge
        if sets[u] != sets[v]:
            mst.add_edge(u, v, weight=w['weight'])
            sets[u] |= sets[v]
            for node in sets[v]:
                sets[node] = sets[u]
    
    return mst

def draw_graph(graph):
    pos = nx.spring_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color='skyblue')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.axis('off')
    plt.show()

def add_edge():
    node1 = entry_node1.get()
    node2 = entry_node2.get()
    weight = float(entry_weight.get())
    
    if node1 and node2 and weight:
        G.add_edge(node1, node2, weight=weight)
        canvas.get_tk_widget().destroy()
        canvas = FigureCanvasTkAgg(plt.figure(), master=frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        draw_graph(G)
        entry_node1.delete(0, tk.END)
        entry_node2.delete(0, tk.END)
        entry_weight.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

def calculate_mst():
    mst = kruskal(G)
    canvas.get_tk_widget().destroy()
    canvas = FigureCanvasTkAgg(plt.figure(), master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    draw_graph(mst)

# Crear una ventana Tkinter
root = tk.Tk()
root.title("Kruskal Algorithm")

# Crear un grafo vacío
G = nx.Graph()

# Crear y configurar los widgets
frame = tk.Frame(root)
frame.pack(pady=10)

label_node1 = tk.Label(frame, text="Nodo 1:")
label_node1.pack()
entry_node1 = tk.Entry(frame)
entry_node1.pack()

label_node2 = tk.Label(frame, text="Nodo 2:")
label_node2.pack()
entry_node2 = tk.Entry(frame)
entry_node2.pack()

label_weight = tk.Label(frame, text="Peso:")
label_weight.pack()
entry_weight = tk.Entry(frame)
entry_weight.pack()

add_edge_button = tk.Button(frame, text="Agregar Arista", command=add_edge)
add_edge_button.pack()

calculate_button = tk.Button(frame, text="Calcular MST", command=calculate_mst)
calculate_button.pack()

canvas = FigureCanvasTkAgg(plt.figure(), master=frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Iniciar la interfaz gráfica
root.mainloop()
