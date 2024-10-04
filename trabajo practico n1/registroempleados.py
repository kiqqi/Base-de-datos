# Lista que almacenará los empleados
empleados = []

# Función para agregar un nuevo empleado
def agregar_empleado(nombre, edad, puesto):
    empleado = {"nombre": nombre, "edad": edad, "puesto": puesto}
    empleados.append(empleado)
    print(f"Empleado {nombre} agregado exitosamente.\n")

# Función para listar todos los empleados
def listar_empleados():
    if empleados:
        print("Lista de empleados:")
        for i, empleado in enumerate(empleados, 1):
            print(f"{i}. Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Puesto: {empleado['puesto']}")
    else:
        print("No hay empleados registrados.\n")

# Función para actualizar información de un empleado
def actualizar_empleado(nombre):
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            print(f"Empleado encontrado: {empleado['nombre']}")
            nueva_edad = input("Ingrese la nueva edad (dejar vacío para no cambiar): ")
            nuevo_puesto = input("Ingrese el nuevo puesto (dejar vacío para no cambiar): ")
            
            if nueva_edad:
                empleado["edad"] = int(nueva_edad)
            if nuevo_puesto:
                empleado["puesto"] = nuevo_puesto
                
            print(f"Empleado {nombre} actualizado.\n")
            return
    print(f"No se encontró un empleado con el nombre {nombre}.\n")

# Función para eliminar un empleado
def eliminar_empleado(nombre):
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            empleados.remove(empleado)
            print(f"Empleado {nombre} eliminado.\n")
            return
    print(f"No se encontró un empleado con el nombre {nombre}.\n")

# Función para calcular la edad promedio de los empleados
def edad_promedio():
    if empleados:
        promedio = sum(empleado["edad"] for empleado in empleados) / len(empleados)
        print(f"La edad promedio de los empleados es: {promedio:.2f} años.\n")
    else:
        print("No hay empleados para calcular la edad promedio.\n")

# Menú de opciones para el usuario
def menu():
    while True:
        print("---- Menú de Administración de Empleados ----")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Actualizar empleado")
        print("4. Eliminar empleado")
        print("5. Calcular edad promedio")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del empleado: ")
            edad = int(input("Ingrese la edad del empleado: "))
            puesto = input("Ingrese el puesto del empleado: ")
            agregar_empleado(nombre, edad, puesto)
        
        elif opcion == "2":
            listar_empleados()
        
        elif opcion == "3":
            nombre = input("Ingrese el nombre del empleado a actualizar: ")
            actualizar_empleado(nombre)
        
        elif opcion == "4":
            nombre = input("Ingrese el nombre del empleado a eliminar: ")
            eliminar_empleado(nombre)
        
        elif opcion == "5":
            edad_promedio()
        
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n")

# Ejecución del programa
menu()
