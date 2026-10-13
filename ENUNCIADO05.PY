catalogo = [
    {'nombre': 'Laptop Gamer', 'categoria': 'Tecnología', 'precio': 2500.0},
    {'nombre': 'Mouse Inalámbrico', 'categoria': 'Accesorios', 'precio': 35.0},
    {'nombre': 'Teclado Mecánico', 'categoria': 'Accesorios', 'precio': 120.0},
    {'nombre': 'Laptop Oficina', 'categoria': 'Tecnología', 'precio': 1500.0}
]

def buscar_productos(lista, termino):
    filtrados = [p for p in lista if termino.lower() in p['nombre'].lower()]
    return sorted(filtrados, key=lambda x: x['precio'])

resultado = buscar_productos(catalogo, "laptop")
print("--- RESULTADOS DE BÚSQUEDA Y FILTRADO ---")
for prod in resultado:
    print(f"- {prod['nombre']} (${prod['precio']})")