# Enunciado 3 - Búsqueda simple en una lista de emails

emails = ['percy_angel_pardo_zapata@gmail.com', 'luis@outlook.com', 'mia@gmail.com', 'juan@yahoo.com']

# 1) Cuántos emails son de Gmail
contador_gmail = 0
for email in emails:
    if 'gmail' in email:
        contador_gmail = contador_gmail + 1
print('Emails de Gmail:', contador_gmail)

# 2) Solo los que terminan en '.com'
print('Emails que terminan en .com:')
for email in emails:
    if email.endswith('.com'):
        print(email)

# 3) Verificar si 'luis@outlook.com' está en la lista (usa 'in')
if 'luis@outlook.com' in emails:
    print('luis@outlook.com SÍ está en la lista')
else:
    print('luis@outlook.com NO está en la lista')
