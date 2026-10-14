# Enunciado 7 - Extracción con expresiones regulares
import re

registros = [
    'Ana García - edad:25 - tel:987654321',
    'Luis Pérez - edad:30 - tel:912345678',
]

personas = []
for texto in registros:
    # Nombre: todo lo que está antes del primer ' - '
    nombre = re.search(r'^[^-]+', texto).group().strip()
    # Edad: dígitos después de 'edad:'
    edad = re.search(r'edad:(\d+)', texto).group(1)
    # Teléfono: dígitos después de 'tel:'
    telefono = re.search(r'tel:(\d+)', texto).group(1)

    personas.append({'nombre': nombre, 'edad': int(edad), 'telefono': telefono})

for p in personas:
    print(p)
