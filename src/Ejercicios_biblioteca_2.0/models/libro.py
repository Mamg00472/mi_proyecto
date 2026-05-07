class Libro:

    def __init__(self, titulo, autor):
        self.comprobar_titulo(titulo)
        self.comprobar_autor(autor)

        self.titulo = titulo
        self.autor = autor
        self.prestado = False

        print("Libro creado correctamente")

    def __eq__(self, other):
        return self.titulo == other.titulo

    def __str__(self):
        return f"El libro: {self.titulo} escrito por: {self.autor} esta prestado: {self.prestado}"
    
    def comprobar_titulo(self, titulo):
        if len(titulo) < 3 or len(titulo) > 50:
            raise ValueError("Título no válido (debe tener entre 3 y 50 caracteres)")

    def comprobar_autor(self, autor):
        if len(autor) < 2 or len(autor) > 50:
            raise ValueError("Autor no válido (debe tener entre 2 y 50 caracteres)")