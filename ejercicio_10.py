# Enunciado 10 - Análisis de texto y estadísticas de palabras
import re

parrafo = ("Python es fácil de aprender. Python es potente y Python es divertido. "
           "I don't know why it's so popular, but it's popular and it's fun. " #por que el ejercicio dice apostrofes por eso pongo esto en ingles
           "Aprender es divertido y es útil.")

# 1) Extraer palabras (solo letras y apóstrofes)
palabras = re.findall(r"[A-Za-zÁÉÍÓÚáéíóúÑñ']+", parrafo)

# 2) Diccionario de frecuencias (sin importar mayúsculas)
frecuencia = {}
for palabra in palabras:
    p = palabra.lower()
    frecuencia[p] = frecuencia.get(p, 0) + 1

# 3) Ordenar por frecuencia (desc) y luego alfabéticamente
ordenadas = sorted(frecuencia.items(), key=lambda par: (-par[1], par[0]))

# 4) Top 5 y palabras únicas ordenadas
print('Top 5 palabras más frecuentes:')
for palabra, cantidad in ordenadas[:5]:
    print(f'  {palabra}: {cantidad}')

unicas = sorted(frecuencia.keys())
print('Palabras únicas ordenadas:')
print(unicas)
