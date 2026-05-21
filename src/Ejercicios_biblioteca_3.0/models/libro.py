from models.recurso import Recurso

class Libro(Recurso):
    
    def __init__(self, id_recurso: str, titulo: str, autor: str, anyo: int, num_paginas: int):
        super().__init__(id_recurso, titulo, autor, anyo)
        self.num_paginas = num_paginas
    
    def info_detallada(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"[Libro] ID: {self.id} | {self.titulo} - {self.autor} ({self.anio}) | Páginas: {self.num_paginas} | Estado: {estado}"