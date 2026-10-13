import re
parrafo = "Python es un lenguaje de programación muy popular. Python es versátil, y la programación en Python es divertida."
def analizar_texto(texto):
    palabras = re.findall(r"[A-Za-z']+", texto)
    frecuencias = {}
    for p in palabras:
        p_lower = p.lower()
        frecuencias[p_lower] = frecuencias.get(p_lower, 0) + 1
    palabras_ordenadas = sorted(frecuencias.items(), key=lambda x: (-x[1], x[0]))
    print("--- TOP 5 PALABRAS MÁS FRECUENTES ---")
    for palabra, freq in palabras_ordenadas[:5]:
        print(f"'{palabra}': {freq} veces")
    print("\n--- PALABRAS ÚNICAS ORDENADAS ---")
    unicas = [item[0] for item in palabras_ordenadas]
    print(unicas)
analizar_texto(parrafo)