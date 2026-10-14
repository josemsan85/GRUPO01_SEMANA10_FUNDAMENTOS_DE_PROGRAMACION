# EJERCICIO 8 – Sistema de calificaciones con estructuras combinadas

# Lista de nombres + diccionario de listas (arreglos paralelos):
# la posición i de cada lista de notas es del estudiante nombres[i]
nombres = ['Ana', 'Luis', 'Mía', 'Juan']
notas = {
    'Matemática':   [18, 14, 16, 12],
    'Programación': [20, 15, 17, 13],
    'Física':       [16, 13, 19, 11],
}


# Función 1: promedio de cada materia
def promedio_por_materia(notas):
    promedios = {}
    for materia, lista in notas.items():
        promedios[materia] = sum(lista) / len(lista)
    return promedios


# Función 2: mejor estudiante de cada materia
def mejor_por_materia(nombres, notas):
    mejores = {}
    for materia, lista in notas.items():
        mejor_nota = 0
        mejor_nombre = ''
        # zip junta cada nombre con su nota
        for nombre, nota in zip(nombres, lista):
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = nombre
        mejores[materia] = mejor_nombre
    return mejores


# Función 3: reporte ordenado por promedio general de cada estudiante
def reporte_general(nombres, notas):
    reporte = []
    for i in range(len(nombres)):          # i = posición del estudiante
        suma = 0
        for materia, lista in notas.items():
            suma = suma + lista[i]         # su nota en cada materia
        promedio = suma / len(notas)       # entre la cantidad de materias
        reporte.append({'nombre': nombres[i], 'promedio': promedio})
    # Ordenar de mayor a menor promedio
    reporte.sort(key=lambda r: r['promedio'], reverse=True)
    return reporte


# Probamos las 3 funciones
print('Promedio por materia:')
for materia, prom in promedio_por_materia(notas).items():
    print(f'  {materia}: {prom:.2f}')

print('Mejor estudiante por materia:')
for materia, nombre in mejor_por_materia(nombres, notas).items():
    print(f'  {materia}: {nombre}')

print('Reporte general (de mayor a menor):')
for r in reporte_general(nombres, notas):
    print(f"  {r['nombre']}: {r['promedio']:.2f}")
