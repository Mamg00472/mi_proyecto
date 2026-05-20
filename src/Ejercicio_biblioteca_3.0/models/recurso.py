from abc import ABC, abstractmethod

class Recurso(ABC):

    def __init__(self, id_recurso: str, titulo: str, autor: str, anyo: int):
        self.id = id_recurso
        self.titulo = titulo
        self.autor = autor
        self.anyo = anyo
        self.prestado = False
        
    @abstractmethod
    def info_detallada(self) -> str:
        """Metodo abstracto para mostrar la informacion detallada de cada recurso"""

    def __eq__(self, other):
        if not isinstance(other, Recurso):
            return False
        return self.id == other.id