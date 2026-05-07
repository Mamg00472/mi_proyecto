class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def __eq__(self, other):
        return self.titulo == other.titulo

    def __str__(self):
        return f"El libro: {self.titulo} escrito por: {self.autor} esta prestado: {self.prestado}"