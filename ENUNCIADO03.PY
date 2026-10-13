emails = ['ana@gmail.com', 'luis@outlook.com', 'mia@gmail.com', 'juan@yahoo.com']
contador_gmail = sum(1 for e in emails if '@gmail.com' in e)
print(f"1) Cantidad de emails de Gmail: {contador_gmail}")
print("2) Emails que terminan en '.com':")
for e in emails:
    if e.endswith('.com'):
        print(f"   - {e}")
buscado = 'luis@outlook.com'
print(f"3) ¿'{buscado}' está en la lista?: {buscado in emails}")