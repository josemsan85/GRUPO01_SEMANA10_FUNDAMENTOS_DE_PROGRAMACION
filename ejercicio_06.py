# Enunciado 6 - Combinación de arreglos y ordenamiento

productos6 = ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Audífonos']
ventas = [120, 450, 300, 80, 210]

# Combinar los dos arreglos paralelos en una lista de diccionarios
lista_ventas = []
for producto, venta in zip(productos6, ventas):
    lista_ventas.append({'producto': producto, 'ventas': venta})

# 1) Ordenar por ventas de mayor a menor
lista_ventas.sort(key=lambda d: d['ventas'], reverse=True)

# 2) Ranking con posición
posicion = 1
for d in lista_ventas:
    print(f"{posicion}° {d['producto']}: {d['ventas']} ventas")
    posicion = posicion + 1

# 3) Promedio de ventas y cuáles están sobre la media
suma = 0
for d in lista_ventas:
    suma = suma + d['ventas']
promedio = suma / len(lista_ventas)
print('Promedio de ventas:', promedio)

print('Sobre la media:')
for d in lista_ventas:
    if d['ventas'] > promedio:
        print(d['producto'], '->', d['ventas'])
