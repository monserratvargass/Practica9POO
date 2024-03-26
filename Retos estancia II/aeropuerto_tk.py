import tkinter as tk
from tkinter import simpledialog

# Función para imprimir el itinerario de una fuente dada
def print_itinerary(dictionary, src):
    dest = dictionary.get(src)
    if not dest:
        return
    itinerary.append(f"{src} -> {dest}")
    print_itinerary(dictionary, dest)

# Función para encontrar el itinerario de la lista de aeropuertos de salida y llegada
def find_itinerary(tickets):
    # Construir un conjunto de aeropuertos de destino
    destinations = {*tickets.values()}
    
    # Considerar cada aeropuerto de salida para encontrar el aeropuerto de origen
    for k, v in tickets.items():
        # El aeropuerto de origen no estará presente en la lista de aeropuertos de destino
        if k not in destinations:
            # Cuando se encuentre el aeropuerto de origen, imprimir el itinerario
            print_itinerary(tickets, k)
            return

def get_ticket_information():
    global tickets
    tickets = {}
    
    num_trayectos_str = simpledialog.askstring("Trayectos", "¿Cuántos trayectos hay?")
    
    if num_trayectos_str is not None:
        try:
            num_trayectos = int(num_trayectos_str)
            for i in range(num_trayectos):
                origen = simpledialog.askstring(f"Trayecto {i + 1}", "Aeropuerto de origen:")
                destino = simpledialog.askstring(f"Trayecto {i + 1}", "Aeropuerto de destino:")
                tickets[origen] = destino

            find_itinerary(tickets)
            display_itinerary()
        except ValueError:
            print("Por favor, ingresa un número válido de trayectos.")


def display_itinerary():
    global itinerary
    itinerary = []
    get_ticket_information()
    
    root = tk.Tk()
    root.title("Itinerario de Trayectos")
    
    label = tk.Label(root, text="Itinerario de Trayectos")
    label.pack()
    
    itinerary_text = "\n".join(itinerary)
    text_widget = tk.Text(root, height=10, width=40)
    text_widget.insert(tk.END, itinerary_text)
    text_widget.pack()
    
    root.mainloop()

if __name__ == '__main__':
    display_itinerary()
