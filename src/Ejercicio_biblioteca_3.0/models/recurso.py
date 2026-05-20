from abc import ABC, abstractmethod
from utils.validaciones import validar_longitud_texto, validar_anyo

class Recurso(ABC):

    def __init__(self, id_recurso: str, titulo: str, autor: str, anyo: int):
        self.id = validar_longitud_texto(id_recurso, "ID", minimo=1, maximo=10)
        self.titulo = validar_longitud_texto(titulo, "Título")
        self.autor = validar_longitud_texto(autor, "Autor")
        self.anyo = validar_anyo(anyo)
        self.prestado = False
        
    @abstractmethod
    def info_detallada(self) -> str:
        """Metodo abstracto para mostrar la informacion detallada de cada recurso"""

    def __eq__(self, other):
        if not isinstance(other, Recurso):
            return False
        return self.id == other.id