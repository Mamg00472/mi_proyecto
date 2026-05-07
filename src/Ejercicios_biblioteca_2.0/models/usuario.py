from models.libro import Libro

class Usuario:

    def __init__(self, nombre):
        self.comprobar_usuario(nombre)

        self.nombre = nombre
        self.lista = []

    def __eq__(self, other):
        return self.nombre == other.nombre
    
    def __str__(self):             
         return f"El usuario {self.nombre} tiene: {self.lista}"

    def devolver_libro(self, libro):
        if libro in self.lista:
            libro.prestado = False
            self.lista.remove(libro)
        else:
            print("el usuario no tiene ese libro")

    def prestar_libro(self, libro):
            libro.prestado = True
            self.lista.append(libro)

    def comprobar_nombre(self, nombre):
        if len(nombre) < 2 or len(nombre) > 50:
             raise ValueError("Nombre no válido (debe tener entre 2 y 50 caracteres)")