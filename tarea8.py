# Lista de nombres de estudiantes
nombres = ["Ana", "Luis", "Carlos", "Maria"]

# Diccionario de listas: cada materia contiene las notas
materias = {
    "Matematica": [18, 15, 17, 20],
    "Comunicacion": [16, 19, 14, 18],
    "Ciencia": [17, 16, 19, 15]
}


# 1. Calcular el promedio de una materia
def promedio_materia(materia):
    notas = materias[materia]

    if len(notas) == 0:
        return 0

    return sum(notas) / len(notas)


# 2. Encontrar al mejor estudiante de cada materia
def mejor_estudiante(materia):
    notas = materias[materia]

    if len(notas) == 0:
        return None

    mejor_nota = max(notas)
    indice = notas.index(mejor_nota)

    return nombres[indice], mejor_nota


# 3. Calcular el promedio general de cada estudiante
def promedio_estudiante(indice):
    notas_estudiante = []

    for materia in materias:
        notas_estudiante.append(materias[materia][indice])

    return sum(notas_estudiante) / len(notas_estudiante)


# 4. Generar reporte ordenado de mayor a menor
def generar_reporte():
    reporte = []

    for i in range(len(nombres)):
        promedio = promedio_estudiante(i)

        reporte.append({
            "nombre": nombres[i],
            "promedio_general": promedio
        })

    reporte.sort(
        key=lambda estudiante: estudiante["promedio_general"],
        reverse=True
    )

    return reporte


# PROGRAMA PRINCIPAL

print("=== PROMEDIOS POR MATERIA ===")

for materia in materias:
    print(f"{materia}: {promedio_materia(materia):.2f}")


print("\n=== MEJOR ESTUDIANTE POR MATERIA ===")

for materia in materias:
    nombre, nota = mejor_estudiante(materia)
    print(f"{materia}: {nombre}, nota: {nota}")


print("\n=== REPORTE GENERAL ===")

for estudiante in generar_reporte():
    print(
        f"{estudiante['nombre']}: "
        f"{estudiante['promedio_general']:.2f}"
    )