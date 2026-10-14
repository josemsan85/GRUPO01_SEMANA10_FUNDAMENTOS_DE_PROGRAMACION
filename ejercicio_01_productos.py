# EJERCICIO 1 – Registro de productos con arreglos paralelos
# Idea: 3 listas del mismo tamaño. La posición i es el MISMO producto en las tres.

nombres = ['Cuaderno', 'Lapicero', 'Mochila', 'Regla']
precios = [6.5, 1.5, 45.0, 3.0]
cantidades = [30, 100, 12, 50]

total = 0   # aquí vamos sumando el valor de todo el inventario

# zip() recorre las 3 listas al mismo tiempo
for nombre, precio, cantidad in zip(nombres, precios, cantidades):
    print(f'{nombre}: precio S/ {precio}, cantidad {cantidad}')
    total = total + precio * cantidad   # precio x cantidad de este producto

print(f'Precio total del inventario: S/ {total}')
