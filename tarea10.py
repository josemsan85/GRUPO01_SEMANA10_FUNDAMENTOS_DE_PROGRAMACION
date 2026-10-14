
import re
from collections import Counter

def analizar_texto(parrafo):
    # 1. Extraer palabras usando regex: solo letras y apóstrofes
    palabras = re.findall(r"[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ']+", parrafo)

    # 2. Normalizar a minúsculas y contar frecuencias
    palabras = [palabra.lower() for palabra in palabras]
    frecuencias = Counter(palabras)

    # 3. Ordenar por frecuencia descendente y alfabéticamente
    palabras_ordenadas = sorted(
        frecuencias.items(),
        key=lambda elemento: (-elemento[1], elemento[0])
    )

    # 4. Obtener el top 5 de palabras más frecuentes
    top_5 = palabras_ordenadas[:5]

    # Obtener palabras que aparecen una sola vez, ordenadas
    palabras_unicas = sorted(
        palabra
        for palabra, frecuencia in frecuencias.items()
        if frecuencia == 1
    )

    # Mostrar resultados
    print("=== FRECUENCIA DE TODAS LAS PALABRAS ===")
    for palabra, frecuencia in palabras_ordenadas:
        print(f"{palabra}: {frecuencia}")

    print("\n=== TOP 5 PALABRAS MÁS FRECUENTES ===")
    for palabra, frecuencia in top_5:
        print(f"{palabra}: {frecuencia}")

    print("\n=== PALABRAS ÚNICAS ORDENADAS ===")
    print(palabras_unicas)

    return {
        "frecuencias": dict(frecuencias),
        "ordenadas": palabras_ordenadas,
        "top_5": top_5,
        "palabras_unicas": palabras_unicas
    }


# Ejemplo de uso
texto = """
Python es un lenguaje sencillo. Python es popular
y el lenguaje Python permite aprender programación.
Aprender Python es útil y aprender es divertido.
"""

resultado = analizar_texto(texto)
