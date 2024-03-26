def selector_peli(pelis, duracion, selector=[], combinaciones=[]):
    if duracion == 0:
        combinaciones.append(selector[:])
        return

    if not pelis:
        return


    sig_peli = pelis[0]
    rest_pelis = pelis[1:]
    selector_sig = selector + [sig_peli]


    if sig_peli[1] <= duracion:
        selector_peli(rest_pelis, duracion - sig_peli[1], selector_sig, combinaciones)


    selector_peli(rest_pelis, duracion, selector, combinaciones)

    return combinaciones


disponibilidad = int(input("Disponibilidad de tiempo: "))


num_pelis = int(input("Número de películas por ver: "))


pelis = []
for i in range(num_pelis):
    nombre = input(f"Película {i + 1}: ")
    duracion = int(input(f"Duracion {i + 1}: "))
    pelis.append((nombre, duracion))

combinacion = selector_peli(pelis, disponibilidad)

if not combinacion:
    print("No se encontraron combinaciones válidas.")
else:
    print("Combinaciones posibles:")
    for i, combinacion in enumerate(combinacion, 1):
        print(f"Combinación {i}:")
        duracion_total= sum(pelis[1] for pelis in combinacion)
        for pelis in combinacion:
            print(f"- {pelis[0]} ({pelis[1]} minutos)")
        print(f"Duración total: {duracion_total} minutos")
