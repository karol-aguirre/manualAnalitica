# Escribir en archivo
with open("mi_archivo.txt", "w") as f:
    f.write("Hola Mundo\nSegunda línea")

# Leer archivo
with open("mi_archivo.txt", "r") as f:
    print(f.read())  # Lee todo el contenido

# Añadir texto
with open("mi_archivo.txt", "a") as f:
    f.write("\nTercera línea añadida")

import csv

# Escribir CSV
with open("datos.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Nombre", "Edad"])
    writer.writerow(["Juan", 25])
    writer.writerow(["Ana", 30])

# Leer CSV
with open("datos.csv", "r") as f:
    lector = csv.reader(f)
    for fila in lector:
        print(fila)  # ['Nombre', 'Edad'], ['Juan', '25'], etc.

import json

# Escribir JSON
datos = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
with open("datos.json", "w") as f:
    json.dump(datos, f)

# Leer JSON
with open("datos.json", "r") as f:
    datos_leidos = json.load(f)
    print(datos_leidos)  # {'nombre': 'Juan', 'edad': 25, ...}