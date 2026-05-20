from datetime import datetime
from services.persistencia import cargar_json, guardar_json

class Historial:
    
    def __init__(self):
        self.registros = cargar_json("data/historial.json")

    def registrar(self, usuario_nombre, libro_titulo, accion):
        self.registros.append({
                "usuario": usuario_nombre,
                "libro" : libro_titulo,
                "accion" : accion,
                "fecha" : datetime.now().strftime("%d-%m-%Y %H:%M")
            })
        
    def guardar(self):
        guardar_json("data/historial.json", self.registros)