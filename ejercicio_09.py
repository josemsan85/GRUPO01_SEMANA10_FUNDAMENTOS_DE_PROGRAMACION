# Enunciado 9 - Buscador inteligente con regex y ordenamiento
import re

catalogo = [
    {'titulo': 'Python a fondo',          'autor': 'Óscar Ramírez',  'año': 2021},
    {'titulo': 'Principios de programación', 'autor': 'Carlos Chacón', 'año': 2023},
    {'titulo': 'Introducción a Python',   'autor': 'Ana Python',     'año': 2019},
    {'titulo': 'Bases de datos',          'autor': 'Luis Pérez',     'año': 2020},
]

def buscador(catalogo, query):
    resultados = []
    for libro in catalogo:
        puntaje = 0
        # 1) Buscar con regex, sin importar mayúsculas (re.IGNORECASE)
        if re.search(query, libro['titulo'], re.IGNORECASE):
            puntaje = puntaje + 2      # 2) título vale 2 puntos
        if re.search(query, libro['autor'], re.IGNORECASE):
            puntaje = puntaje + 1      # autor vale 1 punto
        if puntaje > 0:
            resultados.append({'titulo': libro['titulo'], 'autor': libro['autor'],
                               'año': libro['año'], 'puntaje': puntaje})
    # 3) Ordenar por puntaje (mayor a menor) y luego por año
    resultados.sort(key=lambda r: (-r['puntaje'], r['año']))
    return resultados

for r in buscador(catalogo, 'python'):
    print(f"{r['titulo']} | {r['autor']} | {r['año']} | puntaje: {r['puntaje']}")
