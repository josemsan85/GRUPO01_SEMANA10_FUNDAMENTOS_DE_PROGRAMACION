# Enunciado 4 - Lista de diccionarios de estudiantes

estudiantes = [
    {'nombre': 'Ana',  'carrera': 'Sistemas',    'promedio': 16.5},
    {'nombre': 'Luis', 'carrera': 'Industrial',  'promedio': 14.0},
    {'nombre': 'Mía',  'carrera': 'Sistemas',    'promedio': 18.2},
    {'nombre': 'Juan', 'carrera': 'Civil',       'promedio': 15.3},
]

# Imprimir nombre y promedio de cada estudiante
for est in estudiantes:
    print(est['nombre'], '->', est['promedio'])

# Estudiante con el promedio más alto
mejor = estudiantes[0]
for est in estudiantes:
    if est['promedio'] > mejor['promedio']:
        mejor = est
print('Promedio más alto:', mejor['nombre'], 'con', mejor['promedio'])
