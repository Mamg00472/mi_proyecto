from abc import ABC, abstractmethod

class Recurso(ABC):

    def __init__(self, id_recurso,titulo, autor, anyo):
        self.id = id_recurso
        self.titulo = titulo
        self.autor = autor
        self.anyo = anyo
        self.prestado = False
        
    @abstractmethod
    def info_detallada(self):
        """Metodo abstracto para mostrar la informacion detallada de cada recurso"""

    def __eq__(self, other):
        if not isinstance(other, Recurso):
            return False
        return self.id == other.id