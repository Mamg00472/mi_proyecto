from recurso import Recurso

class RecursoDigital(Recurso):
    
    def __init__(self, id_recurso, titulo, autor, anyo, formato, tamanyo_mb):
        super().__init__(id_recurso, titulo, autor, anyo)
        self.formato = formato
        self.tamanyo_mb = tamanyo_mb

    def info_detallada(self):
        return f"[Digital] ID: {self.id} | '{self.titulo}' - {self.autor} ({self.anyo}) | Formato: {self.formato} ({self.tamano_mb} MB) | Estado: Descargable"