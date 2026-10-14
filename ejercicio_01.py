# Enunciado 1 - Registro de productos con arreglos paralelos

nombres = ['Laptop', 'Mouse', 'Teclado', 'Monitor']   # Lista 1
precios = [2500.0, 50.0, 120.0, 800.0]                # Lista 2
cantidades = [15, 40, 25, 10]                         # Lista 3

# Reporte: una línea por producto (zip recorre las 3 listas en paralelo)
for nombre, precio, cantidad in zip(nombres, precios, cantidades):
    print(f'{nombre}: precio S/ {precio}, stock {cantidad}')

# Precio total del inventario (precio x cantidad de todos)
total = 0
for precio, cantidad in zip(precios, cantidades):
    total = total + precio * cantidad
print(f'Precio total del inventario: S/ {total}')
