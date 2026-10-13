productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
precios = [1200.50, 45.00, 85.50, 450.00]
cantidades = [10, 50, 30, 15]
print("--- REPORTE DE PRODUCTOS ---")
total_inventario = 0
for i in range(len(productos)):
    subtotal = precios[i] * cantidades[i]
    total_inventario += subtotal
    print(f"Producto: {productos[i]} | Precio: ${precios[i]} | Stock: {cantidades[i]}")

print(f"\nPrecio total del inventario: ${total_inventario:.2f}")