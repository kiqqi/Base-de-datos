# Función que desarrolla la historia interactiva
def micro_novela():
    print("Bienvenido a la micro novela interactiva.")
    print("Te encuentras en medio de un bosque oscuro.")

    decision1 = input("¿Quieres ir a la izquierda o a la derecha? (izquierda/derecha): ").lower()

    if decision1 == "izquierda":
        print("Caminas hacia la izquierda y te encuentras con una cueva misteriosa.")
        decision2 = input("¿Entras en la cueva o sigues caminando? (cueva/caminar): ").lower()

        if decision2 == "cueva":
            print("Entras en la cueva y descubres un tesoro escondido. ¡Felicidades!")
        else:
            print("Sigues caminando y encuentras un lago brillante. Decides descansar allí.")
    
    elif decision1 == "derecha":
        print("Caminas hacia la derecha y te encuentras con un río caudaloso.")
        decision2 = input("¿Cruzas el río o sigues el camino? (cruzar/seguir): ").lower()

        if decision2 == "cruzar":
            print("Cruzas el río con dificultad, pero al otro lado encuentras una aldea acogedora. ¡Has llegado a un lugar seguro!")
        else:
            print("Sigues el camino y encuentras una cabaña abandonada donde puedes descansar.")
    
    else:
        print("Decides no moverte y quedarte donde estás. El tiempo pasa y el bosque te envuelve.")

# Ejecutar la micro novela interactiva
micro_novela()
