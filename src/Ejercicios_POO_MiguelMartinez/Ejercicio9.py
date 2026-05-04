class Usuario:

    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} con dni: {self.dni}"
    
    def __eq__(self, other):
        return self.dni == other.dni
    
class RegistroUsuarios:

    def __init__(self):
        self.lista = []

    def agregar_usuario(self, usuario):
        self.lista.append(usuario)

    def buscar_usuario(self, usuario):
        for u in self.lista:
            if usuario == u:
                print(f"Usuario: {usuario} encontrado")
                break
        else:
            print(f"Usuario: {usuario} no encontrado")

    def eliminar_usuario(self, usuario):
        for u in self.lista:
            if usuario == u:
                self.lista.remove(u)
                print(f"Usuario: {usuario} borrado correctamente")
                break
        else:
            print(f"Usuario: {usuario} no encontrado")

usuario1 = Usuario("12345678h", "Manolo")
usuario2 = Usuario("12345678a", "Pepe")
usuario3 = Usuario("12345678i", "Juan")
usuario4 = Usuario("12345678s", "Pedro")
usuario5 = Usuario("12345678g", "Fernando")
usuario6 = Usuario("12345678h", "Jose")

lista = RegistroUsuarios()

lista.agregar_usuario(usuario1)
lista.agregar_usuario(usuario2)
lista.agregar_usuario(usuario3)
lista.agregar_usuario(usuario4)

print("====== Busqueda de usuarios ======\n")

lista.buscar_usuario(usuario1)
lista.buscar_usuario(usuario2)
lista.buscar_usuario(usuario3)
lista.buscar_usuario(usuario4)
lista.buscar_usuario(usuario5)
lista.buscar_usuario(usuario6)

print("\n====== Borrado de usuarios ======\n")

lista.eliminar_usuario(usuario1)
lista.eliminar_usuario(usuario2)
lista.eliminar_usuario(usuario3)
lista.eliminar_usuario(usuario4)
lista.eliminar_usuario(usuario5)
lista.eliminar_usuario(usuario6)