# EJERCICIO 10 – Análisis de texto y estadísticas de palabras

import re   # Módulo de regex

texto = ("Python es fácil. Python es divertido y Python es poderoso. "
         "Aprender Python es genial, y practicar es mejor. "
         "Me gusta programar y me gusta aprender.")

# 1) Extraer todas las palabras con regex (letras y apóstrofes).
#    Pasamos el texto a minúsculas para que 'Python' y 'python' sean la misma palabra.
#    [\w']+ = una o más letras o apóstrofes seguidos
palabras = re.findall(r"[\w']+", texto.lower())

# 2) Diccionario con la frecuencia de cada palabra
frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

# 3) Pasamos el diccionario a dos listas paralelas (la posición i es la misma palabra)
lista_palabras = []
lista_cantidades = []
for palabra, cantidad in frecuencia.items():
    lista_palabras.append(palabra)
    lista_cantidades.append(cantidad)

# Ordenamiento burbuja (semana 6): primero mayor frecuencia;
# si empatan, orden alfabético. Al intercambiar, movemos las DOS listas.
n = len(lista_palabras)
for i in range(n):
    for j in range(0, n - i - 1):
        intercambiar = False
        if lista_cantidades[j] < lista_cantidades[j + 1]:
            intercambiar = True          # el que más se repite va primero
        elif lista_cantidades[j] == lista_cantidades[j + 1] and lista_palabras[j] > lista_palabras[j + 1]:
            intercambiar = True          # si empatan, la palabra alfabéticamente menor va primero
        if intercambiar:
            lista_palabras[j], lista_palabras[j + 1] = lista_palabras[j + 1], lista_palabras[j]
            lista_cantidades[j], lista_cantidades[j + 1] = lista_cantidades[j + 1], lista_cantidades[j]

# 4) Top 5 de palabras más frecuentes
limite = 5
if n < 5:
    limite = n      # por si hay menos de 5 palabras distintas

print('Top 5 palabras más frecuentes:')
for i in range(limite):
    print(f'  {i + 1}. {lista_palabras[i]}: {lista_cantidades[i]}')

# Palabras únicas ordenadas alfabéticamente (copiamos la lista para no tocar la otra)
unicas = lista_palabras.copy()
unicas.sort()
print('Palabras únicas ordenadas:')
print(unicas)
