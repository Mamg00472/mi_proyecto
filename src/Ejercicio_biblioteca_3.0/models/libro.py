from recurso import Recurso

class Libro(Recurso):
    
    def __init__(self, id_recurso, titulo, autor, anyo, genero):
        super().__init__(id_recurso, titulo, autor, anyo)
        self.comprobar_genero(genero)
        self.genero = genero
    
    def comprobar_genero(self, genero):
        if len(genero) < 2 or len(genero) > 50:
            raise ValueError("Género no válido (debe tener entre 2 y 50 caracteres)")
    
    def info_detallada(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"[Libro] ID: {self.id} | {self.titulo} - {self.autor} ({self.anio}) | Estado: {estado}"