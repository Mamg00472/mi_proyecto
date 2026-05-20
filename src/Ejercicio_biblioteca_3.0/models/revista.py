from recurso import Recurso

class Revista(Recurso):
    
    def __init__(self, id_recurso, titulo, autor, anyo, edicion):
        super().__init__(id_recurso, titulo, autor, anyo)
        self.edicion = edicion
    
    def info_detallada(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"[Revista] ID: {self.id} | {self.titulo} - {self.autor} ({self.anyo}) | Edición: {self.edicion} | Estado: {estado}"