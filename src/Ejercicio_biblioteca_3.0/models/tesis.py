from recurso import Recurso

class Tessis(Recurso):
    
    def __init__(self, id_recurso, titulo, autor, anyo, universidad):
        super().__init__(id_recurso, titulo, autor, anyo)
        self.universidad = universidad
    
    def info_detallada(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"[Tesis] ID: {self.id} | {self.titulo} - {self.autor} ({self.anyo}) | Universidad: {self.universidad} | Estado: {estado}"