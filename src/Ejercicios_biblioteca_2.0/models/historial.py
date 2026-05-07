from datetime import datetime


class Historial:
    
    def __init__(self):
        self.registros = []

    def registrar(self, usuario_nombre, libro_titulo, accion):
        self.registros.append({
                "usuario": usuario_nombre.nombre,
                "libro" : libro_titulo.titulo,
                "accion" : accion,
                "fecha" : datetime.now().strftime("%d-%m-%Y %H:%M")
            })