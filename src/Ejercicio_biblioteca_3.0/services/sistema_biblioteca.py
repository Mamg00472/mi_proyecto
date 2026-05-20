from datetime import datetime
from persistencia import cargar_json, guardar_json
from excel_csv import importar_recursos_excel, exportar_recursos_csv, exportar_historial_usuario_csv

# Importamos todos los modelos que creamos antes
from models.estudiante import Estudiante
from models.profesor import Profesor
from models.bibliotecario import Bibliotecario
from models.libro import Libro
from models.revista import Revista
from models.tesis import Tesis
from models.recurso_digital import RecursoDigital
from models.prestamo import Prestamo
from models.historial import Historial

class SistemaBiblioteca:

    def __init__(self):
        self.lista_usuarios = []
        self.lista_recursos = []
        self.historial = Historial()
        self.lista_prestamos = []

        self.cargar_todo()

    def agregar_usuario(self, usuario):
        if any(u.id == usuario.id for u in self.lista_usuarios):
            raise ValueError("Ya existe un usuario con ese ID.")
        self.lista_usuarios.append(usuario)

    def agregar_recurso(self, recurso):
        if any(r.id == recurso.id for r in self.lista_recursos):
            raise ValueError("Ya existe un recurso con ese ID.")
        self.lista_recursos.append(recurso)

    def buscar_usuario(self, id_usuario: str):
        for u in self.lista_usuarios:
            if u.id == id_usuario:
                return u
        raise ValueError("Usuario no encontrado.")

    def buscar_recurso(self, id_recurso: str):
        for r in self.lista_recursos:
            if r.id == id_recurso:
                return r
        raise ValueError("Recurso no encontrado.")

    def prestar_recurso(self, id_usuario: str, id_recurso: str):
        usuario = self.buscar_usuario(id_usuario)
        recurso = self.buscar_recurso(id_recurso)

        # No se puede prestar un recurso ya prestado
        if recurso.prestado:
            raise ValueError("El recurso ya está prestado a otra persona.")

        # Un RecursoDigital no se presta, se descarga
        if isinstance(recurso, RecursoDigital):
            raise ValueError("Los recursos digitales no se prestan. ¡Usa la opción de descarga!")

        # Un Estudiante no tiene acceso a RecursoDigital (controlado arriba, pero por si acaso)
        # Verificar límites de préstamos y sanciones acumuladas
        if not usuario.puede_tomar_prestado():
            raise ValueError(f"El usuario {usuario.nombre} no puede pedir más recursos (Límite máximo alcanzado o tiene sanciones activas).")

        # Si pasa las reglas, se crea el préstamo
        nuevo_prestamo = Prestamo(usuario, recurso)
        recurso.prestado = True
        usuario.prestamos_activos.append(nuevo_prestamo)
        self.lista_prestamos.append(nuevo_prestamo)
        
        # Registramos en el historial
        self.historial.registrar_operacion(usuario.id, usuario.nombre, recurso.id, recurso.titulo, "PRESTADO")

    def devolver_recurso(self, id_usuario: str, id_recurso: str):
        usuario = self.buscar_usuario(id_usuario)
        recurso = self.buscar_recurso(id_recurso)

        # Buscamos el préstamo activo en la lista del usuario
        prestamo_encontrado = None
        for p in usuario.prestamos_activos:
            if p.recurso.id == recurso.id:
                prestamo_encontrado = p
                break

        if not prestamo_encontrado:
            raise ValueError("Este usuario no tiene este recurso en préstamo activo.")

        # Finalizamos el préstamo (cambia fechas y pone prestado=False)
        prestamo_encontrado.finalizar_prestamo()
        usuario.prestamos_activos.remove(prestamo_encontrado)

        # Si tardó más de 30 días, se le añade una sanción al usuario
        if prestamo_encontrado.esta_retrasado():
            dias = prestamo_encontrado.calcular_sancion()
            sancion_msg = f"Retraso de {dias} días en recurso ID {recurso.id} (Devuelto el {datetime.now().strftime('%d-%m-%Y')})"
            usuario.sanciones.append(sancion_msg)
            self.historial.registrar_operacion(usuario.id, usuario.nombre, recurso.id, recurso.titulo, f"SANCIONADO ({dias} días)")

        self.historial.registrar_operacion(usuario.id, usuario.nombre, recurso.id, recurso.titulo, "DEVUELTO")

    def descargar_recurso_digital(self, id_usuario: str, id_recurso: str):
        usuario = self.buscar_usuario(id_usuario)
        recurso = self.buscar_recurso(id_recurso)

        if not isinstance(recurso, RecursoDigital):
            raise ValueError("Este recurso no es digital, requiere un préstamo físico.")

        # Un Estudiante no puede pedir/descargar RecursoDigital. Profesor y Bibliotecario sí.
        if isinstance(usuario, Estudiante):
            raise ValueError("Acceso denegado: Los Estudiantes no tienen permitido descargar recursos digitales.")

        # Si es profesor o bibliotecario, descarga directamente
        self.historial.registrar_operacion(usuario.id, usuario.nombre, recurso.id, recurso.titulo, "DESCARGADO")

    def reporte_general(self):
        print("\n=== REPORTE GENERAL DEL SISTEMA ===")
        print(f"Usuarios registrados: {len(self.lista_usuarios)}")
        print(f"Recursos en catálogo: {len(self.lista_recursos)}")
        prestados = sum(1 for r in self.lista_recursos if r.prestado)
        print(f"Recursos físicos prestados actualmente: {prestados}")
        print("--------------------------------------")

    def exportar_datos_a_archivos(self):
        exportar_recursos_csv("data/recursos.csv", self.lista_recursos)

    def exportar_historial_usuario(self, nombre_usuario: str):
        exportar_historial_usuario_csv(nombre_usuario, self.historial.generar_reporte_historial())

    def importar_desde_excel(self):
        datos_excel = importar_recursos_excel("data/recursos.xlsx")

        for item in datos_excel:
            tipo = item["tipo"]
            try:
                if tipo == "libro":
                    rec = Libro(item["id"], item["titulo"], item["autor"], item["anio"], int(item["extra_1"]))
                elif tipo == "revista":
                    rec = Revista(item["id"], item["titulo"], item["autor"], item["anio"], int(item["extra_1"]))
                elif tipo == "tesis":
                    rec = Tesis(item["id"], item["titulo"], item["autor"], item["anio"], str(item["extra_1"]))
                elif tipo == "digital":
                    rec = RecursoDigital(item["id"], item["titulo"], item["autor"], item["anio"], str(item["extra_1"]), float(item["extra_2"]))
                else:
                    continue # Tipo desconocido, nos lo saltamos
                
                self.agregar_recurso(rec)
            except ValueError:
                pass # Si el ID ya existe, se ignora el recurso importado para evitar duplicados
    
    def guardar_todo(self):
        # 1. Guardar historial
        guardar_json("data/historial.json", self.historial.generar_reporte_historial())

        # 2. Guardar recursos
        datos_recursos = []
        for r in self.lista_recursos:
            # Almacenamos el nombre de la clase para saber qué es al recargar
            info = {
                "id": r.id,
                "tipo": r.__class__.__name__,
                "titulo": r.titulo,
                "autor": r.autor,
                "anio": r.anio,
                "prestado": r.prestado
            }
            # Guardamos sus atributos únicos
            if isinstance(r, Libro): info["extra_1"] = r.numero_paginas
            elif isinstance(r, Revista): info["extra_1"] = r.edicion
            elif isinstance(r, Tesis): info["extra_1"] = r.universidad
            elif isinstance(r, RecursoDigital): 
                info["extra_1"] = r.formato
                info["extra_2"] = r.tamano_mb
            datos_recursos.append(info)
        guardar_json("data/recursos.json", datos_recursos)

        # 3. Guardar usuarios (con sus sanciones)
        datos_usuarios = []
        for u in self.lista_usuarios:
            datos_usuarios.append({
                "id": u.id,
                "tipo": u.__class__.__name__,
                "nombre": u.nombre,
                "correo": u.correo,
                "sanciones": u.sanciones
            })
        guardar_json("data/usuarios.json", datos_usuarios)

    def cargar_todo(self):
        # 1. Cargar Historial
        registros_viejos = cargar_json("data/historial.json")
        self.historial.registros = registros_viejos

        # 2. Cargar Recursos
        recursos_json = cargar_json("data/recursos.json")
        for item in recursos_json:
            tipo = item["tipo"]
            if tipo == "Libro": r = Libro(item["id"], item["titulo"], item["autor"], item["anio"], item["extra_1"])
            elif tipo == "Revista": r = Revista(item["id"], item["titulo"], item["autor"], item["anio"], item["extra_1"])
            elif tipo == "Tesis": r = Tesis(item["id"], item["titulo"], item["autor"], item["anio"], item["extra_1"])
            elif tipo == "RecursoDigital": r = RecursoDigital(item["id"], item["titulo"], item["autor"], item["anio"], item["extra_1"], item["extra_2"])
            r.prestado = item["prestado"]
            self.lista_recursos.append(r)

        # 3. Cargar Usuarios
        usuarios_json = cargar_json("data/usuarios.json")
        for item in usuarios_json:
            tipo = item["tipo"]
            if tipo == "Estudiante": u = Estudiante(item["id"], item["nombre"], item["correo"], item["sanciones"])
            elif tipo == "Profesor": u = Profesor(item["id"], item["nombre"], item["correo"], item["sanciones"])
            elif tipo == "Bibliotecario": u = Bibliotecario(item["id"], item["nombre"], item["correo"], item["sanciones"])
            self.lista_usuarios.append(u)