nombres = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']
print("1) Lista original:", nombres)
ascendente = nombres.copy()
n = len(ascendente)
for i in range(n):
    for j in range(0, n - i - 1):
        if ascendente[j].lower() > ascendente[j + 1].lower():
            ascendente[j], ascendente[j + 1] = ascendente[j + 1], ascendente[j]
print("2) Orden alfabético ascendente:", ascendente)
descendente = nombres.copy()
n = len(descendente)
for i in range(n):
    for j in range(0, n - i - 1):
        if descendente[j].lower() < descendente[j + 1].lower():
            descendente[j], descendente[j + 1] = descendente[j + 1], descendente[j]
print("3) Orden descendente:", descendente)