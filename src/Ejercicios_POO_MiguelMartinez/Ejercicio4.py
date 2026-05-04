class Persona:

    def __init__(self, dni, nombre):
        self.din = dni
        self.nombre = nombre
    

class Empleado(Persona):
    
    def __init__(self, dni, nombre, id):
        super().__init__(dni, nombre)
        self.id = id