from recurso import Recurso

class RecursoDigital(Recurso):
    
    def __init__(self, id_recurso: str, titulo: str, autor: str, anyo: int, formato: str, tamanyo_mb: float):
        super().__init__(id_recurso, titulo, autor, anyo)
        self.formato = formato
        self.tamanyo_mb = tamanyo_mb

    def info_detallada(self) -> str:
        return f"[Digital] ID: {self.id} | '{self.titulo}' - {self.autor} ({self.anyo}) | Formato: {self.formato} ({self.tamano_mb} MB) | Estado: Descargable"