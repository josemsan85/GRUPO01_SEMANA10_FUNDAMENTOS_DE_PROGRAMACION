# EJERCICIO 4 – Lista de diccionarios de estudiantes
# Cada diccionario es un estudiante completo (con sus campos con nombre).

estudiantes = [
    {'nombre': 'Ana',  'carrera': 'Sistemas',     'promedio': 17.5},
    {'nombre': 'Luis', 'carrera': 'Industrial',   'promedio': 14.0},
    {'nombre': 'Mía',  'carrera': 'Contabilidad', 'promedio': 18.5},
    {'nombre': 'Juan', 'carrera': 'Sistemas',     'promedio': 15.0},
]

# Imprimir el nombre y el promedio de cada estudiante
for est in estudiantes:
    print(est['nombre'], '->', est['promedio'])

# Buscar el promedio más alto:
# empezamos suponiendo que el primero es el mejor
mejor = estudiantes[0]
for est in estudiantes:
    if est['promedio'] > mejor['promedio']:   # si encontramos uno mayor, lo cambiamos
        mejor = est

print('Estudiante con el promedio más alto:', mejor['nombre'])
