# Ejercicio 1: Manipulación de archivos
# 1. Crear el archivo y escribir en él
with open("mi archivo.txt", "w") as archivo:
    archivo.write("Hola, estoy aprendiendo Python.")

# 2. Reabrir el archivo en modo lectura
with open("mi archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
