# Función para mostrar el menú de operaciones
def mostrar_menu():
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

# Función principal de la calculadora
def calculadora():
    while True:
        mostrar_menu()  # Mostrar el menú
        opcion = input("Introduce el número de la operación que quieres realizar: ")

        if opcion == '5':  # Salir del programa
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        # Pedir los dos números para la operación
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        # Realizar la operación según la elección del usuario
        if opcion == '1':
            print(f"El resultado de sumar {num1} y {num2} es: {num1 + num2}")
        elif opcion == '2':
            print(f"El resultado de restar {num1} y {num2} es: {num1 - num2}")
        elif opcion == '3':
            print(f"El resultado de multiplicar {num1} y {num2} es: {num1 * num2}")
        elif opcion == '4':
            if num2 != 0:
                print(f"El resultado de dividir {num1} entre {num2} es: {num1 / num2}")
            else:
                print("Error: No se puede dividir entre cero.")
        else:
            print("Opción inválida, por favor selecciona una opción válida.")

# Ejecutar la calculadora
calculadora()
