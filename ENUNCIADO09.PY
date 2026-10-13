import re
catalogo_libros = [
    {'titulo': 'Python para Todos', 'autor': 'Raúl Gómez', 'año': 2020},
    {'titulo': 'Introducción a Java', 'autor': 'Ana Torres', 'año': 2018},
    {'titulo': 'Estructuras de Datos en Python', 'autor': 'Raúl Gómez', 'año': 2022},
    {'titulo': 'Avanzado en Python', 'autor': 'Raúl Pérez', 'año': 2019}
]
def buscador(catalogo, query):
    resultados = []
    patron = re.compile(re.escape(query), re.IGNORECASE)
    for libro in catalogo:
        puntaje = 0
        if patron.search(libro['titulo']):
            puntaje += 2
        if patron.search(libro['autor']):
            puntaje += 1
        if puntaje > 0:
            resultados.append({
                'titulo': libro['titulo'],
                'autor': libro['autor'],
                'año': libro['año'],
                'puntaje': puntaje
            })
    n = len(resultados)
    for i in range(n):
        for j in range(0, n - i - 1):
            if resultados[j]['puntaje'] < resultados[j + 1]['puntaje']:
                resultados[j], resultados[j + 1] = resultados[j + 1], resultados[j]
            elif resultados[j]['puntaje'] == resultados[j + 1]['puntaje']:
                if resultados[j]['año'] > resultados[j + 1]['año']:
                    resultados[j], resultados[j + 1] = resultados[j + 1], resultados[j]
    return resultados
resultados_busqueda = buscador(catalogo_libros, "Python")
for r in resultados_busqueda:
    print(f"Título: {r['titulo']} | Autor: {r['autor']} | Año: {r['año']} | Puntaje: {r['puntaje']}")