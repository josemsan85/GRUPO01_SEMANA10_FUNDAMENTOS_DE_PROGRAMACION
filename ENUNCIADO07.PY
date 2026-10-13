import re
registros = [
    'Ana García - edad:25 - tel:987654321', 
    'Luis Pérez - edad:30 - tel:912345678'
]
lista_diccionarios = []
patron = re.compile(r'^(.*?) - edad:(\d+) - tel:(\d+)$')
for reg in registros:
    match = patron.match(reg)
    if match:
        lista_diccionarios.append({
            'nombre': match.group(1).strip(),
            'edad': int(match.group(2)),
            'telefono': match.group(3)
        })
print("--- EXTRACCIÓN CON REGEX ---")
for d in lista_diccionarios:
    print(d)