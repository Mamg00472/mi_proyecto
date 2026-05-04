class Vehiculo:

    def __init__(self, marca, matricula, ruedas):
        self.marca = marca
        self.matricula = matricula
        self.ruedas = ruedas

class Coche(Vehiculo):

    def __init__(self, marca, matricula):
        super().__init__(marca, matricula, 4)

    def arrancar(self):
        print("brummmm")

coche = Coche("BMW", "3043RGD")

coche.arrancar()