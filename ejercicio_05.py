# Enunciado 5 - Búsqueda y filtrado de productos

productos = [
    {'nombre': 'Laptop Gamer',   'categoria': 'Computo',    'precio': 3500.0},
    {'nombre': 'Mouse inalámbrico', 'categoria': 'Accesorios', 'precio': 60.0},
    {'nombre': 'Laptop Oficina', 'categoria': 'Computo',    'precio': 2200.0},
    {'nombre': 'Teclado',        'categoria': 'Accesorios', 'precio': 120.0},
    {'nombre': 'Funda para laptop', 'categoria': 'Accesorios', 'precio': 45.0},
]

def buscar_productos(lista, termino):
    resultados = []
    for p in lista:
        # lower() en ambos para no importar mayúsculas; 'in' para buscar
        if termino.lower() in p['nombre'].lower():
            resultados.append(p)
    # Ordenar por precio de menor a mayor
    resultados.sort(key=lambda p: p['precio'])
    return resultados

encontrados = buscar_productos(productos, 'LAPTOP')
for p in encontrados:
    print(p['nombre'], '-', p['categoria'], '- S/', p['precio'])
