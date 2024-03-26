import tkinter as tk
from tkinter import messagebox

def findMajorityElement(nums):
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1
    for key, value in d.items():
        if value > len(nums) / 2:
            return key
    return -1

def find_majority_element():
    input_list = entry.get()
    nums = list(map(int, input_list.split(',')))
    result = findMajorityElement(nums)
    if result != -1:
        messagebox.showinfo("Resultado", f"El elemento mayoritario es {result}")
    else:
        messagebox.showinfo("Resultado", "No hay elemento mayoritario")

# Crear una ventana Tkinter
root = tk.Tk()
root.title("Encontrar Elemento Mayoritario")

# Crear y configurar widgets
label = tk.Label(root, text="Ingresa una lista de números separados por comas:")
label.pack()

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Encontrar Elemento Mayoritario", command=find_majority_element)
calculate_button.pack()

# Iniciar la interfaz gráfica
root.mainloop()
