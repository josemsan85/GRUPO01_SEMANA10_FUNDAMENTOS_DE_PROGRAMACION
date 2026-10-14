# Enunciado 2 - Ordenamiento alfanumérico de nombres

lista = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']

# 1) Imprimirla sin modificar
print('Original:', lista)

# 2) Ordenar ignorando mayúsculas con sort()
lista.sort(key=str.lower)
print('Ordenada (sort, ignorando mayúsculas):', lista)

# 3) Nueva lista en orden descendente con sorted()
descendente = sorted(lista, key=str.lower, reverse=True)
print('Nueva lista descendente (sorted):', descendente)

# 4) La lista original (ya ordenada con sort) no cambió con sorted()
print('Lista tras sorted (intacta):', lista)
