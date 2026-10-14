import re

def buscador(catalogo, query):
    resultados = []

    # Compilar la expresión regular sin distinguir mayúsculas
    patron = re.compile(re.escape(query), re.IGNORECASE)

    for libro in catalogo:
        puntaje = 0

        # Buscar en el título: 2 puntos
        if patron.search(libro["titulo"]):
            puntaje += 2

        # Buscar en el autor: 1 punto
        if patron.search(libro["autor"]):
            puntaje += 1

        # Guardar solo libros que coincidan
        if puntaje > 0:
            resultado = libro.copy()
            resultado["puntaje"] = puntaje
            resultados.append(resultado)

    # Ordenar por puntaje descendente y año ascendente
    resultados.sort(
        key=lambda libro: (-libro["puntaje"], libro["año"])
    )

    return resultados


# Catálogo de ejemplo
catalogo = [
    {"titulo": "Python desde cero", "autor": "Ana García", "año": 2020},
    {"titulo": "Aprende programación", "autor": "Luis Pérez", "año": 2018},
    {"titulo": "Python avanzado", "autor": "Carlos Python", "año": 2022},
    {"titulo": "Introducción a Python", "autor": "Ana García", "año": 2019},
    {"titulo": "Bases de datos", "autor": "Ana Torres", "año": 2017}
]

# Realizar la búsqueda
resultados = buscador(catalogo, "Python")

# Mostrar resultados
for libro in resultados:
    print(
        f"Título: {libro['titulo']} | "
        f"Autor: {libro['autor']} | "
        f"Año: {libro['año']} | "
        f"Puntaje: {libro['puntaje']}"
    )