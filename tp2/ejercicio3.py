# Diccionario para registrar personas
personas = [
    {"nombre": "Carlos", "edad": 25, "correo": "carlos@example.com"},
    {"nombre": "Sofía", "edad": 17, "correo": "sofia@example.com"},
    {"nombre": "Pedro", "edad": 30, "correo": "pedro@example.com"}
]

# Función para filtrar personas mayores de 18 años
def filtrar_mayores(personas):
    return [persona for persona in personas if persona["edad"] > 18]

# Resultado
mayores_de_edad = filtrar_mayores(personas)
print("Personas mayores de 18 años:")
for persona in mayores_de_edad:
    print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Correo: {persona['correo']}")
