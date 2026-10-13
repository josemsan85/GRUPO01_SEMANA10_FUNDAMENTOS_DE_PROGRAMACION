#Tienes dos arreglos paralelos: productos (strings) y ventas (enteros).
productos = ["Aceites", "Tasas", "Galletas"]
ventas    = [100, 300 , 400]

#Combínalos en una lista de diccionarios, luego:
dici = []
sum=0  
for i in range (0, len (productos)):
     dici.append ({ "Producto": productos[i], "Ventas":ventas[i]})

#1) Ordena por ventas de mayor a menor.

dici.sort (key= lambda x:x["Ventas"], reverse=True)
print (dici)
#2) Imprime el ranking con posición (1°, 2°, etc.).

for i in range (0, len(dici)):
     
 print("puesto " + str(i+1 ) + dici[i]["Producto"] + "con ventas " + str(dici[i]["Ventas"])) 
#3) Calcula el promedio de ventas e indica cuáles están sobre la media.

for i in range (0, len(dici)):
    sum += dici[i]["Ventas"]
    if i == len (dici)-1:
     prome = sum / len(dici)
     print(str(prome))
  
for i in range (0, len(dici)):
   if dici[i]["Ventas"] > prome:
      print ("por encima del promedio " + dici[i]["Producto"])