class Calculadora:

    def __init__(self):
        pass

    def sumar(self, num1, num2):
        return num1 + num2
    
    def restar(self, num1, num2):
        return num1 - num2
    
    def multiplicar(self, num1, num2):
        return num1 * num2
    
    def dividir(self, num1, num2):
        if num2 == 0:
            return "no se puede dividir entre 0"
        else:
            return num1 / num2
    
resultado = Calculadora()
print(resultado.sumar(5,4))
print(resultado.restar(5,4))
print(resultado.multiplicar(5,4))
print(resultado.dividir(5,4))