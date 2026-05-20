from datetime import datetime

class Historial:
    
    def __init__(self):
        self.registros = []

    def registrar_operacion(self, usuario_id: str, usuario_nombre: str, recurso_id: str, recurso_titulo: str, accion: str):
        self.registros.append({
            "usuario_id": usuario_id,
            "usuario_nombre": usuario_nombre,
            "recurso_id": recurso_id,
            "recurso_titulo": recurso_titulo,
            "accion": accion,  # Ejemplo: "PRESTADO", "DEVUELTO", "DESCARGADO"
            "fecha": datetime.now().strftime("%d-%m-%Y %H:%M")
            })
        
    def generar_reporte_historial(self) -> list:
        return self.registros