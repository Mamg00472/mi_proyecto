import re

class Coche:
    contador = 0
    
    def __init__(self, matricula):
        
        if self.validar_matricula(matricula):
            self.matricula = matricula
            self.id = Coche.contar_coches()
            print("coche creado correctamente")
        else:
            try:
                raise ValueError("Matricula invalida")
            except ValueError as e:
                print("Error:", e)

    def __str__(self):
        return f"Matricula: {self.matricula} con id: {self.id}"

    @staticmethod
    def validar_matricula(matricula):
        return re.match(r"^\d{4}[A-Za-z]{3}$", matricula) is not None
    
    @classmethod
    def contar_coches(cls):
        cls.contador +=1
        return cls.contador

coche1 = Coche("1235EDF")
coche2 = Coche("12355EDF")
coche3 = Coche("1235EDeF")
coche4 = Coche("1235ED4F")
try:
    print(coche1)
    print(coche2)
    print(coche3)
    print(coche4)
except AttributeError as e:
    print("Error:", e)