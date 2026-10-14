# Enunciado 8 - Sistema de calificaciones con estructuras combinadas

# Lista de nombres (paralela a cada lista de notas)
alumnos = ['Ana', 'Luis', 'Mía', 'Juan']

# Diccionario de listas: clave = materia, valor = notas (mismo orden que alumnos)
notas = {
    'Matemática':   [16, 14, 18, 12],
    'Programación': [19, 15, 17, 13],
    'Física':       [14, 16, 15, 18],
}

def promedio_por_materia(notas):
    promedios = {}
    for materia, lista_notas in notas.items():
        suma = 0
        for n in lista_notas:
            suma = suma + n
        promedios[materia] = suma / len(lista_notas)
    return promedios

def mejor_estudiante_por_materia(notas, alumnos):
    mejores = {}
    for materia, lista_notas in notas.items():
        indice_mejor = 0
        for i in range(len(lista_notas)):
            if lista_notas[i] > lista_notas[indice_mejor]:
                indice_mejor = i
        mejores[materia] = alumnos[indice_mejor]   # mismo índice en alumnos
    return mejores

def reporte_general(notas, alumnos):
    # Promedio general de cada alumno (suma de sus notas en todas las materias)
    reporte = []
    for i in range(len(alumnos)):
        suma = 0
        for materia in notas:
            suma = suma + notas[materia][i]
        reporte.append({'alumno': alumnos[i], 'promedio': suma / len(notas)})
    # Ordenar de mayor a menor
    reporte.sort(key=lambda r: r['promedio'], reverse=True)
    return reporte

print('Promedio por materia:')
for materia, prom in promedio_por_materia(notas).items():
    print(f'  {materia}: {prom}')

print('Mejor estudiante por materia:')
for materia, nombre in mejor_estudiante_por_materia(notas, alumnos).items():
    print(f'  {materia}: {nombre}')

print('Reporte ordenado por promedio general:')
for r in reporte_general(notas, alumnos):
    print(f"  {r['alumno']}: {r['promedio']:.2f}")
