# Lista de estudiantes con su edad
estudiantes = [
    {"nombre": "Juan", "edad": 16},
    {"nombre": "Ana", "edad": 18},
    {"nombre": "Luis", "edad": 15},
    {"nombre": "Marta", "edad": 19}
]

# Función para devolver el estudiante con mayor y menor edad
def estudiante_extremos(estudiantes):
    mayor = max(estudiantes, key=lambda estudiante: estudiante["edad"])
    menor = min(estudiantes, key=lambda estudiante: estudiante["edad"])
    return mayor, menor

# Resultado
mayor, menor = estudiante_extremos(estudiantes)
print(f"Estudiante con mayor edad: {mayor['nombre']}, {mayor['edad']} años")
print(f"Estudiante con menor edad: {menor['nombre']}, {menor['edad']} años")
