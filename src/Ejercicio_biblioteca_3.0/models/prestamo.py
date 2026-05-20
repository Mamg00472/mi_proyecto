from datetime import datetime, timedelta
from recurso import Recurso
from usuario import Usuario

class Prestamo:
    def __init__(self, recurso: Recurso, usuario: Usuario, fecha_prestamo: datetime = None):
        self.recurso = recurso
        self.usuario = usuario

        # Si no se proporciona una fecha de préstamo, se establece la fecha actual
        self.fecha_prestamo = datetime.now() if fecha_prestamo is None else fecha_prestamo

        self.fecha_devolucion_estimada = self.fecha_prestamo + timedelta(days=30)  # Plazo de 30 días
        self.fecha_devolucion_real = None  # Se establecerá cuando el recurso sea devuelto

    def esta_retrasado(self) -> bool:
        # Si el recurso ya ha sido devuelto, se compara la fecha de devolución real con la fecha de devolución estimada
        if self.fecha_devolucion_real is not None:
            return self.fecha_devolucion_real > self.fecha_devolucion_estimada
        
        # Si el recurso no ha sido devuelto, se compara la fecha actual con la fecha de devolución estimada
        return datetime.now() > self.fecha_devolucion_estimada
    
    def calcular_sancion(self) -> int:
        # si no tiene ningun retraso por ahora no se le aplica ninguna sancion
        if not self.esta_retrasado():
            return 0
        fin = self.fecha_devolucion_real if self.fecha_devolucion_real is not None else datetime.now()
        dias_retraso = (fin - self.fecha_devolucion_estimada).days
        return dias_retraso
    
    def finalizar_prestamo(self, fecha_devolucion_real: datetime = None):
        # si el recurso aun no ha sido devuelto, se establece la fecha actual, de lo contrario se deja la fecha de cuando se devolvio
        self.fecha_devolucion_real = datetime.now() if fecha_devolucion_real is None else fecha_devolucion_real
        self.recurso.prestado = False  # Marcar el recurso como no prestado

    def __str__(self) -> str:
        formato = "%d-%m-%Y"
        estado = "Devuelto" if self.fecha_devolucion_real else "En préstamo"
        return (f"({estado}) | Usuario: {self.usuario.nombre} | Recurso: {self.recurso.titulo}\n"
                f"Sacado el: {self.fecha_prestamo.strftime(formato)} | "
                f"Devolución estimada: {self.fecha_devolucion_estimada.strftime(formato)}")