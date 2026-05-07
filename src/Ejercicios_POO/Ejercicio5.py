class Direccion:
    def __init__(self, calle, numero, codigo_postal, ciudad, pais):
        self.calle = calle
        self.numero = numero
        self.codigo_postal = codigo_postal
        self.ciudad = ciudad
        self.pais = pais

class Persona:
    
    def __init__(self, dni, nombre, direccion):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion

direccion = Direccion("Calle del Sol", 42, 28013, "Madrid", "España")
persona1 = Persona("12345678H", "Manolo", direccion)