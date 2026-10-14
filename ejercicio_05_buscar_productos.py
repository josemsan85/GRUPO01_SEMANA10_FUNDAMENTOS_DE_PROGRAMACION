# EJERCICIO 5 – Búsqueda y filtrado de productos

productos = [
    {'nombre': 'Leche Entera',   'categoria': 'Lácteos',   'precio': 4.8},
    {'nombre': 'Arroz Extra',    'categoria': 'Abarrotes', 'precio': 5.9},
    {'nombre': 'Leche Light',    'categoria': 'Lácteos',   'precio': 4.2},
    {'nombre': 'Aceite Vegetal', 'categoria': 'Abarrotes', 'precio': 9.8},
]


def buscar_productos(lista, termino):
    resultados = []
    for p in lista:
        # Todo a minúsculas para que no importen las mayúsculas
        if termino.lower() in p['nombre'].lower():
            resultados.append(p)
    # Ordenar los resultados por precio, de menor a mayor
    resultados.sort(key=lambda p: p['precio'])
    return resultados


# Probamos la función con dos búsquedas
print("Búsqueda: 'LECHE'")
for p in buscar_productos(productos, 'LECHE'):
    print(f"  {p['nombre']} - {p['categoria']} - S/ {p['precio']}")

print("Búsqueda: 'arroz'")
for p in buscar_productos(productos, 'arroz'):
    print(f"  {p['nombre']} - {p['categoria']} - S/ {p['precio']}")
