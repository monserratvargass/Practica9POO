import tkinter as tk
import random

# Función para barajar una lista A
def shuffle_data():
    num_elements = int(num_elements_entry.get())
    data = entry.get().split(',')
    
    if len(data) != num_elements:
        result_label.config(text="La cantidad de datos no coincide con el número especificado.")
        return

    random.shuffle(data)
    result_label.config(text=', '.join(data))

# Crear una ventana principal
root = tk.Tk()
root.title("Barajador de Datos")

# Etiqueta para ingresar el número de datos
num_elements_label = tk.Label(root, text="Ingrese el número de datos:")
num_elements_label.pack()

# Cuadro de entrada para el número de datos
num_elements_entry = tk.Entry(root)
num_elements_entry.pack()

# Etiqueta para ingresar datos
label = tk.Label(root, text="Ingrese los datos separados por comas:")
label.pack()

# Cuadro de entrada de datos
entry = tk.Entry(root)
entry.pack()

# Botón para barajar los datos
shuffle_button = tk.Button(root, text="Revolver", command=shuffle_data)
shuffle_button.pack()

# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="")
result_label.pack()

# Iniciar la interfaz de usuario
root.mainloop()


