nombres =  ["ayudin", "kolinos", "aceite", "cepillo"]
precio = [5, 3, 9, 4]
stock = [100, 40, 80, 200]

indice = 0 

#calcula el precio total del inventario
#cada prodcuto con su precio 

def muestraValor ():
    for i in range (0, len(nombres)):

        print ("el producto es " + str(nombres[i]) + " su precio es " + str (precio[i]) + " precio total " +
        "del inventario  es  " + str (precio[i]*stock[i]))
        


muestraValor()