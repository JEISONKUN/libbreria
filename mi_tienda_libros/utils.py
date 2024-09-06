def pedir_opcion():
    while True:
        opcion = input("Ingrese una opción (1-5): ")
        if opcion in ["1", "2", "3", "4", "5"]:
            return int(opcion)
        print("Opción inválida. Intente nuevamente.")