#Tienes una lista de diccionarios de productos con 'nombre', 'categoria' y 'precio'.
productos = [
              { "nombre":"Ariel", "Categoria":"Domestico", "Precio":10}, 
              { "nombre":"Shampoo", "Categoria":"Personal", "Precio":8}, 
              { "nombre":"Aceite", "Categoria":"Cocina", "Precio":15}
]
precios = []
#Implementa una función buscar_productos(lista, termino) que devuelva todos los productos
def buscarProducto (lista, termino):
    resultados = [ 
        producto
        for producto in lista 
                if termino.lower() in producto["nombre"].lower() ]
    return sorted(resultados, key=lambda producto:producto["Precio"])
    

resultado = buscarProducto(productos, "ariel")

for producto in resultado:
    print(producto)

#cuyo nombre contenga el término de búsqueda (sin importar mayúsculas).
#Además, ordena los resultados por precio de menor a mayor.