class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        return f"El libro: {self.titulo} escrito por: {self.autor}"
    

libro1 = Libro("El principito", "Antoine de Saint-Exupéry")
libro2 = Libro("1984", "George Orwell")
libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")

print(libro1)
print(libro2)
print(libro3)