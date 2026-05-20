from abc import ABC, abstractmethod

class Recurso(ABC):

    def __init__(self, id_recurso,titulo, autor, anyo):
        self.comprobar_titulo(titulo)
        self.comprobar_autor(autor)

        self.id = id_recurso
        self.titulo = titulo
        self.autor = autor
        self.anyo = anyo
        self.prestado = False
    
    def comprobar_titulo(self, titulo):
        if len(titulo) < 2 or len(titulo) > 50:
            raise ValueError("Título no válido (debe tener entre 2 y 50 caracteres)")

    def comprobar_autor(self, autor):
        if len(autor) < 2 or len(autor) > 50:
            raise ValueError("Autor no válido (debe tener entre 2 y 50 caracteres)")
        
    @abstractmethod
    def info_detallada(self):
        """"""

    def __eq__(self, other):
        return self.id == other.id