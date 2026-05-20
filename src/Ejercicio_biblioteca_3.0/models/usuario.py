from abc import ABC, abstractmethod

class Usuario(ABC):

    def __init__(self, id_usuario: str,nombre: str, correo: str, sanciones: list=None):
        self.comprobar_nombre(nombre)

        self.id = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.sanciones = sanciones if sanciones is not None else []
        self.prestamos_activos = []

    @abstractmethod
    def limite_prestamos(self) -> int:
        """Funcion abstracta para definir el limite de prestamos segun el tipo de usuario"""
        
    @abstractmethod
    def generar_reporte(self) -> str:
        """Reporte polimórfico."""

    def puede_tomar_prestado(self) -> bool:
         return len(self.prestamos_activos) < self.limite_prestamos() and self.sanciones < 0
        
    def __eq__(self, other):
        if not isinstance(other, Usuario):
            return False
        return self.id == other.id