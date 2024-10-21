import sqlite3

# Ejercicio 3: Base de datos
# 1. Crear la base de datos
conexion = sqlite3.connect("escuela.db")

# 2. Crear la tabla
cursor = conexion.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    curso TEXT NOT NULL
)
""")

# 3. Insertar 3 alumnos
cursor.execute("INSERT INTO alumnos (nombre, curso) VALUES ('Juan', 'Matemáticas')")
cursor.execute("INSERT INTO alumnos (nombre, curso) VALUES ('Ana', 'Programación')")
cursor.execute("INSERT INTO alumnos (nombre, curso) VALUES ('Luis', 'Historia')")

# 4. Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
