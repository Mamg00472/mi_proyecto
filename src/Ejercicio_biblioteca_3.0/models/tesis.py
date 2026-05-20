from models.recurso import Recurso

class Tesis(Recurso):
    
    def __init__(self, id_recurso: str, titulo: str, autor: str, anyo: int, universidad: str):
        super().__init__(id_recurso, titulo, autor, anyo)
        self.universidad = universidad
    
    def info_detallada(self) -> str:
        estado = "Prestado" if self.prestado else "Disponible"
        return f"[Tesis] ID: {self.id} | {self.titulo} - {self.autor} ({self.anyo}) | Universidad: {self.universidad} | Estado: {estado}"