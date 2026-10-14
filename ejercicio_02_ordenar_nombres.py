# EJERCICIO 2 – Ordenamiento alfanumérico de nombres

nombres = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']

# 1) Imprimirla sin modificar
print('1) Original:', nombres)

# 2) sort() con key=str.lower: ordena ignorando mayúsculas y CAMBIA la lista original
nombres.sort(key=str.lower)
print('2) Ordenada con sort():', nombres)

# 3) sorted() crea una lista NUEVA, en orden descendente (reverse=True)
descendente = sorted(nombres, key=str.lower, reverse=True)
print('3) Nueva lista descendente con sorted():', descendente)

# 4) Los resultados de cada paso se muestran con los print de arriba
