#Tienes la lista: emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']
emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']

numeroGamil = 0

nuevoemail = []
#1) Imprime cuántos emails son de Gmail.
for i  in range(0, len(emails)):
    
    if "gmail" in emails[i]:
        numeroGamil +=1 
        
    if i == len(emails)-1:
        print (str(numeroGamil))


#2) Muestra solo los emails que terminan en '.com'.
for i  in range(0, len(emails)):
    
    if ".com" in emails[i]:
        nuevoemail.append(emails[i])
        
    if i == len(emails)-1:
        print (nuevoemail)

#3) Verifica si 'luis@outlook.com' está en la lista (usa 'in')
def seBusca(nombre):
 
 for i  in range(0, len(emails)):
    
    if nombre in emails[i]:
       return True
       
    
       
        
    
print(seBusca("luis@outlook.com"))