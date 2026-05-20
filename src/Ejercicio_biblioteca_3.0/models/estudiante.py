from usuario import Usuario

class Estudiante(Usuario):
    
    def limite_prestamos(self):
        return 3

    def generar_reporte(self):
        estado = "Sancionado" if self.sanciones else "Activo"
        return (f"[Estudiante] ID: {self.id} | Nombre: {self.nombre}\n"
                f"Correo: {self.correo} | Estado: {estado}\n"
                f"Préstamos: {len(self.prestamos_activos)}/{self.limite_prestamos}")