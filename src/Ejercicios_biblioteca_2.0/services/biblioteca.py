from models.libro import Libro
from models.usuario import Usuario

class Biblioteca:

    def __init__(self):
        self.lista_libros = []
        self.lista_usuarios = []

    def agregar_libro(self, libro):
        if libro in self.lista_libros:
            print("El liro ya existe en la biblioteca")
        else:
            self.lista_libros.append(libro)

    def agregar_usuario(self, usuario):
        if usuario in self.lista_usuarios:
            print("El usuario ya existe en la biblioteca")
        else:
            self.lista_usuarios.append(usuario)

    def devolver_libro(self, libro, usuario):
        if libro in self.lista_libros:
            usuario.devolver_libro(libro)

    
    def prestar_libro(self, libro, usuario):
        if libro not in self.lista_libros:
            print("El libro no esta en la biblioteca")
            return
        if libro.prestado:
            print("el libro ya esta prestado")
            return
        usuario.prestar_libro(libro)

    def mostrar_info_libros(self):
        for libro in self.lista_libros:
            print(libro)

    def mostrar_info_usuarios(self):
        for usuario in self.lista_usuarios:
            print(usuario)