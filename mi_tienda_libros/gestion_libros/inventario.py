class Inventario:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_inventario(self):
        for libro in self.libros:
            print(libro)