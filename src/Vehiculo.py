class Vehiculo:
    def __init__(self, id, ruedas, color):
        self.id = id
        self.ruedas = ruedas
        self.color = color

    def __str__(self):
        return f"ID: {self.id}, Ruedas: {self.ruedas}, Color: {self.color}"
    
class Coche(Vehiculo):
    def __init__(self, id, ruedas, color, marca):
        super().__init__(id, ruedas, color)
        self.marca = marca

    def __str__(self):
        return f"{super().__str__()}, Marca: {self.marca}"
    
class Moto(Vehiculo):
    def __init__(self, id, ruedas, color, manillar):
        super().__init__(id, ruedas, color)
        self.manillar = manillar

    def __str__(self):
        return f"{super().__str__()}, Manillar: {self.manillar}"

v1 = Coche("123A", 4, "negro", "Marca1")
v2 = Moto("123B", 2, "blanca", "Pequeño")
v3 = Coche("123C", 4, "blanca", "Marca2")
v4 = Moto("123D", 2, "negro", "Grande")

lista_vehiculos = [v1, v2, v3, v4]

v5 = Coche("123E", 4, "rojo", "Marca3")
lista_vehiculos.append(v5)

for v in lista_vehiculos:
    print(type(v).__name__, v)


