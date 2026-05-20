from models.usuario import Usuario

class Profesor(Usuario):

    @property
    def limite_prestamos(self) -> int:
        return 5

    def generar_reporte(self) -> str:
        estado = "Sancionado" if self.sanciones else "Activo"
        return (f"[Profesor] ID: {self.id} | Nombre: {self.nombre}\n"
                f"Correo: {self.correo} | Estado: {estado}\n"
                f"Préstamos: {len(self.prestamos_activos)}/{self.limite_prestamos}")