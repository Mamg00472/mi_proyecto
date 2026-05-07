from models.libro import Libro
from models.usuario import Usuario
from models.historial import Historial
from services.persistencia import guardar_json, cargar_json

class Biblioteca:

    def __init__(self):
        datos_libros = cargar_json("data/libros.json")
        datos_usuarios = cargar_json("data/usuarios.json")

        self.lista_libros = []
        self.lista_usuarios = []
        
        for l in datos_libros:
            libro = Libro(l["titulo"], l["autor"])
            libro.prestado = l["prestado"]
            self.lista_libros.append(libro)

        for u in datos_usuarios:
            usuario = Usuario(u["nombre"])

            for titulo_libro in u.get("libros", []):
                libro = self.buscar_libro(titulo_libro)
                usuario.lista.append(libro)

            self.lista_usuarios.append(usuario)

        self.historial = Historial()

    def agregar_libro(self, libro):
        if libro in self.lista_libros:
            raise ValueError("El libro ya existe en la biblioteca")
        
        self.lista_libros.append(libro)

    def agregar_usuario(self, usuario):
        if usuario in self.lista_usuarios:
            raise ValueError("El usuario ya existe en la biblioteca")
        
        self.lista_usuarios.append(usuario)

    def devolver_libro(self, libro, usuario):
        if libro not in self.lista_libros:
            raise ValueError("El libro no existe en la biblioteca")
            
        if usuario not in self.lista_usuarios:
            raise ValueError("El usuario no existe en la biblioteca")
            
        usuario.devolver_libro(libro)
        self.historial.registrar(usuario.nombre, libro.titulo, "DEVUELTO")
    
    def prestar_libro(self, libro, usuario):
        if libro not in self.lista_libros:
            raise ValueError("El libro no esta en la biblioteca")
        
        if usuario not in self.lista_usuarios:
            raise ValueError("El usuario no existe en la biblioteca")

        if libro.prestado:
            raise ValueError("El libro ya esta prestado")
        
        usuario.prestar_libro(libro)
        self.historial.registrar(usuario.nombre, libro.titulo, "PRESTADO")
        

    def buscar_libro(self, titulo):
        titulo = titulo.lower().strip()
        for l in self.lista_libros:
            if l.titulo.lower() == titulo:
                return l
        raise ValueError("Libro no encontrado en la biblioteca")
        
    def buscar_usuario(self, nombre):
        nombre = nombre.lower().strip()
        for u in self.lista_usuarios:
            if u.nombre.lower() == nombre:
                return u
        raise ValueError("Usuario no encontrado en la biblioteca")

    def mostrar_info_libros(self):
        for libro in self.lista_libros:
            print(libro)

    def mostrar_info_usuarios(self):
        for usuario in self.lista_usuarios:
            print(usuario)

    def guardar_datos(self):
        self.historial.guardar()

        datos_libros = [
            {
                "titulo" : libro.titulo,
                "autor" : libro.autor,
                "prestado" : libro.prestado
            }
            for libro in self.lista_libros
        ]

        datos_usuarios = [
            {
                "nombre" : usuario.nombre,
                "libros" : [
                    libro.titulo
                    for libro in usuario.lista
                ]
            }
            for usuario in self.lista_usuarios
        ]

        guardar_json("data/libros.json", datos_libros)
        guardar_json("data/usuarios.json", datos_usuarios)
