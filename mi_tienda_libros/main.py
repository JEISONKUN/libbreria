from gestion_libros.inventario import Inventario
from gestion_libros.ventas import Ventas
from utils import pedir_opcion

def main():
    inventario = Inventario()
    ventas = Ventas()

    while True:
        print("1. Agregar libro al inventario")
        print("2. Mostrar inventario")
        print("3. Vender libro")
        print("4. Mostrar total de ventas")
        print("5. Salir")

        opcion = pedir_opcion()

        if opcion == 1:
            libro = input("Ingrese el título del libro: ")
            inventario.agregar_libro(libro)
            print("Libro agregado con éxito.")
        elif opcion == 2:
            inventario.mostrar_inventario()
        elif opcion == 3:
            libro = input("Ingrese el título del libro: ")
            precio = float(input("Ingrese el precio del libro: "))
            ventas.vender_libro(precio)
            print("Libro vendido con éxito.")
        elif opcion == 4:
            ventas.mostrar_total_ventas()
        elif opcion == 5:
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()