#funcion para imprimir el intenerario de una fuente dada 
def print_itinerary(dictionary, src):
    dest=dictionary.get(src)
    if not dest:
        return
    print(src+'->'+dest)
    print_itinerary(dictionary,dest)

#funcion para encontrar el itinerario de la lista dadd de aeropuertos de salida y llegada
def findintinerary(tickets):
    #construir un conjunto de aeropuertos de destino
    destinations={*tickets.values()}
    #considere cada aeropuertos de salida para encontrea rle laaeropuertos de origen
    for k, v in tickets.items():
        #el aeropuerto de origen # no estara presente en la lista de aeropuertos de destino
        if k not in destinations:
            #cuando se en encuenttre el aeropuerto de origen, imprima el itinerario
            print_itinerary(tickets,k)
            return
if __name__=='__main__':
    #entrada #: lista de tickets
    tickets={
        'aragon': 'oceania',
        'hangares': 'pantitlan',
        'misterios': 'valle gomez',
        'instituto del petroleo': 'la raza',
        'consumado': 'aragon',
        'terminal aerea': 'hangares',
        'politecnico': 'instituto del petroleo',
        'valle gomez': 'consumado',
        'oceania': 'terminal aerea',
        'la raza': 'misterios',

    }

    findintinerary(tickets)