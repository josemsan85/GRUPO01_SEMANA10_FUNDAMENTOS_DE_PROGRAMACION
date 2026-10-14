# EJERCICIO 7 – Extracción con expresiones regulares

import re   # Módulo de regex

registros = ['Ana García - edad:25 - tel:987654321',
             'Luis Pérez - edad:30 - tel:912345678']

personas = []

for registro in registros:
    # \w+ \w+  = una palabra, un espacio y otra palabra (nombre y apellido)
    # re.search() busca el primer match y .group() nos da el texto encontrado
    nombre = re.search(r'\w+ \w+', registro).group()

    # \d+ = uno o más dígitos
    # re.findall() devuelve una LISTA con todos los números: ['25', '987654321']
    numeros = re.findall(r'\d+', registro)
    edad = numeros[0]       # el primer número es la edad
    telefono = numeros[1]   # el segundo número es el teléfono

    personas.append({'nombre': nombre, 'edad': edad, 'telefono': telefono})

for persona in personas:
    print(persona)
