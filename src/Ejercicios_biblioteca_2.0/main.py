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
        libro = crear_libro()
        biblioteca.agregar_libro(libro)

    elif menu == "2":
        usuario = crear_usuario()
        biblioteca.agregar_usuario(usuario)

    elif menu == "3":
        titulo = input("Escribe el titulo del libro: ")
        nombre = input("Escriba el nombre del usuario: ")

        libro = biblioteca.buscar_libro(titulo)
        usuario = biblioteca.buscar_usuario(nombre)
        
        if libro is None:
            print("Ese libro no esta en la biblioteca")
            continue
        if usuario is None:
            print("Ese usuario no existe en la biblioteca")
            continue

        biblioteca.prestar_libro(libro, usuario)

    elif menu == "4":
        titulo = input("Escribe el titulo del libro: ")
        nombre = input("Escriba el nombre del usuario: ")

        libro = biblioteca.buscar_libro(titulo)
        usuario = biblioteca.buscar_usuario(nombre)

        if libro is None:
            print("Ese libro no esta en la biblioteca")
            continue

        if usuario is None:
            print("Ese usuario no existe en la biblioteca")
            continue

        biblioteca.devolver_libro(libro, usuario)


    elif menu == "5":
        biblioteca.mostrar_info_libros()

    elif menu == "6":
        break

    else:
        print("Opcion no valida")


print("Saliendo del programa...")