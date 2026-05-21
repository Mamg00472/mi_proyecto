from models.usuario import Usuario

class Bibliotecario(Usuario):

    def limite_prestamos(self) -> int:
        return 9999

    def generar_reporte(self) -> str:
        return f"[Bibliotecario] ID: {self.id} | Nombre: {self.nombre} | Rol: Administrador del Sistema"