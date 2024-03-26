
def select_movies(movies, duration, selected=[]):
    if duration == 0:
        return selected
    if not movies:
        return None

    # Intentar ver la próxima película
    next_movie = movies[0]
    remaining_movies = movies[1:]
    selected_with_next = selected + [next_movie]

    # Caso 1: Ver la próxima película
    if next_movie[1] <= duration:
        result = select_movies(remaining_movies, duration - next_movie[1], selected_with_next)
        if result is not None:
            return result

    # Caso 2: No ver la próxima película
    result = select_movies(remaining_movies, duration, selected)
    return result

# Ejemplo de lista de películas (nombre, duración en minutos)
movies = [("Pelicula A", 120), ("Pelicula B", 90), ("Pelicula C", 150), ("Pelicula D", 60)]

# Duración máxima de la noche en minutos
night_duration = 240

selected_movies = select_movies(movies, night_duration)

if selected_movies:
    print("Películas seleccionadas:")
    for movie in selected_movies:
        print(f"- {movie[0]} ({movie[1]} minutos)")
else:
    print("No se encontró una combinación de películas para la duración de la noche.")

