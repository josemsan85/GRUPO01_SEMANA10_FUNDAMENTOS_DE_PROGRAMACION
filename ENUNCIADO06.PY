productos = ["Teclado", "Mouse", "Monitor", "Impresora"]
ventas = [120, 350, 85, 200]
reporte_ventas = [{'producto': productos[i], 'ventas': ventas[i]} for i in range(len(productos))]
n = len(reporte_ventas)
for i in range(n):
    for j in range(0, n - i - 1):
        if reporte_ventas[j]['ventas'] < reporte_ventas[j + 1]['ventas']:
            reporte_ventas[j], reporte_ventas[j + 1] = reporte_ventas[j + 1], reporte_ventas[j]
print("--- 1 y 2) RANKING DE VENTAS ---")
for i, item in enumerate(reporte_ventas, start=1):
    print(f"   {i}° - {item['producto']}: {item['ventas']} unidades")
suma_ventas = sum(item['ventas'] for item in reporte_ventas)
promedio_ventas = suma_ventas / len(reporte_ventas)
print(f"\n3) Promedio de ventas: {promedio_ventas:.2f}")
print("Productos sobre la media:")
for item in reporte_ventas:
    if item['ventas'] > promedio_ventas:
        print(f"   - {item['producto']} ({item['ventas']} ventas)")