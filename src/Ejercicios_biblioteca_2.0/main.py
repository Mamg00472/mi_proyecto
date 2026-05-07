from utils.menu import Menu
from services.biblioteca import Biblioteca
from models.libro import Libro
from models.usuario import Usuario

def crear_libro():
        titulo = input("Escriba el titulo del libro: ").strip()
        autor = input("Escriba el nombre del autor: ").strip()
        libro = Libro(titulo, autor)
        return libro

def crear_usuario():
        nombre = input("Escriba el nombre del usuario: ").strip()
        usuario = Usuario(nombre)
        return usuario

biblioteca = Biblioteca()

while True:
    Menu.mostrar_menu()
    menu = input("Seleccione una opcion: ")
    
    if menu == "1":
        try:
            libro = crear_libro()
            biblioteca.agregar_libro(libro)

        except ValueError as e:
            print("Error:", e)

    elif menu == "2":
        try:
            usuario = crear_usuario()
            biblioteca.agregar_usuario(usuario)
        
        except ValueError as e:
            print("Error:", e)

    elif menu == "3":
        try:
            titulo = input("Escribe el titulo del libro: ")
            nombre = input("Escriba el nombre del usuario: ")

            libro = biblioteca.buscar_libro(titulo)
            usuario = biblioteca.buscar_usuario(nombre)

            biblioteca.prestar_libro(libro, usuario)

        except ValueError as e:
            print("Error", e)

    elif menu == "4":
        try:
            titulo = input("Escribe el titulo del libro: ")
            nombre = input("Escriba el nombre del usuario: ")

            libro = biblioteca.buscar_libro(titulo)
            usuario = biblioteca.buscar_usuario(nombre)

            biblioteca.devolver_libro(libro, usuario)

        except ValueError as e:
            print("Error:", e)

    elif menu == "5":
        biblioteca.mostrar_info_libros()

    elif menu == "6":
        biblioteca.exportar_csv()
        
    elif menu == "7":
        biblioteca.importar_excel()

    elif menu == "8":
        break

    else:
        print("Opcion no valida")


biblioteca.guardar_datos()
print("Saliendo del programa...")