import curses
import sys
from services.sistema_biblioteca import SistemaBiblioteca
from models.estudiante import Estudiante
from models.profesor import Profesor
from models.bibliotecario import Bibliotecario

def mostrar_menu_curses(stdscr, usuario, biblioteca: SistemaBiblioteca):
    # Configuración inicial de colores y ocultar el cursor de texto
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN) # Barra de selección
    
    rol = usuario.__class__.__name__
    
    # Opciones base que ven todos los roles
    opciones = [
        "1. Ver mi Reporte Personal (Polimorfismo)",
        "2. Ver Reporte General de la Biblioteca",
        "3. Exportar mi Historial a CSV"
    ]
    
    if isinstance(usuario, Profesor):
        opciones.append("4. Descargar Recurso Digital")
    elif isinstance(usuario, Bibliotecario):
        opciones.append("4. Registrar un nuevo Préstamo")
        opciones.append("5. Registrar una Devolución")
        opciones.append("6. Importar recursos nuevos desde Excel")
        opciones.append("7. Exportar catálogo actual a CSV")
        
    opciones.append("Salir del Sistema")
    
    seleccionada = 0
    ejecutando = True  # Control de estado limpio para el bucle
    
    while ejecutando:
        stdscr.clear()
        
        # Dibujamos la interfaz visual
        stdscr.addstr(1, 2, f"====================================================", curses.A_BOLD)
        stdscr.addstr(2, 2, f"  SISTEMA DE GESTIÓN DE BIBLIOTECA - INTERFAZ CURSES  ", curses.A_BOLD)
        stdscr.addstr(3, 2, f"====================================================", curses.A_BOLD)
        stdscr.addstr(5, 2, f"Usuario: {usuario.nombre} | Rol: {rol}")
        stdscr.addstr(6, 2, "Use las FLECHAS (▲/▼) para moverse y ENTER para elegir.", curses.A_DIM)
        stdscr.addstr(7, 2, "----------------------------------------------------")
        
        # Renderizar el menú interactivo
        for idx, opcion in enumerate(opciones):
            y = 9 + idx
            if idx == seleccionada:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, 4, f" > {opcion} ")
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, 4, f"   {opcion} ")
                
        stdscr.refresh()
        tecla = stdscr.getch()
        
        if tecla == curses.KEY_UP and seleccionada > 0:
            seleccionada -= 1
        elif tecla == curses.KEY_DOWN and seleccionada < len(opciones) - 1:
            seleccionada += 1
        elif tecla in [10, 13, curses.KEY_ENTER]: # Si el usuario pulsa ENTER
            opcion_texto = opciones[seleccionada]
            
            # Pausamos curses temporalmente para leer/escribir en consola clásica
            curses.def_prog_mode()
            stdscr.clear()
            curses.endwin()
            
            print(f"\n--- Ejecutando: {opcion_texto} ---\n")
            
            if "Ver mi Reporte Personal" in opcion_texto:
                print(usuario.generar_reporte())
                if usuario.prestamos_activos:
                    print("\nRecursos en préstamo activo:")
                    for p in usuario.prestamos_activos:
                        print(f" - {p.recurso.info_detallada()} (Devolución estimada: {p.fecha_devolucion_estimada.strftime('%d-%m-%Y')})")
                if usuario.sanciones:
                    print("\nSanciones en tu cuenta:")
                    for s in usuario.sanciones:
                        print(f" - {s}")
                        
            elif "Ver Reporte General" in opcion_texto:
                biblioteca.reporte_general()
                print("\nCatálogo completo disponible:")
                for r in biblioteca.lista_recursos:
                    print(r.info_detallada())
                    
            elif "Exportar mi Historial" in opcion_texto:
                biblioteca.exportar_historial_usuario(usuario.nombre)
                print(f"Fichero generado en: data/historial_{usuario.nombre.lower().replace(' ', '_')}.csv")
                
            elif "Descargar Recurso Digital" in opcion_texto:
                id_rec = input("Introduce el ID del Recurso Digital: ").strip()
                try:
                    biblioteca.descargar_recurso_digital(usuario.id, id_rec)
                    print("Descarga completada con éxito. Acción registrada en Historial.")
                except ValueError as e:
                    print("Error:", e)
                    
            elif "Registrar un nuevo Préstamo" in opcion_texto:
                id_usu = input("ID del Usuario solicitante: ").strip()
                id_rec = input("ID del Recurso físico a prestar: ").strip()
                try:
                    biblioteca.prestar_recurso(id_usu, id_rec)
                    print("Préstamo asociado y guardado correctamente.")
                except ValueError as e:
                    print("Error:", e)
                    
            elif "Registrar una Devolución" in opcion_texto:
                id_usu = input("ID del Usuario que devuelve: ").strip()
                id_rec = input("ID del Recurso a devolver: ").strip()
                try:
                    biblioteca.devolver_recurso(id_usu, id_rec)
                    print("Devolución procesada. Se han comprobado retrasos y penalizaciones.")
                except ValueError as e:
                    print("Error:", e)
                    
            elif "Importar recursos nuevos" in opcion_texto:
                try:
                    biblioteca.importar_desde_excel()
                    print("Recursos cargados en lote desde 'data/recursos.xlsx'.")
                except Exception as e:
                    print("Error de importación:", e)
                    
            elif "Exportar catálogo actual" in opcion_texto:
                biblioteca.exportar_datos_a_archivos()
                print("Estado actual exportado a 'data/recursos.csv'.")
                
            elif "Salir" in opcion_texto:
                biblioteca.guardar_todo()
                print("Persistencia JSON actualizada. ¡Cierre de sesión seguro!")
                ejecutando = False  # Rompe el ciclo limpiamente
            
            if ejecutando:
                input("\nPresione ENTER para regresar al menú...")
                curses.reset_shell_mode() # Prepara los descriptores de la terminal de nuevo
                stdscr.clear()
                stdscr.refresh()

def main():
    biblioteca = SistemaBiblioteca()
    
    # Inyectamos unos usuarios iniciales si el JSON está vacío para poder testear
    if not biblioteca.lista_usuarios:
        biblioteca.agregar_usuario(Bibliotecario("ADMIN01", "Bibliotecario Jefe", "admin@biblioteca.com"))
        biblioteca.agregar_usuario(Estudiante("EST01", "Miguel", "miguel@estudiante.com"))
        biblioteca.agregar_usuario(Profesor("PROF01", "Carlos", "carlos@profesor.com"))
        biblioteca.guardar_todo()

    print("===========================================")
    print("LOGIN REQUERIDO - CONTROL DE ROLES")
    print("===========================================")
    print("IDs de prueba disponibles en el sistema:")
    print(" - Estudiante: EST01\n - Profesor: PROF01\n - Bibliotecario: ADMIN01\n")
    
    id_login = input("Introduce tu ID Único: ").strip()
    
    try:
        usuario_logeado = biblioteca.buscar_usuario(id_login)
        # Lanzamos la interfaz curses pasándole el usuario autenticado
        curses.wrapper(mostrar_menu_curses, usuario_logeado, biblioteca)
    except ValueError:
        print("\nError: ID no registrado en la base de datos.")

if __name__ == "__main__":
    main()