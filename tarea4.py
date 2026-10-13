#Crea una lista de diccionarios para 4 estudiantes con los campos: 'nombre', 'carrera' y 'promedio'.

alumnos = [
    { "nombre":"Ana","carrera":"Panaderia nuclear","promedio": 14}, 
    { "nombre":"Raul","carrera":"Soldadura de madera","promedio": 18}, 
    { "nombre":"Anastasio","carrera":"ginecologia de robot","promedio": 15}, 
    { "nombre":"Ortencio","carrera":"ingenieria de transformers","promedio": 16} 
    
   ]

#agregas las notas a otra lista
notaAlumnos = []
notaMayor =0; 
#Imprime el nombre y promedio de cada estudiante.

for i in range (0, len(alumnos)):
    #se agregan en orden a otra lista solo para notas
    notaAlumnos.append (alumnos[i]["promedio"])
    print(alumnos[i]["nombre"],alumnos[i]["promedio"])

#Luego muestra el nombre del estudiante con el promedio más alto.

notaMayor = max(notaAlumnos)

for i in range (0, len(alumnos)):
    if alumnos[i]["promedio"] == notaMayor:
        print(alumnos[i]["nombre"])
