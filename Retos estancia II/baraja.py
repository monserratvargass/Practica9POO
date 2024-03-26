import tkinter as tk
import random

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def shuffler(A):
    for i in range(len(A) - 1):

        j = random.randrange(i, len(A))

        swap(A, i, j)

nombres_cartas = ["2 de Corazones", "3 de Corazones", "4 de Corazones", "5 de Corazones", "6 de Corazones",
                 "7 de Corazones", "8 de Corazones", "9 de Corazones", "10 de Corazones", "J de Corazones",
                 "Q de Corazones", "K de Corazones", "A de Corazones", "2 de Diamantes", "3 de Diamantes",
                 "4 de Diamantes", "5 de Diamantes", "6 de Diamantes", "7 de Diamantes", "8 de Diamantes",
                 "9 de Diamantes", "10 de Diamantes", "J de Diamantes", "Q de Diamantes", "K de Diamantes",
                 "A de Diamantes", "2 de Tréboles", "3 de Tréboles", "4 de Tréboles", "5 de Tréboles",
                 "6 de Tréboles", "7 de Tréboles", "8 de Tréboles", "9 de Tréboles", "10 de Tréboles",
                 "J de Tréboles", "Q de Tréboles", "K de Tréboles", "A de Tréboles", "2 de Picas", "3 de Picas",
                 "4 de Picas", "5 de Picas", "6 de Picas", "7 de Picas", "8 de Picas", "9 de Picas",
                 "10 de Picas", "J de Picas", "Q de Picas", "K de Picas", "A de Picas"]

def repartir_cartas():
    num_jugadores = int(entry_num_jugadores.get())
    
    if num_jugadores < 2 or num_jugadores > 4:
        label_resultado.config(text="Error: Deben haber entre 2 y 4 jugadores.")
    else:
        cartas_por_jugador = 7
        cartas_totales = num_jugadores * cartas_por_jugador
        
        if cartas_totales > len(nombres_cartas):
            label_resultado.config(text="Error: No hay suficientes cartas para repartir.")
        else:
            shuffler(nombres_cartas)
            manos = [[] for _ in range(num_jugadores)]
            for _ in range(cartas_por_jugador):
                for jugador in range(num_jugadores):
                    carta = nombres_cartas.pop()
                    manos[jugador].append(carta)
            
            resultado = "Manos de los jugadores:\n\n"
            for jugador, mano in enumerate(manos, 1):
                resultado += f"Jugador {jugador}: {', '.join(mano)}\n"
            
            resultado += "\nCartas restantes en la baraja:\n" + ', '.join(nombres_cartas)
            label_resultado.config(text=resultado)


ventana_principal = tk.Tk()
ventana_principal.title("Repartir Cartas")
ventana_principal.geometry("800x400")

label_num_jugadores = tk.Label(ventana_principal, text="Número de jugadores (2-4):")
label_num_jugadores.pack()
entry_num_jugadores = tk.Entry(ventana_principal)
entry_num_jugadores.pack()

boton_repartir = tk.Button(ventana_principal, text="Repartir Cartas", command=repartir_cartas)
boton_repartir.pack()

label_resultado = tk.Label(ventana_principal, text="",justify="center")
label_resultado.pack()

ventana_principal.mainloop()