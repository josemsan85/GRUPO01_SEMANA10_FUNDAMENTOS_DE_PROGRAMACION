sistema_academico = {
    'Matemáticas': {'estudiantes': ['Ana', 'Carlos', 'Beatriz'], 'notas': [15, 18, 12]},
    'Programación': {'estudiantes': ['Ana', 'Carlos', 'Beatriz'], 'notas': [19, 14, 16]}
}
print("--- PROMEDIO POR MATERIA ---")
for materia, datos in sistema_academico.items():
    promedio = sum(datos['notas']) / len(datos['notas'])
    print(f"{materia}: {promedio:.2f}")
alumnos = list(sistema_academico['Matemáticas']['estudiantes'])
acumulador_notas = {alumno: [] for alumno in alumnos}
for materia, datos in sistema_academico.items():
    for i, alumno in enumerate(datos['estudiantes']):
        acumulador_notas[alumno].append(datos['notas'][i])
reporte_general = [{'estudiante': a, 'promedio_general': sum(n)/len(n)} for a, n in acumulador_notas.items()]
reporte_general.sort(key=lambda x: x['promedio_general'], reverse=True)
print("\n--- REPORTE GENERAL DE ESTUDIANTES ---")
for r in reporte_general:
    print(f"Estudiante: {r['estudiante']} | Promedio General: {r['promedio_general']:.2f}")