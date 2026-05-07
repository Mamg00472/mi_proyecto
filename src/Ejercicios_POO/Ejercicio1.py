class Animal:
    
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Saludos de {self.nombre}")

a = Animal("pedro")
a.saludar()