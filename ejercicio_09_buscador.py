# EJERCICIO 9 – Buscador inteligente con regex y ordenamiento

import re   # Módulo de regex

catalogo = [
    {'titulo': 'Python a fondo',            'autor': 'Óscar Ramírez',  'año': 2021},
    {'titulo': 'Principios de programación', 'autor': 'Carlos Chacón',  'año': 2023},
    {'titulo': 'Introducción a Python',     'autor': 'Python Academy', 'año': 2019},
    {'titulo': 'Python Básico',             'autor': 'Luis Torres',    'año': 2018},
    {'titulo': 'Bases de Datos',            'autor': 'Ana Pérez',      'año': 2020},
]


def buscador(catalogo, query):
    resultados = []

    # 1) y 2) Buscar el query en título y autor, y dar puntos
    for libro in catalogo:
        puntaje = 0
        # Todo a minúsculas para no distinguir mayúsculas.
        # re.search() devuelve algo si encuentra el texto, y None si no lo encuentra
        if re.search(query.lower(), libro['titulo'].lower()):
            puntaje = puntaje + 2        # coincidencia en el título = 2 puntos
        if re.search(query.lower(), libro['autor'].lower()):
            puntaje = puntaje + 1        # coincidencia en el autor = 1 punto
        if puntaje > 0:                  # guardamos solo los que coincidieron
            resultados.append({'titulo': libro['titulo'],
                               'autor': libro['autor'],
                               'año': libro['año'],
                               'puntaje': puntaje})

    # 3) Ordenar: es el ordenamiento burbuja de la semana 6,
    #    pero comparando dos cosas: primero el puntaje, luego el año
    n = len(resultados)
    for i in range(n):
        for j in range(0, n - i - 1):
            actual = resultados[j]
            siguiente = resultados[j + 1]
            intercambiar = False
            if actual['puntaje'] < siguiente['puntaje']:
                intercambiar = True      # mayor puntaje debe ir primero
            elif actual['puntaje'] == siguiente['puntaje'] and actual['año'] > siguiente['año']:
                intercambiar = True      # si empatan, el año menor va primero
            if intercambiar:
                resultados[j], resultados[j + 1] = resultados[j + 1], resultados[j]

    return resultados


# Probamos el buscador
for consulta in ['python', 'ANA']:
    print(f"Búsqueda: '{consulta}'")
    for r in buscador(catalogo, consulta):
        print(f"  {r['puntaje']} pts - {r['titulo']} - {r['autor']} - {r['año']}")
