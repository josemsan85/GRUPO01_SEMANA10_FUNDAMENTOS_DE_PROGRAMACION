estudiantes = [
    {'nombre': 'Lucía', 'carrera': 'Ingeniería de Sistemas', 'promedio': 16.5},
    {'nombre': 'Mateo', 'carrera': 'Software', 'promedio': 18.2},
    {'nombre': 'Sofía', 'carrera': 'Industrial', 'promedio': 14.8},
    {'nombre': 'Diego', 'carrera': 'Civil', 'promedio': 17.0}
]
print("--- LISTA DE ESTUDIANTES ---")
for est in estudiantes:
    print(f"Estudiante: {est['nombre']} | Promedio: {est['promedio']}")
mejor_estudiante = max(estudiantes, key=lambda x: x['promedio'])
print(f"\nEstudiante con el promedio más alto: {mejor_estudiante['nombre']} ({mejor_estudiante['promedio']})")