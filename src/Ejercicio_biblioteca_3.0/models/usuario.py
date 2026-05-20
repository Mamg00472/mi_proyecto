from abc import ABC, abstractmethod

class Usuario(ABC):

    def __init__(self, id_usuario,nombre, correo, sanciones=None):
        self.comprobar_nombre(nombre)

        self.id = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.sanciones = sanciones if sanciones is not None else []
        self.prestamos_activos = []

    @abstractmethod
    def limite_prestamos(self):
        """Funcion abstracta para definir el limite de prestamos segun el tipo de usuario"""
        

    def puede_tomar_prestado(self):
         return len(self.prestamos_activos) < self.limite_prestamos() and self.sanciones < 0

    def devolver_libro(self, libro):
        if libro in self.prestamos_activos:
            libro.prestado = False
            self.prestamos_activos.remove(libro)
        else:
            raise ValueError("el usuario no tiene ese libro")

    def prestar_libro(self, libro):
        if not self.puede_tomar_prestado():
            raise ValueError("El usuario no puede realizar más préstamos (límite alcanzado o tiene sanciones)")
        libro.prestado = True
        self.prestamos_activos.append(libro)

    def comprobar_nombre(self, nombre):
        if len(nombre) < 2 or len(nombre) > 50:
             raise ValueError("Nombre no válido (debe tener entre 2 y 50 caracteres)")
        
    def __eq__(self, other):
        return self.id == other.id
    
    def __str__(self):
         libros = [libro.titulo for libro in self.prestamos_activos]
         return f"[{self.__class__.__name__}] ID: {self.id} | {self.nombre} tiene: {libros}"