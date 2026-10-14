# EJERCICIO 3 – Búsqueda simple en una lista de emails

emails = ['ana@gmail.com', 'luis@outlook.com', 'mia@gmail.com', 'juan@yahoo.com']

# 1) Contar cuántos emails son de Gmail
contador = 0
for email in emails:
    if 'gmail' in email:                  # 'in' revisa si el texto está dentro del email
        contador = contador + 1
print('1) Emails de Gmail:', contador)

# 2) Mostrar solo los que terminan en '.com'
print('2) Emails que terminan en .com:')
for email in emails:
    if email.endswith('.com'):            # endswith() revisa cómo termina el texto
        print('   ', email)

# 3) Verificar con 'in' si luis@outlook.com está en la lista
if 'luis@outlook.com' in emails:
    print('3) luis@outlook.com SÍ está en la lista')
else:
    print('3) luis@outlook.com NO está en la lista')
