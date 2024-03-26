class Persona:
    def __init__(self, nombre, padre=None):
        self.nombre = nombre
        self.padre = padre
        self.descendientes = []

    def agregar_descendiente(self, descendiente):
        self.descendientes.append(descendiente)

def crear_arbol():
    nombre_raiz = "Zeus"
    raiz = Persona(nombre_raiz)
    return raiz

def agregar_descendientes(persona, descendientes):
    for nombre, padre in descendientes:
        if padre == persona.nombre:
            descendiente = Persona(nombre, padre=persona)
            persona.agregar_descendiente(descendiente)
            agregar_descendientes(descendiente, descendientes)

def encontrar_ancestro_comun(personas):
    ancestros = set()
    for persona in personas:
        ancestros_de_persona = set()
        while persona:
            ancestros_de_persona.add(persona)
            persona = persona.padre

        if not ancestros:
            ancestros = ancestros_de_persona
        else:
            ancestros = ancestros.intersection(ancestros_de_persona)

    if ancestros:
        return max(ancestros, key=lambda x: personas.index(x))
    else:
        return None

def buscar_ancestro_comun_arbol(arbol):
    while True:
        num_personas = int(input("¿Cuántas personas quieres buscar? "))

        nombres = []
        for i in range(num_personas):
            nombre = input(f"Ingresa el nombre de la persona {i + 1}: ")
            nombres.append(nombre)

        personas = [persona for persona in arbol.descendientes if persona.nombre in nombres]

        if len(personas) != num_personas:
            print("Uno o más nombres no se encuentran en el árbol.")
        else:
            ancestro_comun = encontrar_ancestro_comun(personas)
            if ancestro_comun is not None:
                print(f"El ancestro común más cercano de {', '.join(nombres)} es {ancestro_comun.nombre}.")
            else:
                print(f"{', '.join(nombres)} no tienen un ancestro común en este árbol.")



arbol = crear_arbol()
descendientes = [ 
    ("Zeus", ""),
    ("Artemisa", "Zeus"),
    ("Apolo", "Zeus"),
    ("Hermes", "Artemisa"),
    ("Callisto", "Artemisa"),
    ("Asclepio", "Apolo"),
    ("Orfeo", "Apolo"),
    ("Podalirio", "Asclepio"),
    ("Machaon", "Asclepio"),
    ("Linus", "Orfeo"),
    ("Eurydice", "Orfeo"),
    ("Pan", "Hermes"),
    ("Dionisio", "Hermes"),
    ("Arcas", "Callisto"),
    ("Iasion", "Callisto"),
    ("Machaon", "Podalirio"),
    ("Polidoro", "Podalirio"),
    ("Nireo", "Machaon"),
    ("Nicomedes", "Machaon"),
    ("Gargareia", "Eurydice"),
    ("Argonautas", "Eurydice"),
    ("Silenos", "Pan"),
    ("Eufeme", "Pan"),
    ("Priapo", "Dionisio"),
    ("Ámpelo", "Dionisio"),
    ("Elato", "Arcas"),
    ("Azeo", "Arcas"),
    ("Demofonte", "Iasion"),
    ("Pluto", "Iasion"),
    ("Peonio", "Polidoro"),
    ("Polifonte", "Polidoro"),
    ("Iofante", "Nireo"),
    ("Pandaro", "Nireo"),
    ("Linanto", "Nicomedes"),
    ("Medonte", "Nicomedes"),
    ("Licaón", "Gargareia"),
    ("Cecropia", "Gargareia"),
    ("Cánace", "Argonautas"),
    ("Estinfalo", "Argonautas"),
    ("Fauno", "Silenos"),
    ("Marone", "Silenos"),
    ("Batus", "Eufeme"),
    ("Eurínome", "Eufeme"),
    ("Adono", "Priapo"),
    ("Céfiro", "Priapo"),

    ("Bromio", "Ámpelo"),
    ("Oinopion", "Ámpelo"),

    ("Apolis", "Elato"),
    ("Toxeo", "Elato"),

    ("Carpo", "Azeo"),
    ("Eufrósine", "Azeo"),
    ("Amintor", "Demofonte"),
    ("Cale", "Demofonte"),
    ("Zagreo", "Pluto"),
    ("Íaco", "Pluto"),
    ("Anficlea", "Peonio"),
    ("Icario", "Peonio"),
    ("Bacis", "Polifonte"),
    ("Cometes", "Polifonte"),

    #primer pagina

    ("Sicino", "Iofante"),
    ("Ceáfix", "Iofante"),
    ("Atymnius", "Pandaro"),
    ("Equeclea", "Pandaro"),
    ("Aleimón", "Linanto"),
    ("Acestor", "Linanto"),
    ("Lago", "Medonte"),
    ("Capaneo", "Medonte"),

    ("Nicomaсo", "Licaón"),
    ("Misipe", "Licaón"),
    ("Erecteo", "Cecropia"),
    ("Atenea", "Cecropia"),
    ("Linceo", "Cánace"),
    ("Abante", "Cánace"),
    ("Atys", "Estínfalo"),
    ("Milón", "Estínfalo"),
    ("Latínus", "Fauno"),
    ("Tarquino", "Fauno"),
    ("Sileno", "Marone"),
    ("Milo", "Marone"),
    ("Elatiades", "Batus"),
    ("Epeio", "Batus"),
    ("Lacedemon", "Eurínome"),
    ("Gala", "Eurínome"),
    ("Ninias", "Adono"),
    ("Agdistis", "Adono"),
    ("Balio", "Céfiro"),
    ("Xanto", "Céfiro"),
    ("Liriope", "Bromio"),
    ("Naso", "Bromio"),
    ("Ampelo", "Oinopion"),
    ("Tiro", "Oinopion"),
    ("Ascaio", "Carpo"),
    ("Corinto", "Carpo"),
    ("Cleta", "Eufrósine"),
    ("Euforión", "Eufrósine"),
    ("Emetes", "Amintor"),
    ("Estesícoro", "Amintor"),
    ("Micceón", "Cale"),
    ("Lutro", "Cale"),
    ("Ágave", "Zagreo"),
    ("Pantíno", "Zagreo"),
    ("Acasto", "Íaco"),
    ("Pelias", "Íaco"),
    ("Milo", "Anficlea"),
    ("Bato", "Anficlea"),
    ("Ersínoe", "Icario"),
    ("Ritmo", "Icario"),
    ("Cleoboea", "Bacis"),
    ("Ismaro", "Bacis"),
    ("Lelanto", "Cometes"),
    ("Titono", "Cometes"),
    ("Etolo", "Sicino"),
    ("Sibaris", "Sicino"),
    ("Toloso", "Ceáfix"),
    ("Cécrope", "Ceáfix"),
    ("Aglao", "Atymnius"),
    ("Androgea", "Atymnius"),
    ("Ergino", "Equeclea"),
    ("Periboea", "Equeclea"),
    ("Pilos", "Aleimón"),
    ("Argeo", "Aleimón"),

    #segunda pagina

    ("Poeas", "Acestor"),
    ("Piritoo", "Acestor"),
    ("Clitio", "Lago"),
    ("Perieres", "Lago"),
    ("Licofonte", "Capaneo"),
    ("Ilares", "Capaneo"),
    ("Alcmeón", "Nicomaco"),
    ("Erato", "Nicomaco"),
    ("Anaxibia", "Misipe"),
    ("Astioquia", "Misipe"),
    ("Aglauro", "Erecteo"),
    ("Herse", "Erecteo"),
    ("Erictonio", "Atenea"),
    ("Pandión", "Atenea"),
    ("Abante", "Linceo"),
    ("Eurícione", "Linceo"),
    ("Pero", "Abante"),
    ("Laódice", "Abante"),

    ("Aglaura", "Atys"),
    ("Aglie", "Atys"),

    ("Deifobo", "Milón"),
    ("Deifobo", "Milón"),

    ("Silvius", "Latínus"),
    ("Aventino", "Latínus"),

    ("Arúntio", "Tarquino"),
    ("Tanaquil", "Tarquino"),
    ("Sileno", "Marone"),
    ("Milo", "Marone"),
    ("Elatiades", "Batus"),
    ("Epeio", "Batus"),
    ("Himera", "Lutro"),
    ("Eryx", "Lutro"),
    ("Penteo", "Ágave"),
    ("Pirante", "Ágave"),
    ("Menesicle", "Pantíno"),
    ("Leocoridas", "Pantíno"),
    ("Ceneo", "Androgea"),
    ("Glanis", "Androgea"),
    ("Corinna", "Ergino"),
    ("Hípaso", "Ergino"),
    ("Oeneus", "Periboea"),
    ("Agrius", "Periboea"),
    ("Philammon", "Poeas"),
    ("Sarpedon", "Poeas"),
    ("Polidoro", "Piritoo"),
    ("Cleopatra", "Piritoo"),
    ("Andrómaca", "Nicomaco"),
    ("Astianacte", "Nicomaco"),
    ("Harmonia", "Misipe"),
    ("Semele", "Misipe"),
    ("Cecrops", "Aglauro"),
    ("Erysichthon", "Aglauro"),
    ("Pandión", "Erictonio"),
    ("Butes", "Erictonio"),
    #tercera pagina
    ("Fílira", "Sileno"),
    ("Pegaso", "Sileno"),
    ("Astídamas", "Milo"),
    ("Tiagro", "Milo"),
    ("Ameinias", "Elatiades"),
    ("Molon", "Elatiades"),
    ("Endeo", "Epeio"),
    ("Toxeo", "Epeio"),
    ("Dorio", "Lacedemon"),
    ("Eurice", "Lacedemon"),
    ("Alexiada", "Gala"),
    ("Polydora", "Gala"),
    ("Cuidir", "Ninias"),
    ("Polyxeño", "Ninias"),
    ("Circe", "Agdistis"),
    ("Acis", "Agdistis"),
    ("Jocasta", "Balio"),
    ("Harmonía", "Balio"),
    ("Antígona", "Xanto"),
    ("Ismene", "Xanto"),
    ("Narciso", "Liriope"),
    ("Melo", "Liriope"),
    ("Línea", "Ampelo"),
    ("Calcone", "Ampelo"),
    ("Neleo", "Tiro"),
    ("Pelias", "Tiro"),
    ("Ateneo", "Ascaio"),
    ("Autoctona", "Ascaio"),
    #termina segunda pagina
    #tercera pagina ""
    ("Eunostos", "Corinto"),
    ("Bellerofonte", "Corinto"),
    ("Doris", "Cleta"),
    ("Melite", "Cleta"),
    ("Deífone", "Euforión"),
    ("Danae", "Euforión"),
    ("Psamathe", "Emetes"),
    ("Echinades", "Emetes"),
    ("Arete", "Estesícoro"),
    ("Nicias", "Estesícoro"),
    ("Hipseo", "Micceón"),
    ("Sceus", "Micceón"),
    ("Himera", "Lutro"),
    ("Eryx", "Lutro"),
    ("Penteo", "Ágave"),
    ("Pirante", "Ágave"),
    ("Menesicle", "Pantíno"),
    ("Leocoridas", "Pantíno"),
    ("Butes", "Ersínoe"),
    ("Crenaeus", "Ersínoe"),
    ("Tirreno", "Ritmo"),
    ("Carme", "Ritmo"),
    ("Clytie", "Cleoboea"),
    ("Leucothea", "Cleoboea"),
    ("Marpessa", "Ismaro"),
    ("Hypsipyle", "Ismaro"),
    ("Pegasides", "Lelanto"),
    ("Nereides", "Lelanto"),
    ("Eos", "Titono"),
    ("Hemera", "Titono"),
    ("Leucippe", "Etolo"),
    ("Thestius", "Etolo"),
    ("Hesperia", "Sibaris"),
    ("Iapyx", "Sibaris"),
    ("Gelone", "Toloso"),
    ("Batis", "Toloso"),
    ("Europa", "Cécrope"),
    ("Cadmus", "Cécrope"),
    ("Lilaea", "Aglao"),
    ("Podargos", "Aglao"),
    ("Ceneo", "Androgea"),
    ("Glanis", "Androgea"),
    ("Corinna", "Ergino"),
    ("Hípaso", "Ergino"),
    ("Oeneus", "Periboea"),
    ("Agrius", "Periboea"),
    ("Philammon", "Poeas"),
    ("Sarpedon", "Poeas"),
    ("Polidoro", "Piritoo"),
    ("Cleopatra", "Piritoo"),
    ("Andrómaca", "Nicomaco"),
    ("Astianacte", "Nicomaco"),
    ("Harmonia", "Misipe"),
    ("Semele", "Misipe"),
    ("Cecrops", "Aglauro"),
    ("Erysichthon", "Aglauro"),
    ("Pandión", "Erictonio"),
    ("Butes", "Erictonio"),
    # termina cuarta pagina """
    ("Egeo", "Pandión"),
    ("Pallas", "Pandión"),
    ("Heraclides", "Cálice"),
    ("Perseus", "Cálice"),
    ("Bellerofonte", "Pegaso"),
    ("Melanip", "Pegaso"),# Aquí van tus descendientes como en el código original
]

agregar_descendientes(arbol, descendientes)
buscar_ancestro_comun_arbol(arbol)



