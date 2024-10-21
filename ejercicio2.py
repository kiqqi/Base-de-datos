# Ejercicio 2: Notas de materias
# 1. Crear el archivo y escribir en él
with open("notas.txt", "w") as archivo:
    archivo.write("Matemáticas\n")
    archivo.write("Programación\n")
    archivo.write("Historia\n")

# 2. Reabrir el archivo y mostrar las líneas
with open("notas.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())  # .strip() elimina los saltos de línea
