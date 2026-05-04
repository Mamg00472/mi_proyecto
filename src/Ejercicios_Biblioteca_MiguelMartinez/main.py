from utils import Utils
from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario

def crear_libro():
    titulo = input("Escriba el titulo del libro: ")
    autor = input("Escriba el nombre del autor: ")
    libro = Libro(titulo, autor)
    return libro

def crear_usuario():
    nombre = input("Escriba el nombre del usuario: ")
    usuario = Usuario(nombre)
    return usuario

biblioteca = Biblioteca()

while True:
    Utils.mostrar_menu()
    menu = input("Seleccione una opcion: ")
    
    if menu == "1":
        libro = crear_libro()
        biblioteca.agregar_libro(libro)

    elif menu == "2":
        usuario = crear_usuario()
        biblioteca.agregar_usuario(usuario)

    elif menu == "3":
        libro = crear_libro()
        usuario = crear_usuario()
        biblioteca.prestar_libro(libro, usuario)
        for l in biblioteca.lista_libros:
            if libro.prestado == True and l.prestado == False:
                l.prestado = True
        

    elif menu == "4":
        libro = crear_libro()
        usuario = crear_usuario()
        biblioteca.devolver_libro(libro, usuario)

    elif menu == "5":
        biblioteca.mostrar_info_libros()

    elif menu == "6":
        break

    else:
        print("Opcion no valida")


print("Saliendo del programa...")