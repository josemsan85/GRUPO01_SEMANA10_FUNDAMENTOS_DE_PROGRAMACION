# EJERCICIO 6 – Combinación de arreglos y ordenamiento

# Dos arreglos paralelos
productos = ['Pollo a la brasa', 'Ceviche', 'Lomo saltado', 'Chicha morada', 'Ají de gallina']
ventas = [85, 120, 95, 60, 110]

# Combinarlos en una lista de diccionarios
lista = []
for producto, venta in zip(productos, ventas):
    lista.append({'producto': producto, 'ventas': venta})

# 1) Ordenar por ventas de mayor a menor
lista.sort(key=lambda d: d['ventas'], reverse=True)

# 2) Imprimir el ranking con su posición (enumerate empieza en 0, por eso i + 1)
print('Ranking de ventas:')
for i, d in enumerate(lista):
    print(f"{i + 1}° {d['producto']}: {d['ventas']} ventas")

# 3) Promedio de ventas y productos que están sobre la media
promedio = sum(ventas) / len(ventas)
print(f'Promedio de ventas: {promedio}')

print('Productos sobre la media:')
for d in lista:
    if d['ventas'] > promedio:
        print(' -', d['producto'])
