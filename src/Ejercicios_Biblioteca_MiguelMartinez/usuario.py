from libro import Libro

class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre
        self.lista = []

    def __eq__(self, other):
        return self.nombre == other.nombre

    def devolver_libro(self, libro):
        if libro in self.lista:
            libro.prestado = False
            self.lista.remove(libro)
        else:
            print("el usuario no tiene ese libro")

    def prestar_libro(self, libro):
        if libro.prestado:
            print("El libro ya esta prestado")
        else:
            libro.prestado = True
            self.lista.append(libro)